from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import include, path, re_path
from django.conf.urls.i18n import i18n_patterns
from django.views.generic.base import TemplateView

schema_view = get_schema_view(
    openapi.Info(
        title="aftab API",
        default_version='v1',
        description="aftab",
        contact=openapi.Contact(email="aftab"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


admin.site.site_title = "Aftab Administration"
admin.site.site_header = "Aftab Administration"


urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    prefix_default_language=False
)

handler404 = 'aftab.views.handler404'
handler500 = 'aftab.views.handler500'

if settings.DEBUG:

    urlpatterns += [
        re_path(r'^swagger(?P<format>\.json|\.yaml)$',
                schema_view.without_ui(cache_timeout=0), name='schema-json'),
        path('swagger/', schema_view.with_ui('swagger',
                                             cache_timeout=0), name='schema-swagger-ui'),
        path('redoc/', schema_view.with_ui('redoc',
                                           cache_timeout=0), name='schema-redoc'),
        path('api-auth/', include('rest_framework.urls')),
        path('v1/api/auth/', include('user.urls')),
    ]

    urlpatterns += [
        path('404/', TemplateView.as_view(template_name='404.html'), name='404'),
        path('500/', TemplateView.as_view(template_name='500.html'), name='500'),
    ]

    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
