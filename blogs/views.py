# Create your views here.
from django.shortcuts import render
from django.views import generic
from .models import Contents
from django.views.generic import ListView
from django.views.generic import CreateView
from .forms import ContentsModelForm


def home_view(request):
    return render(request, 'home.html')

# def display(request):
#   return render('index.html', {'obj': models.Contents.objects.all()})

class ContentsList(ListView):
    model=Contents
    queryset = Contents.objects.all().order_by('-created_at')
    template_name = 'index.html'


class ContentsDetail(generic.DetailView):
    model = Contents
    template_name = 'contents_detail.html'


class ContentsCreateView(CreateView):
    form_class = ContentsModelForm
    template_name = 'create.html'
    success_url = '/blogs'