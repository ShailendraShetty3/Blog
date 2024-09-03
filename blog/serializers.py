from rest_framework import serializers
from .models import Blog

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['pub_date', 'headline', 'content']
