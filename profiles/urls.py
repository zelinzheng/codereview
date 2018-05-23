from django.conf.urls import url
from .views import sign_up
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^sign-up/$', sign_up, name='sign-up'),
    url(r'sign-in/$', auth_views.login,
        {'template_name':'profiles/sign_in.html'},
        name='sign-in'
        ),
    url(r'^log-out/$', auth_views.logout,
        {'next_page': '/'},
        name='log-out'),


]