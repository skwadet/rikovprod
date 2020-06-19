from rest_framework import serializers
from .models import *


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('title', 'image')


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('title', 'tag', 'embedded_url', 'preview_image', 'slug')
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class TagSerializer(serializers.ModelSerializer):
    videos = serializers.SlugRelatedField(many=True, read_only=True, slug_field='slug')

    class Meta:
        model = Tag
        fields = ['name', 'slug', 'videos']
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


# not for views, just provides field for DateSerializer
class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ['name', 'freedate', 'phone', 'email', 'is_busy', 'callstatus']


class DateSerializer(serializers.ModelSerializer):
    sessions = SessionSerializer(many=True, read_only=True)

    class Meta:
        model = VacantDate
        fields = ['date', 'sessions']


# for sessions create, don't provide is_bust and calledstatus fields, because they're default value for new session
class SessionPOSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ['name', 'freedate', 'phone', 'email']


class VacantDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = VacantDate
        fields = ['date']
