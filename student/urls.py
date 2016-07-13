'''
Created on 11-Jul-2016

@author: aayush.agrawal
'''
from views import LoginView,ProfileView,HobbyView,RegisterView,SearchView,SuggestionsView
from django.conf.urls import url
from django.conf import settings
from django.conf.urls import patterns
from django.conf.urls.static import static
from . import views
from django.contrib.auth.decorators import login_required
urlpatterns = [
    # url(r'^', views.index, name='index'),
    # url(r'^about/', MyView.as_view()),
    url(r'^register/',RegisterView.as_view(), name='register'),
    url(r'^login/',LoginView.as_view(), name='login'),
    url(r'^profile/',login_required(ProfileView.as_view()), name='profile'),
    url(r'^hobby/(?P<roll_no>[\w\-]+)',HobbyView.as_view(), name='hobby'),
    url(r'^hobby/',HobbyView.as_view(), name='hobby'),
    url(r'^aboutus/',views.About, name='aboutus'),
    url(r'^search/',SearchView.as_view(), name='search'),
    url(r'^suggestions/',SuggestionsView.as_view(), name='suggestions'),
    url(r'^logout/',views.Logout, name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )