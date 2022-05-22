from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from idea.models import Idea
from .serializers import IdeaSerializer  


class IdeaViewSet(viewsets.ModelViewSet):
    """CRUD用APIクラス"""
    
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
