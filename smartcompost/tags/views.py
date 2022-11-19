from rest_framework import filters, viewsets

from smartcompost.tags.models import Tag
from smartcompost.tags.serializers import TagSerializer


class TagViewSet(viewsets.ModelViewSet):

    queryset = Tag.objects.all()

    serializer_class = TagSerializer
    filter_backends = [
        filters.SearchFilter,
    ]
    search_fields = [
        "name",
    ]

    def perform_create(self, serializer):
        Tag.objects.get_or_create(**serializer.data)
