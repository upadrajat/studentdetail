from django.shortcuts import render,HttpResponse
from .forms import StudentForm
from .models import Student
from django.template import loader


def home(request):
    return render(request,'home.html')
def insert(request):
    if request.method=='POST':
        form=StudentForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            data="<h1>Insertion is successfully done</h1>"\
            "<a href='./'>Goto home</a>"
            return HttpResponse(data)
        else:
            print(form.errors)

    else:
        form=StudentForm()
        return render(request,'insert.html',{'form':form})

def display(request):
    det=Student.objects.all()
    if len(det)==0:
        data="<h1>no data found</h1>"\
              "<a href='./'>Goto home</a>"
        return HttpResponse(data)
    else:
        template=loader.get_template('details.html')
        context={'det':det}
        r=template.render(context,request)
        return HttpResponse(r)




