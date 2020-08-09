from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods


# Create your views here.
def index(request):
    return render(request, 'api/index.html')


@require_http_methods(["POST"])
def get_books(request):
    return HttpResponse(f"{request.POST['query']}")