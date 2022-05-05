from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Printer)
class PrinterAdmin(admin.ModelAdmin):
    pass


@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    pass


@admin.register(PrintType)
class PrintTypeAdmin(admin.ModelAdmin):
    pass
