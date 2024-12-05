from flask import Flask, render_template, request

import models.animal
from models.animal import Animal
from models.perro import Perro
from models.gato import Gato
from models.boa import Boa
from models.huron import Huron

app = Flask(__name__, template_folder="views")


@app.route("/")
def result():
    return render_template('index.html')


@app.route("/procesar", methods=['POST'])
def procesar():
    nombre_animal = request.form.get('nombre_animal')
    if nombre_animal == 'perro':
        return f'{nombre_animal}, tiene el sonido {models.perro.Perro.hacer_sonido(Animal)} '
    if nombre_animal == 'gato':
        return f'{nombre_animal}, tiene el sonido {models.gato.Gato.hacer_sonido(Animal)} '
    if nombre_animal == 'boa':
        return f'{nombre_animal}, tiene el sonido {models.boa.Boa.hacer_sonido(Animal)} '
    if nombre_animal == 'huron':
        return f'{nombre_animal}, tiene el sonido {models.huron.Huron.hacer_sonido(Animal)} '


if __name__ == '__main__':
    app.run(debug=True, port=8080, use_reloader=False)
