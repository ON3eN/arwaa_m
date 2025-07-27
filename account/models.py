from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name="المستخدم"
    )
    phone = models.CharField("رقم الجوال", max_length=20, blank=True)
    address = models.TextField("العنوان", blank=True)

    class Meta:
        verbose_name = "الملف الشخصي"
        verbose_name_plural = "الملفات الشخصية"

    def __str__(self):
        return f"الملف الشخصي لـ {self.user.username}"
