from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['id']

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    class Meta:
        ordering = ['id']

    category = models.ForeignKey("Category", null=True, blank=True,
                                 on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    detail = models.CharField(max_length=254, blank=True)
    description = models.TextField()
    size = models.CharField(max_length=12)
    proof = models.DecimalField(max_digits=3, decimal_places=1)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=2, decimal_places=1, null=True,
                                 blank=True, default=0.0)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name
