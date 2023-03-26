from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from .forms import NotesheetForm
from .models import Notesheet, NotesheetReview

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid email or password')
    return render(request, 'login.html')

@login_required
def dashboard(request):
    user = request.user
    if user.is_student:
        notesheets = Notesheet.objects.filter(student=user.student)
    elif user.is_class_coordinator:
        notesheets = Notesheet.objects.filter(channel__class_coordinator=user.classcoordinator)
    elif user.is_head_of_department:
        notesheets = Notesheet.objects.filter(channel__head_of_department=user.headofdepartment)
    elif user.is_dean:
        notesheets = Notesheet.objects.filter(channel__dean=user.dean)
    return render(request, 'dashboard.html', {'notesheets': notesheets})

@login_required
def create_notesheet(request):
    form = NotesheetForm(request.POST or None)
    if form.is_valid():
        notesheet = form.save(commit=False)
        notesheet.student = request.user.student
        notesheet.save()
        messages.success(request, 'Notesheet created successfully')
        return redirect('dashboard')
    return render(request, 'create_notesheet.html', {'form': form})
