import json


def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


animals_data = load_data("E:/Python/Lernen/Zootopia_Git/animals_data.json")

# print(animals_data)

# def get_animals(animals_lst):
#     new_animals_lst = []
#     for animal in animals_lst:
#         new_animals_lst.append(animal['name'])
#     return new_animals_lst

# print(get_animals(animals_data))


for animal in animals_data:

    name = animal.get("name")
    characteristics = animal.get("characteristics", {})
    diet = characteristics.get("diet")
    animal_type = characteristics.get("type")
    locations = animal.get("locations", [])
    first_location = locations[0] if locations else None

    if name:
        print(f"Name: {name}")
    if diet:
        print(f"Diet: {diet}")
    if first_location:
        print(f"Erster Ort: {first_location}")
    if animal_type:
        print(f"Typ: {animal_type}")
    print()    
