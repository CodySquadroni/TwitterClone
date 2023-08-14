from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField(User, related_name='followed_by', symmetrical=False)
    # image = models.ImageField(blank=True, default="profile_pic.jpg", upload_to='profile_pictures')
    # bio = models.CharField(blank=True, max_length=160)
    # birth_date = models.CharField(blank=True, max_length=9)
    # location = models.CharField(blank=True, max_length=100)
    joined_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username


# Create Profile when a new User is created
def build_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        print('TEST')
        print(instance.profile.id)
        print(user_profile.id)

        # Have the user follow themselves to be able to show its own tweets
        # user_profile.follows.set([instance.profile.id])
        # user_profile.follows.set(user_profile.id)
        # user_profile.follows.set([user_profile.id])
        user_profile.follows.add(user_profile.user)
        user_profile.save()


post_save.connect(build_profile, sender=User)
