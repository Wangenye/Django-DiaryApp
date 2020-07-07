# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import DiaryEntry
from .forms import DataEntryForm

# Create your views here.


def homePage(request):
    entries = DiaryEntry.objects.order_by('time_posted')
    # entry = DiaryEntry.objects.all()
    context = {'entries': entries}

    return render(request, 'diaryApp/index.html', context)


def addEntry(request):
    # tasks = DiaryEntry.objects.all()

    form = DataEntryForm()

    if request.method == 'POST':
        form = DataEntryForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('/')

    context = {'form': form}
    return render(request, 'diaryApp/add.html', context)


def updateTask(request, pk):
    entry = DiaryEntry.objects.get(id=pk)

    form = DataEntryForm(instance=entry)

    if request.method == 'POST':
        form = DataEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}

    return render(request, 'diaryApp/update.html', context)
