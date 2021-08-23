from django.contrib import admin
from django.urls import path,include
from django.views.static import serve
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "TAUKIR Portfolio Panel"
admin.site.site_title = "TAUKIR Portfolio Administration Panel"
admin.site.index_title = "Welcome to Website"


urlpatterns = [
    path('',include('aa.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL,document_root= settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)