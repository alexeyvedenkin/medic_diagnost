from django.contrib import admin
from django.urls import path, include


class ServiceListView:
    pass


urlpatterns = [
    path("admin/", admin.site.urls),
    # path("", ServiceListView.as_view(), name="homepage"),
    path("users/", include("users.urls", namespace="users")),

]
