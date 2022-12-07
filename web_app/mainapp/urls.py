from django.urls import path

from mainapp.views import record

urlpatterns = [
    path('/<int:pk>', record, name='detail'),
]
