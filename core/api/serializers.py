from rest_framework.serializers import ModelSerializer
from core.models import Parking

class ParkingSerializer(ModelSerializer):
  class Meta:
    model = Parking
    fields = ('id', 'plate', 'time', 'paid', 'left')
    lookup_field = 'plate'
    extra_kwargs = {
      'url': {'lookup_field': 'plate'}
    }