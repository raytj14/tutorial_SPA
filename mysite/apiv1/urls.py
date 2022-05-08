from django.urls import path, include
from rest_framework import routers

from. import views

router = routers.DefaultRouter()
router.register('Ideas', views.IdeaViewSet)

app_name = 'apiv1'
urlpatterns = [
    path('', include(router.urls)),
] 
