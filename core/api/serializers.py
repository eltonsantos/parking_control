from rest_framework.serializers import ModelSerializer
from core.models import Parking

class ParkingSerializer(ModelSerializer):
  class Meta:
    model = Parking
    fields = ('plate', )