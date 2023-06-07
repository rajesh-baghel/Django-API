from rest_framework import serializers
from api.models import Company

#creating serializer

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    company_id = serializers.ReadOnlyField()
    class Meta:
        model = Company
        fields = "__all__"
        