import pandas as pd
import os
import numpy as np

if __name__ == '__main__':

    acculturation_2011_df = pd.read_csv('data/raw/2011-2012_acculturation.csv')
    alcohol_use_2011_df = pd.read_csv('data/raw/2011-2012_alcohol_use.csv')
    bp_cholesterol_2011_df = pd.read_csv('data/raw/2011-2012_bp_cholesterol.csv')
    #oops
    cardiovascular_2011_df = pd.read_csv('data/raw/2011-2012_cardiovascular.csv')
    consumer_behavior_2011_df = pd.read_csv('data/raw/2011-2012_consumer_behavior.csv')
    demographic_2011_df = pd.read_csv('data/raw/2011-2012_demographic.csv')
    dermatology_2011_df = pd.read_csv('data/raw/2011-2012_dermatology.csv')
    diabetes_2011_df = pd.read_csv('data/raw/2011-2012_diabetes.csv')
    diet_nutrition_2011_df = pd.read_csv('data/raw/2011-2012_diet_nutrition.csv')
    #I'll just test it out first because I don't want this to be a pain later (in case it doesn't work)
    #Yup, it doesn't work
    # Ohhh, thank you! I do the same thing but for tabbing, I didn't know it would work for comments
    drug_use_2011_df = pd.read_csv('data/raw/2011-2012_drug_use.csv')
    early_childhood_2011_df = pd.read_csv('data/raw/2011-2012_early_childhood.csv')
    food_security_2011_df = pd.read_csv('data/raw/2011-2012_food_security.csv')
    health_insurance_2011_df = pd.read_csv('data/raw/2011-2012_health_insurance.csv')
    health_status_2011_df = pd.read_csv('data/raw/2011-2012_health_status.csv')
    hospital_access_to_care_2011_df = pd.read_csv('data/raw/2011-2012_hospital_access_to_care.csv')
    housing_2011_df = pd.read_csv('data/raw/2011-2012_housing.csv')
    immunization_2011_df = pd.read_csv('data/raw/2011-2012_immunization.csv')
    income_2011_df = pd.read_csv('data/raw/2011-2012_income.csv')
    medical_conditions_2011_df = pd.read_csv('data/raw/2011-2012_medical_conditions.csv')
    mental_health_2011_df = pd.read_csv('data/raw/2011-2012_mental_health.csv')
    occupation_2011_df = pd.read_csv('data/raw/2011-2012_occupation.csv')
    oral_health_2011_df = pd.read_csv('data/raw/2011-2012_oral_health.csv')
    pesticide_use_2011_df = pd.read_csv('data/raw/2011-2012_pesticide_use.csv')
    # I can't believe I'm not done yet
    physical_activity_2011_df = pd.read_csv('data/raw/2011-2012_physical_activity.csv')
    physical_functioning_2011_df = pd.read_csv('data/raw/2011-2012_physical_functioning.csv')
    preventative_aspirin_use_2011_df = pd.read_csv('data/raw/2011-2012_preventative_aspirin_use.csv')
    reproductive_2011_df = pd.read_csv('data/raw/2011-2012_reproductive.csv')
    sexual_behavior_2011_df = pd.read_csv('data/raw/2011-2012_sexual_behavior.csv')
    sleep_disorder_2011_df = pd.read_csv('data/raw/2011-2012_sleep_disorder.csv')
    smoking_cigarette_2011_df = pd.read_csv('data/raw/2011-2012_smoking_cigarette.csv')
    smoking_recent_tobacco_2011_df = pd.read_csv('data/raw/2011-2012_smoking_recent_tobacco.csv')
    urology_2011_df = pd.read_csv('data/raw/2011-2012_urology.csv')
    weight_history_2011_df = pd.read_csv('data/raw/2011-2012_weight_history.csv')
    #Done! Yay!!
    #Actually, I think I had this issue before
    #Yes

    all_2011_df = acculturation_2011_df.merge(alcohol_use_2011_df, how='outer')
    # okay, let's use a loop
    df_list = [alcohol_use_2011_df,
                bp_cholesterol_2011_df,
               cardiovascular_2011_df,
              consumer_behavior_2011_df,
              demographic_2011_df,
               dermatology_2011_df,
               diabetes_2011_df,
               diet_nutrition_2011_df,
               drug_use_2011_df,
               early_childhood_2011_df,
               food_security_2011_df,
               health_insurance_2011_df,
               health_status_2011_df,
               hospital_access_to_care_2011_df,
               housing_2011_df,
               immunization_2011_df,
               income_2011_df,
               medical_conditions_2011_df,
               mental_health_2011_df,
               occupation_2011_df,
               oral_health_2011_df,
               pesticide_use_2011_df,
               physical_activity_2011_df,
               physical_functioning_2011_df,
               preventative_aspirin_use_2011_df,
               reproductive_2011_df,
               sexual_behavior_2011_df,
               sleep_disorder_2011_df,
               smoking_cigarette_2011_df,
               smoking_recent_tobacco_2011_df,
               urology_2011_df,
               weight_history_2011_df,
              ]
    for df in df_list:
        all_2011_df = all_2011_df.merge(df, how='outer')

    all_2011_df.to_csv('notebooks/all_2011_df.csv', index=False)

    acculturation_2013_df = pd.read_csv('data/raw/2013-2014_acculturation.csv')
    alcohol_use_2013_df = pd.read_csv('data/raw/2013-2014_alcohol_use.csv')
    bp_cholesterol_2013_df = pd.read_csv('data/raw/2013-2014_bp_cholesterol.csv')
    cardiovascular_2013_df = pd.read_csv('data/raw/2013-2014_cardiovascular.csv')
    consumer_behavior_2013_df = pd.read_csv('data/raw/2013-2014_consumer_behavior.csv')
    demographic_2013_df = pd.read_csv('data/raw/2013-2014_demographic.csv')
    dermatology_2013_df = pd.read_csv('data/raw/2013-2014_dermatology.csv')
    diabetes_2013_df = pd.read_csv('data/raw/2013-2014_diabetes.csv')
    diet_nutrition_2013_df = pd.read_csv('data/raw/2013-2014_diet_nutrition.csv')
    drug_use_2013_df = pd.read_csv('data/raw/2013-2014_drug_use.csv')
    early_childhood_2013_df = pd.read_csv('data/raw/2013-2014_early_childhood.csv')
    food_security_2013_df = pd.read_csv('data/raw/2013-2014_food_security.csv')
    health_insurance_2013_df = pd.read_csv('data/raw/2013-2014_health_insurance.csv')
    health_status_2013_df = pd.read_csv('data/raw/2013-2014_health_status.csv')
    hospital_access_to_care_2013_df = pd.read_csv('data/raw/2013-2014_hospital_access_to_care.csv')
    housing_2013_df = pd.read_csv('data/raw/2013-2014_housing.csv')
    immunization_2013_df = pd.read_csv('data/raw/2013-2014_immunization.csv')
    income_2013_df = pd.read_csv('data/raw/2013-2014_income.csv')
    medical_conditions_2013_df = pd.read_csv('data/raw/2013-2014_medical_conditions.csv')
    mental_health_2013_df = pd.read_csv('data/raw/2013-2014_mental_health.csv')
    occupation_2013_df = pd.read_csv('data/raw/2013-2014_occupation.csv')
    oral_health_2013_df = pd.read_csv('data/raw/2013-2014_oral_health.csv')
    pesticide_use_2013_df = pd.read_csv('data/raw/2013-2014_pesticide_use.csv')
    # I can't believe I'm not done yet
    physical_activity_2013_df = pd.read_csv('data/raw/2013-2014_physical_activity.csv')
    physical_functioning_2013_df = pd.read_csv('data/raw/2013-2014_physical_functioning.csv')
    preventative_aspirin_use_2013_df = pd.read_csv('data/raw/2013-2014_preventative_aspirin_use.csv')
    reproductive_2013_df = pd.read_csv('data/raw/2013-2014_reproductive.csv')
    sexual_behavior_2013_df = pd.read_csv('data/raw/2013-2014_sexual_behavior.csv')
    sleep_disorder_2013_df = pd.read_csv('data/raw/2013-2014_sleep_disorder.csv')
    smoking_cigarette_2013_df = pd.read_csv('data/raw/2013-2014_smoking_cigarette.csv')
    smoking_recent_tobacco_2013_df = pd.read_csv('data/raw/2013-2014_smoking_recent_tobacco.csv')
    urology_2013_df = pd.read_csv('data/raw/2013-2014_urology.csv')
    weight_history_2013_df = pd.read_csv('data/raw/2013-2014_weight_history.csv')

    df_list = [alcohol_use_2013_df,
            bp_cholesterol_2013_df,
           cardiovascular_2013_df,
          consumer_behavior_2013_df,
          demographic_2013_df,
           dermatology_2013_df,
           diabetes_2013_df,
           diet_nutrition_2013_df,
           drug_use_2013_df,
           early_childhood_2013_df,
           food_security_2013_df,
           health_insurance_2013_df,
           health_status_2013_df,
           hospital_access_to_care_2013_df,
           housing_2013_df,
           immunization_2013_df,
           income_2013_df,
           medical_conditions_2013_df,
           mental_health_2013_df,
           occupation_2013_df,
           oral_health_2013_df,
           pesticide_use_2013_df,
           physical_activity_2013_df,
           physical_functioning_2013_df,
           preventative_aspirin_use_2013_df,
           reproductive_2013_df,
           sexual_behavior_2013_df,
           sleep_disorder_2013_df,
           smoking_cigarette_2013_df,
           smoking_recent_tobacco_2013_df,
           urology_2013_df,
           weight_history_2013_df,
          ]
          all_2013_df = acculturation_2013_df
          for df in df_list:
              all_2013_df = all_2013_df.merge(df, how='outer')

    all_2013_df.to_csv('notebooks/all_2013_df.csv', index=False)

    acculturation_2015_df = pd.read_csv('data/raw/2015-2016_acculturation.csv')
    alcohol_use_2015_df = pd.read_csv('data/raw/2015-2016_alcohol_use.csv')
    bp_cholesterol_2015_df = pd.read_csv('data/raw/2015-2016_bp_cholesterol.csv')
    cardiovascular_2015_df = pd.read_csv('data/raw/2015-2016_cardiovascular.csv')
    consumer_behavior_2015_df = pd.read_csv('data/raw/2015-2016_consumer_behavior.csv')
    demographic_2015_df = pd.read_csv('data/raw/2015-2016_demographic.csv')
    dermatology_2015_df = pd.read_csv('data/raw/2015-2016_dermatology.csv')
    diabetes_2015_df = pd.read_csv('data/raw/2015-2016_diabetes.csv')
    diet_nutrition_2015_df = pd.read_csv('data/raw/2015-2016_diet_nutrition.csv')
    drug_use_2015_df = pd.read_csv('data/raw/2015-2016_drug_use.csv')
    early_childhood_2015_df = pd.read_csv('data/raw/2015-2016_early_childhood.csv')
    food_security_2015_df = pd.read_csv('data/raw/2015-2016_food_security.csv')
    health_insurance_2015_df = pd.read_csv('data/raw/2015-2016_health_insurance.csv')
    health_status_2015_df = pd.read_csv('data/raw/2015-2016_health_status.csv')
    hospital_access_to_care_2015_df = pd.read_csv('data/raw/2015-2016_hospital_access_to_care.csv')
    housing_2015_df = pd.read_csv('data/raw/2015-2016_housing.csv')
    immunization_2015_df = pd.read_csv('data/raw/2015-2016_immunization.csv')
    income_2015_df = pd.read_csv('data/raw/2015-2016_income.csv')
    medical_conditions_2015_df = pd.read_csv('data/raw/2015-2016_medical_conditions.csv')
    mental_health_2015_df = pd.read_csv('data/raw/2015-2016_mental_health.csv')
    occupation_2015_df = pd.read_csv('data/raw/2015-2016_occupation.csv')
    oral_health_2015_df = pd.read_csv('data/raw/2015-2016_oral_health.csv')
    pesticide_use_2015_df = pd.read_csv('data/raw/2015-2016_pesticide_use.csv')
    physical_activity_2015_df = pd.read_csv('data/raw/2015-2016_physical_activity.csv')
    physical_functioning_2015_df = pd.read_csv('data/raw/2015-2016_physical_functioning.csv')
    prescription_2015_df = pd.read_csv('data/raw/2015-2016_prescription.csv')
    preventative_aspirin_use_2015_df = pd.read_csv('data/raw/2015-2016_preventative_aspirin_use.csv')
    reproductive_2015_df = pd.read_csv('data/raw/2015-2016_reproductive.csv')
    sexual_behavior_2015_df = pd.read_csv('data/raw/2015-2016_sexual_behavior.csv')
    sleep_disorder_2015_df = pd.read_csv('data/raw/2015-2016_sleep_disorder.csv')
    smoking_cigarette_2015_df = pd.read_csv('data/raw/2015-2016_smoking_cigarette.csv')
    smoking_recent_tobacco_2015_df = pd.read_csv('data/raw/2015-2016_smoking_recent_tobacco.csv')
    urology_2015_df = pd.read_csv('data/raw/2015-2016_urology.csv')
    weight_history_2015_df = pd.read_csv('data/raw/2015-2016_weight_history.csv')

    all_2015_df = acculturation_2015_df.merge(alcohol_use_2015_df, how='outer')
    df_list = [alcohol_use_2015_df,
            bp_cholesterol_2015_df,
           cardiovascular_2015_df,
          consumer_behavior_2015_df,
          demographic_2015_df,
           dermatology_2015_df,
           diabetes_2015_df,
           diet_nutrition_2015_df,
           drug_use_2015_df,
           early_childhood_2015_df,
           food_security_2015_df,
           health_insurance_2015_df,
           health_status_2015_df,
           hospital_access_to_care_2015_df,
           housing_2015_df,
           immunization_2015_df,
           income_2015_df,
           medical_conditions_2015_df,
           mental_health_2015_df,
           occupation_2015_df,
           oral_health_2015_df,
           pesticide_use_2015_df,
           physical_activity_2015_df,
           physical_functioning_2015_df,
           prescription_2015_df,
           preventative_aspirin_use_2015_df,
           reproductive_2015_df,
           sexual_behavior_2015_df,
           sleep_disorder_2015_df,
           smoking_cigarette_2015_df,
           smoking_recent_tobacco_2015_df,
           urology_2015_df,
           weight_history_2015_df,
          ]
    for df in df_list:
        all_2015_df = all_2015_df.merge(df, how='outer')

    all_2015_df.to_csv('notebooks/all_2015_df.csv', index=False)

    all_2011_df = pd.read_csv('all_2011_df.csv')
    all_2013_df = pd.read_csv('all_2013_df.csv')
    all_2015_df = pd.read_csv('all_2015_df.csv')

    all_data_df = pd.concat([all_2011_df, all_2013_df, all_2015_df], axis=0)

    all_data_df.to_csv('notebooks/all_data_df.csv', index=False)
