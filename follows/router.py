from rest_framework import routers

from follows.views import FollowViewSet

router = routers.DefaultRouter()
router.register(r'follows', FollowViewSet)