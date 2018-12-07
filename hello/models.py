from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from jsonfield import JSONField

class  profile(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    ucont = JSONField(default={},blank=True, null=False)
    uconfig = JSONField(default={},blank=True, null=False)
    city = models.CharField(default='0000000',blank=True, null=False, max_length=30)
    description = models.TextField(default='0000000',blank=True, null=False)
    template01 = models.TextField(default='Template 01 Is Empty!',blank=True, null=False)
    template02 = models.TextField(default='Template 02 Is Empty!',blank=True, null=False)
    template03 = models.TextField(default='Template 03 Is Empty!',blank=True, null=False)
    template04 = models.TextField(default='Template 04 Is Empty!',blank=True, null=False)
    template05 = models.TextField(default='Template 05 Is Empty!',blank=True, null=False)
    template06 = models.TextField(default='Template 06 Is Empty!',blank=True, null=False)
    template07 = models.TextField(default='Template 07 Is Empty!',blank=True, null=False)
    template08 = models.TextField(default='Template 08 Is Empty!',blank=True, null=False)
    template09 = models.TextField(default='Template 09 Is Empty!',blank=True, null=False)
    template10 = models.TextField(default='Template 10 Is Empty!',blank=True, null=False)
    noresptemplate01 = models.TextField(default='No Response Template 01 Is Empty!',blank=True, null=False)
    noresptemplate02 = models.TextField(default='No Response Template 02 Is Empty!',blank=True, null=False)
    noresptemplate03 = models.TextField(default='No Response Template 03 Is Empty!',blank=True, null=False)
    noresptemplate04 = models.TextField(default='No Response Template 04 Is Empty!',blank=True, null=False)
    noresptemplate05 = models.TextField(default='No Response Template 05  Is Empty!',blank=True, null=False)


    def __str__(self):
    	return str(self.User)
   



def set_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile = profile.objects.create(User=kwargs['instance'])


post_save.connect(set_profile, sender=User)




