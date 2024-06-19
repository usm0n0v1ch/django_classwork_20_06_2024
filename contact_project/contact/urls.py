from django.urls import path

from contact import views

urlpatterns = [
    path('', views.contact_view, name='contact'),
    path('thanks/', views.thanks_view, name='thanks'),
]