from django.urls import path
from .views import dashboard, profile_list, profile, index


urlpatterns = [
    path('', index, name='home'),
    path("dashboard/", dashboard, name="dashboard"),
    path("profile_list/", profile_list, name="profile_list"),
    path("profile/<int:pk>", profile, name="profile"),
]
