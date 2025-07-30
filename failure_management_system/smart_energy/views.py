# smart_energy/views.py
from django.shortcuts import render
from .models import GridFailure # <--- Import your GridFailure model

def home_page(request):
    # Fetch all GridFailure objects from the database, ordered by timestamp
    failures = GridFailure.objects.all().order_by('-timestamp') # .all() gets all, .order_by('-timestamp') sorts by newest first

    context = {
        'page_title': "Grid Failures Dashboard",
        'grid_failures': failures # Pass the fetched data to the template
    }
    return render(request, 'smart_energy/home.html', context)