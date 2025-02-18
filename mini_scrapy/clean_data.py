import os
import re
import json


with open("./ data.json", "r") as f:
    data = json.load(f)

def get_first(lst):
    return lst[0].strip() if lst else None

def extract_number(value):
    match = re.search(r"[\d.]+", value)
    return float(match.group()) if match else 0.0

def extract_int(value):
    match = re.search(r"\d+", value)
    return int(match.group()) if match else 0

def get_available_colors(available_colours):
    available = []
    for entry in available_colours:
        color_match = re.search(r"Color (.+)", entry)
        color = color_match.group(1).strip() if color_match else "Unknown"

        if "unavailable" not in entry.lower():
            available.append(color)

    return available

transformed_data = []
for item in data:
    new_item = {
        "name": get_first(item.get("name")),
        "price": extract_number(get_first(item.get("price"))),
        "colour": get_first(item.get("colour")),
        "availableColours": get_available_colors(item.get("availableColours")),
        "reviews_count": extract_int(get_first(item.get("reviews_count"))),
        "reviews_score": extract_number(get_first(item.get("reviews_score"))),
    }
    transformed_data.append(new_item)

with open("filtered_data.json", "w") as f:
    json.dump(transformed_data, f, indent=2)

print(json.dumps(transformed_data, indent=2))

os.remove("./ data.json")
print("Processing completed. <data.json> has been deleted.")
