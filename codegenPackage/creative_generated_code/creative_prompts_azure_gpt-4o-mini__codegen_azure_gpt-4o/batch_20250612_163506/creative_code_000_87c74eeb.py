"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://itaca.in
Prompt: Generate a code snippet for a web application that allows users to select and customize ceramic tiles based on size and mood, similar to the "Tile That Change Your Mood" feature on Itaca's website.
Generated: DETERMINISTIC_87c74eeb037a0c9b
Batch ID: 20250612_163506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Predefined tile options
TILE_SIZES = ["Small", "Medium", "Large"]
MOODS = ["Relaxing", "Energetic", "Neutral"]

@app.route('/')
def homepage():
    """
    Render the homepage where users can select tile size and mood.
    """
    return render_template('index.html', tile_sizes=TILE_SIZES, moods=MOODS)

@app.route('/customize', methods=['POST'])
def customize_tile():
    """
    Handle customization request for ceramic tiles based on size and mood.
    """
    try:
        # Parse user input
        data = request.json
        tile_size = data.get('tile_size')
        mood = data.get('mood')

        # Validate inputs
        if tile_size not in TILE_SIZES:
            return jsonify({"error": "Invalid tile size selected!"}), 400
        if mood not in MOODS:
            return jsonify({"error": "Invalid mood selected!"}), 400

        # Generate customization response
        response = {
            "message": "Tile customization successful!",
            "tile_size": tile_size,
            "mood": mood,
            "recommendation": f"Selected {tile_size} tiles for a {mood} ambiance."
        }
        return jsonify(response), 200

    except Exception as e:
        # Catch unexpected errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=True)
```

### Frontend (HTML) - `templates/index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ceramic Tile Customizer</title>
    <script>
        async function submitCustomization() {
            const tileSize = document.getElementById('tile-size').value;
            const mood = document.getElementById('mood').value;

            const response = await fetch('/customize', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ tile_size: tileSize, mood: mood })
            });

            const result = await response.json();
            if (response.ok) {
                alert(result.message + "\n" + result.recommendation);
            } else {
                alert(result.error);
            }
        }
    </script>
</head>
<body>
    <h1>Customize Your Ceramic Tiles</h1>
    <form onsubmit="event.preventDefault(); submitCustomization();">
        <label for="tile-size">Select Tile Size:</label>
        <select id="tile-size" name="tile_size">
            {% for size in tile_sizes %}
            <option value="{{ size }}">{{ size }}</option>
            {% endfor %}
        </select>
        <br><br>
        <label for="mood">Select Mood:</label>
        <select id="mood" name="mood">
            {% for mood in moods %}
            <option value="{{ mood }}">{{ mood }}</option>
            {% endfor %}
        </select>
        <br><br>
        <button type="submit">Submit</button>
    </form>
</body>
</html>
```
