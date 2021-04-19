from django.contrib import admin
from django.urls import path, include
from . import views

admin.site.site_header = "Hackclub.co Admin Panel🐱‍👤"
admin.site.index_title = "Well Come To Hackclub.co"
admin.site.site_title = "Admin Panel🐱‍💻"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('blog/', include('blog.urls'))
]
