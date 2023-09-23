from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path
urlpatterns =(
    [
    path('admin/', admin.site.urls),
        path("tinymce/", include("tinymce.urls")),
        
        path("", include("web.urls"))
        
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
admin.site.site_header = "Gedexo Administration"
admin.site.site_title = "Gedexo Admin Portal"
admin.site.index_title = "Welcome to Gedexo Admin Portal"