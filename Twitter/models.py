from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    avatar = models.ImageField(
        upload_to='user_avatars/',
        blank=True,
        null=True,
        default='user_avatars/user_default.png')
    about = models.TextField(blank=True)
    mobile = models.PositiveBigIntegerField(blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.first_name} {self.last_name}"

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.TextField()
    image = models.ImageField(upload_to='tweet_images', blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def like_count(self):
        return self.tweetlike_set.filter(is_like=True).count()

    def dislike_count(self):
        return self.tweetlike_set.filter(is_like=False).count()

    def __str__(self):
        return f'{self.user.username} - {self.tweet[:20]}'

class TweetLike(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_like = models.BooleanField(null=True)

    class Meta:
        unique_together = ('tweet', 'user')
    
class Comment(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def like_count(self):
        return self.likes.filter(is_like=True).count()

    def dislike_count(self):
        return self.likes.filter(is_like=False).count()

    def __str__(self):
        return f"{self.author} on {self.tweet}"

class CommentLike(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_like = models.BooleanField(null=True)

    class Meta:
        unique_together = ('comment', 'user')
