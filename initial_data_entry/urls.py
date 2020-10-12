from django.urls import path
from .views import *

urlpatterns = [
    
    path('', PersonCreate, name="entry"),
    path('in-out', InOut, name="in_out"),
    path('index', index, name="index"),
    path('iolisting', IssuedWeaponList, name="iolist"),
    path('returnweapon/<int:pk>', returnweapon, name="returnweapon"),
    path('today-in-out', TodayWeaponList, name="today-in-out"),
    path('export/csv', export_users_csv, name='export_users_csv'),

    

]