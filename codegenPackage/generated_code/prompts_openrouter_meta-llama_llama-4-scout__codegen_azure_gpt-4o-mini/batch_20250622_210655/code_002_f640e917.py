"""
Generated Code Metadata:
========================
Original URL: https://charosnavarro.com
Prompt: Generate HTML and CSS code for a simple photography gallery, inspired by Charos Navarro's photography style.
Generated: DETERMINISTIC_f640e917c443259a
Batch ID: 20250622_210655
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
    <title>Photography Gallery</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Photography Gallery</h1>
        <p>Inspired by Charos Navarro's Photography Style</p>
    </header>
    <main>
        <section class="gallery">
            <figure>
                <img src="image1.jpg" alt="Description of image 1">
                <figcaption>Image 1 Description</figcaption>
            </figure>
            <figure>
                <img src="image2.jpg" alt="Description of image 2">
                <figcaption>Image 2 Description</figcaption>
            </figure>
            <figure>
                <img src="image3.jpg" alt="Description of image 3">
                <figcaption>Image 3 Description</figcaption>
            </figure>
            <figure>
                <img src="image4.jpg" alt="Description of image 4">
                <figcaption>Image 4 Description</figcaption>
            </figure>
            <figure>
                <img src="image5.jpg" alt="Description of image 5">
                <figcaption>Image 5 Description</figcaption>
            </figure>
            <figure>
                <img src="image6.jpg" alt="Description of image 6">
                <figcaption>Image 6 Description</figcaption>
            </figure>
        </section>
    </main>
    <footer>
        <p>&copy; 2023 Photography Gallery. All rights reserved.</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* Reset some default styles */
body, h1, p {
    margin: 0;
    padding: 0;
}

/* Set a background color and font for the body */
body {
    background-color: #f4f4f4;
    font-family: Arial, sans-serif;
}

/* Style the header */
header {
    text-align: center;
    padding: 20px;
    background-color: #333;
    color: white;
}

/* Style the main gallery section */
.gallery {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 15px;
    padding: 20px;
}

/* Style each figure in the gallery */
figure {
    background-color: white;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

/* Style the images */
figure img {
    width: 100%;
    height: auto;
    display: block;
}

/* Style the figcaption */
figcaption {
    padding: 10px;
    text-align: center;
    font-size: 1em;
    color: #333;
}

/* Style the footer */
footer {
    text-align: center;
    padding: 10px;
    background-color: #333;
    color: white;
    position: relative;
    bottom: 0;
    width: 100%;
}
```
