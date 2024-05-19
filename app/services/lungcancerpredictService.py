from app.model.load import loadlungmodel
from app.serializers import Lung

class LungCancerPredictService:
    
    def __init__(self,request:dict) -> None:
        self.request=request
        self.dataList=[]
        self.convert()

    def convert(self):
        serializer=Lung(data=self.request.data)
        print(serializer.is_valid())
        print(serializer.validated_data)
        if (serializer.is_valid()):          
          for i in serializer.validated_data:
            self.dataList.append(serializer.validated_data.get(i))
        else:
            raise Exception(str(serializer.errors))

    def predict(self):
        try:
            return loadlungmodel(self.dataList)
        except Exception as e:
            print(e)
            raise Exception(str(e))