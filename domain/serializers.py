from rest_framework import serializers
from domain.models import Domain

class Domainserializer(serializers.Serializer):
    dName = serializers.CharField(required=True, max_length=200)

    def create(self, validated_data):
        return Domain.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.dName = validated_data.get('name', instance.dName)
        instance.save()
        return instance

    class Meta:
        model = Domain
        fields = ("dName", "ctime")