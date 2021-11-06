from typing import ContextManager
from django.shortcuts import render
from .forms import NewAccountForm

# Create your views here.

def register(request):
    form = NewAccountForm()
    if request.method   ==  'POST':
        form    =   NewAccountForm(request.POST)
        if  form.is_valid():
            form.save()
            print('Saved')
    context = {
        "form":form,
    }
    return render(request,'registration/register.html',context)




