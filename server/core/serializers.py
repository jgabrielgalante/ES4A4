from rest_framework import serializers

from . import models


class ThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Thread
        fields = '__all__'
        read_only_fields = ['slug','id']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = '__all__'

