from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Bed)
class DefaultAdmin(admin.ModelAdmin):
    list_display = ['id','number_of_bed']
@admin.register(BedDetails)
class BedDetailsAdmin(admin.ModelAdmin):


    list_display = ['id', 'type','occupied','bed_index','created_on']


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = [ 'patient_name',
                    'allocated_on','unallocated_on',
                    'discharged','bed_type','bed_index','occupied_bed']

    def bed_type(self, inst):
        return inst.bed.type

    bed_type.allow_tags = True
    bed_type.short_description = "Bed Type"


    def bed_index(self, inst):
        return inst.bed.bed_index

    bed_index.allow_tags = True
    bed_index.short_description = "Bed Index"

    def occupied_bed(self, inst):
        return inst.bed.occupied

    occupied_bed.allow_tags = True
    occupied_bed.short_description = "Bed Occupied"