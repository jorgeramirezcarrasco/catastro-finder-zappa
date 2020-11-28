from flask import Flask, Response, request
import json
from catastro_finder import CatastroFinder
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

@app.route("/get_provinces",methods=['POST']) 
def get_provinces():
    provincias = CatastroFinder().get_provincias()
    return Response(json.dumps(provincias),  mimetype='application/json')

@app.route("/get_municipalities",methods=['POST']) 
def get_municipalities():
    data = request.json
    if not data or not "code_province" in data:
        return Response("missing input")
    else:
        municipios = CatastroFinder().get_municipios(data["code_province"])
        return Response(json.dumps(municipios),  mimetype='application/json')


@app.route("/get_streets",methods=['POST']) 
def get_streets():
    data = request.json
    if not data or not "code_province" in data or not "code_municipalities" in data or not "input_street" in data:
        return Response("missing input")
    else:
        via_results = CatastroFinder().get_vias(data["code_province"],data["code_municipalities"],data["input_street"])
        return Response(json.dumps(via_results),  mimetype='application/json')

@app.route("/search_property",methods=['POST']) 
def search_property():
    data = request.json
    if not data or not "selected_province" in data or not "selected_municipality" in data or not "street_result" in data or not "street_number" in data:
        return Response("missing input")
    else:
        inmueble_results = CatastroFinder().search_inmueble(data["street_result"],data["street_number"],data["selected_province"],data["selected_municipality"])
        return Response(json.dumps(inmueble_results),  mimetype='application/json')

if __name__ == "__main__":
    app.run()
    