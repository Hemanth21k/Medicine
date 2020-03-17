from django.contrib.auth.models import User
from django.db import models
from cart.models import Cart
from django.db.models.signals import post_save
from django.dispatch import receiver

class History(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    ordered_date = models.DateTimeField()
    ordered_items = models.ManyToManyField(Cart)

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    cart_items=models.ManyToManyField(Cart)
    signup_confirmation = models.BooleanField(default=False)
    address = models.CharField(max_length=256, default=True)
    history = models.ManyToManyField(History)


@receiver(post_save,sender=User)
def update_profile_signal(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()





