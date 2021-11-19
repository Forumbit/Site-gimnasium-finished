from django.urls import path
from .views import *

urlpatterns = [
    path('', Hello.as_view(), name='index_url'),
    path('create/', ZamenaCreateView.as_view(), name='create_url'),
    path('update/<int:pk>/', ZamenaUpdateView.as_view(), name='edit_url'),
    path('delete/<int:pk>/', ZamenaDeleteView.as_view(), name='delete_url'),
    path('delete/', Zamena_all_delete.as_view(), name='delete_all_url'),
    path('addit/create/', AdditZamenaCreateView.as_view(), name='addit_create_url'),
    path('addit/update/<int:pk>/', AdditZamenaUpdateView.as_view(), name='addit_update_url'),
    path('addit/delete/<int:pk>/', AdditZamenaDeleteView.as_view(), name='addit_delete_url'),
]
