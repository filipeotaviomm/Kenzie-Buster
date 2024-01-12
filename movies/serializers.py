from rest_framework import serializers
from movies.models import RatingOptions
from movies.models import Movie


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, allow_blank=True, default="")
    rating = serializers.ChoiceField(
        choices=RatingOptions.choices, default=RatingOptions.G
    )
    synopsis = serializers.CharField(allow_blank=True, default="")
    added_by = serializers.CharField(read_only=True, source="user.email")

    def create(self, validated_data: dict):
        return Movie.objects.create(**validated_data)
