from django.db import models
class Bed(models.Model):
    number_of_bed = models.IntegerField()

    def save(self, *args, **kwargs):
        number_of_bed = int(self.number_of_bed)
        switch = "private"
        for i in range(0, number_of_bed):
            if i % 2 == 0:
                BedDetails.objects.create(type= 'GENERAL',bed_index =i, occupied= False)  # (0,2,4)
            elif switch == "private":
                BedDetails.objects.create(type= 'SEMI_PRIVATE', bed_index=i,occupied =False)  # (1,5,9)
                switch = "semi_private"
            else:
                BedDetails.objects.create(type= 'PRIVATE',bed_index=i,occupied= False)  # (3,7,11)
                switch = "private"
        super(Bed, self).save(*args, **kwargs)

class BedDetails(models.Model):
    BED_TYPE = (
        ('GENERAL', 'GENERAL'),
        ('SEMI_PRIVATE', 'SEMI_PRIVATE'),
        ('PRIVATE', 'PRIVATE'),
    )

    type = models.CharField(max_length=100, choices=BED_TYPE, default='')
    occupied= models.BooleanField(default=False)
    bed_index = models.IntegerField()
    created_on = models.DateField(auto_now_add=True)

class Patient(models.Model):
    patient_name = models.CharField(max_length=200)
    bed = models.ForeignKey(BedDetails,on_delete=models.CASCADE,default=None,blank=True,null=True)
    allocated_on = models.DateField(auto_now_add=True)
    unallocated_on = models.DateTimeField(auto_now=False,null=True,blank=True)
    discharged = models.BooleanField(default=False)









