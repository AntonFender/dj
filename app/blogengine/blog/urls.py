
from django.urls import path
from .views import *

#Здесь порядок ссылок имеет значение.
#path('tag/create', должен стоять выше чем path('tag/<str:slug>/
#Это связано с тем, чтобы не возникало ошибок при обработки запроса
urlpatterns = [
    path('', posts_list, name='posts_list_url'),
    path('post/<str:slug>/', PostDetail.as_view(), name='post_detail_url'),
    path('tags/', tags_list, name='tags_list_url'),
    path('tag/create', TagCreate.as_view(), name='tag_create_url'),
    path('tag/<str:slug>/', TagDetail.as_view(), name='tag_detail_url')
]
