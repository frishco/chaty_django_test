from django.conf.urls import url
from django.urls import path
from RestAPI import views

urlpatterns = [
    url(r'^erase$', views.DeleteEventsView.as_view()),
    url(r'^events/$', views.EventCreateListView.as_view()),
    url(r'^events/actors/(?P<pk>.+)/$', views.ActorsEventsView.as_view()),
    url(r'^actors/$', views.ActorsList.as_view()),
]
