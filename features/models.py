from django.db import models

# Create your models here.


class FeaturesName(models.Model):
    feature_name = models.CharField(max_length=50)
    feature_description = models.CharField(max_length=200)

    def __str__(self):
        return self.feature_name


class PluggableDatabase(models.Model):
    database_name = models.CharField(max_length=50)

    def __str__(self):
        return self.database_name


class PluggableRequest(models.Model):
    database = models.ForeignKey(PluggableDatabase, on_delete=models.CASCADE, related_name='request')
    request_name = models.CharField(max_length=50)
    # mapping = models.ForeignKey(FeatureMapping, on_delete=models.CASCADE, related_name='mapping-request')

    def __str__(self):
        return self.request_name


class FeatureMapping(models.Model):
    feature = models.ForeignKey(FeaturesName, on_delete=models.CASCADE, related_name='status')
    database = models.ForeignKey(PluggableDatabase, on_delete=models.CASCADE, related_name='pdb_mapping')
    feature_status = models.BooleanField(default=False)
    requests = models.ForeignKey(PluggableRequest, on_delete=models.CASCADE, related_name='pdb_request')

    def __str__(self):
        return str(self.feature_status)
