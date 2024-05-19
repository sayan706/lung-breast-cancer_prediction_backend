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
      return "Yes! You are effected by Lung Cancer"
    else:
      return "No! You are not effected by Lung Cancer"
    
  except Exception as e:
    raise Exception(str(e))




