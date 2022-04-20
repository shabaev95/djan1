import graphene
from graphene_django import DjangoObjectType
from .models import Profile, Photos, Contacts
from users.models import CustomUser, Photos
from django.db.models import Q


class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile
        fields = "__all__"


class PhotosType(DjangoObjectType):
    class Meta:
        model = Photos
        fields = "__all__"


class ContactsType(DjangoObjectType):
    class Meta:
        model = Contacts
        fields = "__all__"


class Query(graphene.ObjectType):
    all_profiles = graphene.List(ProfileType)
    all_photos = graphene.List(PhotosType)
    all_contacts = graphene.List(ContactsType)
    find_user = graphene.List(CustomUserType,
                              findBy=graphene.String(required=True),
                              offset=graphene.Int(required=False),
                              limit=graphene.Int(required=False))

    def resolve_all_profiles(root, info):
        # Здесь достаём.
        return Profile.objects.all()

    def resolve_all_photos(root, info):
        # Здесь достаём.
        return Photos.objects.all()

    def resolve_all_contacts(root, info):
        # Здесь достаём.
        return Contacts.objects.all()

    def resolve_find_user(self, info, findBy, offset=None, limit=None):
        # Здесь достаём.
        result = CustomUser.objects.filter(Q(username__icontains=findBy) | Q(first_name__icontains=findBy) | Q(last_name__icontains=findBy) |
                                       Q(email__icontains=findBy) | Q(status__icontains=findBy))
        if offset:
            result = result[offset:]

        if limit:
            result = result[:limit]

        return result