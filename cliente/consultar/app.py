from flask import Flask

app = Flask(__name__)

@app.route("/consultar/<int:idCliente>")
def consultar(idCliente):
    if(idCliente == "0")
        return "Todos los clientes"
    else
        return "Cliente correspondiente id ingresado"

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)