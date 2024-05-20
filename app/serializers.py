from rest_framework import serializers

class Lung(serializers.Serializer):
  GENDER = serializers.IntegerField()
  AGE  = serializers.IntegerField()
  SMOKING = serializers.IntegerField()
  YELLOW_FINGERS = serializers.IntegerField()
  ANXIETY = serializers.IntegerField()
  PEER_PRESSURE = serializers.IntegerField()
  CHRONIC_DISEASE = serializers.IntegerField()
  FATIGUE = serializers.IntegerField()
  ALLERGY = serializers.IntegerField()
  WHEEZING = serializers.IntegerField()
  ALCOHOL_CONSUMING = serializers.IntegerField()
  COUGHING = serializers.IntegerField()
  SHORTNESS_OF_BREATH = serializers.IntegerField()
  SWALLOWING_DIFFICULTY = serializers.IntegerField()
  CHEST_PAIN   = serializers.IntegerField()

  def validate_GENDER(self,value):
    value = int(value)
    if(value == 1 or value == 0):
      return value
    raise ValueError("Invalid Gender")
  
  def validate_AGE(self,value):
    value = int(value)
    if(value > 0 and value < 100):
      return value
    raise ValueError("Invalid AGE")

  def validate_SMOKING(self,value):
    value = int(value)
    if(value == 1 or value == 2):
      return value
    raise ValueError("Invalid Smoking Input")

  def validate_YELLOW_FINGERS(self,value):
    value = int(value)
    if(value == 1 or value == 2):
      return value
    raise ValueError("Invalid Yellow_Fingers Input")    
  
  def validate_ANXIETY(self,value):
    value = int(value)
    if(value == 1 or value == 2):
      return value
    raise ValueError("Invalid ANXIETY Input")
  
  def validate_PEER_PRESSURE(self,value):
    value = int(value)
    if(value == 1 or value == 2):
      return value
    raise ValueError("Invalid PEER_PRESSURE Input")

  def validate_CHRONIC_DISEASE(self,value):
    value = int(value)
    if(value == 1 or value == 2):
      return value
    raise ValueError("Invalid CHRONIC_DISEASE Input")
  
  def validate_FATIGUE(self,value):
    value = int(value)
    if(value == 1 or value == 2):
      return value
    raise ValueError("Invalid FATIGUE Input")

  def validate_ALLERGY(self,value):
    value = int(value)
    if(value == 1 or value == 2):
      return value
    raise ValueError("Invalid ALLERGY Input")
  
  def validate_WHEEZING(self,value):
    value = int(value)
    if(value == 1 or value == 2):
      return value
    raise ValueError("Invalid WHEEZING Input")

  def validate_ALCOHOL_CONSUMING(self,value):
    value = int(value)
    if(value == 1 or value == 2):
      return value
    raise ValueError("Invalid ALCOHOL_CONSUMING Input")

  def validate_COUGHING(self,value):
    value = int(value)
    if(value == 1 or value == 2):
      return value
    raise ValueError("Invalid COUGHING Input")

  def validate_SHORTNESS_OF_BREATH(self,value):
    value = int(value)
    if(value == 1 or value == 2):
      return value
    raise ValueError("Invalid SHORTNESS_OF_BREATH Input")     

  def validate_SWALLOWING_DIFFICULTY(self,value):
    value = int(value)
    if(value == 1 or value == 2):
      return value
    raise ValueError("Invalid SWALLOWING_DIFFICULTY Input")         
    
  def validate_CHEST_PAIN(self,value):
    value = int(value)
    if(value == 1 or value == 2):
      return value
    raise ValueError("Invalid CHEST_PAIN Input")  