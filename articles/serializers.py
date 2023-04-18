from articles.models import Articles
from rest_framework import serializers

class ArticleSerialize(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = '__all__'