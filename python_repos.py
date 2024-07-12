import requests

# Wykonanie wywołania API i zachowanie otrzymanej odpowiedzi.
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Kod stanu: {r.status_code}")

# Konwersja obiektu odpowiedzi na słownik.
response_dict = r.json()
print(f"Całkowita liczba repozytoriów: {response_dict['total_count']}")
print(f"Pełny zbiór wynikowy?: {not response_dict['incomplete_results']}")

# Przetworzenie informacji o repozytoriach.
repo_dicts = response_dict['items']
print(f"Liczba zwróconych repozytoriów: {len(repo_dicts)}")

# Przeanalizowanie wybranych danych o każdym repozytorium.
print("\nWybrane informacje o każdym repozytorium:")
for repo_dict in repo_dicts:  
    print(f"\nNazwa: {repo_dict['name']}")
    print(f"Właściciel: {repo_dict['owner']['login']}")
    print(f"Gwiazdki: {repo_dict['stargazers_count']}")
    print(f"Repozytorium: {repo_dict['html_url']}")
    print(f"Utworzone: {repo_dict['created_at']}")
    print(f"Uaktualnione: {repo_dict['updated_at']}")
    print(f"Opis: {repo_dict['description']}")