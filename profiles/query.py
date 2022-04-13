import graphene
from graphene_django import DjangoObjectType
from .models import Profile, Photos, Contacts


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

    def resolve_all_profiles(root, info):
        # Здесь достаём.
        return Profile.objects.all()

    def resolve_all_photos(root, info):
        # Здесь достаём.
        return Photos.objects.all()

    def resolve_all_contacts(root, info):
        # Здесь достаём.
        return Contacts.objects.all()