"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://itaca.in
Prompt: Develop a JavaScript application that allows users to select tile sizes and preview how ITACA Ceramic's Belle Forme tiles would look in a virtual room setting.
Generated: DETERMINISTIC_ce48cb5c8df285f7
Batch ID: 20250612_151109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tile Previewer</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }
        #tile-selector {
            margin-bottom: 20px;
        }
        #preview {
            width: 100%;
            height: 400px;
            border: 1px solid #ccc;
            background-size: cover;
            display: flex;
            align-items: center;
            justify-content: center;
            position: relative;
            background-image: url('room-background.jpg'); /* Replace with actual room image */
        }
        .tile {
            position: absolute;
            border: 2px solid #fff;
            box-shadow: 0 0 5px rgba(0, 0, 0, 0.5);
            pointer-events: none; /* Disable interaction with tiles */
        }
    </style>
</head>
<body>

    <h1>ITACA Ceramic's Belle Forme Tile Previewer</h1>
    <div id="tile-selector">
        <label for="tile-size">Select Tile Size:</label>
        <select id="tile-size">
            <option value="50">50x50 cm</option>
            <option value="60">60x60 cm</option>
            <option value="80">80x80 cm</option>
            <option value="100">100x100 cm</option>
        </select>
        <button id="add-tile">Add Tile</button>
    </div>
    
    <div id="preview"></div>

    <script>
        // Get references to DOM elements
        const tileSelector = document.getElementById('tile-size');
        const addTileButton = document.getElementById('add-tile');
        const previewArea = document.getElementById('preview');

        // Function to add a tile to the preview area
        const addTile = () => {
            try {
                const tileSize = parseInt(tileSelector.value) * 2; // Convert size to pixels
                const tile = document.createElement('div');
                tile.classList.add('tile');
                tile.style.width = `${tileSize}px`;
                tile.style.height = `${tileSize}px`;
                tile.style.left = `${Math.random() * (previewArea.clientWidth - tileSize)}px`;
                tile.style.top = `${Math.random() * (previewArea.clientHeight - tileSize)}px`;
                tile.style.backgroundImage = "url('tile-image.jpg')"; // Replace with actual tile image
                tile.style.backgroundSize = 'cover';
                
                previewArea.appendChild(tile);
            } catch (error) {
                console.error('Error adding tile:', error);
                alert('An error occurred while adding the tile. Please try again.');
            }
        };

        // Event listener for the button click
        addTileButton.addEventListener('click', addTile);
    </script>

</body>
</html>
```
