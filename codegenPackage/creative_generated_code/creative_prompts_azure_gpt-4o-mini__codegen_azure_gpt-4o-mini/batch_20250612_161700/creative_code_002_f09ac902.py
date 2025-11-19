"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://assistenzatecnicapalermo.it
Prompt: Create an API integration example for a security system that monitors and manages surveillance cameras, reflecting the security services provided by Assistenza Tecnica Palermo.
Generated: DETERMINISTIC_f09ac902e5d7fd29
Batch ID: 20250612_161700
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.assistenzatecnicapalermo.com/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

# Configuration for the Assistenza Tecnica Palermo API
API_BASE_URL = 'https://api.assistenzatecnicapalermo.com/v1'
API_KEY = 'your_api_key_here'  # Replace with your actual API key


def get_headers():
    """
    Generate the headers for API requests.
    :return: Dictionary of headers including the API key for authentication.
    """
    return {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }


@app.route('/cameras', methods=['GET'])
def list_cameras():
    """
    Retrieve a list of surveillance cameras.
    :return: JSON response containing camera data or error message.
    """
    try:
        response = requests.get(f'{API_BASE_URL}/cameras', headers=get_headers())
        response.raise_for_status()
        return jsonify(response.json()), 200
    except requests.exceptions.HTTPError as http_err:
        return jsonify({'error': str(http_err)}), response.status_code
    except Exception as e:
        return jsonify({'error': 'An error occurred while retrieving cameras.', 'details': str(e)}), 500


@app.route('/cameras/<int:camera_id>', methods=['GET'])
def get_camera(camera_id):
    """
    Retrieve details of a specific surveillance camera by its ID.
    :param camera_id: The ID of the camera to retrieve.
    :return: JSON response containing camera details or error message.
    """
    try:
        response = requests.get(f'{API_BASE_URL}/cameras/{camera_id}', headers=get_headers())
        response.raise_for_status()
        return jsonify(response.json()), 200
    except requests.exceptions.HTTPError as http_err:
        return jsonify({'error': str(http_err)}), response.status_code
    except Exception as e:
        return jsonify({'error': 'An error occurred while retrieving camera details.', 'details': str(e)}), 500


@app.route('/cameras', methods=['POST'])
def create_camera():
    """
    Add a new surveillance camera to the system.
    :return: JSON response containing the created camera data or error message.
    """
    try:
        camera_data = request.json
        response = requests.post(f'{API_BASE_URL}/cameras', headers=get_headers(), json=camera_data)
        response.raise_for_status()
        return jsonify(response.json()), 201
    except requests.exceptions.HTTPError as http_err:
        return jsonify({'error': str(http_err)}), response.status_code
    except Exception as e:
        return jsonify({'error': 'An error occurred while creating the camera.', 'details': str(e)}), 500


@app.route('/cameras/<int:camera_id>', methods=['PUT'])
def update_camera(camera_id):
    """
    Update the details of an existing surveillance camera.
    :param camera_id: The ID of the camera to update.
    :return: JSON response containing the updated camera data or error message.
    """
    try:
        camera_data = request.json
        response = requests.put(f'{API_BASE_URL}/cameras/{camera_id}', headers=get_headers(), json=camera_data)
        response.raise_for_status()
        return jsonify(response.json()), 200
    except requests.exceptions.HTTPError as http_err:
        return jsonify({'error': str(http_err)}), response.status_code
    except Exception as e:
        return jsonify({'error': 'An error occurred while updating the camera.', 'details': str(e)}), 500


@app.route('/cameras/<int:camera_id>', methods=['DELETE'])
def delete_camera(camera_id):
    """
    Delete a surveillance camera from the system.
    :param camera_id: The ID of the camera to delete.
    :return: JSON response indicating success or error message.
    """
    try:
        response = requests.delete(f'{API_BASE_URL}/cameras/{camera_id}', headers=get_headers())
        response.raise_for_status()
        return jsonify({'message': 'Camera deleted successfully.'}), 204
    except requests.exceptions.HTTPError as http_err:
        return jsonify({'error': str(http_err)}), response.status_code
    except Exception as e:
        return jsonify({'error': 'An error occurred while deleting the camera.', 'details': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)

```
Make sure to replace `'your_api_key_here'` with your actual API key for the Assistenza Tecnica Palermo service.
