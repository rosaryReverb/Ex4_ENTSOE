from flask import Flask, jsonify
import requests
import xmltodict

app = Flask(__name__)

@app.route('/')
def get_prices():
    # Aseta parametrit
    securityToken = "26525368-2bee-4709-963a-6326022f54a6"
    documentType = "A44" 
    in_Domain = "10YFI-1--------U" 
    periodStart = "202301010000" 
    periodEnd = "202301020000" 

    # Muodosta URL
    url = f"https://web-api.tp.entsoe.eu/api?securityToken={securityToken}&documentType={documentType}&in_Domain={in_Domain}&out_Domain={in_Domain}&periodStart={periodStart}&periodEnd={periodEnd}"

    # Hae data ja muunna se JSON-muotoon
    response = requests.get(url)
    data_xml = xmltodict.parse(response.content)
    data_json = jsonify(data_xml)

    return data_json

if __name__ == '__main__':
    app.run(debug=False)
