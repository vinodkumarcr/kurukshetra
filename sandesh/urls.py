from django.urls import path
from . import views

urlpatterns=[
    path('',views.regista),
    path('main/',views.main,name='name')

]
