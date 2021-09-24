from simple.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'data', Data_view, basename='data')