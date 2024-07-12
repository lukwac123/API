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
repo_links, stars, hover_texts = [], [], []
for repo_dict in repo_dicts:
    # Zmiana nazwy repozytorium na łącze.
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    stars.append(repo_dict['stargazers_count'])

    # Przygotowanie podpowiedzi.
    owner = repo_dict['owner'] ['login']
    description = repo_dict['description']
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)

# Utworzenie wizualizacji.
title = "Oznaczone największą liczbą gwiazdek projekty Pythona w serwisie GitHub"
labels = {'x': 'Repozytorium', 'y': 'Gwiazdki'}
fig = px.bar(x=repo_links, y=stars, title=title, labels=labels, hover_name=hover_texts)

fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)
fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)

fig.show()