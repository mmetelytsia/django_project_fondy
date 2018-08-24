from django.urls import path

from . import views

urlpatterns = [
    # ex: /orders/
    path('', views.index, name='index'),
    path('<int:order_id>/', views.order, name='order'),
]