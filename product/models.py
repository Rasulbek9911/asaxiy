from re import T
from django.db import models
from helpers.models import BaseModel
# Create your models here.
from ckeditor_uploader.fields import RichTextUploadingField
from common.models import User
from product.managers import ProductManager


class Option(BaseModel):
    title = models.CharField(max_length=256)
    is_filter = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class OptionValue(BaseModel):
    title = models.CharField(max_length=256)
    option = models.ForeignKey(Option, on_delete=models.CASCADE, related_name='options')

    def __str__(self):
        return self.title


class Category(BaseModel):
    title = models.CharField(max_length=256)
    content = models.TextField(null=True, blank=True)
    slug = models.CharField(max_length=256)
    icon = models.FileField(upload_to="category/", null=True, blank=True)

    options = models.ManyToManyField(Option)
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Product(BaseModel):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256)
    content = models.TextField()
    image = models.ImageField(
        upload_to="product_image", editable=False, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    in_stock = models.IntegerField(default=0)

    price = models.DecimalField(
        max_digits=19, decimal_places=2, verbose_name="Sotilish narxi")
    price_discount = models.DecimalField(
        max_digits=19, decimal_places=2, null=True, blank=True, verbose_name="Chegirmadagi narxi(ustiga chizilgan)")

    rate = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)

    saveds = models.ManyToManyField(User, related_name="saved_products", null=True, blank=True)
    options = models.ManyToManyField(Option)

    is_popular = models.BooleanField(default=False)
    is_summer = models.BooleanField(default=False)
    is_discount = models.BooleanField(default=False)
    is_week = models.BooleanField(default=False)
    is_top = models.BooleanField(default=False)

    objects = ProductManager()

    def set_image(self):
        main_image = ProductImage.objects.filter(
            product=self, is_main=True).first()
        self.image = main_image
        self.save()

    def __str__(self):
        return self.title


class ProductImage(BaseModel):
    product = models.ForeignKey(
        Product, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="product_image/")
    is_main = models.BooleanField(default=False)


class Comment(BaseModel):
    product = models.ForeignKey(Product, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, related_name="comments", on_delete=models.CASCADE)
    rate = models.IntegerField(default=0)
    content = models.TextField()

# SIGNAL
# comment count, rate.
