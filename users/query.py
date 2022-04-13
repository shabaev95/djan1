import graphene
from graphene_django import DjangoObjectType

from users.models import CustomUser


class CategoryType(DjangoObjectType):
    class Meta:
        model = CustomUser
        fields = "__all__"

class Query(graphene.ObjectType):
    all_users = graphene.List(CategoryType)

    def resolve_all_users(root, info):
        # Здесь достаём.
        return CustomUser.objects.all()