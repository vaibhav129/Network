from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    followe = models.ManyToManyField(
        "self", blank=True, symmetrical=False, related_name="ufollowing"
    )
    def follow(self,target):
        profilei.objects.create(follower=self,following=target)

    def unfollow(self,target):
        profilei.objects.get(follower=self,following=target).delete()

class post(models.Model):
    content = models.TextField(max_length=300)
    user = models.CharField(max_length=64,null=True,blank=True)
    time = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)

    def serialize(self):
        return {
            "likes": self.likes
        }

class profilei(models.Model):
    follower = models.ForeignKey(User, related_name='following',on_delete=models.CASCADE,default=0)
    following = models.ForeignKey(User,related_name='followers',on_delete=models.CASCADE,default=0)
    user = models.ManyToManyField(User,related_name='dsds',null=True,blank=True)




class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likeduser")
    post = models.ForeignKey(post, on_delete=models.CASCADE, related_name="likedpost")

