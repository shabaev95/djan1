import graphene

class ChangeStatus(graphene.Mutation):
    class Arguments:
        status = graphene.String()

    ok = graphene.Boolean()

    def mutate(root, info, status):
        user = info.context.user
        user.status = status
        return ChangeStatus(status=status, ok=True)

class ProfileMutation(graphene.ObjectType):
    change_status = ChangeStatus.Field()