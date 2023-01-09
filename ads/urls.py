from django.urls import path
from .views import *

app_name = 'ads'

urlpatterns = [
    path('', CategoriesList.as_view(), name='categories_list'),
    path('add/', AddCategoryForm.as_view(), name='category_add'),
    path('<str:category>/edit/', EditCategoryForm.as_view(), name='category_edit'),
    path('<str:category>/add/', AddAdvertisementForm.as_view(), name='advertisement_add'),
    path('<str:category>/', AdvertisementsList.as_view(), name='advertisements_list'),
    path('<str:category>/<int:ad_id>/', AdvertisementDetail.as_view(), name='advertisement_detail'),
    path('<str:category>/<int:ad_id>/edit/', EditAdvertisementForm.as_view(), name='advertisement_edit'),
    # path('home/', HomePage.as_view(), name='home_page'),
]
