from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'cart'

urlpatterns=[
    url(r'^home/', views.home, name='home'),
    url(r'^itemlist/', views.itemlist, name='itemlist'),
    url(r'^shoppingcart/', views.shoppingcart, name='shoppingcart'),
    url(r'^search/', views.searchpage , name='searchpage'),
    url(r'^searchitem/', views.search , name='search'),
    url(r'^checkout/', views.checkout , name='checkout'),
    url(r'^productpage/(?P<Id>[0-9]+)', views.product_page, name='product_page'),
    url(r'^add_to_cart/(?P<Item_id>[0-9]+)',views.add_to_cart, name='add_to_cart'),
    url(r'^remove_from_cart/(?P<Item_id>[0-9]+)',views.remove_from_cart, name='remove_from_cart'),
    url(r'^remove_single_item_from_cart/(?P<Item_id>[0-9]+)',views.remove_single_item_from_cart, name='remove_single_item_from_cart'),
    url(r'^add_single_item_into_cart/(?P<Item_id>[0-9]+)',views.add_single_item_into_cart, name='add_single_item_into_cart')

]

