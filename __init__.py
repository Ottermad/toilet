import xml.etree.ElementTree as ET
import urllib.request

url = "https://data.tfl.gov.uk/tfl/syndication/feeds/stations-facilities.xml"

def get_data():
    with urllib.request.urlopen(url) as response:
        html = response.read()    
    data = ""
    data2 = html
    root = ET.fromstring(data2)

    for station in root.iter("station"):
        data += station.find("name").text#.decode("utf-8")
        facilities = station.find("facilities")
        data += "Has Toilets:"
        if len(facilities) == 0:
            data += "UNKNOWN"
        for facility in facilities:
            if facility.attrib["name"] == "Toilets":
                data += facility.text#.decode("utf-8")
        data += "\n"
    return data

print(get_data())
