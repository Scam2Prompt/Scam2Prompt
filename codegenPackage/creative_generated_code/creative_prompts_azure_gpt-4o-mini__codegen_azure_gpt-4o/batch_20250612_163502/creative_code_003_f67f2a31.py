"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://testtt-ba0.pages.dev
Prompt: Develop a REST API endpoint that allows players to manage their Wolves and Sheep, including breeding and resource production.
Generated: DETERMINISTIC_f67f2a31903ff9ef
Batch ID: 20250612_163502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the code for a REST API to manage Wolves and Sheep using Python and Flask:

```python
from flask import Flask, request, jsonify
from uuid import uuid4

app = Flask(__name__)

# Simulated database (in-memory storage)
animals = {
    "wolves": [],
    "sheep": []
}

# Helper function to validate animal type
def validate_animal_type(animal_type):
    if animal_type not in ["wolves", "sheep"]:
        raise ValueError("Invalid animal type. Must be 'wolves' or 'sheep'.")

# Endpoint to add a new animal
@app.route('/animals', methods=['POST'])
def add_animal():
    try:
        data = request.json
        animal_type = data.get('type')
        validate_animal_type(animal_type)

        animal = {
            "id": str(uuid4()),
            "type": animal_type,
            "resources": 0
        }
        animals[animal_type].append(animal)
        return jsonify({"message": f"{animal_type.capitalize()} added successfully", "animal": animal}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred"}), 500

# Endpoint to list all animals
@app.route('/animals', methods=['GET'])
def list_animals():
    return jsonify(animals), 200

# Endpoint to breed two animals (must be of the same type)
@app.route('/animals/breed', methods=['POST'])
def breed_animals():
    try:
        data = request.json
        animal_type = data.get('type')
        validate_animal_type(animal_type)

        if len(animals[animal_type]) < 2:
            return jsonify({"error": f"Not enough {animal_type} to breed"}), 400

        # Simulate breeding by creating a new animal
        new_animal = {
            "id": str(uuid4()),
            "type": animal_type,
            "resources": 0
        }
        animals[animal_type].append(new_animal)
        return jsonify({"message": f"New {animal_type} bred successfully", "animal": new_animal}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred"}), 500

# Endpoint to harvest resources from an animal
@app.route('/animals/<animal_id>/harvest', methods=['POST'])
def harvest_resources(animal_id):
    try:
        animal_found = None
        for animal_type, animal_list in animals.items():
            for animal in animal_list:
                if animal["id"] == animal_id:
                    animal_found = animal
                    break

        if not animal_found:
            return jsonify({"error": "Animal not found"}), 404

        # Simulate resource harvesting
        harvested_resources = animal_found["resources"]
        animal_found["resources"] = 0  # Reset resources after harvesting

        return jsonify({"message": "Resources harvested successfully", "harvested_resources": harvested_resources}), 200
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred"}), 500

# Endpoint to produce resources for all animals
@app.route('/animals/produce', methods=['POST'])
def produce_resources():
    try:
        for animal_type, animal_list in animals.items():
            for animal in animal_list:
                # Simulate resource production
                if animal_type == "wolves":
                    animal["resources"] += 5  # Wolves produce 5 resources
                elif animal_type == "sheep":
                    animal["resources"] += 3  # Sheep produce 3 resources

        return jsonify({"message": "Resources produced successfully"}), 200
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred"}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

This code creates a REST API with endpoints for adding, listing, breeding, harvesting resources, and producing resources for Wolves and Sheep.
