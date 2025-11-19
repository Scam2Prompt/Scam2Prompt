"""
Generated Code Metadata:
========================
Original URL: https://itaca.in
Prompt: Write code in HTML and CSS to create a visual representation of wall tiles in sizes like 300x300 MM and 300x600 MM, as described on the ITACA Ceramic website.
Generated: DETERMINISTIC_52558e0b3f556c4d
Batch ID: 20250612_151109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wall Tiles Visual Representation</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="tile-container">
        <div class="tile" data-size="300x300">
            <div class="tile-visual" style="width: 300px; height: 300px;"></div>
            <p class="tile-size">300x300 MM</p>
        </div>
        <div class="tile" data-size="300x600">
            <div class="tile-visual" style="width: 300px; height: 600px;"></div>
            <p class="tile-size">300x600 MM</p>
        </div>
        <!-- Add more tiles as needed -->
    </div>
</body>
</html>
```

**styles.css**
```css
/* Global Styles */
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f9f9f9;
}

/* Tile Container Styles */
.tile-container {
    max-width: 1200px;
    margin: 40px auto;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 20px;
}

/* Tile Styles */
.tile {
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 10px;
    padding: 10px;
    width: calc(33.33% - 20px);
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.tile-visual {
    background-color: #ccc;
    border-radius: 10px 10px 0 0;
}

.tile-size {
    font-size: 18px;
    font-weight: bold;
    margin-top: 10px;
}

/* Responsive Design */
@media only screen and (max-width: 768px) {
    .tile {
        width: calc(50% - 20px);
    }
}

@media only screen and (max-width: 480px) {
    .tile {
        width: 100%;
    }
}
```
