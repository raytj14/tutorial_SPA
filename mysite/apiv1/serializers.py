from rest_framework import serializers

from idea.models import Idea

class IdeaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Idea
        fields = ['idea', 'remind', 'status']