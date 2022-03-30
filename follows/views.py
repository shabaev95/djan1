from ..api.serializers import DualSerializerViewSet
from .models import Follow

from .serializers import FollowSerializer


class FollowViewSet(DualSerializerViewSet):
    queryset = Follow.objects.all()

    serializer_classes = {
        'create': FollowSerializer,
        'update': FollowSerializer
    }

    default_serializer_class = FollowSerializer