from django.db import models

class Category(models.Model):
    name = models.CharField("اسم التصنيف", max_length=100)

    class Meta:
        verbose_name = "تصنيف"
        verbose_name_plural = "التصنيفات"

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name="التصنيف"
    )
    name = models.CharField("اسم المنتج", max_length=200)
    price = models.DecimalField("السعر", max_digits=8, decimal_places=2)
    image = models.ImageField("صورة المنتج", upload_to='products/', blank=True, null=True)

    class Meta:
        verbose_name = "منتج"
        verbose_name_plural = "المنتجات"

    def __str__(self):
        return self.name
