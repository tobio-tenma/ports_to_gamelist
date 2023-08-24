import json
import xml.etree.ElementTree as ET
from xml.dom import minidom
import sys

# Function to transform date format
def transform_date(date):
    return f"{date.replace('-', '')}T000000"

# Function to transform screenshot to image
def transform_screenshot(screenshot, image_prefix="./images/"):
    return f"{image_prefix}{screenshot}"

# Function to transform genres
def transform_genres(genres):
    return " / ".join(genres)

# Load JSON data from command-line argument
json_path = sys.argv[1]
with open(json_path, "r") as json_file:
    json_data = json.load(json_file)

# Create XML root element
root = ET.Element("gamelist")

# Loop through each ports in JSON data
for ports in json_data["ports"]:
    try:
        port_items = ports["items"]
        expanded_ports = [
            item
            for item in port_items
            if item.endswith(".sh")]
        
        for expanded_port in expanded_ports:

            game = ET.SubElement(root, "game")        
            ET.SubElement(game, "file").text = f"./{ports['name']}"
            ET.SubElement(game, "path").text = f"./{expanded_port}"
            ET.SubElement(game, "name").text = ports["attr"]["title"]
            ET.SubElement(game, "desc").text = ports["attr"]["desc"]
            ET.SubElement(game, "image").text = transform_screenshot(ports["attr"]["media"]["screenshot"])
            ET.SubElement(game, "developer").text = ports["attr"]["porter"]
            ET.SubElement(game, "publisher").text = "PortMaster"
            ET.SubElement(game, "releasedate").text = transform_date(ports["date_added"])
            ET.SubElement(game, "genre").text = transform_genres(ports["attr"]["genres"])
            ET.SubElement(game, "playcount").text = "0"
            ET.SubElement(game, "lastpllayed").text = " "

    except Exception as e:
        print(f"Failed to process ports: {ports['name']}. Error: {e}")

# Create XML tree and convert to a pretty-printed string
tree = ET.ElementTree(root)
xml_str = ET.tostring(root, encoding='unicode')
pretty_xml_str = minidom.parseString(xml_str).toprettyxml(indent="  ")

# Output pretty-printed XML to terminal
print(pretty_xml_str)
