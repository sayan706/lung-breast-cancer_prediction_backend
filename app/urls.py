from django.urls import path,include
# from cancer.controller.lungpredictController import LungCancerPredict
# from cancer.controller.breastpredictController import BreastCancerPredict
from app.controller.lungpredictController import LungCancerPredict

urlpatterns = [
    path('lung-predict',LungCancerPredict.as_view()),    
]