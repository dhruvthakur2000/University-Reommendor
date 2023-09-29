import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from dataclasses import dataclass
from data_transformation import DataTransformation
from data_transformation import DataTransformationConfig
#from src.COMPONENTS.model_training import ModelTrainer
#from src.COMPONENTS.model_training import ModelTrainerConfig

###data class decorator are used only when you have only variables inside the class if there are other methods then simply use init method
@dataclass
class dataIngenstionConfig:
    #train_data_path:str=os.path.join("\Univ-prdictor",'artifacts',"train.csv")
    #test_data_path:str=os.path.join("\Univ-prdictor",'artifacts',"train.csv")
    raw_data_path:str=os.path.join("artifacts","data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestionConfig=dataIngenstionConfig() 

    def initiate_data_ingestion(self):
        logging.info("entered data ingestion method")
        try:
            df=pd.read_csv("data_given\clean_sample_50k.csv")
            
            logging.info("read data as df")


            #here we are using only .train data path as till the previous folder the path will be same as the last file name is not taken into consideration
            #os.path.dirname will extract the directory part of the train_data_path and removes the last component of the path (the filename) 
            # and gives you the path to the directory where the file should be located.
            os.makedirs(os.path.dirname(self.ingestionConfig.raw_data_path),exist_ok=True)

            df.to_csv(self.ingestionConfig.raw_data_path,index=False,header=True)

            logging.info("ingestion process completed ")

            return self.ingestionConfig.raw_data_path
        
        except Exception as e:
            raise CustomException(e,sys)

    

if __name__=="__main__":
    obj=DataIngestion()
    data=obj.initiate_data_ingestion()
    
    data_transformation=DataTransformation()
    train_arr,_=data_transformation.initiate_data_transformation(data)