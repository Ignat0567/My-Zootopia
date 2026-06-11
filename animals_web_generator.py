import json


# JSON read
def load_data(file_path):
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


# HTML read
def load_template(file_path):
    with open(file_path, "r", encoding="utf-8") as fileobj:
        return fileobj.read()


# HTML cards
def serialize_animal(animal):
    name = animal.get("name")
    characteristics = animal.get("characteristics", {})
    diet = characteristics.get("diet")
    animal_type = characteristics.get("type")
    locations = animal.get("locations", [])
    first_location = locations[0] if locations else None

    output = '    <li class="cards__item">\n'

    # Title
    if name:
        output += f'      <div class="card__title">{name}</div>\n'

    # Text-block
    output += '      <div class="card__text">\n'
    output += "        <ul>\n"
    if diet:
        output += f"          <li><strong>Diet:</strong> {diet}</li>\n"
    if first_location:
        output += f"          <li><strong>Location:</strong> {first_location}</li>\n"
    if animal_type:
        output += f"          <li><strong>Type:</strong> {animal_type}</li>\n"
    output += "        </ul>\n"
    output += "      </div>\n"
    output += "    </li>\n"

    return output


def write_html(file_path, html_content):
    with open(file_path, "w", encoding="utf-8") as output_file:
        output_file.write(html_content)


def main():
    json_path = "My-Zootopia/animals_data.json"
    template_path = "My-Zootopia/animals_template.html"
    output_path = "My-Zootopia/animals.html"

    animals_data = load_data(json_path)
    html_template = load_template(template_path)

    cards_html = ""
    for animal in animals_data:
        cards_html += serialize_animal(animal)

    final_html = html_template.replace("__REPLACE_ANIMALS_INFO__", cards_html)

    write_html(output_path, final_html)


if __name__ == "__main__":
    main()
