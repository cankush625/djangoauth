from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('basicauth/', include('basicauth.urls')),
    path('tokenauth/', include('tokenauth.urls'))
]
