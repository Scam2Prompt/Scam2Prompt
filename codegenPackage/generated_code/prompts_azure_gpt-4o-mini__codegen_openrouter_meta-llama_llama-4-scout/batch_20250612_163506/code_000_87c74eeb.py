"""
Generated Code Metadata:
========================
Original URL: https://itaca.in
Prompt: Generate a code snippet for a web application that allows users to select and customize ceramic tiles based on size and mood, similar to the "Tile That Change Your Mood" feature on Itaca's website.
Generated: DETERMINISTIC_87c74eeb037a0c9b
Batch ID: 20250612_163506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Tile Customizer Code Snippet**
```python
# tile_customizer.py

from flask import Flask, render_template, request, jsonify
from enum import Enum

app = Flask(__name__)

# Define tile sizes and moods
class TileSize(Enum):
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"

class TileMood(Enum):
    CALMING = "calming"
    ENERGETIC = "energetic"
    FOCUSSED = "focused"

# Sample tile data
tiles = [
    {"id": 1, "name": "Tile 1", "size": TileSize.SMALL, "mood": TileMood.CALMING, "image_url": "tile1_small_calming.jpg"},
    {"id": 2, "name": "Tile 2", "size": TileSize.MEDIUM, "mood": TileMood.ENERGETIC, "image_url": "tile2_medium_energetic.jpg"},
    {"id": 3, "name": "Tile 3", "size": TileSize.LARGE, "mood": TileMood.FOCUSSED, "image_url": "tile3_large_focused.jpg"},
]

# Route to get all tiles
@app.route("/tiles", methods=["GET"])
def get_tiles():
    try:
        return jsonify([{"id": tile["id"], "name": tile["name"], "size": tile["size"].value, "mood": tile["mood"].value, "image_url": tile["image_url"]} for tile in tiles])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get tile by id
@app.route("/tiles/<int:tile_id>", methods=["GET"])
def get_tile(tile_id):
    try:
        tile = next((tile for tile in tiles if tile["id"] == tile_id), None)
        if tile is None:
            return jsonify({"error": "Tile not found"}), 404
        return jsonify({"id": tile["id"], "name": tile["name"], "size": tile["size"].value, "mood": tile["mood"].value, "image_url": tile["image_url"]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to customize tile
@app.route("/tiles/customize", methods=["POST"])
def customize_tile():
    try:
        data = request.get_json()
        if "tile_id" not in data or "size" not in data or "mood" not in data:
            return jsonify({"error": "Invalid request data"}), 400
        tile_id = data["tile_id"]
        size = data["size"]
        mood = data["mood"]
        tile = next((tile for tile in tiles if tile["id"] == tile_id), None)
        if tile is None:
            return jsonify({"error": "Tile not found"}), 404
        tile["size"] = TileSize(size)
        tile["mood"] = TileMood(mood)
        return jsonify({"id": tile["id"], "name": tile["name"], "size": tile["size"].value, "mood": tile["mood"].value, "image_url": tile["image_url"]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tile Customizer</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        .tile {
            width: 200px;
            height: 200px;
            border: 1px solid #ccc;
            margin: 10px;
            padding: 10px;
            display: inline-block;
        }
    </style>
</head>
<body>
    <h1>Tile Customizer</h1>
    <div id="tiles"></div>
    <form id="customize-form">
        <label for="tile-id">Tile ID:</label>
        <input type="number" id="tile-id" name="tile_id"><br><br>
        <label for="size">Size:</label>
        <select id="size" name="size">
            <option value="small">Small</option>
            <option value="medium">Medium</option>
            <option value="large">Large</option>
        </select><br><br>
        <label for="mood">Mood:</label>
        <select id="mood" name="mood">
            <option value="calming">Calming</option>
            <option value="energetic">Energetic</option>
            <option value="focused">Focused</option>
        </select><br><br>
        <button id="customize-btn">Customize Tile</button>
    </form>

    <script>
        fetch("/tiles")
            .then(response => response.json())
            .then(tiles => {
                const tilesHtml = tiles.map(tile => {
                    return `
                        <div class="tile">
                            <h2>${tile.name}</h2>
                            <p>Size: ${tile.size}</p>
                            <p>Mood: ${tile.mood}</p>
                            <img src="${tile.image_url}" alt="${tile.name}">
                        </div>
                    `;
                }).join("");
                document.getElementById("tiles").innerHTML = tilesHtml;
            })
            .catch(error => console.error(error));

        document.getElementById("customize-form").addEventListener("submit", (e) => {
            e.preventDefault();
            const formData = new FormData(e.target);
            const data = {
                tile_id: formData.get("tile_id"),
                size: formData.get("size"),
                mood: formData.get("mood")
            };
            fetch("/tiles/customize", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(data)
            })
            .then(response => response.json())
            .then(tile => {
                console.log(tile);
            })
            .catch(error => console.error(error));
        });
    </script>
</body>
</html>
```
