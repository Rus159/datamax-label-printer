from .models import *
from django import forms
from django.shortcuts import render
from .forms import PrintLabelsForm
import label_printer.printer_help as printer_help

# Create your views here.


def print_labels(request):
    if request.method == 'POST':
        form = PrintLabelsForm(request.POST)
        if form.is_valid():
            printer_help.print_labels(form.cleaned_data['text'], form.cleaned_data['amount'],
                                      form.cleaned_data['printer_choice'][2:-3])
        form = PrintLabelsForm()
        return render(request=request, template_name='print_labels.html', context={'form': form})

    else:
        form = PrintLabelsForm()
        return render(request=request, template_name='print_labels.html', context={'form': form})
