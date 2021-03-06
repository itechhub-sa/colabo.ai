from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'^\Z$', views.SignIn.as_view(), name='signin'),
    url(r'^home/$', views.Home.as_view(), name='home'),
    url(r'^signin/$', views.SignIn.as_view(), name='signin'),
    url(r'^signup/$', views.SignUp.as_view(), name='signup'),
    url(r'^data/$', views.GetData.as_view(), name='data'),
    url(r'^sims/$', views.EmployeeDetails.as_view(), name='sims'),
    url(r'^rand/$', views.EmployeeRandomDetails.as_view(), name='rand'),
    url(r'^rands/$', views.EmployeeRandomXDetails.as_view(), name='rands'),
    url(r'^randx/$', views.EmployeeRandomYDetails.as_view(), name='randx'),

]
