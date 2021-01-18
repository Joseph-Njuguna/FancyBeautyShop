from django.urls import path
from fancybeautyshop import settings
from django.contrib.staticfiles.urls import static
from . import views

app_name = 'web'
urlpatterns = [
    path('', views.home, name='home'),
    path('gallery', views.gallery, name='gallery'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
