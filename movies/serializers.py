from rest_framework import serializers
from movies.models import Movie
from django.db.models import Avg
from genres.serializers import GenreSerializer
from actors.serializers import ActorSerializer
from reviews.serializers import ReviewSerializer


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

    
    def validate_release_date(self, value):
        if value.year < 1950:
            raise serializers.ValidationError("Insira um ano posterior à 1970")
        else:
            return value
        
    
    def validate_resume(self, value):
        if len(value.resume) > 300:
            raise serializers.ValidationError("A descrição deve ter menos que 300 caracteres")
        else:
            return value


class MovieListDetailSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)
    genre = GenreSerializer()
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'actors', 'release_date', 'rate', 'resume']
    

    def get_rate(self, object):
        rate = object.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return round(rate, 2)
        
        return None


class MovieReviewListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'reviews']
    


class MovieStatsSerializer(serializers.Serializer):

    total_movies = serializers.IntegerField()
    movies_by_genre = serializers.ListField()
    total_reviews = serializers.IntegerField()
    average_stars = serializers.FloatField()