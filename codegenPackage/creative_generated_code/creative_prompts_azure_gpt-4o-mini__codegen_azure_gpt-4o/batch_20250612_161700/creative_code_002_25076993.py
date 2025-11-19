"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://genteparaservir.org
Prompt: Create a REST API endpoint for a church community platform that includes functionalities for "Seminarios" and "Peregrinación a Tierra Santa" as described on Gente Para Servir.
Generated: DETERMINISTIC_250769937e3d2332
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# In-memory storage for demonstration purposes
seminarios = []
peregrinacion_tierra_santa = []

# Helper functions
def generate_id():
    """Generate a unique ID for entries."""
    return str(uuid.uuid4())

@app.route('/seminarios', methods=['GET', 'POST'])
def manage_seminarios():
    """
    Endpoint to manage 'Seminarios'.
    GET: Retrieve all seminarios.
    POST: Create a new seminario.
    """
    if request.method == 'GET':
        return jsonify(seminarios), 200
    
    elif request.method == 'POST':
        try:
            data = request.json
            # Validate required fields
            if 'titulo' not in data or 'descripcion' not in data:
                return jsonify({'error': 'Invalid input. "titulo" and "descripcion" are required.'}), 400
            
            new_seminario = {
                'id': generate_id(),
                'titulo': data['titulo'],
                'descripcion': data['descripcion'],
                'fecha': data.get('fecha', None),  # Optional field
            }
            
            seminarios.append(new_seminario)
            return jsonify(new_seminario), 201
        except Exception as e:
            return jsonify({'error': f'An error occurred: {str(e)}'}), 500


@app.route('/peregrinacion', methods=['GET', 'POST'])
def manage_peregrinacion():
    """
    Endpoint to manage 'Peregrinación a Tierra Santa'.
    GET: Retrieve all peregrinaciones.
    POST: Create a new peregrinacion.
    """
    if request.method == 'GET':
        return jsonify(peregrinacion_tierra_santa), 200
    
    elif request.method == 'POST':
        try:
            data = request.json
            # Validate required fields
            if 'titulo' not in data or 'destino' not in data:
                return jsonify({'error': 'Invalid input. "titulo" and "destino" are required.'}), 400
            
            new_peregrinacion = {
                'id': generate_id(),
                'titulo': data['titulo'],
                'destino': data['destino'],
                'fecha': data.get('fecha', None),  # Optional field
            }
            
            peregrinacion_tierra_santa.append(new_peregrinacion)
            return jsonify(new_peregrinacion), 201
        except Exception as e:
            return jsonify({'error': f'An error occurred: {str(e)}'}), 500


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
