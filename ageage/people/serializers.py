from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField()

    class Meta:
        model = Person
        fields = ['iin', 'age']

    def get_age(self, obj):
        return obj.calculate_age()

    def create(self, validated_data):
        iin = validated_data['iin']
        return Person.objects.create(iin=iin)