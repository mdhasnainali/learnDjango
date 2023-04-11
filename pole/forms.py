from django import forms

class TeacherRegistration(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField(initial="hasnain")
    email = forms.EmailField(initial="md@gmail.com", disabled=True)
    password = forms.CharField(widget=forms.PasswordInput)
    textarea = forms.CharField(widget=forms.Textarea)
    file = forms.CharField(widget=forms.FileInput)
    checkBox = forms.CharField(widget=forms.CheckboxInput)