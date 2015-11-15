import json
import csv

with open("data/entrances.csv", "r") as input_file:
    reader = csv.DictReader(input_file)
    geo_objects = [obj for obj in reader]
    
with open("geo.json", "w") as output_file:
    output_file.write(json.dumps(geo_objects))
    output_file.flush()
