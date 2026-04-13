from django.contrib import admin
from jobapp.models import HyderabadJobs, BangaloreJobs, ChennaiJobs, PuneJobs

# Register your models here.

class HyderabadJobsAdmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title', 'eligibility', 'address', 'email', 'phone_number']


class BangaloreJobsAdmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title', 'eligibility', 'address', 'email', 'phone_number']


class ChennaiJobsAdmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title', 'eligibility', 'address', 'email', 'phone_number']


class PuneJobsAdmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title', 'eligibility', 'address', 'email', 'phone_number']


admin.site.register(HyderabadJobs, HyderabadJobsAdmin)
admin.site.register(BangaloreJobs, BangaloreJobsAdmin)
admin.site.register(ChennaiJobs, ChennaiJobsAdmin)
admin.site.register(PuneJobs, PuneJobsAdmin)
