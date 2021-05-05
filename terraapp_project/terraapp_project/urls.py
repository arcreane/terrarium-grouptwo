from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('terrarium/', include('terrarium.urls')),
    path('admin/', admin.site.urls),
]