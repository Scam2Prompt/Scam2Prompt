"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://villaandreas.gr
Prompt: Suggest a RESTful API design for a villa rental service that includes endpoints for searching villas by location and amenities, based on the offerings of Villa Andreas in Kefalonia.
Generated: DETERMINISTIC_1b06668e2f5e940c
Batch ID: 20250612_161435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# villa_rental_service.py

from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data for villas (In production, this data should be stored in a database)
villas = [
    {
        "id": 1,
        "name": "Villa Andreas",
        "location": "Kefalonia",
        "amenities": ["pool", "wifi", "parking"],
        "price_per_night": 200
    },
    {
        "id": 2,
        "name": "Villa Sunset",
        "location": "Kefalonia",
        "amenities": ["pool", "wifi"],
        "price_per_night": 180
    },
    {
        "id": 3,
        "name": "Villa Paradise",
        "location": "Zakynthos",
        "amenities": ["wifi", "parking"],
        "price_per_night": 150
    }
]

@app.route('/api/villas', methods=['GET'])
def search_villas():
    """
    Endpoint to search for villas by location and amenities.
    Query Parameters:
      - location: string (required)
      - amenities: comma-separated string (optional)
    Returns:
      JSON object containing the list of villas matching the search criteria.
    """
    try:
        location = request.args.get('location')  # Required parameter
        amenities = request.args.get('amenities')  # Optional parameter

        if not location:
            return jsonify({"error": "Location parameter is required"}), 400

        # Filter villas based on location
        filtered_villas = [villa for villa in villas if villa["location"].lower() == location.lower()]

        # Further filter based on amenities if provided
        if amenities:
            amenities_list = [amenity.strip().lower() for amenity in amenities.split(',')]
            filtered_villas = [
                villa for villa in filtered_villas
                if all(amenity in villa["amenities"] for amenity in amenities_list)
            ]

        return jsonify(filtered_villas), 200

    except Exception as e:
        # Catch any unexpected errors and return a meaningful message
        return jsonify({"error": "An error occurred while processing your request", "details": str(e)}), 500


@app.route('/api/villas/<int:villa_id>', methods=['GET'])
def get_villa_by_id(villa_id):
    """
    Endpoint to retrieve details of a specific villa by its ID.
    Path Parameter:
      - villa_id: integer (required)
    Returns:
      JSON object containing details of the villa, or a 404 error if the villa is not found.
    """
    try:
        villa = next((villa for villa in villas if villa["id"] == villa_id), None)

        if not villa:
            return jsonify({"error": f"Villa with ID {villa_id} not found"}), 404

        return jsonify(villa), 200

    except Exception as e:
        # Catch any unexpected errors and return a meaningful message
        return jsonify({"error": "An error occurred while processing your request", "details": str(e)}), 500


# Entry point for the application
if __name__ == '__main__':
    app.run(debug=True)
```
