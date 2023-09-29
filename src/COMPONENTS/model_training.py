import os
import sys
from dataclasses import dataclass
from sklearn.neighbors import KNeighborsClassifier
from src.utils import save_object
from src.logger import logging
from src.exception import CustomException

@dataclass
class ModelTrainerConfig:
    trained_model_file_path=os.path.join('artifacts','model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()
    
    def initiate_model_trainer(self,train_arr):
        try:
            logging.info(f"Spliting features and labels")
            X_train,Y_train=(train_arr[:,:-1],
            train_arr[:,-1]
            )
            model={"K-nearest Neighbours":KNeighborsClassifier()}

            model.values()[0].fit(X_train,Y_train)



        except:
            pass