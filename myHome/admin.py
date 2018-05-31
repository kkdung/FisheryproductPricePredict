from django.contrib import admin
from myHome.models import place

# Register your models here.
class viewAdmin(admin.ModelAdmin):
    list_display = ('index','수산물표준코드명','산지조합명')
admin.site.register(place,viewAdmin)