from django.http import HttpResponse


def index(request):
    return HttpResponse("Marcos Jonnhy Paixão")