from django.db import models
from django.urls import reverse

from main.models.supply import Supply
from main.models.supply_chain import SupplyChain


class UploadFiles(models.Model):
    file = models.FileField(verbose_name='Файл')
    supply = models.ForeignKey(Supply, on_delete=models.CASCADE, verbose_name='Доставка')
    supply_chain = models.ForeignKey(SupplyChain, on_delete=models.CASCADE, verbose_name='Цепь доставки', null=True)
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name

    class Meta:
        ordering = ['supply', 'supply_chain', '-time_create']
        indexes = [
            models.Index(fields=['supply', 'supply_chain', '-time_create'])
        ]
    #
    # def get_absolute_url(self):
    #     return reverse('cargo', kwargs={'supply_id': self.supply_id, 'cargo_id': self.id})