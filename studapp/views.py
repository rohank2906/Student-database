
from django.shortcuts import render,redirect
from studapp.models import Student
from studapp.forms import StudentForm


def home(request):
    return render(request,'home.html')

def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def login_validate(request):
    uemail = request.POST.get('uemail')
    upass = request.POST.get('upass')
    print(uemail, upass)
    if (uemail == "rohan@gmail.com" and upass == "rohan"):
        return render(request, 'home.html')


def error(request):
    return render(request,'error.html')

def show_all(request):
    students=Student.objects.all()
    return render(request,'show_all.html',{'students':students})

def stud_add_record(request):
    if request.method == "POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show_all")
                
            except:
                return redirect("/error")
                
    else:
        form=StudentForm()
    return render(request, 'stud_add_record.html', {'form':form})



def stud_data_saved(request):
    return render(request,'stud_data_saved.html')



def edit_rec(request):
    students=Student.objects.all()
    return render(request,'edit_rec.html',{'students':students})

def edit(request,id):
    student=Student.objects.get(id=id)
    return render(request,'edit.html',{'student':student})



def update(request,id):
    student=Student.objects.get(id=id)
    form=StudentForm(request.POST ,instance=student)
    if form.is_valid():
        form.save()
        return redirect('/edit_rec')

    return render(request,'edit_rec.html',{'student':student})

def delete_rec(request):
    students=Student.objects.all()
    return render(request,'delete_rec.html',{'students':students})

def destroy(request,id):
    student=Student.objects.get(id=id)
    student.delete()
    return redirect('/delete_rec')