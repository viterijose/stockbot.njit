from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gainers', views.gainers, name='gainers'),
    path('losers', views.losers, name='losers'),
    path('pennystocks', views.pennystocks, name='pennystocks'),
    path('techstocks', views.techstocks, name='techstocks'),
    path('overall',views.overall,name='overall'),
    path('homes',views.homes,name='homes')
]