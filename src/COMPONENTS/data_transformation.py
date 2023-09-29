import sys
import os
import pandas as pd
import numpy as np
from src.exception import CustomException
from src.logger import logging
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from dataclasses import dataclass
from src.constants import Major_groups
import sklearn

from sklearn.pipeline import Pipeline
from utils import save_object




@dataclass
class DataTransformationConfig():
    preprcessor_obj_file_path=os.path.join('artifacts',"preprocessor.pkl")

class DataTransformation():
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()
        
    def convert_10pt_to_4pt(self,score):
        def CGPA_Convertor(score):
             return (score/10)*4                
        return CGPA_Convertor(score) if score > 4 else score

    def remove_nan_values(self, data):
    # Remove rows with NaN values in any column
        data = data.dropna()
        return data    

    def major_grouping(self,data):
        data['Major_groups']=data['Major'].map(Major_groups).fillna(data['Major'])
        return data
        

    def get_data_transformer_object(self):
        try:
            columns=['Major','Program','Q_Score', 'V_Score', 'AWA_Score', 'GPA_Score', 'University']
            num_columns=['Q_Score', 'V_Score', 'AWA_Score', 'GPA_Score']
            
            pipeline=Pipeline(
                steps=[
                    ("scaler",StandardScaler())
                ]
            )
            logging.info(f"columns :{columns}")
            logging.info(f"numerical columns:{num_columns}")
            
            preprocessor=ColumnTransformer(
                [
                    ("pipeline",pipeline,num_columns)
                ]
            )
            return preprocessor
        
        except Exception as e:
            raise CustomException(e,sys)



    def data_standard_form(self,data):
        try: 
            data = data[(data['Program'].str.contains("PhD") | data['Program'].str.contains("Masters")) & (data['Status'] == 'Accepted')]
            data = data[['Major','Program','Q_Score', 'V_Score', 'AWA_Score', 'GPA_Score', 'University']]
            data = self.remove_nan_values(data)
            data = self.major_grouping(data)
            data['GPA_Scores'] = data['GPA_Score'].apply(self.convert_10pt_to_4pt)
            return data

        except Exception as e:
            raise CustomException(e,sys)
    

    def initiate_data_transformation(self,data_path):
        try:
            data=pd.read_csv(data_path)
            logging.info("Reading data completed")

            logging.info("Obtaining data preprocessing object")
            preprocessing_obj=self.get_data_transformer_object()


            logging.info("Transforming data into standard form")
            transformed_data = self.data_standard_form(data)


            target_col=transformed_data['University']
            transformed_data_features=transformed_data[['Q_Score', 'V_Score', 'AWA_Score', 'GPA_Score']]

            data_features_arr=preprocessing_obj.fit_transform(transformed_data_features)

            train_features=np.c_[transformed_data_features,np.array(target_col)]
            logging.info("Transformed data into standard form")
            logging.info(f"Saving preprocessing object")
            save_object(file_path=self.data_transformation_config.preprcessor_obj_file_path,
                obj=preprocessing_obj
            )


            return (
                train_features,
                preprocessing_obj
            )

        except Exception as e:
            raise CustomException(e,sys)