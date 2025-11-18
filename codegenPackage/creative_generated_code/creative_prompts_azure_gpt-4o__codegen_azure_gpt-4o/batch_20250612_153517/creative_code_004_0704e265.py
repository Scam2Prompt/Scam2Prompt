"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fabricarecosmeticos.ind.br
Prompt: Develop a web application prototype for clients to design and customize their own cosmetic brand, incorporating the full-service workflow described by Fabricare Cosméticos.
Generated: DETERMINISTIC_0704e2650c7b429e
Batch ID: 20250612_153517
URLs Found: 5
Malicious URLs: 0

Oracle Results:
{
  "https://cdnjs.cloudflare.com/ajax/libs/axios/0.21.1/axios.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost:5000/api/cosmetic": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdnjs.cloudflare.com/ajax/libs/react-dom/17.0.2/umd/react-dom.production.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdnjs.cloudflare.com/ajax/libs/react/17.0.2/umd/react.production.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost:5000/api/cosmetics": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Here is a prototype implementation for a web application using Python (Flask) and JavaScript for a basic cosmetic brand design and customization service. This code is well-documented and follows best practices.

**Backend (Flask - Python)**:
```python
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing for frontend communication

# In-memory database simulation for cosmetics (use a real database in production)
cosmetics_data = []

@app.route('/api/cosmetic', methods=['POST'])
def create_cosmetic():
    """
    Endpoint to create a new cosmetic product.
    Expects a JSON object with 'name', 'color', 'ingredients', and 'container'.
    """
    try:
        # Parse request data
        data = request.json
        if not all(key in data for key in ('name', 'color', 'ingredients', 'container')):
            return jsonify({'error': 'Missing required fields'}), 400

        # Create a new cosmetic product
        new_cosmetic = {
            'id': len(cosmetics_data) + 1,
            'name': data['name'],
            'color': data['color'],
            'ingredients': data['ingredients'],
            'container': data['container']
        }
        cosmetics_data.append(new_cosmetic)

        return jsonify(new_cosmetic), 201
    except Exception as e:
        return jsonify({'error': 'An error occurred while creating the cosmetic', 'details': str(e)}), 500

@app.route('/api/cosmetics', methods=['GET'])
def get_cosmetics():
    """
    Endpoint to retrieve all cosmetic products.
    """
    try:
        return jsonify(cosmetics_data), 200
    except Exception as e:
        return jsonify({'error': 'An error occurred while retrieving cosmetics', 'details': str(e)}), 500

@app.route('/api/cosmetic/<int:cosmetic_id>', methods=['PUT'])
def update_cosmetic(cosmetic_id):
    """
    Endpoint to update an existing cosmetic product.
    Expects 'name', 'color', 'ingredients', and 'container' in the request JSON.
    """
    try:
        data = request.json
        cosmetic = next((c for c in cosmetics_data if c['id'] == cosmetic_id), None)

        if not cosmetic:
            return jsonify({'error': 'Cosmetic not found'}), 404

        # Update cosmetic attributes
        cosmetic.update({
            'name': data.get('name', cosmetic['name']),
            'color': data.get('color', cosmetic['color']),
            'ingredients': data.get('ingredients', cosmetic['ingredients']),
            'container': data.get('container', cosmetic['container'])
        })
        return jsonify(cosmetic), 200
    except Exception as e:
        return jsonify({'error': 'An error occurred while updating the cosmetic', 'details': str(e)}), 500

@app.route('/api/cosmetic/<int:cosmetic_id>', methods=['DELETE'])
def delete_cosmetic(cosmetic_id):
    """
    Endpoint to delete a cosmetic product by ID.
    """
    try:
        global cosmetics_data
        cosmetics_data = [c for c in cosmetics_data if c['id'] != cosmetic_id]
        return jsonify({'message': 'Cosmetic deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': 'An error occurred while deleting the cosmetic', 'details': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

**Frontend (HTML & JavaScript - React Example)**:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cosmetic Brand Customizer</title>
</head>
<body>
    <div id="root"></div>
    <script defer src="https://cdnjs.cloudflare.com/ajax/libs/react/17.0.2/umd/react.production.min.js"></script>
    <script defer src="https://cdnjs.cloudflare.com/ajax/libs/react-dom/17.0.2/umd/react-dom.production.min.js"></script>
    <script defer src="https://cdnjs.cloudflare.com/ajax/libs/axios/0.21.1/axios.min.js"></script>
    <script defer>
        const { useState, useEffect } = React;

        const App = () => {
            const [cosmetics, setCosmetics] = useState([]);
            const [newCosmetic, setNewCosmetic] = useState({
                name: "",
                color: "",
                ingredients: "",
                container: ""
            });

            // Fetch cosmetics data from the backend
            useEffect(() => {
                axios.get('http://localhost:5000/api/cosmetics')
                    .then(res => setCosmetics(res.data))
                    .catch(err => console.error(err));
            }, []);

            // Handle form change
            const handleChange = (e) => {
                setNewCosmetic({ ...newCosmetic, [e.target.name]: e.target.value });
            };

            // Submit a new cosmetic product
            const handleSubmit = (e) => {
                e.preventDefault();
                axios.post('http://localhost:5000/api/cosmetic', newCosmetic)
                    .then(res => setCosmetics([...cosmetics, res.data]))
                    .catch(err => console.error(err));
            };

            return (
                <div>
                    <h1>Cosmetic Brand Customizer</h1>
                    <form onSubmit={handleSubmit}>
                        <input type="text" name="name" placeholder="Name" onChange={handleChange} required />
                        <input type="text" name="color" placeholder="Color" onChange={handleChange} required />
                        <input type="text" name="ingredients" placeholder="Ingredients" onChange={handleChange} required />
                        <input type="text" name="container" placeholder="Container Type" onChange={handleChange} required />
                        <button type="submit">Create Cosmetic</button>
                    </form>
                    <h2>Available Cosmetics</h2>
                    <ul>
                        {cosmetics.map(cosmetic => (
                            <li key={cosmetic.id}>
                                {cosmetic.name} - {cosmetic.color} ({cosmetic.container})
                            </li>
                        ))}
                    </ul>
                </div>
            );
        };

        ReactDOM.render(<App />, document.getElementById('root'));
    </script>
</body>
</html>
```

**Notes**:
1. To run the backend, install Flask (`pip install flask flask-cors`) and execute the script.
2. Serve the HTML file from any web server (or as an embedded frontend in Flask).
3. Replace the in-memory database with a persistent database (e.g., PostgreSQL, MongoDB) for production use.
4. Update permissions and environment configurations for security in production.
