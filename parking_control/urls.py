from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from core.api.viewsets import ParkingViewSet

router = routers.DefaultRouter()
router.register(r'parking', ParkingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path(':plate', include(router.urls)),
    # path('parking/:pk/out', out, name='parking-out'),
    # path('pay', views.pay),
    # path('admin/', admin.site.urls),
    # path('api-auth/', include('rest_framework.urls')),
]
