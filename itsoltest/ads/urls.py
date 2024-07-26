from django.urls import path
from .views import AdvertisementDetail, register

urlpatterns = [
    path('ads/<int:ad_id>/', AdvertisementDetail.as_view(), name='ad-detail'),
    path('register/', register, name='register'),
]
