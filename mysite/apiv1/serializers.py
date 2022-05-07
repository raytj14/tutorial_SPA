from rest_framework import serializers

from todo.models import Idea

class IdeaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Idea
        fields = ['idea', 'remind', 'status']