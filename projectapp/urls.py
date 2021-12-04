from django.urls.conf import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
    path('login/', views.login)
]
