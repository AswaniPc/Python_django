from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.conf import settings
from django.contrib.auth.models import User
from django.db import connection
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.template.loader import render_to_string


class UserDefaultAddress(models.Model):
	user = models.OneToOneField(User)
	shipping = models.ForeignKey("UserAddress", null=True, blank=True, related_name="user_address_shipping_default")
	billing = models.ForeignKey("UserAddress", null=True,blank=True, related_name="user_address_billing_default")

	def __unicode__(self):
		return str(self.user.username)

class UserAddressManager(models.Manager):
	def get_billing_addresses(self, user):
		return super(UserAddressManager, self).filter(billing=True).filter(user=user)

class UserAddress(models.Model):
	user = models.ForeignKey(User)
	address = models.CharField(max_length=120)
	address2 = models.CharField(max_length=120, null=True, blank=True)
	city = models.CharField(max_length=120)
	state = models.CharField(max_length=120, null=True, blank=True)
	country = models.CharField(max_length=120)
	zipcode = models.CharField(max_length=25)
	phone =  models.CharField(max_length=120)
	shipping = models.BooleanField(default=True)
	billing = models.BooleanField(default=False)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return self.get_address()

	def get_address(self):
		return "%s, %s, %s, %s, %s" %(self.address, self.city, self.state, self.country, self.zipcode)

	objects = UserAddressManager()

	class Meta:
		ordering = ['-updated', '-timestamp']


class EmailConfirmed(models.Model):
	user = models.OneToOneField(User)
	activation_key = models.CharField(max_length=200)
	confirmed = models.BooleanField(default=False)

	def __unicode__(self):
		return str(self.confirmed)

	def activate_user_email(self):
		#send email here & render a string
		activation_url = "%s%s" %(settings.SITE_URL, reverse("activation", args=[self.activation_key]))
		context = {
			"activation_key": self.activation_key,
			"activation_url": activation_url,
			"user": self.user.username,
		}
		message = render_to_string("accounts/activation_message.txt", context)
		subject = "Activate your Email"
		self.email_user(subject, message, settings.DEFAULT_FROM_EMAIL)

	def email_user(self, subject, message, from_email=None, **kwargs):
		send_mail(subject, message, from_email, [self.user.email], kwargs)




class UserStripe(models.Model):
	user = models.OneToOneField(User)
	stripe_id = models.CharField(max_length=120, null=True, blank=True)

	def __unicode__(self):
		return str(self.stripe_id)