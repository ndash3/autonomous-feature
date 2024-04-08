from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.FeaturesName)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ['feature_name', 'feature_description']


@admin.register(models.FeatureMapping)
class FeatureMappingAdmin(admin.ModelAdmin):
    list_display = ['feature_id', 'feature_status']


@admin.register(models.PluggableRequest)
class PluggableRequestAdmin(admin.ModelAdmin):
    list_display = ['request_name']


@admin.register(models.PluggableDatabase)
class PluggableDatabaseAdmin(admin.ModelAdmin):
    list_display = ['id', 'database_name']
