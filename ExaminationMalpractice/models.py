from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.utils import timezone

from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255,unique=True)
    registration_no = models.CharField(max_length=255,unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    email = models.EmailField(max_length=255,unique=True)
    tel = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    course = models.CharField(max_length=255)
    year_of_study = models.IntegerField
    added_on = models.DateTimeField(_('date joined'), default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(_('active'), default=True)
    photograph = models.ImageField(upload_to='photos/')

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','registration_no','first_name','last_name']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self):
        return f"{self.username},{self.first_name},{self.last_name},{self.tel}"



        
