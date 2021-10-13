from django.urls import path
from . import views

app_name = 'myapp1'

urlpatterns = [
    
    path('', views.root.as_view(), name="index"),
    path('index', views.MyIndexView.as_view(), name="my_index_view"),
    path('dashboard', views.Dashboard.as_view(), name="dashboard"),
    path('after', views.After.as_view(), name="after_appointment_view"),

]