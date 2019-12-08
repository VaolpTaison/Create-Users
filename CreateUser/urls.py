from django.contrib import admin
from django.urls import path
from Users.views import Register
from rest_framework.authtoken import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Register, name='register'),
]
