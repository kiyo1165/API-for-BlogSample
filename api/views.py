from .serializers import BlogSerializer, UserSerializer, TagSerializer, BlogCreateSerializer
from rest_framework.permissions import AllowAny
from .models import Blog, Tag
from auth_api.models import User
from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters import rest_framework as filters

# Create your views here.

class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class LoginUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    queryset = User.objects.all()

    # ログインしている自身の情報を取得
    def get_object(self):
        return self.request.user

    # 更新はさせない。
    def update(self, request, *args, **kwargs):
        response = {'message': 'PUTメソッドは許可されていません。'}
        return Response(response, status=status.HTTP_400_BAD_REQUES)

class BlogListView(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = (AllowAny,)

    def update(self, request, *args, **kwargs):
        response = {'message': 'PUTメソッドは許可されていません。'}
        return Response(response, status=status.HTTP_400_BAD_REQUES)

    def create(self, request, *args, **kwargs):
        response = {'message': 'POSTメソッドは許可されていません。'}
        return Response(response, status=status.HTTP_400_BAD_REQUES)

    def destroy(self, request, *args, **kwargs):
        response = {'message': 'DESTROYメソッドは許可されていません。'}
        return Response(response, status=status.HTTP_400_BAD_REQUES)

    def get_queryset(self):
        queryset = super().get_queryset()

        tag = self.request.query_params.get('tags', None)
        print(self.request.query_params)
        if tag:
            queryset = queryset.filter(tags__name=tag)
        return queryset

class BlogCreateViewSets(viewsets.ModelViewSet):
    serializer_class = BlogCreateSerializer
    queryset = Blog.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        if not self.request.data["image"]:
            serializer.save(image="estlove.jpeg")
        # serializer.save(user=self.request.user)

    # @action(detail=True, methods=['put'])
    # def created_tags(self, request, pk=None):
    #     # return Response(["hoges"])
    #     for i in request.data['tags']:
    #         print(i)
    #         # 入力されたタグがモデルにない場合は新規作成
    #         if not Tag.objects.filter(name=i).exists():
    #             tag_serializer = TagSerializer(data={'name': i})
    #             if tag_serializer.is_valid():
    #                 tag_serializer.save()
    #                 return Response(tag_serializer.data)
        # data = {
        #     'title': request.data['title'],
        #     'content': request.data['content'],
        #     'tags': request.data['tags'],
        #     'user': request.data['user'],
        #     'image': request.data['image'],
        #     'is_active': request.data['is_active']}
        # serializer = self.serializer_class(request.user, data=data, partial=True)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)


class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = Tag.objects.all()
        name = self.request.query_params.get("name", None)
        if name is not None:
            queryset = queryset.filter(name__istartswith=name)
        return queryset


