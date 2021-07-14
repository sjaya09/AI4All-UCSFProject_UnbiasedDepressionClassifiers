import pandas as pd
import os

if __name__ == '__main__':

    # Create data/raw directory if it doesn't already exist
    if 'data' not in os.listdir():
        os.mkdir('data')

    if 'raw' not in os.listdir('data'):
        os.mkdir('data/raw')

    # Read data (2011-2016) from NHANES website
    year_data_mapping = {
        '2011-2012': 'G',
        '2013-2014': 'H',
        '2015-2016': 'I'
    }

    data_sources = {
        year: {
            'demographic': pd.read_sas('https://wwwn.cdc.gov/Nchs/Nhanes/{}/DEMO_{}.XPT'.format(year, letter)),
            'acculturation': pd.read_sas('https://wwwn.cdc.gov/Nchs/Nhanes/{}/ACQ_{}.XPT'.format(year, letter)),
            'alcohol_use': pd.read_sas('https://wwwn.cdc.gov/Nchs/Nhanes/{}/ALQ_{}.XPT'.format(year, letter)),
            'bp_cholesterol': pd.read_sas('https://wwwn.cdc.gov/Nchs/Nhanes/{}/BPQ_{}.XPT'.format(year, letter)),
            'cardiovascular': pd.read_sas('https://wwwn.cdc.gov/Nchs/Nhanes/{}/CDQ_{}.XPT'.format(year, letter)),
            'consumer_behavior': pd.read_sas('https://wwwn.cdc.gov/Nchs/Nhanes/{}/CBQ_{}.XPT'.format(year, letter)),
            'health_status': pd.read_sas('https://wwwn.cdc.gov/Nchs/Nhanes/{}/HSQ_{}.XPT'.format(year, letter)),
            'dermatology': pd.read_sas('https://wwwn.cdc.gov/Nchs/Nhanes/{}/DEQ_{}.XPT'.format(year, letter)),
            'diabetes': pd.read_sas('https://wwwn.cdc.gov/Nchs/Nhanes/{}/DIQ_{}.XPT'.format(year, letter)),
            'diet_nutrition': pd.read_sas('https://wwwn.cdc.gov/Nchs/Nhanes/{}/DBQ_{}.XPT'.format(year, letter)),
            'drug_use': pd.read_sas('https://wwwn.cdc.gov/Nchs/Nhanes/{}/DUQ_{}.XPT'.format(year, letter)),
            'early_childhood': pd.read_sas('https://wwwn.cdc.gov/Nchs/Nhanes/{}/ECQ_{}.XPT'.format(year, letter)),
            'food_security': pd.read_sas('https://wwwn.cdc.gov/Nchs/Nhanes/{}/FSQ_{}.XPT'.format(year, letter)),
            'health_insurance': pd.read_sas('https://wwwn.cdc.gov/Nchs/Nhanes/{}/HIQ_{}.XPT'.format(year, letter)),
            'hospital_access_to_care': pd.read_sas('https://wwwn.cdc.gov/Nchs/Nhanes/{}/HUQ_{}.XPT'.format(year, letter)),
            'housing': pd.read_sas('https://wwwn.cdc.gov/Nchs/Nhanes/{}/HOQ_{}.XPT'.format(year, letter)),
            'immunization': pd.read_sas('https://wwwn.cdc.gov/Nchs/Nhanes/{}/IMQ_{}.XPT'.format(year, letter)),
            'income': pd.read_sas('https://wwwn.cdc.gov/Nchs/Nhanes/{}/INQ_{}.XPT'.format(year, letter)),
            'urology': pd.read_sas('https://wwwn.cdc.gov/Nchs/Nhanes/{}/KIQ_U_{}.XPT'.format(year, letter)),
            'medical_conditions': pd.read_sas('https://wwwn.cdc.gov/Nchs/Nhanes/{}/MCQ_{}.XPT'.format(year, letter)),
            'occupation': pd.read_sas('https://wwwn.cdc.gov/Nchs/Nhanes/{}/OCQ_{}.XPT'.format(year, letter)),
            'mental_health': pd.read_sas('https://wwwn.cdc.gov/Nchs/Nhanes/{}/DPQ_{}.XPT'.format(year, letter)),
            'oral_health': pd.read_sas('https://wwwn.cdc.gov/Nchs/Nhanes/{}/OHQ_{}.XPT'.format(year, letter)),
            'pesticide_use': pd.read_sas('https://wwwn.cdc.gov/Nchs/Nhanes/{}/PUQMEC_{}.XPT'.format(year, letter)),
            'physical_activity': pd.read_sas('https://wwwn.cdc.gov/Nchs/Nhanes/{}/PAQ_{}.XPT'.format(year, letter)),
            'physical_functioning': pd.read_sas('https://wwwn.cdc.gov/Nchs/Nhanes/{}/PFQ_{}.XPT'.format(year, letter)),
            'prescription': pd.read_sas('https://wwwn.cdc.gov/Nchs/Nhanes/{}/RXQ_RX_{}.XPT'.format(year, letter)),
            'preventative_aspirin_use': pd.read_sas('https://wwwn.cdc.gov/Nchs/Nhanes/{}/RXQASA_{}.XPT'.format(year, letter)),
            'reproductive': pd.read_sas('https://wwwn.cdc.gov/Nchs/Nhanes/{}/RHQ_{}.XPT'.format(year, letter)),
            'sexual_behavior': pd.read_sas('https://wwwn.cdc.gov/Nchs/Nhanes/{}/SXQ_{}.XPT'.format(year, letter)),
            'sleep_disorder': pd.read_sas('https://wwwn.cdc.gov/Nchs/Nhanes/{}/SLQ_{}.XPT'.format(year, letter)),
            'smoking_cigarette': pd.read_sas('https://wwwn.cdc.gov/Nchs/Nhanes/{}/SMQ_{}.XPT'.format(year, letter)),
            'smoking_recent_tobacco': pd.read_sas('https://wwwn.cdc.gov/Nchs/Nhanes/{}/SMQRTU_{}.XPT'.format(year, letter)),
            'weight_history': pd.read_sas('https://wwwn.cdc.gov/Nchs/Nhanes/{}/WHQ_{}.XPT'.format(year, letter))
        }
        for year, letter in year_data_mapping.items()
    }

    # Keep track of columns that are consistent across years
    column_tracker = {
        file: []
        for file in data_sources['2011-2012']
    }

    for year, data in data_sources.items():
        for file in column_tracker:

            if len(column_tracker[file]) == 0:
                column_tracker[file] = data[file].columns
            else:
                column_tracker[file] = [
                    col
                    for col in data[file].columns
                    if col in column_tracker[file]
                ]

    # Save dataframes to data/raw directory
    for year, data in data_sources.items():
        for file, df in data.items():
            df[column_tracker[file]].to_csv(
                'data/raw/{}_{}.csv'.format(year, file),
                index = False
            )
