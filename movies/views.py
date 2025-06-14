from rest_framework import generics, views, response, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from movies.models import Movie
from reviews.models import Review
from movies.serializers import MovieSerializer, MovieStatsSerializer, MovieListDetailSerializer, MovieReviewListSerializer
from app.permissions import GlobalDefaultPermission
from django.db.models import Count, Avg


class MovieCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieListDetailSerializer
        return MovieSerializer


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieListDetailSerializer
        return MovieSerializer


class MovieStatsView(views.APIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Movie.objects.all()

    def get(self, request):
        total = self.queryset.count()
        movies_by_genre = self.queryset.values('genre__name').annotate(count=Count("id"))
        total_reviews = Review.objects.count()
        average_stars = Review.objects.aggregate(avg_stars=Avg('stars'))['avg_stars']

        data={
            'total_movies': total,
            'movies_by_genre': movies_by_genre,
            'total_reviews': total_reviews,
            'average_stars': round(average_stars, 1) if average_stars else 0}
        
        serializer = MovieStatsSerializer(data=data)
        serializer.is_valid(raise_exception=True)


        return response.Response(
            data=serializer.validated_data,
            status=status.HTTP_200_OK
        )
    

class MovieReviewsView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieReviewListSerializer
        return MovieSerializer

        
