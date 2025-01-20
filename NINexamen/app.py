from flask import Flask, render_template, request

app = Flask(__name__)
users = {
    "juan": "admin",
    "pepe": "user"
}
# Ruta principal
@app.route('/')
def index():
    return render_template('index.html')

# Ejercicio 1
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    resultado = None
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad = int(request.form['cantidad'])

        precio_unitario = 9000
        total_sin_descuento = cantidad * precio_unitario
        descuento = 0

        # Aplicar descuento según la edad
        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25

        total_con_descuento = total_sin_descuento * (1 - descuento)

        resultado = {
            "nombre": nombre,
            "total_sin_descuento": total_sin_descuento,
            "total_con_descuento": total_con_descuento
        }

    return render_template("ejercicio1.html", resultado=resultado)

# Ejercicio 2
from flask import Flask, render_template, request

app = Flask(__name__)

# Diccionario de usuarios para el ejercicio 2
users = {
    "juan": "admin",
    "pepe": "user"
}

@app.route('/')
def index():
    return render_template('index.html')  # Página principal

# Ejercicio 1: Cálculo con descuento por edad
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    resultado = None
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad = int(request.form['cantidad'])

        # Precio por producto
        precio_unitario = 9000
        total_sin_descuento = cantidad * precio_unitario
        descuento = 0

        # Aplicar descuento según la edad
        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25  # 25% de descuento si tiene más de 30 años

        total_con_descuento = total_sin_descuento * (1 - descuento)

        resultado = {
            "nombre": nombre,
            "total_sin_descuento": total_sin_descuento,
            "total_con_descuento": total_con_descuento
        }

    return render_template("ejercicio1.html", resultado=resultado)

# Ejercicio 2: Login de usuario
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    resultado = ""
    if request.method == 'POST':
        nombre = request.form['nombre']
        contrasena = request.form['contrasena']

        # Verificar las credenciales
        if nombre in users and users[nombre] == contrasena:
            if nombre == "juan":
                resultado = f"Bienvenido administrador {nombre}"
            elif nombre == "pepe":
                resultado = f"Bienvenido usuario {nombre}"
        else:
            resultado = "Usuario o contraseña incorrectos"

    return render_template('ejercicio2.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)


if __name__ == '__main__':
    app.run(debug=True)

