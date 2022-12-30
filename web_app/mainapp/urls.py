from django.urls import path

from mainapp.views import record

urlpatterns = [
    # path('', record),
    path('<int:pk>', record),
]
