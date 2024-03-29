from graphene import ObjectType, String, Schema
from users.query import Query as UsersQuery
from follows.query import Query as FollowsQuery
from posts.query import Query as PostsQuery
from profiles.query import Query as ProfileQuery
from profiles.mutations import ProfileMutation


class Query(UsersQuery, ObjectType, ProfileQuery, PostsQuery, FollowsQuery):
    hello = String(name=String(default_value="stranger"))
    goodbye = String()

class Mutation(ProfileMutation):
    pass

schema = Schema(query=Query, mutation=Mutation)
