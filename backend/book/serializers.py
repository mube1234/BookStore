from rest_framework import serializers
from .models import Category, Book  

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__' 

class BookSerializer(serializers.ModelSerializer):
    # category = CategorySerializer()  # Use the CategorySerializer for the 'category' field
    class Meta:
        model = Book
        fields = '__all__'  

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})   
    #  The write_only=True attribute for the password field ensures that the password is not included in the serialized response.