import email
from fractions import Fraction
import imp
from multiprocessing import context
from django.shortcuts import redirect, render
from .forms import FormForm

# Create your views here.

def index(request):
    context = {}
    return render(request, 'djangoapp/index.html', context=context)


def home(request):
    form = FormForm()
    context = {'form':form}

    if request.method == 'POST':
        form = FormForm(request.POST)

        if form.is_valid():
            print('validation success')
            print('name: '+ form.cleaned_data['name'])
            print('email: '+ form.cleaned_data['email'])
            print('text: '+ form.cleaned_data['text'])

            # name = request.POST.get('name')
            # email = request.POST.get('email')
            # text = request.POST.get('text')
            # print(name, email, text)
            return redirect('home')

        context = {'form':form}
    
        return render(request, 'djangoapp/home.html', context=context)
        
    
        






    return render(request, 'djangoapp/home.html', context=context)