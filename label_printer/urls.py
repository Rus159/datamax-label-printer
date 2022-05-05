from . import views
from django.urls import re_path


urlpatterns = [
    re_path('', views.print_labels, name='print-labels'),
]
