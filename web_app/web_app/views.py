from django.shortcuts import render

from mainapp.models import MainTable


def main(request):
    main_table = MainTable.objects.order_by('id')
    return render(request, 'web_app/index.html', {'main_table': main_table})


def about(request):
    return render(request, 'web_app/about.html')