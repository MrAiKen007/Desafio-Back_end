from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile, AcaoSustentavel

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=AcaoSustentavel)
def update_user_points(sender, instance, created, **kwargs):
    if created:
        profile = instance.user.profile
        profile.total_points += instance.points
        profile.save()
