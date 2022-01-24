from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from posts.api import post_router

api = NinjaAPI(title="Nija Blog API", description="A REST API For a Ninja Blog website")

api.add_router(prefix="/", router=post_router)

urlpatterns = [path("admin/", admin.site.urls), path("api/", api.urls)]
