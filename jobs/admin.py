from django.contrib import admin
from .models import Ups, Customer, Fse, Job, Note,Cap, UpsPart, CapDc, CapInput, CapOutput
# Register your models here.

admin.site.register(Ups)
admin.site.register(Customer)
admin.site.register(Fse)
admin.site.register(Job)
admin.site.register(Note)
admin.site.register(Cap)
admin.site.register(UpsPart)
admin.site.register(CapDc)
admin.site.register(CapInput)
admin.site.register(CapOutput)

