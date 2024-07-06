from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('form/home/',views.home,name="Home"),
    path('home/',views.home,name="Home"),
    path('',views.home,name="Home"),
    path('form/',views.form,name="Form"),
    path('search/',views.search,name="Search"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)