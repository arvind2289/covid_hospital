from datetime import datetime

from django.shortcuts import render

# Create your views here.
from bed.models import Patient
from django.views import View
from django.views.generic import CreateView, ListView
from django.shortcuts import render

from .models import BedDetails


def CreatePatient(request):
    # def get(self, request):
    if request.method == 'POST':
        patient = request.POST['patient']
        bed_type = request.POST['bed_type']
        # BedDetails.objects.filter()
        beds =BedDetails.objects.filter(type__icontains=bed_type, occupied__icontains=0)
        index = []
        for i in beds:
            index.append(i)

        if not index:
            mgs = bed_type+" " +''+'This type bed not free'
            return render(request, 'index.html', {'bed_type': mgs})

        idx = index[0].bed_index


        instance_obj = BedDetails.objects.get(bed_index=idx)
        instance_obj.occupied = 1
        instance_obj.save()
        patient=Patient.objects.create(patient_name=patient,bed=instance_obj)
        return render(request, 'index.html',{'patient':patient})

    return render(request, 'index.html',)

def Discharge(request):
        if request.method == "POST":
            patient = request.POST['patient']
            try:
                pt = Patient.objects.filter(patient_name__icontains=patient,discharged__icontains=0)[0]
                pt.bed.occupied = False
                pt.discharged = True
                pt.unallocated_on = datetime.now()
                pt.save()
                return render(request,'discharge.html',{'pt':pt})
            except:
                pts = patient+' '+'this patient is no found our record'
                return render(request, 'discharge.html', {'pts': pts})
        return render(request, 'discharge.html', )


class BedList(ListView):
    def get_queryset(self):
        model = BedDetails
        template_name = "total_bed.html"
        #if status == 'ALL':
        queryset = BedDetails.objects.all().order_by("id")
        return queryset

class PatientDischargelist(ListView):
    def get_queryset(self):
        model = Patient
        template_name = "patient_list.html"
        #if status == 'ALL':
        queryset = Patient.objects.filter(discharged=1).order_by("id")
        return queryset
