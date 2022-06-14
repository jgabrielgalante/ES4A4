from rest_framework import viewsets, response

from . import models, serializers


class ThreadViewSet(viewsets.ModelViewSet):
    queryset = models.Thread.objects.all()
    serializer_class = serializers.ThreadSerializer

    def get_queryset(self):
        queryset = models.Thread.objects.all()
        slug = self.request.query_params.get('slug')
        if slug is not None:
            queryset = queryset.filter(slug=slug)
        return queryset

    def create(self, *args, **kwargs):
        serializer = self.get_serializer(data=self.request.data)

        new_thread = None

        if serializer.is_valid():
            new_thread = models.Thread.objects.create(
            **serializer.validated_data).save()
        else:
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(new_thread, many=False)

        return response.Response(serializer.data)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer

    def get_queryset(self):
        queryset = models.Comment.objects.all()
        thread = self.request.query_params.get('thread')
        if thread is not None:
            queryset = queryset.filter(thread__slug=thread)
        return queryset.order_by('-id')

