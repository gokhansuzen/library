from django.contrib import admin
from django.urls import path,include
from root.views import homeView
from django.conf import settings
from django.conf.urls.static import static
from user.views import login_view,logout_view,register_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homeView,name='home'),
    path('login/',login_view,name='login'),
    path('logout/',logout_view,name='logout'),
    path('register/',register_view,name='register'),

    path('library/',include('library.urls')),
    path('u/',include('user.urls')),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)