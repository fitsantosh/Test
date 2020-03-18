
from django import forms
from .models import Employee
class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields=['Actions','Employement_Type']

class EmployeeFormBU(forms.ModelForm):
    class Meta:
        model=Employee
        fields=['Actions2']
class EmployeeFormHR(forms.ModelForm):
    class Meta:
        model=Employee
        fields=['Actions3']
class EmployeeFormFinance(forms.ModelForm):
    class Meta:
        model=Employee
        fields=['Actions4']
