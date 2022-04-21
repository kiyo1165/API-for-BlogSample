from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('get-blogs', views.BlogListView)
router.register('create-blog', views.BlogCreateViewSets)


app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
    path('register/', views.CreateUserView.as_view(), name='register'),
    path('self_user/', views.LoginUserView.as_view(), name="self_user"),
    path('tags/', views.TagListCreateView.as_view(), name="tags"),
]