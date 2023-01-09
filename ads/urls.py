from django.urls import path
from .views import *

app_name = 'ads'

urlpatterns = [
    path('', CategoriesList.as_view(), name='categories_list'),
    path('add/', AddCategoryForm.as_view(), name='category_add'),
    path('<str:cat_name>/edit/', EditCategoryForm.as_view(), name='category_edit'),
    path('<str:cat_name>/add/', AddAdvertisementForm.as_view(), name='advertisement_add'),
    path('<str:cat_name>/', AdvertisementsList.as_view(), name='advertisements_list'),
    path('<str:cat_name>/<int:ad_id>/', AdvertisementDetail.as_view(), name='advertisement_detail'),
    path('<str:cat_name>/<int:ad_id>/edit/', EditAdvertisementForm.as_view(), name='advertisement_edit'),
    # path('home/', HomePage.as_view(), name='home_page'),
]
