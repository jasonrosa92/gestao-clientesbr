from django.shortcuts import render, redirect, get_object_or_404,resolve_url
from django.http import HttpResponseRedirect, HttpResponse
from .models import Person
from .form import PersonForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

@login_required
def persons_list(request):
    persons = Person.objects.all()
    return render(request, 'cliente/person.html', {'persons': persons})


@login_required
def persons_new(request):
    form = PersonForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(resolve_url('persons_list'))
    return render(request, 'cliente/person_form.html', {'form': form})


@login_required
def persons_update(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)


   # if form.is_valid():
    #    form.save()
     #   return redirect('persons_list')
    #return render(request, 'person_form.html', {'form': form})


@login_required
def persons_delete(request, id):
    person = get_object_or_404(Person, pk=id)

    if request.method == 'POST':
        person.delete()
        return HttpResponseRedirect(resolve_url('persons_list'))
    return render(request, 'cliente/person_deleted.html', {'person': person})
