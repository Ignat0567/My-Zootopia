import json
import os

# JSON read
with open("E:/Python/Lernen/Zootopia_Git/animals_data.json", "r", encoding="utf-8") as handle:
    animals_data = json.load(handle)

# HTML read
with open("Zootopia_Git/animals_template.html", "r", encoding="utf-8") as fileobj:
    html_temp = fileobj.read()

# String with animals-data
output = ''
for animal in animals_data:
    name = animal.get("name")
    characteristics = animal.get("characteristics", {})
    diet = characteristics.get("diet")
    animal_type = characteristics.get("type")
    locations = animal.get("locations", [])
    first_location = locations[0] if locations else None

    if name:
        output += f"Name: {name}\n"
    if diet:
        output += f"Diet: {diet}\n"
    if first_location:
        output += f"Location: {first_location}\n"
    if animal_type:
        output += f"Type: {animal_type}\n"
    output += "\n"

final_html = html_temp.replace("__REPLACE_ANIMALS_INFO__", output)

with open("Zootopia_Git/animals.html", "w", encoding="utf-8") as output_file:
    output_file.write(final_html)