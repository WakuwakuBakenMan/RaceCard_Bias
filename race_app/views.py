import csv
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UploadFileForm
from .models import Race, Horse
from django.shortcuts import render

def race_card(request):
    races = Race.objects.all()
    return render(request, 'race_app/race_card.html', {'races': races})

def home(request):
    return render(request, 'race_app/home.html')

def import_races(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['file']
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)
            for row in reader:
                Race.objects.update_or_create(
                    id=row['id'],
                    defaults={
                        'date': row['date'],
                        'location': row['location'],
                    }
                )
            messages.success(request, 'Races imported successfully')
            return redirect('import_races')
    else:
        form = UploadFileForm()
    return render(request, 'race_app/import_races.html', {'form': form})

def import_horses(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['file']
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)
            for row in reader:
                race_id = row['race_id']
                try:
                    race = Race.objects.get(id=race_id)
                except Race.DoesNotExist:
                    messages.error(request, f'Race with id {race_id} does not exist')
                    continue

                Horse.objects.update_or_create(
                    name=row['name'],
                    defaults={
                        'age': row['age'],
                        'weight': row['weight'],
                        'odds': row['odds'],
                        'popularity': row['popularity'],
                        'race': race,
                        'jockey': row['jockey'],
                        'trainer': row['trainer'],
                        'body_weight': row['body_weight'],
                        'body_weight_change': row['body_weight_change'],
                    }
                )
            messages.success(request, 'Horses imported successfully')
            return redirect('import_horses')
    else:
        form = UploadFileForm()
    return render(request, 'race_app/import_horses.html', {'form': form})
