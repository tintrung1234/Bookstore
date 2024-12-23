from django.db import models
from user.models import CustomerUser
from cart.models import Cart

class Order(models.Model):
    user = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    cart =  models.ForeignKey(Cart, on_delete=models.CASCADE)
    ship_address = models.CharField(max_length=255, default='')
    order_description = models.TextField(default='')
    status = models.BooleanField(default=False)
