from django import forms
from .models import *


class PrintLabelsForm(forms.Form):
    text = forms.CharField(label='Текст для печати')
    amount = forms.IntegerField(label='Количество наклеек')
    printer_choice = forms.ChoiceField(label='Выбор принтера', choices=zip(Printer.objects.all().
                                                                           values_list('cups_name'),
                                                                           Printer.objects.all()))
