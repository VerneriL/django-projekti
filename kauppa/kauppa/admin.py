from django.contrib import admin

from .models import Tuote

class TuoteAdmin(admin.ModelAdmin):
    fields = ["nimi"]

admin.site.register(Tuote, TuoteAdmin)
