from rest_framework.serializers import ModelSerializer
from .models import *

class AlternateNameSerializer(ModelSerializer):
    class Meta:
        model = AlternateName
        fields = ["name"]

class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ["id", "name"]

class IllustratorSerializer(ModelSerializer):
    class Meta:
        model = Illustrator
        fields = ["id", "name"]

class PublisherSerializer(ModelSerializer):
    class Meta:
        model = Publisher
        fields = ["id", "name", "region"]

class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name", "description"]

class GenreLightNovelSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name"]

class VolumeSerializer(ModelSerializer):
    class Meta:
        model = Volume
        fields = ["id", "name", "illustration", "publish_date"]

class LightNovelSerializer(ModelSerializer):
    alternatenames =AlternateNameSerializer(many=True)
    authors = AuthorSerializer(many=True)
    illustrators = IllustratorSerializer(many=True)
    publishers = PublisherSerializer(many=True)
    genres = GenreLightNovelSerializer(many=True)
    volumes = VolumeSerializer(many=True)
    class Meta:
        model = LightNovel
        fields = ["id", "title", "alternatenames", "description", "illustration", "status",
                  "authors", "illustrators", "publishers", "genres", "volumes"]