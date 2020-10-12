

from django import forms

from .models import *




class InitialDataEntryForm(forms.ModelForm):
    class Meta:
        model = InitialDataEntry
        fields = "__all__"

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        exclude=('weapon_out','weapon_in','date')        

class AttendanceReturnForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ('weapon_in',)                
  