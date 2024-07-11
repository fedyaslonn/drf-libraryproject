from rest_framework import serializers
from .models import *

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = '__all__'

    def create(self, validated_data):
        validated_data['loan_date'] = timezone.now().date()
        return Loan.objects.create(**validated_data)