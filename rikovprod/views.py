from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from .serializers import *


# all api set for presentation, updating, etc
class PhotoAPISet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


# same, but with detail view
class VideoAPISet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    lookup_field = 'slug'


# same
class TagAPISet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = 'slug'


# list sessions
class DatesAPISet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = VacantDate.objects.all()
    serializer_class = DateSerializer


# create session
class SessionPOSTAPI(generics.CreateAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionPOSTSerializer

    def perform_create(self, serializer):
        serializer.save()


class VacantDateAPISet(viewsets.ModelViewSet):
    queryset = VacantDate.objects.all()
    serializer_class = VacantDateSerializer
