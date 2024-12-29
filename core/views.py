from django.shortcuts import render
from .models import DataTable, Task
from .forms import DataTableForm


def dashboard(request):
    tables = DataTable.objects.all()
    tasks = Task.objects.filter(assigned_to=request.user)
    return render(request, 'dashboard.html', {'tables': tables, 'tasks': tasks})

def create_table(request):
    if request.method == 'POST':
        form = DataTableForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = DataTableForm()
    return render(request, 'create_table.html', {'form': form})