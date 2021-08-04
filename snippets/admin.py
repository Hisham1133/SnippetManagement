from django.contrib import admin
from .models import SnipetNotes, Tag, Snipets
# Register your models here.

admin.site.register([Snipets,SnipetNotes,Tag])


