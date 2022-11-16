from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework_simplejwt.views import \
    TokenObtainPairView,\
    TokenRefreshView


urlpatterns = [
   path("admin/", admin.site.urls),
   path('api/users/', include('accounts.api.urls', namespace='users')),
   path('api/', include('exchange_app.api.urls')),
   path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
   path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


schema_view = get_schema_view(
   openapi.Info(
      title="Exchange API",
      default_version='v1',
      description="API для взаимодействия с букроссинговым сайтом.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="admin@admin.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns += [
   re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]