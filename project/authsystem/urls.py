from django.conf.urls import patterns, url


from project.authsystem import views

urlpatterns = patterns('',
    url(r'^$', views.HomePage.as_view(), name='home'),
)
