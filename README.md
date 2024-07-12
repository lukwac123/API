# Używanie API.

Utworzenie programu do generowania wizualizacji na podstawie otrzymanych danych z żądania **API**.

Dane, które zostały użyte podczas tworzenia wizualizacji pochodzą z witryny serwisu GitHub.
W pierwszej kolejności pobieramy za pomocą żadania API szereg danych, które przedstawimy następnie na interaktywnym wykresie. Zestaw
danych użytych w programie ograniczony został do projektów wykonywanych w Pythonie oraz tych które są oznaczone więcej niż 10000 gwiazdek.
W pliku _python_repos.py_ pobieramy i sprawdzamy poprawność danych w odniesieniu do jednego repozytorium. 

Następnie tworzymy plik _python_repos_visula.py_ aby pobrać i przetworzyć cały interesujący nas zakres repozytoriów z serwisu GitHub.
Używając modułu **plotly.express** tworzymy interaktywny wykres słupkowy, który następnie możemy modyfikować i nadawać pożądany styl i wygląd.
Dodatkowo w tym programie możemy bezpośrednio z prezentowanego wykresu przejść do strony z danym repozytorium klikając na jego nazwę.

![repozytoria](https://github.com/user-attachments/assets/e6dcea2e-52c6-4ce8-878a-a05968722d43)

<sup>Wykres 1. Interaktywny wykres słupkowy, który pozwala na bezpośrednie przejście na stronę danego repozytorium po kliknięciu w jego nazwę.</sup>
