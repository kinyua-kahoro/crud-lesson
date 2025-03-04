from django.shortcuts import render,redirect
from .models import User
from .forms import UserForm


# Create your views here.
def user_list(request):
    users = User.objects.all()
    return render(request, 'listing_page.html', {'users':users})

def add_user(request):
    mydict={}
    form = UserForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    mydict['form'] = form
    return render(request, 'add.html', mydict)

def Edituser(request,id=None):
    one_record = User.objects.get(pk=id)
    form = UserForm(request.POST or None, request.FILES or None, instance=one_record)
    if form.is_valid():
        form.save()
        return redirect('/')
    mydict={'form':form}
    return render(request, 'edit.html', context=mydict)

def Deleteuser(request,eid=None):
    one_record = User.objects.get(pk=eid)
    if request.method == 'POST':
        one_record.delete()
        return redirect('/')
    return render(request, 'delete.html')

def Viewuser(request,eid=None):
    mydict={}
    one_record = User.objects.get(pk=eid)
    mydict['user'] = one_record
    return render(request, 'views.html', mydict)