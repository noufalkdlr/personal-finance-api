from rest_framework.generics import ListCreateAPIView
from rest_framework import permissions
from .models import Category
from .serializers import CategorySerializer


class CategoryListView(ListCreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Category.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
