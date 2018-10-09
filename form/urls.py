from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^myapp1/', include('myapp1.urls', namespace='myapp1')),
    # url(r'^admin/', admin.site.urls),
]
