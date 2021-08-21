from flask import Flask
from flask import request
from flask import jsonify
from urllib.request import urlopen
import requests
import json


app = Flask(__name__)

allUser = [{"id":0, "nombre" : "Claudio"},{"id":1, "nombre" : "Andres"}]

@app.route('/app/v1/users/<id>' , methods=["GET"])
def users_action(id):
    return jsonify(allUser[int(id)])  

@app.route('/app/v1/users' , methods=["POST", "GET"])
def users_action2():
    if(request.method == "GET"):
        return jsonify(allUser)
    else:
        user = {"id" : request.form["id"], "nombre" : request.form["nombre"]}
        allUser.append(user)
        return jsonify(user)

@app.route('/google')
def go():
    url = "https://test.salesforce.com/services/oauth2/token"

    payload={'client_id': '3MVG98EE59.VIHmyRTyhJwa5zZMA3YQMcFgbWQh7S1SCj8WMgcft5vLzrJ4BWgZ7uwcever.YsMbv_yGDAOPR',
    'grant_type': 'password',
    'client_secret': '5BEF3988C06F962E4DF1CF696F5E1C3F445DC0D8346FEDA50D9E044AD59E7F3F',
    'username': 'consultor@cuatroi.com.InsCallV2',
    'password': 'Prtk1945L5D3JnFqeR8vMglolHZzvo1D'}
    files=[

    ]
    headers = {
        'Cookie': 'BrowserId=W7VZ_QRIEeuNf4VeKfQx0A; CookieConsentPolicy=0:0'
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    print(response.text)
    return response.text
    



app.run(debug=True)