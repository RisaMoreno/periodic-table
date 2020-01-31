from django.shortcuts import render, redirect
import json
from atomicData import data
all_atoms = json.loads(data)

def index(request):
    return render(request, "index.html")

def show_atom(request, atomic_num):
    print(all_atoms[int(atomic_num-1)])
    context = {
        'atom' : all_atoms[atomic_num-1]
    }
    return render(request, "show.html", context)