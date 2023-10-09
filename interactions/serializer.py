from rest_framework import serializers
from .models import CustomerInteraction


class CustomerInteractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerInteraction
        fields = "__all__"
