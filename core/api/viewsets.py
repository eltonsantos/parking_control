from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from core.models import Parking
from .serializers import ParkingSerializer

class ParkingViewSet(ModelViewSet):
    queryset = Parking.objects.all()
    serializer_class = ParkingSerializer
    lookup_field = ('plate')

    # def get_queryset(self):
    #     id = self.request.query_params.get('id')
    #     plate = self.request.query_params.get('plate')
    #     queryset = Parking.objects.all()

    #     if id:
    #         queryset = queryset.filter(pk=id)

    #     if plate:
    #         queryset = queryset.filter(plate__iexact=plate)

    #     return queryset

    # def list(self, request, *args, **kwargs):
    #     return super(Parking, self).list(request, *args, **kwargs)


    @action(methods=['put'], detail=True)
    def pay(self, request, pk=None):
        pass

    @action(methods=['put'], detail=True)
    def out(self, request, pk=None):
        pass
