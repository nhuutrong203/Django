from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('huutrong', views.huutrong, name="huutrong"),
    path('<str:name>',views.greeting, name="greeting")
]