from rest_framework import serializers
from bushtree.models import *

class FlowerSerializer(serializers.ModelSerializer):
    """Форма для запроса необходимого цветника"""

    class Meta:
        model = Flower
        fields = "__all__"
class ColorSerializer(serializers.Serializer):
    color_main = serializers.CharField(max_length=255)
    color_other = serializers.CharField(max_length=255)

    def validate(self, attrs):
        return super().validate(attrs)
class FlowerBandIdSerializer(serializers.Serializer):
    flower_band_id = serializers.CharField(max_length=255)
    
    def validate(self, attrs):
        return super().validate(attrs)
    
class FlowerBandSerializer(serializers.Serializer):
    flower_band_id = serializers.CharField(max_length=255, read_only=True)
    mass = serializers.CharField(max_length=255)
    flower_band = serializers.FileField()

    regex_mask = '/[0-9]+\.(?:jpg|png)/g'
    def validate(self, attrs):
        return super().validate(attrs)
    
    def create(self, validated_data):
        flower_band = validated_data.get("flower_band", None)
        _flower_band_id = str(flower_band).split(".")[0]
        return FlowerBand.objects.create(flower_band_id=_flower_band_id, **validated_data)
    
class GardenSerializer(serializers.Serializer):
    """Форма для получения данных по картинкам цветников"""
    garden_id = serializers.CharField(max_length=255, read_only=True)
    gardens = serializers.FileField()

    def validate(self, attrs):
        return super().validate(attrs)
        
    def create(self, validated_data):
        gardens = validated_data.get("gardens", None)
        _gardens_id = str(gardens).split(".")[0]
        return Garden.objects.create(garden_id=_gardens_id, **validated_data)

class GardenIdSerializer(serializers.Serializer):
    """Форма для удаления цветников"""
    garden_id = serializers.CharField(max_length=255)

    def validate(self, attrs):
        return super().validate(attrs)
    