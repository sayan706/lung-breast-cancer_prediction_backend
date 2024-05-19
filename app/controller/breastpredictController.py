from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime

from app.services import breastcancerpredictService

class BreastCancerPredict(APIView):

    def post(self,request):
        try:
            predict=breastcancerpredictService.BreastCancerPredictService(request=request)
            res=predict.predict()
            return Response({"message":res,"timestamp":datetime.timestamp(datetime.now())},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message":str(e),"timestamp":datetime.timestamp(datetime.now())},status=status.HTTP_400_BAD_REQUEST)