from .views import (
    FeatureView,
    FeatureMappingView,
    FeatureMappingDetailsView,
    FeatureNameDetailsView,
    PluggableRequestListView,
    PluggableDatabaseViewset,
)
from rest_framework.routers import DefaultRouter
from django.urls import path

# router = DefaultRouter()
# router.register(r'feature-names', FeatureView, basename='features_name_details')
# router.register(r'feature-names/<int:pk>', FeatureView, basename='features_name_details')

router = DefaultRouter()
router.register(r'pluggables',
                PluggableDatabaseViewset,
                basename='pluggable-database-view')
# router.register(r'feature-names/<int:pk>', FeatureView, basename='features_name_details')

# urlpatterns = router.urls + [
#     path("feature-mapping/", FeatureMappingView.as_view(), name="mapping"),
#     path("feature-mapping/<int:pk>", FeatureMappingDetailsView.as_view(), name="feature_mapping_details"),
# ]

urlpatterns = router.urls + [
    path('pluggables/<str:database_id>/pluggable-request', PluggableRequestListView.as_view(), name='pluggable-request-view'),
    path("pluggables/<str:database_id>/feature-mapping", FeatureMappingView.as_view(), name="mapping"),
    path("pluggables/<str:database_id>/feature-mapping/<int:feature_id>", FeatureMappingDetailsView.as_view(), name="feature_mapping_details"),
    path("feature-names/", FeatureView.as_view(), name="name_details"),
    path("feature-names/<int:pk>/", FeatureNameDetailsView.as_view(), name="features_name_details"),
]