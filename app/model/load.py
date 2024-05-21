import pickle,os
from django.conf import settings

def loadlungmodel(inp):
  try:
    os.chdir(settings.BASE_DIR)
    scaler = "scaler.pkl"
    model = "lung_cancer_model.pkl"
    scaler=pickle.load(open(scaler,"rb"))
    user_input = scaler.transform([inp])
    model=pickle.load(open(model,"rb"))
    modelPrediction=model.predict(user_input)

    if(modelPrediction == 1):
      return "You have a high probability of Lung Cancer. Please Consult with the Doctor and Professionals to avoid Risks."
    else:
      return "There is no such probability of Lung Cancer, for any further confirmation please reach out to Professionals and Doctors. Thank You!"
    
  except Exception as e:
    raise Exception(str(e))

def loadbreastmodel(inp):
  try:
    os.chdir(settings.BASE_DIR)
    scaler = "scaler_2.pkl"
    model = "breast_cancer_model.pkl"
    scaler=pickle.load(open(scaler,"rb"))
    user_input = scaler.transform([inp])
    model=pickle.load(open(model,"rb"))
    modelPrediction=model.predict(user_input)

    if(modelPrediction == 1):
      return "You have a high probability of having Malignant Tumor. Please Consult with the Doctor and Professionals to avoid Risks."
    else:
      return "There is no such probability of having Malingnant Tumor, for any further confirmation please reach out to Professionals and Doctors. Thank You!"
    
  except Exception as e:
    raise Exception(str(e))



