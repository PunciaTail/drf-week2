from rest_framework.generics import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from articles.serializers import ArticleSerialize
from drf_yasg.utils import swagger_auto_schema
from articles.models import Articles
        

class ArticleList(APIView):
    def get(self, request, format=None):
        articles = Articles.objects.all()
        serialize = ArticleSerialize(articles, many=True)
        return Response(serialize.data)

    @swagger_auto_schema(request_body=ArticleSerialize)
    def post(self, request, format=None):
        serialize = ArticleSerialize(data = request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        else:
            print(serialize.errors)
            return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)
        

class ArticleDetail(APIView):
    def get(self, request, article_id, format=None):
        article = get_object_or_404(Articles, id=article_id)
        serialize = ArticleSerialize(article)
        return Response(serialize.data)

    def put(self, request, article_id, format=None):
        article = get_object_or_404(Articles, id=article_id)
        serialize = ArticleSerialize(article, data = request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, article_id, format=None):
        article = get_object_or_404(Articles, id=article_id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

