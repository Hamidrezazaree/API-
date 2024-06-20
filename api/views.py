from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView , ListCreateAPIView , ListAPIView, DestroyAPIView

from api.models import Note
from api.serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated,IsAdminUser
from rest_framework.response import Response


class CreateUser(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class ListCreateNote(ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def get_queryset(self):
        return Note.objects.filter(author = self.request.user)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author = self.request.user)
        else:
            return Response('Not accepted')

class DeleteNote(DestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

    def get_queryset(self):
        return Note.objects.filter(author = self.request.user)



class Notee(ListAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


