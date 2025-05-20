from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Twitter import views
from django.contrib.auth.urls import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.tweet_list, name='tweet_list'),
    
    path('my_tweets/', views.my_tweet_list, name='my_tweet_list'),
    
    path('tweet/create/', views.tweet_create, name='tweet_create'),
    
    path('tweet/<int:tweet_id>/update/', views.tweet_edit, name='tweet_edit'),
    
    path('tweet/<int:tweet_id>/delete/', views.tweet_delete, name='tweet_delete'),
    
    path('rough/', views.rough, name='rough'),
    
    path('register/', views.register, name='register'),
    
    path('accounts/login/', views.login_view, name='login'),
    
    path('accounts/', include('django.contrib.auth.urls')),
    
    path('profile/', views.profile, name='profile'),
    
    path('update_profile/', views.update_profile, name='update_profile'),
    
    path('add_comment/<int:tweet_id>/', views.add_comment, name='add_comment'),
    
    path('like_comment/<int:comment_id>/', views.like_comment, name='like_comment'),
    
    path('dislike_comment/<int:comment_id>/', views.dislike_comment, name='dislike_comment'),
    
    path('like_tweet/<int:tweet_id>/', views.like_tweet, name='like_tweet'),
    
    path('dislike_tweet/<int:tweet_id>/', views.dislike_tweet, name='dislike_tweet'),


    
] + static(settings.STATIC_URL, document_root=settings.BASE_DIR / 'static') + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
