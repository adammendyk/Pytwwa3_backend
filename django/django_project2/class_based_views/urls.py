from django.urls import path

from . import views

app_name = "views"

urlpatterns = [
    path('hello', views.hello, name="hello"),
    path('hello2', views.HelloView.as_view(), name='hello2'),

    path('person/<int:id>', views.person_detail, name='person_detail')
]