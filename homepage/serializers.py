from homepage.models import Roast_Boast
from rest_framework import serializers

class Roast_BoastSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Roast_Boast
        fields = ['id', 
        'is_boast', 
        'content', 
        'upvotes',
        'downvotes', 
        'post_date', 
        'total']