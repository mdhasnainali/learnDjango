from django.http import HttpResponse
from django.shortcuts import render
from pole.models import Teacher
from pole.forms import TeacherRegistration


def index(request):
    text = {"hello":"for All", "a":1}
    return render(request, 'pole/ml.html',context=text)

def teachers_info(request):
    teach = Teacher.objects.all()
    return render(request, 'pole/show.html',{'t':teach})

def showFrom(request):
    if request.method == 'POST':
        fm = TeacherRegistration(request.POST)
        print(fm)
        print('This is post statement')
        print(fm.cleaned_data)
    else:
        fm = TeacherRegistration()
        print('This is get statement')
        # print(fm.cleaned_data)
    # fm.order_fields(field_order=['email','first_name', 'last_name'])
    return render(request, 'pole/forms.html',{'form':fm})

