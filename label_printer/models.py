from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.


class PrintType(models.Model):
    name = models.CharField(max_length=150, blank=False)

    def __str__(self):
        return self.name


class Label(models.Model):
    width = models.IntegerField(verbose_name='Ширина, мм', blank=False)
    height = models.IntegerField(verbose_name='Высота, мм', blank=False)
    can_be_printed = MultiSelectField(verbose_name='Что может быть напечатано',
                                      choices=((item.name, item.name) for item in PrintType.objects.all()), default='')

    def __str__(self):
        return f'{self.width}x{self.height}'


class Printer(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=150, blank=False)
    place = models.CharField(verbose_name='Место', max_length=150, blank=False)

    cups_name = models.CharField(verbose_name='Имя в CUPS', max_length=50, blank=False)

    label_size = models.ForeignKey(Label, verbose_name='Размер наклейки',
                                   blank=False, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.name}, {self.place}'
