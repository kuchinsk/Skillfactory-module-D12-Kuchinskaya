from django.urls import path
from django.views.decorators.cache import cache_page

from .views import News, PostList, Search, PostCreate, PostEdit, PostDelete, CategoryDetailView, subscribe, unsubscribe

app_name = 'news'
urlpatterns = [
    # path('', News.as_view(), name='post_list'),
    path('', cache_page(60)(News.as_view()), name='post_list'),
    # path('<int:pk>/', PostList.as_view(), name='post'),
    path('<int:pk>/', cache_page(60*5)(PostList.as_view()), name='post'),
    path('search/', Search.as_view(), name='post_search'),
    path('add/', PostCreate.as_view(), name='post_add'),
    path('<int:pk>/edit/', PostEdit.as_view(), name='post_edit'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category'),
    path('subscribe/<int:pk>', subscribe, name='subscribe'),
    path('unsubscribe/<int:pk>', unsubscribe, name='unsubscribe'),
]