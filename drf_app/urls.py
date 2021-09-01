from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api/user/$', views.UserView.as_view()),
    url(r'^api/seminar/$', views.SeminarView.as_view()),
    url(r'^api/section/$', views.SectionView.as_view()),
]