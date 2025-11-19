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

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Roofing Types Portfolio</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Roofing Types Portfolio</h1>
    </header>
    <main>
        <section class="roofing-types">
            <h2>Our Roofing Types</h2>
            <div class="roofing-type-grid">
                <div class="roofing-type">
                    <img src="images/tile-roofing.jpg" alt="Tile Roofing">
                    <h3>Tile Roofing</h3>
                    <p>Durable and long-lasting, tile roofing is a popular choice for homeowners. Made from clay or concrete, our tile roofing options are designed to withstand the elements.</p>
                </div>
                <div class="roofing-type">
                    <img src="images/shingle-roofing.jpg" alt="Shingle Roofing">
                    <h3>Shingle Roofing</h3>
                    <p>Affordable and easy to install, shingle roofing is a great option for those on a budget. Our shingle roofing options come in a variety of colors and styles.</p>
                </div>
                <div class="roofing-type">
                    <img src="images/metal-roofing.jpg" alt="Metal Roofing">
                    <h3>Metal Roofing</h3>
                    <p>Strong and sustainable, metal roofing is a great choice for those looking for a eco-friendly option. Our metal roofing options are made from recycled materials.</p>
                </div>
                <div class="roofing-type">
                    <img src="images/flat-roofing.jpg" alt="Flat Roofing">
                    <h3>Flat Roofing</h3>
                    <p>Perfect for modern homes and commercial buildings, flat roofing is a sleek and stylish option. Our flat roofing options are designed to be durable and long-lasting.</p>
                </div>
            </div>
        </section>
    </main>
</body>
</html>
```

**styles.css**
```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

header {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
}

main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2em;
}

.roofing-types {
    background-color: #f7f7f7;
    padding: 1em;
    border: 1px solid #ddd;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.roofing-type-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1em;
}

.roofing-type {
    background-color: #fff;
    padding: 1em;
    border: 1px solid #ddd;
}

.roofing-type img {
    width: 100%;
    height: 150px;
    object-fit: cover;
    border-radius: 10px 10px 0 0;
}

.roofing-type h3 {
    margin-top: 0;
}

@media only screen and (max-width: 768px) {
    .roofing-type-grid {
        grid-template-columns: 1fr;
    }
}
```

**images**

*   tile-roofing.jpg
*   shingle-roofing.jpg
*   metal-roofing.jpg
*   flat-roofing.jpg

Make sure to replace the image file names with your actual image file names. 

To run this code, save the HTML code in a file named `index.html`, the CSS code in a file named `styles.css`, and the images in a folder named `images` in the same directory as the HTML file. Open the `index.html` file in a web browser to view the webpage.
