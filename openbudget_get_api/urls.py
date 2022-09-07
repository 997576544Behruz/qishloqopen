from django.urls import path
from .views import home, home1, exam

urlpatterns = [
    path('', home, name="home"),
    path('home1', home1, name="home1"),
    path('exam', exam, name="exam"),
]