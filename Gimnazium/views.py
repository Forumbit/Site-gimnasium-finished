from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.generic import CreateView, UpdateView, DeleteView, View
from .forms import ZamenaForm, Additional_zamenaForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class Hello(View):
    def get(self, request):
        zamena = Zamena.objects.all()
        additional = Additional_zamena.objects.all()
        return render(request, 'index.html', context={'zamena': zamena, 'addit': additional})


class ZamenaCreateView(LoginRequiredMixin, CreateView):
    raise_exception = True
    model = Zamena
    form_class = ZamenaForm
    template_name = 'zamena_create.html'
    success_url = reverse_lazy('index_url')


class ZamenaUpdateView(LoginRequiredMixin, UpdateView):
    raise_exception = True
    model = Zamena
    form_class = ZamenaForm
    template_name = 'zamena_update.html'
    context_object_name = 'zamena'
    success_url = reverse_lazy('index_url')


class ZamenaDeleteView(LoginRequiredMixin, DeleteView):
    raise_exception = True
    model = Zamena
    template_name = 'index.html'
    success_url = reverse_lazy('index_url')


class AdditZamenaCreateView(LoginRequiredMixin, CreateView):
    raise_exception = True
    model = Additional_zamena
    form_class = Additional_zamenaForm
    template_name = 'addit_create.html'
    success_url = reverse_lazy('index_url')


class AdditZamenaUpdateView(LoginRequiredMixin, UpdateView):
    raise_exception = True
    model = Additional_zamena
    form_class = Additional_zamenaForm
    template_name = 'addit_update.html'
    context_object_name = 'addit'
    success_url = reverse_lazy('index_url')


class AdditZamenaDeleteView(LoginRequiredMixin, DeleteView):
    raise_exception = True
    model = Additional_zamena
    template_name = 'index.html'
    success_url = reverse_lazy('index_url')


class Zamena_all_delete(LoginRequiredMixin, View):
    raise_exception = True

    def get(self, request):
        model = Zamena.objects.all()
        model.delete()
        return render(request, 'index.html')
