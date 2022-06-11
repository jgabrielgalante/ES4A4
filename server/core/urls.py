from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'threads', views.ThreadViewSet, basename='thread')
router.register(r'comments', views.CommentViewSet, basename='comment')
urlpatterns = router.urls
