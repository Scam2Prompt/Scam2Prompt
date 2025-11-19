"""
Generated Code Metadata:
========================
Original URL: https://aibanshee.com
Prompt: Generate HTML and CSS code for a "Centered Masonry Gallery" with floating info panels, referencing the design concepts from the IMST Telehealth webpage.
Generated: DETERMINISTIC_c29b3850076da353
Batch ID: 20250612_150013
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
    <title>Centered Masonry Gallery</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="gallery">
        <div class="gallery-item">
            <img src="image1.jpg" alt="Image 1">
            <div class="info-panel">Info about Image 1</div>
        </div>
        <div class="gallery-item">
            <img src="image2.jpg" alt="Image 2">
            <div class="info-panel">Info about Image 2</div>
        </div>
        <div class="gallery-item">
            <img src="image3.jpg" alt="Image 3">
            <div class="info-panel">Info about Image 3</div>
        </div>
        <div class="gallery-item">
            <img src="image4.jpg" alt="Image 4">
            <div class="info-panel">Info about Image 4</div>
        </div>
        <div class="gallery-item">
            <img src="image5.jpg" alt="Image 5">
            <div class="info-panel">Info about Image 5</div>
        </div>
    </div>
</body>
</html>
```

```css
/* styles.css */

/* Reset some default styles */
body {
    margin: 0;
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
}

/* Center the gallery and apply masonry layout */
.gallery {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

/* Style for each gallery item */
.gallery-item {
    position: relative;
    margin: 10px;
    overflow: hidden;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

/* Style for images */
.gallery-item img {
    display: block;
    width: 100%;
    height: auto;
    border-radius: 8px;
}

/* Style for the info panel */
.info-panel {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: rgba(0, 0, 0, 0.7);
    color: white;
    padding: 10px;
    opacity: 0;
    transition: opacity 0.3s ease;
}

/* Show the info panel on hover */
.gallery-item:hover .info-panel {
    opacity: 1;
}
```

### Notes:
- Replace `image1.jpg`, `image2.jpg`, etc., with the actual paths to your images.
- Ensure that the images are of appropriate size for a masonry layout.
- The CSS uses flexbox for layout and includes a hover effect for the info panels.
