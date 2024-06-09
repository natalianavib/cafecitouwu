from django.shortcuts import render, redirect
from .models import Complaint
from .forms import ComplaintForm

def submit_complaint(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ComplaintForm()
    return render(request, 'complaints/index.html', {'form': form})

def success(request):
    return render(request, 'complaints/success.html')
