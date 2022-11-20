from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('weather/', include('weather.urls')),
    path('captcha/', include('captcha.urls')),
    path('', include('portfolio.urls')),
]
