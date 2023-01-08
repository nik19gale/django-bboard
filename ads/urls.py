from django.urls import path, include
from .views import *

urlpatterns = [
    path('', CategoriesList.as_view(), name='categories_list'),
    path('category/add/', CategoryAdd.as_view(), name='category_add'),
    path('category/<str:cat_name>/edit/', CategoryEdit.as_view(), name='category_edit'),
    path('category/<str:cat_name>/<int:page>/', AdvertisementsList.as_view(), name='advertisements_list'),
    path('advertisement/add/', AdvertisementAdd.as_view(), name='advertisement_add'),
    path('advertisement/<int:ad_id>/edit/', AdvertisementEdit.as_view(), name='advertisement_edit'),
    path('advertisement/<int:ad_id>/', AdvertisementDetail.as_view(), name='advertisement_detail'),
]
