from rest_framework.serializers import ModelSerializer

from .models import Subject,Class

class SubSerializer(ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class ClassSerializer(ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'