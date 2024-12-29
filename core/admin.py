from django.contrib import admin
from.models import *


# class CustomUserAdmin(admin.ModelAdmin):
#     pass
#
#
# # Register your models here.
# admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(CustomUser)
admin.site.register(DataTable)
admin.site.register(Task)
admin.site.register(Report)