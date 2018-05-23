from django.conf.urls import url
from . import views as polls_views

urlpatterns = [
    url(r'^signup/$', polls_views.signup, name='signup'),
]