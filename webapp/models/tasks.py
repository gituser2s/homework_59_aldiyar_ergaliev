from django.db import models
from django.utils import timezone


class Task(models.Model):
    description = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name="Заголовок"
    )
    detailed_description = models.TextField(
        max_length=2000,
        null=True,
        blank=True,
        verbose_name="Описание"
    )
    status = models.ForeignKey(
        to="webapp.Status",
        on_delete=models.PROTECT,
    )
    type = models.ManyToManyField(
        to="webapp.Type"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Время и дата создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Время и дата обновления"
    )
    is_deleted = models.BooleanField(
        verbose_name='Удалено',
        null=False,
        default=False
    )
    deleted_at = models.DateTimeField(
        verbose_name="Время и дата удаления",
        null=True,
        default=None
    )

    def __str__(self):
        return f"{self.description} - {self.status}"

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задание'
