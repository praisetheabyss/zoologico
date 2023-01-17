from django.contrib import admin
from app.models import *

# Register your models here.

@admin.register(Animais)
class AnimaisAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", 'animal', 'sexo')
admin.site.register(EspeciesAnimais)
admin.site.register(Sexo)