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

    @request_mapping("/next4", method="get")
    def next4(self, request):
        return render(request, 'next4.html')

    @request_mapping("/register", method="get")
    def register(self, request):
        return render(request, 'register.html')

    @request_mapping('/css', method="get")
    def css(self, request):
        return render(request, 'css.html')

    @request_mapping('/css2', method="get")
    def css2(self, request):
        return render(request, 'css2.html')

    @request_mapping('/css3', method="get")
    def css3(self, request):
        return render(request, 'css3.html')

    @request_mapping('/css4', method="get")
    def css4(self, request):
        return render(request, 'css4.html')

    @request_mapping('/css5', method="get")
    def css5(self, request):
        return render(request, 'css5.html')