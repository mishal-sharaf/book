from rest_framework import serializers
from api.models import Books

class BooksSerializers(serializers.Serializer):
    id=serializers.CharField(read_only=True)
    name=serializers.CharField()
    price=serializers.IntegerField()
    author=serializers.CharField()
    category=serializers.CharField()
    image=serializers.ImageField()

class BooksModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Books
        fields=__all__
