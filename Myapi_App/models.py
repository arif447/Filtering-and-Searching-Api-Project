from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.


class UserProfileManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('User must have email')
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=300, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    object = UserProfileManager()
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email


class Ingredient(models.Model):
    salad = models.IntegerField(default=0)
    cheese = models.IntegerField(default=0)
    meat = models.IntegerField(default=0)

    def __str__(self):
        return str(self.salad + self.cheese + self.meat)


class CustomerDetail(models.Model):
    delivery_address = models.TextField(blank=True)
    phone = models.IntegerField(blank=True)
    payment_type = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.delivery_address


class Order(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    ingredients = models.OneToOneField(Ingredient, on_delete=models.CASCADE, null=True)
    customer = models.OneToOneField(CustomerDetail, on_delete=models.CASCADE, null=True)
    price = models.CharField(max_length=20, blank=False)
    order_time = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.user + 'order'