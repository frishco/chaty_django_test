from rest_framework import serializers
from .models import Actor, Repository, Event


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'login', 'avatar_url']
        extra_kwargs = {
            'id': {'validators': []}
        }


class RepoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repository
        fields = ['id', 'name', 'url']
        extra_kwargs = {
            'id': {'validators': []}
        }

class EventSerializer(serializers.ModelSerializer):
    actor = ActorSerializer()
    repo = RepoSerializer()

    class Meta:
        model = Event
        fields = ['id', 'type', 'actor', 'repo', 'created_at']

    def create(self, validated_data):
        actor_data = validated_data.pop('actor')
        repo_data = validated_data.pop('repo')

        try:
            actor = Actor.objects.get(pk=actor_data['id'])
        except Actor.DoesNotExist:
            actor = Actor.objects.create(**actor_data)

        try:
            repo = Repository.objects.get(pk=repo_data['id'])
        except Repository.DoesNotExist:
            repo = Repository.objects.create(**repo_data)


        event = Event.objects.create(actor=actor, repo=repo, **validated_data)
        return event
