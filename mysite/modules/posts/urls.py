from django.conf.urls import url, include
from rest_framework import routers
from .views import UserViewSet

router = routers.DefaultRouter()
router.register(r'posts', UserViewSet, base_name='post')
urlpatterns = router.urls
