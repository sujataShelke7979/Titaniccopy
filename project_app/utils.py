import numpy as np
import pandas as pd
import pickle
import json
import warnings
warnings.filterwarnings("ignore")
import config
class Titanic():
    def __init__(self,Pclass,Gender,Age,SibSp,Parch,Fare,Embarked):
        self.Pclass=Pclass
        self.Gender=Gender
        self.Age=Age
        self.SibSp=SibSp
        self.Parch=Parch
        self.Fare=Fare
        self.Embarked=Embarked

    def load_models(self):
        with open(config.MODEL_FILE_PATH,"rb") as f:
            self.model=pickle.load(f)

        with open(config.JSON_FILE_PATH,"r") as f:
            self.json_data=json.load(f)     

    def get_predicted(self):
        
        self.load_models()  
        
        test_array=np.zeros(len(self.json_data["columns"]))
       
        test_array[0]=self.Pclass
        test_array[1]=self.json_data["Gender"][self.Gender]
        test_array[2]=self.Age
        test_array[3]=self.SibSp
        test_array[4]=self.Parch
        test_array[5]=self.Fare
        test_array[6]=self.json_data["Embarked"][self.Embarked]
        print("test array -->\n",test_array)
        charges=round(self.model.predict([test_array])[0],2) 
        return charges
if __name__== "__main__":
    Pclass=3.00
    Gender="male"
    Age=22.00
    SibSp=1.00
    Parch=0.00
    Fare=7.25
    Embarked="S"
    
    
    tat_pri=Titanic(Pclass,Gender,Age,SibSp,Parch,Fare,Embarked)
    premium=tat_pri.get_predicted_charges()
    print("Predicted Prices:",premium,"/-rs")        


