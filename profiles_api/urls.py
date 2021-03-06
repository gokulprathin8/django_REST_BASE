from django.urls import path, include
from profiles_api import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'hello-viewset', views.HelloViewSet, basename='hello-viewset')
router.register(r'profile-viewset', views.UserProfileViewSet)
router.register(r'feed', views.UserProfileFeedViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view())
]