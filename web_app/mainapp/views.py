from django.shortcuts import render, get_object_or_404, redirect

from mainapp.forms import MainTableForm
from mainapp.models import MainTable


def record(request, pk):
    record = get_object_or_404(MainTable, pk=pk)

    if request.method == "POST":
        rform = MainTableForm(request.POST, instance=record)
        if rform.is_valid():
            record = rform.save(commit=False)
            record.save()
            return redirect('record', pk=record.pk)
    else:
        rform = MainTableForm()
    return render(request, 'mainapp/record.html', {'record': record, 'rform': rform})


    # title = f'{MainTable.snils}'
    # context = {
    #     'title': title,
    #     'record': record,
    # }
