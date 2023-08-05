from django.shortcuts import render

# Create your views here.
from ads.models import Ad
from ads.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView


class AdListView(OwnerListView):
    model = Ad
    fields = ['title', 'text', 'price']
    # By convention:
    # template_name = "myarts/article_list.html"


class AdDetailView(OwnerDetailView):
    model = Ad
    fields = ['title', 'text', 'price']

class AdCreateView(OwnerCreateView):
    model = Ad
    # List the fields to copy from the Article model to the Article form
    fields = ['title', 'text', 'price']

class AdUpdateView(OwnerUpdateView):
    model = Ad
    fields = ['title', 'text', 'price']
    # This would make more sense
    # fields_exclude = ['owner', 'created_at', 'updated_at']


class AdDeleteView(OwnerDeleteView):
    model = Ad
