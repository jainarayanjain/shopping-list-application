from rest_framework import serializers

from items.models import ItemDetail


class ItemDetailModelSerializer(serializers.ModelSerializer):
    """Item Detail Model Serializer"""

    class Meta:
        model = ItemDetail
        fields = "__all__"
