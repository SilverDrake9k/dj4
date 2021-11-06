from django.urls import include, path
from django.conf.urls import url
from . import views
app_name = 'cats'
urlpatterns = [
    path('', views.CatList.as_view(), name='all'),
    path('main/create/', views.CatCreate.as_view(), name='cat_create'),
    path('main/<int:pk>/update/', views.CatUpdate.as_view(), name='cat_update'),
    path('main/<int:pk>/delete/', views.CatDelete.as_view(), name='cat_delete'),
    path('breed/', views.BreedList.as_view(), name='breed_all'),
    path('breed/create/', views.BreedCreate.as_view(), name='breed_create'),
    path('breed/<int:pk>/update/', views.BreedUpdate.as_view(), name='breed_update'),
    path('bread/<int:pk>/delete/', views.BreedDelete.as_view(), name='breed_delete'),
]