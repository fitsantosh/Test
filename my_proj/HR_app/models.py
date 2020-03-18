from django.db import models
from django.db import models
from django.urls import reverse

In_CHOICES = [
    ('Approved', 'Approved'),
    ('On_Hold', 'On_Hold'),]
on_CHOICES = [
    ('Bench', 'Bench'),
    ('Internal', 'Internal'),
    ('External', 'External')]
G_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),]
# Create your models here.
class Employee(models.Model):
    Candidate_Name=models.CharField(blank=False,default=None,max_length=30)
    Gender=models.CharField(blank=False,choices=G_CHOICES,max_length=10)
    Email_ID=models.EmailField(blank=False,default=None,max_length=254)
    Contact_Number=models.IntegerField(blank=False,default=None)
    Experience=models.CharField(blank=False,default=None,max_length=30)
    Total_Experience=models.CharField(blank=False,default=None,max_length=30)
    Relevant_Experience=models.CharField(blank=False,default=None,max_length=30)
    Skill_Set=models.CharField(blank=False,default=None,max_length=30)
    Current_CTC=models.FloatField(blank=False,default=None,max_length=30)
    Notice_Period=models.CharField(blank=False,default=None,max_length=30)
    Actions=models.CharField(blank=False,choices=In_CHOICES,max_length=10)
    Actions2=models.CharField(blank=False,choices=In_CHOICES,max_length=10)
    Actions3=models.CharField(blank=False,choices=In_CHOICES,max_length=10)
    Actions4=models.CharField(blank=False,choices=In_CHOICES,max_length=10)
    Employement_Type=models.CharField(blank=False,choices=on_CHOICES,max_length=10)



    #def get_absolute_url(self):
        #return reverse("products:product-detail", kwargs={"id": self.id}) #f"/products/{self.id}/"
