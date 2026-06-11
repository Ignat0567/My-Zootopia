import json
import os

# JSON read
with open(
    "E:/Python/Lernen/Zootopia_Git/animals_data.json", "r", encoding="utf-8"
) as handle:
    animals_data = json.load(handle)

# HTML read
with open("Zootopia_Git/animals_template.html", "r", encoding="utf-8") as fileobj:
    html_temp = fileobj.read()

# String with animals-data
output = ""

for animal in animals_data:
    name = animal.get("name")
    characteristics = animal.get("characteristics", {})
    diet = characteristics.get("diet")
    animal_type = characteristics.get("type")
    locations = animal.get("locations", [])
    first_location = locations[0] if locations else None

    output += "<li class='cards__item'></br>"

    if name:
        output += f"    <div class='card__title'>{name}</div>"
    output += " <p class='card__text'>"
    if diet:
        output += f"    <strong>Diet:</strong> {diet}<br/>"
    if first_location:
        output += f"    <strong>Location:</strong> {first_location}<br/>"
    if animal_type:
        output += f"    <strong>Type:</strong> {animal_type}<br/>"
    output += "  </p></li>\n"


final_html = html_temp.replace("__REPLACE_ANIMALS_INFO__", output)

with open("Zootopia_Git/animals.html", "w", encoding="utf-8") as output_file:
    output_file.write(final_html)

print(output)
