from django.shortcuts import render
from homepage.models import Roast_Boast
from homepage.serializers import Roast_BoastSerializer

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

class Roast_BoastViewSet(viewsets.ModelViewSet):
    queryset = Roast_Boast.objects.all().order_by('-post_date')
    serializer_class = Roast_BoastSerializer

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