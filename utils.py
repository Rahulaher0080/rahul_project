import numpy as np
import json
import pickle
import config

class HealthInsurance():
    def __init__(self,user_data):
        self.user_data = user_data
        self.model_path = config.MODEL_FILE_PATH
        self.project_path = config.PROJECT_FILE_PATH 

    def load_saved_data(self):
        with open(self.model_path,"rb") as f:
            self.model = pickle.load(f)

        # with gzip.open("lin_model.gzip","rb") as f:
        #       self.model = pickle.load(f)


        with open(self.project_path,"r") as f:
            self.project_data = json.load(f)
       
       
    def pred_health(self):
        self.load_saved_data()

        sex = self.user_data["sex"]
        smoker = self.user_data["smoker"]
        region = self.user_data["region"]

        sex = self.project_data["sex"][sex]    
        smoker = self.project_data["smoker"][smoker]

        region = "region_"+ region  
        region_index = self.project_data["columns"].index(region)

        test_array = np.zeros(len(self.project_data['columns']))
        test_array[0] = eval(self.user_data["age"])
        test_array[1] = sex
        test_array[2] = eval(self.user_data["bmi"])
        test_array[4] = eval(self.user_data["children"])
        test_array[5] = smoker
        test_array[region_index] = 1

        pred1_charges = self.model.predict([test_array])[0]
        print("Predicted charges are : ",pred1_charges)
        return pred1_charges


if __name__ == "__main__":
    obj =  HealthInsurance()
    obj         


