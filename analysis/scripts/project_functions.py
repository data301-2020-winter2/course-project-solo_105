import pandas as pd
import numpy as np

def load_and_process(url_or_path_to_csv_file):
    df = (pd.read_csv(url_or_path_to_csv_file)
          .rename(columns={'age':'Age','sex':'Sex','bmi':'BMI','children':'Children',
                           'smoker':'Smoker','region':'Region','charges':'Charges'})
          .dropna()
          .reset_index()
          .drop(['index'], axis=1)
          .drop_duplicates()
          .sort_values(by = ['Age'])
          .assign(Risk= lambda x: x['BMI'].apply(lambda y: "Under Weight" if y < 18.5 else
                                                 ("Healthy Weight" if 18.5 <= y < 25 else
                                                  ("Over Weight" if 25 <= y < 30 else "Obese"))))
         )
    return df 