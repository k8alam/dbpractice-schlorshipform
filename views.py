from django.shortcuts import render
from .forms import scholorshipform
# Create your views here.
def show(r):
    form = scholorshipform
    my_dict = {'form':form}

    return render(r,'formapp.html/',context=my_dict)