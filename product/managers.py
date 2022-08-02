from django.db import models


class ProductQuerySet(models.QuerySet):
    def is_popular(self):
        return self.filter(is_popular=True).order_by('-created_at')[:12]

    def is_summer(self):
        return self.filter(is_summer=True).order_by('-created_at')[:12]

    def is_discount(self):
        return self.filter(is_discount=True).order_by('-created_at')[:12]

    def is_week(self):
        return self.filter(is_week=True).order_by('-created_at')[:1]

    def is_top(self):
        return self.filter(is_top=True).order_by('-created_at')[:1]


class ProductManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return ProductQuerySet(self.model, using=self._db)

    def is_popular(self):
        return self.get_queryset().is_popular()

    def is_summer(self):
        return self.get_queryset().is_summer()

    def is_discount(self):
        return self.get_queryset().is_discount()

    def is_week(self):
        return self.get_queryset().is_week()

    def is_top(self):
        return self.get_queryset().is_top()


class CategoryQuerySet(models.QuerySet):
    pass
