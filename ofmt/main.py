import sys
import xml.etree.ElementTree as ET

def reformat(xmlFilename):
    print(f"Reformatting: {xmlFilename}")
    tree = ET.parse(xmlFilename)

    root = tree.getroot()
    # Perform sorting on root here

    # tree.write(xmlFilename)
    tree.write(f"{xmlFilename}.out.xml")

def main():
    if len(sys.argv) < 2:
        print("Syntax: ofmt [xmlFilename] ([xmlFilename]...)")
        return

    for i, arg in enumerate(sys.argv):
        if i < 1:
            continue

        reformat(arg)

if __name__ == "__main__":
    main()
