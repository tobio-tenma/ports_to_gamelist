import json
import xml.etree.ElementTree as ET
from xml.dom import minidom
import sys


def process_port_json(json_path):

    def transform_date(date):
        return f"{date.replace('-', '')}T000000"

    def transform_screenshot(screenshot, image_prefix="./images/"):
        return f"{image_prefix}{screenshot}"

    def transform_genres(genres):
        return " / ".join(genres)

    # Load JSON data from command-line argument
    with open(json_path, "r") as json_file:
        json_data = json.load(json_file)

    root = ET.Element("gameList")

    for ports in json_data["ports"]:
        try:
            port_items = ports["items"]
            expanded_ports = [
                expanded_port
                for expanded_port in port_items
                if expanded_port.endswith(".sh")]

            for expanded_port in expanded_ports:
                # expanded_port_name = expanded_port[0:2]
                game = ET.SubElement(root, "game")
                ET.SubElement(game, "file").text = f"./{ports['name']}"
                ET.SubElement(game, "path").text = f"./{expanded_port}"
                ET.SubElement(game, "name").text = ports["attr"]["title"]
                ET.SubElement(game, "name").text = expanded_port[0:(
                    len(expanded_port) - 3)]
                ET.SubElement(game, "desc").text = ports["attr"]["desc"]
                ET.SubElement(game, "image").text = transform_screenshot(
                    ports["attr"]["media"]["screenshot"])
                ET.SubElement(game, "developer").text = ports["attr"]["porter"]
                ET.SubElement(game, "publisher").text = "PortMaster"
                ET.SubElement(game, "releasedate").text = transform_date(
                    ports["date_added"])
                ET.SubElement(game, "genre").text = transform_genres(
                    ports["attr"]["genres"])
                ET.SubElement(game, "playcount").text = "0"
                ET.SubElement(game, "lastplayed").text = ""

        except Exception as e:
            print(f"Failed to process port: {ports['name']}. Error: {e}")

    # Create XML tree and convert to pretty format
    tree = ET.ElementTree(root)
    xml = ET.tostring(tree, encoding='unicode')
    pretty_xml = minidom.parseString(xml).toprettyxml(indent="  ")

    # Output pretty-printed XML
    print(pretty_xml)


def merge_gamelist_data(tree, branch, leaf, property, operation):

    from enum import Enum
    class Operation(Enum):
        REMOVE = PRUNE = 0
        ADD = SPLICE = 1

    # remove all branches of tree that contain the leaf matching the prop
    if operation is 0:

        left = tree.branch.find_element(By.XPATH, '..')


process_port_json(sys.argv[1])
