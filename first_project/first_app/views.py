from django.forms import forms
from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, WebPage, AccessRecord, Users
from first_app import forms
from first_app.forms import NewUserForm

# Create your views here.
def index(request):
    my_data = {'name': 'Deep', 'age': 22}
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_record': webpage_list}
    return render(request, 'index.html', context = date_dict)

def users(request):
    user_list = Users.objects.all()
    users = {'users': user_list}
    return render(request, 'users.html', context=users)

def form_name_view(request):
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            print("SUCESSFULLY CONNECTED")
            print("Name:" + form.cleaned_data['name'])
            print("Email:" + form.cleaned_data['email'])
            print("Text:" + form.cleaned_data['text'])            
        
    return render(request, 'form.html', {'form': form})
    
def new_user_form(request):
    form = NewUserForm()
    
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            raise Exception("Form is not Valid")

    return render(request, 'signup.html', {'form': form})

def other(request):
    return render(request, 'other.html')

def relative(request):
    context = {'text': "hello deep", 'number': 100}
    return render(request, 'relative_url_template.html', context)