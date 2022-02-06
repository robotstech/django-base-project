import debug_toolbar
from django.contrib import admin
from django.urls import path, include

from base import settings

urlpatterns = [
    path('admin/', admin.site.urls),

]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
