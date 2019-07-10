from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('charts', views.ChartView.as_view(), name='charts')
]

#    url(r'^api/data/$', get_data, name='api-data')
