from rest_framework import serializers
from movies_orders.models import MovieOrder


class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.SerializerMethodField("get_title")
    purchased_at = serializers.DateTimeField(read_only=True)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    purchased_by = serializers.SerializerMethodField()

    # esses dois jeitos dessas duas funções a baixo funcionam, elas substituem o source no parâmetro direto de cada campo
    def get_title(self, obj: MovieOrder):
        return obj.movie.title

    def get_purchased_by(self, obj: MovieOrder):
        return obj.user.email

    def create(self, validated_data: dict):
        return MovieOrder.objects.create(**validated_data)
