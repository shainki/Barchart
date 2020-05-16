from django.urls import include, path
from django.views.generic import TemplateView
from .views import show


urlpatterns=[
    path('page', show.as_view(), name='view')

]
