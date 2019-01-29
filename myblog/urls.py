from django.urls import path
from .views import home, about

urlpatterns = [
    path('', home, name='myblog'),
    path('about/', about, name='myblog-about')
]
