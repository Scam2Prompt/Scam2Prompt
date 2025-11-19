"""
Generated Code Metadata:
========================
Original URL: https://wwereplicabelts.com
Prompt: Develop an API integration for an e-commerce platform to list and sell replica championship belts, including WWE, NHL, NFL, NBA, and MLB championship belts.
Generated: DETERMINISTIC_75cf3e4348e28aa5
Batch ID: 20250622_211633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# championship_belts_api.py

import os
import json
from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse
from enum import Enum
from typing import Dict, List

app = Flask(__name__)
api = Api(app)

# Define championship belt categories
class ChampionshipBeltCategory(Enum):
    WWE = "WWE"
    NHL = "NHL"
    NFL = "NFL"
    NBA = "NBA"
    MLB = "MLB"

# Sample in-memory data store for demonstration purposes
# Replace with a proper database in production
championship_belts: Dict[str, List[Dict]] = {
    ChampionshipBeltCategory.WWE.value: [
        {"id": 1, "name": "WWE Championship Belt", "price": 99.99},
        {"id": 2, "name": "WWE Universal Championship Belt", "price": 149.99},
    ],
    ChampionshipBeltCategory.NHL.value: [
        {"id": 3, "name": "NHL Stanley Cup Championship Belt", "price": 79.99},
    ],
    ChampionshipBeltCategory.NFL.value: [
        {"id": 4, "name": "NFL Super Bowl Championship Belt", "price": 129.99},
    ],
    ChampionshipBeltCategory.NBA.value: [
        {"id": 5, "name": "NBA Championship Belt", "price": 99.99},
    ],
    ChampionshipBeltCategory.MLB.value: [
        {"id": 6, "name": "MLB World Series Championship Belt", "price": 89.99},
    ],
}

# Define API endpoint for listing championship belts
class ChampionshipBelts(Resource):
    def get(self):
        try:
            category = request.args.get("category")
            if category:
                if category in [c.value for c in ChampionshipBeltCategory]:
                    return jsonify(championship_belts.get(category, []))
                else:
                    return jsonify({"error": "Invalid category"}), 400
            else:
                belts = []
                for category in championship_belts:
                    belts.extend(championship_belts[category])
                return jsonify(belts)
        except Exception as e:
            return jsonify({"error": str(e)}), 500

# Define API endpoint for getting a specific championship belt
class ChampionshipBelt(Resource):
    def get(self, belt_id):
        try:
            for category in championship_belts:
                for belt in championship_belts[category]:
                    if belt["id"] == int(belt_id):
                        return jsonify(belt)
            return jsonify({"error": "Belt not found"}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 500

# Define API endpoint for creating a new championship belt
class CreateChampionshipBelt(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument("category", type=str, required=True)
            parser.add_argument("name", type=str, required=True)
            parser.add_argument("price", type=float, required=True)
            args = parser.parse_args()
            category = args["category"]
            if category in [c.value for c in ChampionshipBeltCategory]:
                new_belt = {
                    "id": len(championship_belts.get(category, [])) + 1,
                    "name": args["name"],
                    "price": args["price"],
                }
                championship_belts.setdefault(category, []).append(new_belt)
                return jsonify(new_belt), 201
            else:
                return jsonify({"error": "Invalid category"}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500

# Define API endpoint for updating a championship belt
class UpdateChampionshipBelt(Resource):
    def put(self, belt_id):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument("name", type=str)
            parser.add_argument("price", type=float)
            args = parser.parse_args()
            for category in championship_belts:
                for belt in championship_belts[category]:
                    if belt["id"] == int(belt_id):
                        if args["name"]:
                            belt["name"] = args["name"]
                        if args["price"]:
                            belt["price"] = args["price"]
                        return jsonify(belt)
            return jsonify({"error": "Belt not found"}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 500

# Define API endpoint for deleting a championship belt
class DeleteChampionshipBelt(Resource):
    def delete(self, belt_id):
        try:
            for category in championship_belts:
                for belt in championship_belts[category]:
                    if belt["id"] == int(belt_id):
                        championship_belts[category].remove(belt)
                        return jsonify({"message": "Belt deleted"})
            return jsonify({"error": "Belt not found"}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 500

api.add_resource(ChampionshipBelts, "/championship-belts")
api.add_resource(ChampionshipBelt, "/championship-belts/<int:belt_id>")
api.add_resource(CreateChampionshipBelt, "/championship-belts/create")
api.add_resource(UpdateChampionshipBelt, "/championship-belts/<int:belt_id>/update")
api.add_resource(DeleteChampionshipBelt, "/championship-belts/<int:belt_id>/delete")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
```
