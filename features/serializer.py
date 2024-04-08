from rest_framework import serializers
from . import models
from django.shortcuts import get_object_or_404


class PluggableRequestSerializer(serializers.ModelSerializer):
    # database = serializers.SlugRelatedField(
    #     read_only=True,
    #     slug_field='request'
    # )

    class Meta:
        model = models.PluggableRequest
        fields = '__all__'


class PluggableDatabaseSerializer(serializers.ModelSerializer):
    request = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='database'
    )
    class Meta:
        model = models.PluggableDatabase
        fields = '__all__'


class FeatureSerializer(serializers.ModelSerializer):
    # feature_name = serializers.CharField()
    # feature_description = serializers.CharField()
    #feature = FeatureMappingSerializer(many=True, read_only=True)
    # feature_status = serializers.StringRelatedField(many=True)
    # feature_status = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # status = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name="feature_mapping_details"
    # )

    class Meta:
        model = models.FeaturesName
        # fields = [
        #     "id",
        #     "feature_name",
        #     "feature_description",
        #     # "status",
        # ]
        fields = '__all__'


class FeatureMappingSerializer(serializers.ModelSerializer):
    # feature = serializers.SlugRelatedField(
    #     read_only=True,
    #     slug_field='feature_name'
    # )
    # feature_id = serializers.StringRelatedField(
    #     read_only=True
    # )
    # feature_id = serializers.HyperlinkedRelatedField(
    #     read_only=True,
    #     view_name="features_name_details"
    # )
    database = serializers.SlugRelatedField(
        read_only=True,
        slug_field='pdb_mapping'
    )

    requests = PluggableRequestSerializer(many=True, read_only=True)

    class Meta:
        model = models.FeatureMapping
        fields = ['database', 'feature', 'feature_status', 'requests']
        read_only_fields = ['database', 'requests']


class FeatureMappingCreateSerializer(FeatureMappingSerializer):
    def validate(self, data):
        data = self._validated_database(data)
        data = self._validated_feature(data)
        return data

    def _validated_database(self, data):
        database_id = self.context["view"].kwargs["database_id"]
        data["database_id"] = get_object_or_404(models.PluggableDatabase, pk=database_id).id
        return data

    def _validated_feature(self, data):
        feature_id = self.context['view'].request.data['feature']
        data['feature_id'] = get_object_or_404(models.FeaturesName, pk=feature_id).id
        return data
