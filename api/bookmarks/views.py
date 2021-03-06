from django.contrib.auth.models import User

from rest_framework import generics

from bookmarks.models import Bookmark
from bookmarks.serializers import BookmarkSerializer, UserSerializer
from bookmarks.permissions import IsPostMethodOrAdmin


class BookmarkList(generics.ListCreateAPIView):
    serializer_class = BookmarkSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return Bookmark.objects.order_by('owner_id')

        return Bookmark.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BookmarkDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookmarkSerializer

    def get_queryset(self):
        return Bookmark.objects.filter(owner=self.request.user)


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = (IsPostMethodOrAdmin,)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)
