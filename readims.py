import pandas as pd 
import logging 
from pathlib import Path 
from sqlalchemy import create_engine

logging.basicConfig(level=logging.INFO)

input_paths=Path(r"C:\Users\Ravindra Chilhate\OneDrive\Desktop\keggel projects\readmission_dataset.csv") 

class readins:
    def __init__(self,input_paths):
        self.input_paths=input_paths

    def extract(self):
        logging.info("Rading files") 
        df=pd.read_csv(self.input_paths)
        return df 

    def file_infos(self,df):
        logging.info("Got the basic info......")
        print("TOP 5 rows \n",df.head(5))
        print("shape or data \n",df.shape)
        print("basic info \n",df.info())
        print("check nulls \n",df.isna())
        print("show duplicated \n",df.duplicated())
        # print("drop duplicateded \n",df.drop_duplicated())

        return df
    def transform(self,df):
        logging.info("Transforming data ")
        df['patient_id']=df['patient_id']
        df['age']=df['age'].fillna(0)
        df['gender']=df['gender'].str.strip()
        df['admission_type']=df['admission_type'].str.lower()
        df['primary_diagnosis_code']=df['primary_diagnosis_code'].str.strip()
        df['num_prior_admissions']=df['num_prior_admissions'].fillna(0)
        df['time_in_hospital']=df['time_in_hospital'].fillna(0)
        df['num_lab_procedures']=df['num_lab_procedures'].fillna(0)
        df['num_medications']=df['num_medications'].fillna(0)
        df['has_comorbidity']=df['has_comorbidity'].fillna(0)
        df['discharge_disposition']=df['discharge_disposition'].fillna(0)
        df['insurance_type']=df['insurance_type'].str.upper()
        df['hospital_id']=df['hospital_id'].fillna(0)
        logging.info("transforming complited successfuly ")

        return df 
    def loads(self,df):
         logging.info("loding data  ")

         engine = create_engine("mysql+pymysql://root:root@localhost:3306/hospitals?charset=utf8mb4")
         df.to_sql("meri_table", engine, if_exists="append", index=False, chunksize=10000, method="multi")


    def run(self):
        try:
            df=self.extract()
            df=self.file_infos(df)
            df=self.transform(df)
            df=self.loads(df)
            logging.info("pipeline complited succesfully")

        except Exception as e:
                   logging.error(f"piprline failde{e}")

pipelines= readins(input_paths)   

pipelines.run()                 