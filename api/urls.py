from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('menus/', views.getMenus),
    path('menus/create/', views.createMenu),
    path('menus/<str:pk>/update', views.updateMenu),
    path('menus/<str:pk>/delete', views.deleteMenu),
    path('menus/<str:pk>/', views.getMenu),
    

]