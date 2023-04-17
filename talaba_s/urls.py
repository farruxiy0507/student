from django.urls import path
from .views import talaba


urlpatterns = [
    path('talaba/', talaba, name='talaba'),
]
