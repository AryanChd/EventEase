from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Events.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls'))
]

# Styling Admin site
admin.site.site_header = "EventEase Administration Page"
admin.site.site_title =  "EventEase Site Admin"
admin.site.index_title = "EventEase Administration"