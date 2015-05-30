import requests
import xml.etree.ElementTree as ET

url = "https://data.tfl.gov.uk/tfl/syndication/feeds/stations-facilities.xml"

r = requests.get(url)

data = r.content
root = ET.fromstring(data)

f = open("data3", "a")
for station in root.iter("station"):
    print(station.find("name").text)
    facilities = station.find("facilities")
    print("Has Toilets:")
    if len(facilities) == 0:
        print("UNKNOWN")
    for facility in facilities:
        if facility.attrib["name"] == "Toilets":
            print(facility.text)
