"""
URL configuration for backend_social project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from app_backend.views import *
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', get_profile, name='get_profile'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('create-user/', create_user, name='create_user'),
    path('posts/', all_posts, name='all_posts'),
    path('posts/create/', create_post, name='create_post'),
    path('user/posts/', user_posts, name='user_posts'),
    path('posts/<int:pk>/delete/', delete_post, name='delete_post'),
    path('posts/<int:pk>/update/', update_post, name='update_post'),


]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)