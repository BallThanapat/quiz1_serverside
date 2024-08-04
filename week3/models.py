from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=150)
    address = models.JSONField(null=True)

class Cart(models.Model):
    customer_id = models.ForeignKey("shop.Customer",on_delete=models.PROTECT)
    create_date = models.DateTimeField(auto_now_add=True,null=False)
    expired_in = models.IntegerField(null=True,default=60)

class CartItem(models.Model):
    cart_id = models.ForeignKey("shop.Cart",on_delete=models.PROTECT)
    product_id = models.ForeignKey("shop.Product",on_delete=models.PROTECT)
    amount = models.IntegerField(null=False,default=1)

class Order(models.Model):
    customer_id = models.ForeignKey("shop.Customer",on_delete=models.PROTECT)
    order_date = models.DateField(auto_now_add=True,null=False)
    remark = models.TextField(null=True)

class OrderItem(models.Model):
    order_id = models.ForeignKey("shop.Order",on_delete=models.PROTECT)
    product_id = models.ForeignKey("shop.Product",on_delete=models.PROTECT)
    amount = models.IntegerField(null=False,default=1)

class ProductCategory(models.Model):
    name = models.CharField(max_length=150,null=False)

class Product(models.Model):
    name = models.CharField(max_length=150,null=False)
    description = models.TextField(null=True)
    remaining_amount = models.IntegerField(null=False,default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2,null=False)
    product_category = models.ManyToManyField("shop.ProductCategory")

class Payment(models.Model):
    order_id = models.OneToOneField("shop.Order",on_delete=models.PROTECT)
    payment_date = models.DateField(auto_now_add=True,null=False)
    remark = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,null=False)
    discount = models.DecimalField(max_digits=10, decimal_places=2,null=False,default=0)

class PaymentItem(models.Model):
    payment_id = models.ForeignKey("shop.Payment",on_delete=models.PROTECT)
    order_item = models.OneToOneField("shop.OrderItem",on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=10, decimal_places=2,null=False)
    discount = models.DecimalField(max_digits=10, decimal_places=2,null=False,default=0)

class PaymentMethod(models.Model):
    payment_id = models.ForeignKey("shop.Payment",on_delete=models.PROTECT)
    method_choice = {
        ('OR', 'OR'),
        ('CREDIT', 'CREDIT'),
    }
    method = models.CharField(max_length=10,choices=method_choice,null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2,null=False)