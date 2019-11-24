from django.shortcuts import render, redirect
from .models import Messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm,StatusForm
from .models import Task,TaskStatus
from django.contrib.auth.models import User
from .models import Profile
# Create your views here.

def index(request):
    if request.method == 'POST':
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        print(ip)
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        message = request.POST.get("message")
        messageObject = Messages.objects.create(ip=ip,fname=fname,lname=lname,email=email,message=message)
        messageObject.save()
    return render(request,'Core/index.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'Core/register.html',{'form':form})

@login_required
def update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance = request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES, instance = request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)
    context = {
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request,'Core/updateProfile.html',context)

@login_required
def home(request):
    taskData = Task.objects.all()
    for data in taskData:
        checkObject = TaskStatus.objects.filter(taskCode=data,user=request.user)
        if not checkObject:
            TaskStatusObject = TaskStatus.objects.create(taskCode=data,user=request.user)
            TaskStatusObject.save()
    data = Task.objects.all().order_by('-startDate')
    return render(request,'Core/home.html',{'dataset':data})

@login_required
def profile(request):
    return render(request,'Core/profile.html')

@login_required
def progress(request):
    return render(request,'Core/progress.html')


@login_required
def taskDetail(request,pk):
    if request.method == 'POST':
        data = request.POST.get('inlineRadioOptions')
        TaskStatusObject = TaskStatus.objects.get(taskCode=pk,user=request.user)
        TaskStatusObject.status = data
        TaskStatusObject.save()
        print(data)
        if data == 'COMPLETE':
            TaskObject = Task.objects.get(id=pk)
            ProfileObject = Profile.objects.get(user=request.user)
            if TaskObject.isActive:
                ProfileObject.score+=TaskObject.taskScore
            ProfileObject.save()
    data = Task.objects.get(id=pk)
    userData = TaskStatus.objects.get(taskCode=data,user=request.user)
    return render(request,'Core/taskDetail.html',{'data':data, 'userData':userData})