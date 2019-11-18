# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Actor, Event
from .serializers import ActorSerializer, EventSerializer
from django.http import Http404
from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



class DeleteEventsView(APIView):
    def delete(self, request, format=None):
        events = Event.objects.all()
        events.delete()
        return Response(status=status.HTTP_200_OK)


class EventCreateListView(APIView):

    def get(self, request, format=None):
        events = Event.objects.all().order_by('id')
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ActorsEventsView(APIView):

    def get_object(self, pk):
        try:
            return Actor.objects.get(pk=pk)
        except Actor.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        actor = self.get_object(pk)
        events = actor.events.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ActorsList(APIView):

    def get_object(self, pk):
        try:
            return Actor.objects.get(pk=pk)
        except Actor.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        actors = Actor.objects.all().annotate(num_events=Count('events')).order_by('-num_events', 'login', 'id')
        serializer = ActorSerializer(actors, many=True)
        return Response(serializer.data)

    def put(self, request, format=None):
        data = request.data
        pk = data['id']
        actor = self.get_object(pk)
        serializer = ActorSerializer(actor, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)