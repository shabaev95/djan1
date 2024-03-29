from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from graphene_django.views import GraphQLView

from follows.router import router as follows_router
from users.router import router as users_router
from profiles.router import router as profiles_router
from posts.router import router as posts_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(users_router.urls)),
    path('', include(follows_router.urls)),
    path('', include(profiles_router.urls)),
    path('', include(posts_router.urls)),
    url(r'^graphql$', GraphQLView.as_view(graphiql=True)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]