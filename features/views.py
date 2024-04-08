from django.shortcuts import render, HttpResponse, get_object_or_404
from rest_framework import viewsets
from . import models
from .serializer import (
    FeatureSerializer,
    FeatureMappingSerializer,
    FeatureMappingCreateSerializer,
    PluggableRequestSerializer,
    PluggableDatabaseSerializer,
)
from django.views import View
from django.utils.decorators import method_decorator
from django.http import JsonResponse, HttpResponseRedirect
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
# Create your views here.


# class FeatureView(viewsets.ModelViewSet):
#     """
#     A viewset for viewing and editing user instances.
#     """
#     serializer_class = FeatureSerializer
#     queryset = models.FeaturesName.objects.all()


class PluggableDatabaseViewset(viewsets.ModelViewSet):
    queryset = models.PluggableDatabase.objects.all()
    serializer_class = PluggableDatabaseSerializer

    def get_queryset(self):
        base_queryset = super().get_queryset()
        if self.action == "list":
            print("step-1")
            queryset = base_queryset.prefetch_related(
                "request"
            )
            print(queryset)
            return queryset


class PluggableRequestListView(generics.ListCreateAPIView):
    serializer_class = PluggableRequestSerializer

    def get_queryset(self):
        database_id = self.kwargs['database_id']
        queryset = models.PluggableRequest.objects.filter(database=database_id)
        return queryset


# @method_decorator(csrf_exempt, name="dispatch")
class FeatureView(generics.ListCreateAPIView):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = FeatureSerializer

    def get_queryset(self):

        queryset = models.FeaturesName.objects.all()
        return queryset


class FeatureNameDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FeatureSerializer
    lookup_field = "pk"

    def get_queryset(self, pk=None):
        queryset = models.FeaturesName.objects.all()
        return queryset


# @method_decorator(csrf_exempt, name="dispatch")
class FeatureMappingView(generics.ListCreateAPIView):

    def get_serializer_class(self):
        database_id = self.kwargs["database_id"]
        pluggable = get_object_or_404(models.PluggableDatabase, pk=database_id)
        self.check_object_permissions(self.request, pluggable)
        if self.request.method == 'POST':
            return FeatureMappingCreateSerializer
        return FeatureMappingSerializer

    # def get_serializer_class(self):
    #     feature_id = self.kwargs["feature_id"]

    def get_queryset(self):
        database_id = self.kwargs["database_id"]
        queryset = models.FeatureMapping.objects.filter(database=database_id)
        return queryset

    # def get(self, request, format=None, pk=None):
    #     if pk is not None:
    #         id = pk
    #         obj = models.FeatureMapping.objects.get(id=id)
    #         serializer = FeatureMappingSerializer(obj)
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     features = models.FeatureMapping.objects.all()
    #     serializer = FeatureMappingSerializer(features, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    #
    # def put(self, request, format=None, pk=None):
    #     id = pk
    #     features = models.FeatureMapping.objects.get(pk=id)
    #     print(request.data)
    #     serializer = FeatureMappingSerializer(features, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         response_msg = {"msg": "Record Updated!!!"}
    #         return Response(response_msg)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FeatureMappingDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FeatureMappingSerializer
    lookup_field = "feature_id"

    def get_queryset(self, pk=None):
        database_id = self.kwargs["database_id"]
        queryset = models.FeatureMapping.objects.filter(database=database_id)
        return queryset
