from django.db.models import Q
from rest_framework import viewsets, generics
from .models import *
from .serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class LightNovelViewSet(viewsets.ViewSet, generics.ListAPIView,
                        generics.RetrieveAPIView):
    queryset = LightNovel.objects.all()
    serializer_class = LightNovelSerializer

    @action(methods=['get'], detail=False, url_path=r'search/(?P<keyword>\w[\w ]*\w)', url_name="search")
    def search(self, request, keyword):
        ln = LightNovel.objects.filter(Q(title__icontains=keyword)|Q(alternatenames__name__icontains=keyword)).distinct()
        return Response(LightNovelSerializer(ln, many=True).data, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=True, url_path='get-volumes', url_name="get-volumes")
    def get_volumes(self, request, pk):
        ln = Volume.objects.filter(light_novel__id=pk)
        return Response(VolumeSerializer(ln, many=True).data, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False, url_path=r'get-by-genre/(?P<genrename>\w[\w ]*\w)', url_name="get-by-genre")
    def get_by_genre(self, request, genrename):
        ln = LightNovel.objects.filter(genres__name__iexact=genrename)
        return Response(LightNovelSerializer(ln, many=True).data, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False, url_path=r'get-by-author/(?P<authorname>\w[\w ]*\w)',url_name="get-by-author")
    def get_by_author(self, request, authorname):
        ln = LightNovel.objects.filter(authors__name__iexact=authorname)
        return Response(LightNovelSerializer(ln, many=True).data, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False, url_path=r'get-by-illustrator/(?P<illustratorname>\w[\w ]*\w)',url_name="get-by-illustrator")
    def get_by_illustrator(self, request, illustratorname):
        ln = LightNovel.objects.filter(illustrators__name__iexact=illustratorname)
        return Response(LightNovelSerializer(ln, many=True).data, status=status.HTTP_200_OK)


class AuthorViewSet(viewsets.ViewSet, generics.ListAPIView,
                    generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class GenreViewSet(viewsets.ViewSet, generics.ListAPIView,
                    generics.RetrieveAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class IllustratorViewSet(viewsets.ViewSet, generics.ListAPIView,
                    generics.RetrieveAPIView):
    queryset = Illustrator.objects.all()
    serializer_class = IllustratorSerializer

class PublisherViewSet(viewsets.ViewSet, generics.ListAPIView,
                      generics.RetrieveAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


