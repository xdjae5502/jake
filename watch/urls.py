from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.Index, name="Index"),
    path('edit_part/<int:part_id>/', views.edit_part, name='edit_part'),
    path('delete_part/<int:part_id>/', views.delete_part, name='delete_part'),
    path('watch-parts/', views.watch_parts, name='watch_parts'),
    path('add-parts/', views.add_parts, name='add_parts'),
    path('contact/', views.contact, name='contact'),
    path('store-location/', views.store_location, name='store_location'),
    path('our-story/', views.our_story, name='our_story'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('edit_battery/<int:battery_id>/', views.edit_battery, name='edit_battery'),
    path('delete_battery/<int:battery_id>/', views.delete_battery, name='delete_battery'),
    path("Batteries/", views.Batteries, name="Batteries"),
    path('watch/', views.watch_page, name='watch_page'),
    path('watch/add_product/', views.add_product, name='add_product'),
    path('add_battery/', views.add_battery, name='add_battery'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
