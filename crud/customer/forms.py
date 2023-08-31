from django import forms
from .models import employee
class employeeform(forms.ModelForm):
    
    class Meta:
        model = employee
        fields = '__all__'

    labels={
        'fullname':'Full Name',
        'emp_code':'EMP.Code'
    }

    def __init__(self,*args,**kwargs):
        super(employeeform,self).__init__(*args,**kwargs)
        self.fields['position'].empty_label ="select"