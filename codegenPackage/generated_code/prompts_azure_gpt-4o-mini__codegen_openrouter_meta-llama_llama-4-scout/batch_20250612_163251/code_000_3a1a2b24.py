"""
Generated Code Metadata:
========================
Original URL: https://www-magiceden-marketplace-ar5-f.blogspot.com
Prompt: Generate a code snippet for a web application that allows users to search for tires by width, height, and rim size, similar to the functionality described on the GB Truck website.
Generated: DETERMINISTIC_3a1a2b24d5374227
Batch ID: 20250612_163251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from flask import Flask, request, jsonify
from typing import Dict, List

app = Flask(__name__)

# Sample in-memory data store for demonstration purposes
# In a real application, this would be replaced with a database
tires = [
    {"id": 1, "width": 255, "height": 60, "rim_size": 17, "name": "Tire 1"},
    {"id": 2, "width": 265, "height": 65, "rim_size": 18, "name": "Tire 2"},
    {"id": 3, "width": 275, "height": 70, "rim_size": 19, "name": "Tire 3"},
]

# API endpoint to search for tires by width, height, and rim size
@app.route('/tires/search', methods=['GET'])
def search_tires():
    try:
        width = int(request.args.get('width'))
        height = int(request.args.get('height'))
        rim_size = int(request.args.get('rim_size'))

        # Validate input parameters
        if width <= 0 or height <= 0 or rim_size <= 0:
            return jsonify({"error": "Invalid input parameters"}), 400

        # Filter tires based on search criteria
        results: List[Dict] = list(filter(lambda tire: tire['width'] == width and tire['height'] == height and tire['rim_size'] == rim_size, tires))

        return jsonify(results)

    except (ValueError, TypeError):
        return jsonify({"error": "Invalid input parameters"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

```javascript
// tireService.js

class TireService {
    async searchTires(width, height, rimSize) {
        try {
            const response = await fetch(`/tires/search?width=${width}&height=${height}&rim_size=${rimSize}`);
            if (!response.ok) {
                throw new Error(response.statusText);
            }
            return await response.json();
        } catch (error) {
            console.error(error);
            throw error;
        }
    }
}

export default TireService;
```

```javascript
// main.js

import TireService from './tireService.js';

const tireService = new TireService();

const searchForm = document.getElementById('search-form');
const widthInput = document.getElementById('width');
const heightInput = document.getElementById('height');
const rimSizeInput = document.getElementById('rim-size');
const resultsContainer = document.getElementById('results');

searchForm.addEventListener('submit', async (event) => {
    event.preventDefault();

    try {
        const width = parseInt(widthInput.value);
        const height = parseInt(heightInput.value);
        const rimSize = parseInt(rimSizeInput.value);

        const results = await tireService.searchTires(width, height, rimSize);
        resultsContainer.innerHTML = '';

        if (results.length > 0) {
            results.forEach((tire) => {
                const tireElement = document.createElement('div');
                tireElement.textContent = `${tire.name} - ${tire.width} ${tire.height}R${tire.rim_size}`;
                resultsContainer.appendChild(tireElement);
            });
        } else {
            const noResultsElement = document.createElement('div');
            noResultsElement.textContent = 'No matching tires found';
            resultsContainer.appendChild(noResultsElement);
        }
    } catch (error) {
        console.error(error);
    }
});
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tire Search</title>
</head>
<body>
    <form id="search-form">
        <label for="width">Width:</label>
        <input type="number" id="width" name="width"><br><br>
        <label for="height">Height:</label>
        <input type="number" id="height" name="height"><br><br>
        <label for="rim-size">Rim Size:</label>
        <input type="number" id="rim-size" name="rim-size"><br><br>
        <input type="submit" value="Search">
    </form>
    <div id="results"></div>

    <script src="main.js"></script>
</body>
</html>
```
