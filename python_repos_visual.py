import requests
import plotly.express as px

# Wykonanie wywołania API i zachowanie otrzymanej odpowiedzi.
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Kod stanu: {r.status_code}")

# Przetworzenie otrzymanych wyników.
response_dict = r.json()
print(f"Pełny zbiór wynikowy?: {not response_dict['incomplete_results']}")

# Przetworzenie informacji o repozytoriach.
repo_dicts = response_dict['items']
repo_names, stars = [], []
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# Utworzenie wizualizacji.
fig = px.bar(x=repo_names, y=stars)
fig.show()