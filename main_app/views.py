from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from .models import Finch
from .forms import FeedingForm

# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello World</h1>')

def about(request):
    return render(request, 'about.html',)

def finches_index(request):
    finches = Finch.objects.order_by('name')
    return render(request, 'finches/index.html', {'finches' : finches})


def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    feeding_form = FeedingForm()
    return render(request, 'finches/detail.html', {'finch': finch,
    'feeding_form': feeding_form })
    

class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'

class FinchUpdate(UpdateView):
    model = Finch
    fields = ['color', 'description', 'feedsPerDay']

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches/'


def add_feeding(request, finch_id):
    form = FeedingForm(request.POST)
    # validate the form first
    if form.is_valid():
        new_feeding = form.save(commit=False)
        # new_feeding.cat = finch_id
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect('finches_detail', finch_id=finch_id)
