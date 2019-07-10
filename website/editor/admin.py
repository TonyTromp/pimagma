from django.contrib import admin
# Register your models here.
from .models import *
from django.contrib.admin import SimpleListFilter

class L1StrategicalThreatAdmin(admin.ModelAdmin):
    ordering = ('id','Title',)

def custom_titled_filter(title):
    class Wrapper(admin.FieldListFilter):
        def __new__(cls, *args, **kwargs):
            instance = admin.FieldListFilter.create(*args, **kwargs)
            instance.title = title
            return instance
    return Wrapper


class L2TacticalThreatAdmin(admin.ModelAdmin):
    ordering = ('id','Classifier','Title')
    search_fields = ['Title','Description']
    list_display = ('get_class','Title','Description')
    list_filter = ['Parent__Title','Parent__RiskDriver']

admin.site.register(BusinessDriver)
admin.site.register(ComplianceDriver)

admin.site.register(SecurityLayer)
admin.site.register(SecurityControl)
admin.site.register(SecurityPerimeter)

admin.site.register(L1StrategicalThreat, L1StrategicalThreatAdmin)
admin.site.register(L2TacticalThreat, L2TacticalThreatAdmin)
admin.site.register(L3OperationalThreat)

admin.site.site_header = 'UseCase Administration'
admin.site.site_title = 'Magma | UseCase Administration'

admin.site.index_title = 'Site administration'
