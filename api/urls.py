from django.urls import path


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from api.models import Note
from api.views import CreateUser, ListCreateNote, Notee, DeleteNote

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('create-user', CreateUser.as_view(), name='create_user'),
    path('note',Notee.as_view(),name= 'list_note'),
    path('listcreate-note',ListCreateNote.as_view(), name='list-create'),
    path('delete-note/<int:pk>',DeleteNote.as_view(),name= 'delete-note'),
]