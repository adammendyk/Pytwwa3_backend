from django.http import Http404
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.core.exceptions import ObjectDoesNotExist


from .models import Person
from .forms import PersonForm

# Function-based view
def hello(request):
    return HttpResponse("Hello, world!")


# Class-based view
class HelloView(View):
    def get(self, request):
        return HttpResponse("Hello, world!")


# Function-based view
def person_detail(request, id):
    p = get_object_or_404(Person, id=id)

    return render(request, 'class_based_views/person.html', {
        "person": p
    })


# Class-based view
class PersonView(View):
    def get(self, request, id):
        p = get_object_or_404(Person, id=id)
        return render(request, 'class_based_views/person.html', {
            "person": p
        })


# Generic view - DetailView
class PersonDetailView(DetailView):
    model = Person


# Function-based view
def create_person(request):
    if request.method == "GET":
        form = PersonForm()
        return render(request, 'class_based_views/create-person.html', {
            "form": form
        })
    else:
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()

        return HttpResponse("ok")


# Class-based view
class PersonCreate(View):
    def get(self, request):
        form = PersonForm()
        return render(request, 'class_based_views/create-person.html', {
            "form": form
        })

    def post(self, request):
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()

        return HttpResponse("ok")


# Generic view - CreateView
class PersonCreateView(CreateView):
    model = Person
    fields = '__all__'