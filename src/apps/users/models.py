from datetime import timezone

from django.contrib.auth.models import User
from django.db import models


class Role(models.Model):
    role_id = models.AutoField(primary_key=True, verbose_name="ID роли")
    role_name = models.CharField(max_length = 50, unique=True,verbose_name = "Название роли")
    max_books_allowed = models.PositiveIntegerField(default=5, verbose_name="Mакс. доступное количество книг") # type: ignore
    max_days_allowed = models.PositiveBigIntegerField(default=14, verbose_name="Макс. доступное количество дней") # type: ignore

    class Meta:
        db_table = "roles"
        verbose_name = "Роль"
        verbose_name_plural = "Роли"

    def __str__(self) -> str:
        return f"{self.role_name} до {self.max_books_allowed} книг / {self.max_days_allowed} дней"

class Reader(models.Model):
    reader_id = models.AutoField(primary_key = True, verbose_name ="ID читателя")
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null = True,
        blank = True,
        related_name = "readers",
        verbose_name = "Роль"
    )

    role = models.ForeignKey(
        Role,
        on_delete=models.PROTECT,
        db_column = "role_id",
        related_name= "readers",
        verbose_name = "Роль"
    )

    full_name = models.CharField(max_length=150, verbose_name="ФИО")
    phone = models.CharField(max_lenght = 30, verbose_name="Номер телефона")
    email = models.EmailField(unique=True, verbose_name="Почта")
    registration_date = models.DateField(default = timezone.now, verbose_name = "Дата регистрации") # type: ignore

    class Meta:
        db_table = "readers"
        verbose_name = "Читатель"
        verbose_name_plural = "Читатели"

    def __str__(self) -> str:
            return f" ФИО: {self.full_name} почта: ({self.email})"
