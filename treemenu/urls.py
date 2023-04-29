from django.urls import path, re_path
from django.contrib.auth import views as authViews
from .views import *

urlpatterns = [
    path('', home, name='home'),
    re_path(r'^Order/(?P<url_to_process>.*)/$', order, name='order'),
]