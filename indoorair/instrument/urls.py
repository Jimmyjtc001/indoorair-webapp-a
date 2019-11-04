from django.urls import path

from . import views
urlpatterns = [
    path('create',views.create_page, name = 'create_page'),
    path('api/create',views.create_api, name = 'create_api'),
    path('retrieve',views.retrieve_page, name = 'retrieve_page'),
    path('api/retrieve',views.retrieve_api, name = 'retrieve_api'),
    path('update',views.update_page, name = 'update_page'),
    path('api/update',views.update_api, name = 'update_api'),
    path('list',views.list_page, name = 'list_page'),
    path('api/list',views.list_api, name = 'list_api'),
    ]
