from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from . import views
app_name='schoolApp'
urlpatterns = [
    path('',views.home,name='home'),
    path('stud_form/',views.stud_form,name='stud_form'),
    path('form1/',views.form1,name='form1'),
    path('order_details/',views.orderDetail,name='orderDetail'),
    path('details/<int:order_id>/',views.Details,name='Details'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)