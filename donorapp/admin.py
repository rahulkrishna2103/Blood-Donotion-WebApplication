from django.contrib import admin
from .models import BloodDonor
# Register your models here.
class BloodDonorAdmin(admin.ModelAdmin):
    list_display = ('name', 'bloodgroup', 'gender', 'phonenumber', 'city')

admin.site.register(BloodDonor, BloodDonorAdmin)