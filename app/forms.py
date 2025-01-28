from django import forms
from .models import *
class StudentDjangoForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    pno = forms.CharField(max_length=100, required=False)
    email = forms.CharField(max_length=100, required=False)
    add = forms.CharField(max_length=100, required=False)
    gender = forms.CharField(max_length=100, required=False)
    un = forms.CharField(max_length=100, required=True)
    pw = forms.CharField(max_length=100, required=True)

class StudentModelForm(forms.ModelForm):
    class Meta:
        model = StudentData
        fields = '__all__'
    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 5:
            return name
        return None
    
    def clean_pw(self):
        pw = self.cleaned_data.get('password')
        if len(pw) >= 8:
            return pw
        return None