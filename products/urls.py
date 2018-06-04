from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'products'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('add', views.AddprodcutView.as_view(), name="addProduct"),
    path('insert', views.insertProduct, name="insertProduct"),
    path('edit/<int:product_id>', views.editProduct, name='editProduct'),
    path('update', views.updateProduct, name="updateProduct"),
    path('delete/<int:product_id>', views.deleteProduct, name="deleteProduct"),
    path('game', views.GameView.as_view(), name='game'),
    path('checktic', views.checktic, name='checktic'),
]
