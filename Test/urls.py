from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('count/', views.count, name = 'count'),
    path('results/', views.cresultrs, name='results')
    ]
