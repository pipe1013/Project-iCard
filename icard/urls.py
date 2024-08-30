from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from users.api.router import router_user


schema_view = get_schema_view(
   openapi.Info(
      title="iCard - ApiDoc",
      default_version='v1',
      description="Documentación de la Api de iCard",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="felipemorenobuitrago506@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/', include(router_user.urls))
]
