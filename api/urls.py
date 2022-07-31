from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('get-series', views.LightNovelViewSet)
router.register('get-authors', views.AuthorViewSet)
router.register('get-genres', views.GenreViewSet)
router.register('get-illustrators', views.IllustratorViewSet)
router.register('get-publishers', views.PublisherViewSet)
urlpatterns = [
    path('',include(router.urls))
]