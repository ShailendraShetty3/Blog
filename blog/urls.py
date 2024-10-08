
from django.contrib import admin
from django.urls import path

from . import views

from django.urls import path 
from rest_framework_swagger.views import get_swagger_view

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Blog API",
        default_version='v1',
        description="blog api's",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="xyz@example.com"),
        license=openapi.License(name="Awesome License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path("blogs/", views.blog_post_list, name='schema-swagger-ui'),
    # path("articles/<int:year>/<int:month>/", views.month_archive),
    # path("articles/<int:year>/<int:month>/<int:pk>/", views.article_detail),



    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),


    
]
