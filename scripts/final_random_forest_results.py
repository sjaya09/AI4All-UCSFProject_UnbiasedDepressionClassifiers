import pandas as pd
import os
import numpy as np
from  sklearn.model_selection import train_test_split

from sklearn.pipeline import Pipeline

from sklearn.decomposition import PCA
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler

from sklearn.discriminant_analysis import LogisticRegression

from sklearn.metrics import roc_auc_score
from sklearn.metrics import confusion_matrix

from sklearn.inspection import permutation_importance

from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.model_selection import GridSearchCV

if __name__ == '__main__':

    all_data_df = pd.read_csv('notebooks/all_data_df.csv')
    all_data_df.index = all_data_df['SEQN']

    mental_health_df = all_data_df.loc[:, 'DPQ010':'DPQ100'].dropna(how='all')
    all_data_df = all_data_df.loc[mental_health_df.index]

    def mh(x):
        if x == '\.':
            return 'missing'
        elif x == 1:
            return 'several days'
        elif x == 2:
            return 'more than half the days'
        elif x == 3:
            return 'nearly every day'
        elif x == 7:
            return 'refused'
        elif x == 9:
            return "don't know"
        else:
            return 'not at all'

    for col in mental_health_df.columns:
        mental_health_df[col] = mental_health_df[col].apply(lambda x: mh(x))

    def calc(row):
        sum = 0
        for i in ['DPQ010', 'DPQ020', 'DPQ030', 'DPQ040',
                  'DPQ050', 'DPQ060', 'DPQ070','DPQ080',
                  'DPQ090', 'DPQ100']:
            if row[i] == 'several days':
                sum += 1
            if row[i] == 'more than half the days':
                sum += 2
            if row[i] == 'nearly every day':
                sum += 3
        return sum
    mental_health_df['labels_raw'] = mental_health_df.apply(calc, axis=1)
    mental_health_df['labels'] = mental_health_df['labels_raw'].apply(lambda x: 1 if x >= 10 else 0)

    features = [
        'DIQ170',
        'SLQ050',
        'PAQ620',
        'PAQ640',
        'PAQ650',
        'PAQ665',
        'PAQ715',
        'WHQ030',
        'WHQ040',
        'HUQ010',
        'HUQ020',
        'HUQ090',
        'HSD010',
        'HSQ500',
        'HSQ590',
        'INQ090',
        'INQ140',
        'IND235',
        'HOQ065',
        'OCD150',
        'OCQ180',
        'OCD270',
        'OCQ380',
        'DBQ700',
        'DUQ210',
        'DUQ211',
        'DUQ213',
        'DUQ215Q',
        'DUQ219',
        'DUQ220U'
    ]
    X = all_data_df[features]
    y = mental_health_df['labels']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    X_val, X_test, y_val, y_test = train_test_split(X_test, y_test, test_size=0.5, random_state=42)

    rf_pipe = Pipeline([
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('enc', OneHotEncoder(sparse=False, handle_unknown='ignore')),
        ('red', PCA(n_components=3)),
        ('clf', LogisticRegression(shrinkage=0, solver='lsqr'))
    ])
    rf_pipe.fit(X_train, y_train)
    rf_training_score = roc_auc_score(y_train.values, rf_pipe.predict_proba(X_train)[:, 1])
    rf_validation_score = roc_auc_score(y_val.values, rf_pipe.predict_proba(X_val)[:, 1])
    rf_test_score = roc_auc_score(y_test.values, rf_pipe.predict_proba(X_test)[:, 1])
    final_rf_results_df = pd.DataFrame(data=['rf_training_score','rf_validation_score','rf_test_score'], columns=['scores'])
    final_rf_results_df.to_csv('notebooks/final_rf_results.csv', index=False)
