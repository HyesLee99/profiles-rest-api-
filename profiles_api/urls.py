from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
# base name is needed if the viewset does not have queryset or want to override queryset name 
router.register('profile', views.UserProfileViewSet) # don't need base_name, because
# User profileViewSet has queryset. REST framework could figure out from userprofile of the models

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls))
]
