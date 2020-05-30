# __ENG__
## GR-AntarcticIce
AntarcticIce is an animation showing changes of the Antarctic ice extent over a period of 500 days.
On the animation two changing objects can percived.
- Real ice range. (blue)
- Expected ice range generated as a mathematical model. (orange)


## Used technologies and modules:
- Python 3
- numpy
- matplotlib
- json


## Specification 
**NOTE:** Actual data covers a period of 9530 days, however data for mathematical
the model has been upset only for the last 500 days.

The project has been divided into two parts:
  - Data preparation
  - Visualization
  
  Data preparation -
  The script 'data / clear_data.py' retrieves data from a .txt file, converts it to a state acceptable by Python tools,
  cuts and assigns data to appropriate variables, and then, by converting to JSON, saves the output.
  
  Visualisation -
  The script 'animation.py' will use the matplotlib module. Uses FuncAnimation () functions to refresh the animation window view.
  Retrieves data from text files prepared by the 'clear_data.py' script discussed earlier.
  
 # __PL__
 ## GR-AntarcticIce
 ArcticIce jest animacją przedstawiającą zmiany zasięgu lodu na Antarktydzie przez okres 500 dni.
 Na animacji widoczne są dwa zmieniające się obiekty.
 - Rzeczywisty zasięg lodu. (niebieski)
 - Przewidywany zasięg lodu wygenerowany jako matematyczny model. (pomarańczowy)


## Użyte technologie i moduły
- Python 3
- numpy
- matplotlib
- json

## Specyfikacja
**UWAGA:** Rzeczywiste dane obejmują okres 9530 dni, jednak dane dla matematycznego 
modelu zostały wygenerwowane tylko dla ostatnich 500 dni.

Projekt został podzielony na dwie częsci:
  - Przygotowanie danych
  - Wizalizacja
  
  Przygotowanie danych -
  Skrypt 'data/clear_data.py' pobiera dane z pliku .txt, konwertuje do stau akceptowalnego przez narzędzia Pythona,
  wycina i przydziela dane do odpowiednich zmiennych, po czym przez konwersje do formatu JSON, zapisuje output.
  
  Wizualizacja -
  Skrypt 'animation.py' korzyta z modułu matplotlib. Wykorzystuje funkcje FuncAnimation() do odświerznia widoku okna animacji.
  Pobiera dane z plików tekstowych przygotowanych przez wcześniej omówiony skrypy 'clear_data.py'.
  
  
