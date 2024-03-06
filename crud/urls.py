from django.urls import path
from . import views
urlpatterns = [
    path('addpost/', views.item_create, name="itemadd"),
    path('postlist/', views.item_list, name= "itemlist"),
    path('postdetails/<int:pk>', views.item_detail, name= "itemdetails"),
    path('postedit/<int:pk>', views.item_edit, name= "itemedit"),
    path('postdelete/<int:pk>', views.item_delete, name= "itemdelete"),
    path('search/', views.search, name='search'),

]