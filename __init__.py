from flask import Flask, render_template
import xml.etree.ElementTree as ET
import urllib.request

app = Flask(__name__)

url = "https://data.tfl.gov.uk/tfl/syndication/feeds/stations-facilities.xml"

@app.route("/")
def get_data():
    with urllib.request.urlopen(url) as response:
        html = response.read()    
    stations = []
    data2 = html
    root = ET.fromstring(data2)

    for station in root.iter("station"):
        data = ""
        data += station.find("name").text#.decode("utf-8")
        facilities = station.find("facilities")
        data += "Has Toilets:"
        if len(facilities) == 0:
            data += "UNKNOWN"
        for facility in facilities:
            if facility.attrib["name"] == "Toilets":
                data += facility.text#.decode("utf-8")
        stations.append(data)
    return render_template("index.html", stations=stations)

#print(get_data())
#input()

app.run(debug=True)