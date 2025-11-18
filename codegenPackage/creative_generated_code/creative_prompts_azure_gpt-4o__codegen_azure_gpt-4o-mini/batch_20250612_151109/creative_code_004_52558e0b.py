"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://itaca.in
Prompt: Write code in HTML and CSS to create a visual representation of wall tiles in sizes like 300x300 MM and 300x600 MM, as described on the ITACA Ceramic website.
Generated: DETERMINISTIC_52558e0b3f556c4d
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
    <title>Wall Tiles Visual Representation</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Wall Tiles Representation</h1>
        <div class="tile-container">
            <div class="tile" style="width: 300px; height: 300px;">300x300 MM</div>
            <div class="tile" style="width: 300px; height: 600px;">300x600 MM</div>
            <div class="tile" style="width: 300px; height: 300px;">300x300 MM</div>
            <div class="tile" style="width: 300px; height: 600px;">300x600 MM</div>
            <div class="tile" style="width: 300px; height: 300px;">300x300 MM</div>
            <div class="tile" style="width: 300px; height: 600px;">300x600 MM</div>
        </div>
    </div>
</body>
</html>
```

```css
/* styles.css */

/* Reset some default styles */
body, h1 {
    margin: 0;
    padding: 0;
}

/* Set a background color for the body */
body {
    background-color: #f0f0f0;
    font-family: Arial, sans-serif;
}

/* Centering the container */
.container {
    max-width: 800px;
    margin: 20px auto;
    text-align: center;
}

/* Styling the tile container */
.tile-container {
    display: flex; /* Using Flexbox for layout */
    flex-wrap: wrap; /* Allowing tiles to wrap to the next line */
    justify-content: center; /* Centering tiles horizontally */
}

/* Styling each tile */
.tile {
    background-color: #ffffff; /* White background for tiles */
    border: 2px solid #ccc; /* Light grey border */
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1); /* Subtle shadow for depth */
    margin: 10px; /* Margin around tiles */
    display: flex; /* Flexbox for center text */
    align-items: center; /* Center text vertically */
    justify-content: center; /* Center text horizontally */
    font-size: 16px; /* Font size for tile text */
    font-weight: bold; /* Make the text bold */
    transition: transform 0.2s; /* Animation for hover effect */
}

/* Adding hover effect on tiles */
.tile:hover {
    transform: scale(1.05); /* Slightly enlarge on hover */
    border-color: #888; /* Darker border color on hover */
}
```
