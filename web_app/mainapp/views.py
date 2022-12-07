from django.shortcuts import render, get_object_or_404

from mainapp.models import MainTable


def record(request, pk, slug):
    record = get_object_or_404(MainTable, pk=pk, slug=slug)
    title = f'{MainTable.snils}'
    context = {
        'title': title,
        'record': record,
    }
    return render(request, 'mainapp/record.html', context)
