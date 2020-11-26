from flask import Flask, Response, request
import json
from catastro_finder import CatastroFinder
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

@app.route("/get_provincias",methods=['POST']) 
def get_provincias():
    provincias = CatastroFinder().get_provincias()
    return Response(json.dumps(provincias),  mimetype='application/json')

@app.route("/get_municipios",methods=['POST']) 
def get_municipios():
    data = request.json
    if not data or not "code_provincia" in data:
        return Response("missing input")
    else:
        municipios = CatastroFinder().get_municipios(data["code_provincia"])
        return Response(json.dumps(municipios),  mimetype='application/json')


@app.route("/get_vias",methods=['POST']) 
def get_vias():
    data = request.json
    if not data or not "code_provincia" in data or not "code_municipio" in data or not "input_via" in data:
        return Response("missing input")
    else:
        via_results = CatastroFinder().get_vias(data["code_provincia"],data["code_municipio"],data["input_via"])
        return Response(json.dumps(via_results),  mimetype='application/json')

@app.route("/search_inmueble",methods=['POST']) 
def search_inmueble():
    data = request.json
    if not data or not "selected_provincia" in data or not "selected_municipio" in data or not "via_result" in data or not "via_numero" in data:
        return Response("missing input")
    else:
        inmueble_results = CatastroFinder().search_inmueble(data["via_result"],data["via_numero"],data["selected_provincia"],data["selected_municipio"])
        return Response(json.dumps(inmueble_results),  mimetype='application/json')

if __name__ == "__main__":
    app.run()
    