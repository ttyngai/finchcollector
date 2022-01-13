from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    # 'finch/' - finch Index Route
    path('finches/', views.finches_index, name='finches_index'),

    # 'finches/<int:cat_id>/' - Cat Details Route
    path('finches/<int:finch_id>/', views.finches_detail, name='finches_detail'),

    #   'cats/create/' - Cat Create Route
    path('finches/create/', views.FinchCreate.as_view(), name='finches_create'),

    # 'cats/<int:pk>/update/ - Cats Update Route
    path('finches/<int:pk>/update/', views.FinchUpdate.as_view(), name='finches_update'),

    # 'finches/<int:pk>/delete/ - Cats Delete Route
    path('finches/<int:pk>/delete/', views.FinchDelete.as_view(), name='finches_delete'),

    # 'finches/<int:finch_id>/add-feeding/ add feeding route
    path('finches/<int:finch_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('finches/<int:finch_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),

    path('toys/', views.ToyList.as_view(), name='toys_index'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
]