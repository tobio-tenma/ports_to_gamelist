# ports_to_gamelist.py

This is very much a **work in progress**

A simple utility that converts PortMaster ports.json into gamelist.xml format for EmulationStation. It's been tested on Ark OS and JELOS so far.

## Usage

The script is called with the ports.json file provided as the one and only argument.

**Example Usage**:

```python ports_to_gamelist.py ports.json```

## Troubleshooting

You can use the [JSON validation schema](https://github.com/kloptops/harbourmaster/blob/main/data/ports.schema.json) to to ensure that your input json is formatted correctly.

## Work in progress

**TODO***:

* Implement the splice / prune logic to clean up the gamelist.xml tree after adding / removing ports from your collection
* More testing of the various screen sizes, OSes, devices, etc.
* Implement the additional metadata for media associated with the port
* Customize gamelist generation further, based on the target environment

### Attribution

Thanks to [Christian Haitian](https://github.com/christianhaitian/) for the creation of PortMaster and his continuing service to retro handlheld community.

Thanks to the [PortMaster](https://github.com/PortsMaster) Crew for their guidance, patience, and wisdom.

Thanks to [kloptops](https://github.com/kloptops) and **Bamboozler** for their extensions to the ports metadata which is why this can now exist.
