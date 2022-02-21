from django.shortcuts import render
from django.views import View
from django_request_mapping import request_mapping


@request_mapping("")
class MyView(View):

    @request_mapping("/", method="get")
    def home(self, request):
        return render(request, 'home.html')

    @request_mapping("/next", method="get")
    def next(self, request):
        return render(request, 'next.html')

    @request_mapping("/next2", method="get")
    def next2(self, request):
        return render(request, 'next2.html')

    @request_mapping("/next3", method="get")
    def next3(self, request):
        return render(request, 'next3.html')