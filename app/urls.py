from django.urls import path,include
from app.controller.lungpredictController import LungCancerPredict
from app.controller.breastpredictController import BreastCancerPredict

urlpatterns = [
  path('lung-predict',LungCancerPredict.as_view()),
  path('breast-predict',BreastCancerPredict.as_view()),    
]