# TODO 1: Importieren Sie das Flask-Objekt aus dem Flask-Modul.
from flask import Flask
# TODO 2: Erstellen Sie eine Instanz der Flask-Anwendung.
#         Der erste Parameter ist der Name des Moduls oder Pakets der Anwendung.
#         Verwenden Sie '__name__' für diese einfache Anwendung.
app = Flask(__name__) # Ersetzen Sie None durch die Flask-Instanz

# TODO 3: Definieren Sie eine Route für die Startseite ('/').
#         Verwenden Sie den Decorator '@app.route('/')'.
#         Die Funktion, die direkt darunter definiert wird, wird ausgeführt, wenn diese URL aufgerufen wird.
#         Sie sollte eine einfache Begrüßungsnachricht zurückgeben, z.B. "Willkommen auf der Startseite!".
@app.route('/')
def index():
    return "Willkommen auf der Startseite!"
#     pass # Implementieren Sie hier die Rückgabe

# TODO 4: Definieren Sie eine weitere Route für '/hello'.
#         Verwenden Sie den Decorator '@app.route('/hello')'.
#         Die Funktion sollte "Hallo von Flask!" zurückgeben.
@app.route('/hello')
def hello():
    return "Hallo von Flask!"
#     pass # Implementieren Sie hier die Rückgabe

# Dies ist der Standardweg, um die Flask-Anwendung auszuführen.
# 'if __name__ == "__main__":' stellt sicher, dass der Server nur gestartet wird,
# wenn das Skript direkt ausgeführt wird.
if __name__ == "__main__":
    app.run(debug=True) # 'debug=True' ermöglicht den Debug-Modus, was nützlich für die Entwicklung ist.