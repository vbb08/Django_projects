'''
#NOT needed if in views.py there are classes with CreateView, UpdateView and DeleteView
from django.forms import ModelForm
from autos.models import Make


# Create the form class.
class MakeForm(ModelForm):
    class Meta:
        model = Make
        fields = '__all__'
'''