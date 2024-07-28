from django.urls import path
from .views import race_card, home, import_horses, import_races

urlpatterns = [
    path('', home, name='home'),  # ルートURLに対応するビュー
    path('race_card/', race_card, name='race_card'),
    path('import_horses/', import_horses, name='import_horses'),
    path('import_races/', import_races, name='import_races'),    
]
