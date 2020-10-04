from django.shortcuts import render
from homepage.models import Roast_Boast
from homepage.serializers import Roast_BoastSerializer
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

class Roast_BoastViewSet(viewsets.ModelViewSet):
    queryset = Roast_Boast.objects.all().order_by('-post_date')
    serializer_class = Roast_BoastSerializer

    @action(detail=False)
    def boasts(self, request):
        boast = Roast_Boast.objects.filter(is_boast=True).order_by('-post_date')
        serializer = self.get_serializer(boast, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def roasts(self, request):
        roast = Roast_Boast.objects.filter(is_boast=False).order_by('-post_date')
        serializer = self.get_serializer(roast, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def add_upvote(self, request, pk=None):
        roast_boast = self.get_object()
        roast_boast.upvotes += 1
        roast_boast.score = roast_boast.upvotes - roast_boast.downvotes
        roast_boast.save()
        return Response({'status': 'upvoted'})

    @action(detail=True, methods=['post'])
    def add_downvote(self, request, pk=None):
        roast_boast = self.get_object()
        roast_boast.downvotes += 1
        roast_boast.score = roast_boast.upvotes - roast_boast.downvotes
        roast_boast.save()
        return Response({'status': 'downvoted'})

    @action(detail=False)
    def most_popular(self, request):
        best = most_popular = Roast_Boast.objects.all().order_by('-total')
        serializer = self.get_serializer(best, many=True)
        return Response(serializer.data)
