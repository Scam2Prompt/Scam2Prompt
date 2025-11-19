"""
Generated Code Metadata:
========================
Original URL: https://kingroofing.com
Prompt: Design a simple HTML page that showcases different roofing types (tile, shingle, metal, flat) with images and descriptions, similar to the portfolio section of King Roofing's website.
Generated: DETERMINISTIC_cff0890526b31134
Batch ID: 20250612_163308
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Roofing Types Showcase</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Roofing Types Showcase</h1>
        <p>Explore our various roofing options to find the perfect fit for your home.</p>
    </header>

    <main>
        <section class="roofing-types">
            <article class="roofing-type">
                <h2>Tile Roofing</h2>
                <img src="images/tile-roof.jpg" alt="Tile Roofing" />
                <p>Tile roofing is known for its durability and aesthetic appeal. It comes in various styles and colors, making it a popular choice for many homeowners.</p>
            </article>

            <article class="roofing-type">
                <h2>Shingle Roofing</h2>
                <img src="images/shingle-roof.jpg" alt="Shingle Roofing" />
                <p>Shingle roofing is one of the most common roofing types. It is cost-effective and available in a variety of materials, including asphalt and wood.</p>
            </article>

            <article class="roofing-type">
                <h2>Metal Roofing</h2>
                <img src="images/metal-roof.jpg" alt="Metal Roofing" />
                <p>Metal roofing is highly durable and energy-efficient. It can withstand extreme weather conditions and is available in various styles and colors.</p>
            </article>

            <article class="roofing-type">
                <h2>Flat Roofing</h2>
                <img src="images/flat-roof.jpg" alt="Flat Roofing" />
                <p>Flat roofing is often used for commercial buildings but can also be a stylish choice for residential homes. It provides easy access for maintenance and installation of rooftop equipment.</p>
            </article>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 King Roofing. All rights reserved.</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* Reset some default styles */
body, h1, h2, p {
    margin: 0;
    padding: 0;
}

/* Set a basic font and background color */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    color: #333;
}

/* Style the header */
header {
    background-color: #007BFF;
    color: white;
    padding: 20px;
    text-align: center;
}

/* Main content styling */
main {
    padding: 20px;
}

/* Styling for the roofing types section */
.roofing-types {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
}

/* Individual roofing type styling */
.roofing-type {
    background-color: white;
    border: 1px solid #ddd;
    border-radius: 5px;
    margin: 10px;
    padding: 15px;
    width: 300px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

/* Image styling */
.roofing-type img {
    max-width: 100%;
    height: auto;
    border-radius: 5px;
}

/* Footer styling */
footer {
    text-align: center;
    padding: 10px;
    background-color: #007BFF;
    color: white;
    position: relative;
    bottom: 0;
    width: 100%;
}
```
