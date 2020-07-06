from django.contrib import admin
from django.urls import include, path
from handler import urls
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('handler.api.urls')),
    path('token-auth/', obtain_jwt_token)
]
