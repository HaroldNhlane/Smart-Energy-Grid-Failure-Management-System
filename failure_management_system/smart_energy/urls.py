# failure_management_system/smart_energy/urls.py (App Level)

from django.urls import path
from . import views

urlpatterns = [ # <--- This line should also be at the top level of the file
    path('', views.home_page, name='home'),
]