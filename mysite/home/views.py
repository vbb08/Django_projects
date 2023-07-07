from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic


class HomeView(generic.ListView):
    template_name = 'home/main.html'

    '''
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]
'''

def owner(request):
    return HttpResponse("Hello, world. eae25100 is the polls owner.")
