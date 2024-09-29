
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signup),
    path('signup/', views.signup),
    path('login/', views.login),
    path('todo/', views.todo),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
