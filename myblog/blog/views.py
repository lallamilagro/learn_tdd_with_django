from django.shortcuts import render

from django.views.generic import DetailView
from .models import Entry

class EntryDetail(DetailView):
    model = Entry
