from django.contrib import admin
from django.urls import path
from Core import views
from django.contrib.auth import views as auth_views
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('home/',views.home,name='home'),
    path('login/',auth_views.LoginView.as_view(template_name='Core/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='Core/logout.html'),name='logout'),
    path('updateProfile/',views.update,name='updateProfile'),
    path('profile/',views.profile,name='profile'),
    path('progress/',views.progress,name='progress'),
    path('task/<int:pk>',views.taskDetail,name='taskDetail')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)