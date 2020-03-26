from rest_framework import serializers
from reader.models import DataStore


class DataStoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = DataStore
        fields = '__all__'