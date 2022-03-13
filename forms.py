from django import forms

class scholorshipform(forms.Form):
    School_Name = forms.CharField(max_length=50)
    Student_Name = forms.CharField(max_length=40)
    Father_Name = forms.CharField(max_length=40)
    Mother_Name = forms.CharField(max_length=40)
    Class_std = forms.IntegerField()
    Roll_No = forms.IntegerField()
    Mobile = forms.IntegerField()
    Mail_id = forms.EmailField()