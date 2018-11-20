from django.conf.urls import url
from . import views
app_name="studentapp"

urlpatterns=[
    url('^$',views.home,name='home'),
    url('^insert$',views.insert,name='insert'),
    url('^display$',views.display,name='display'),

]
