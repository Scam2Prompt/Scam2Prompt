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

**index.html**
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
    <div class="gallery-container">
        <div class="gallery">
            <div class="gallery-item">
                <img src="image1.jpg" alt="Image 1">
                <div class="info-panel">
                    <h2>Image 1</h2>
                    <p>This is a description of image 1.</p>
                </div>
            </div>
            <div class="gallery-item">
                <img src="image2.jpg" alt="Image 2">
                <div class="info-panel">
                    <h2>Image 2</h2>
                    <p>This is a description of image 2.</p>
                </div>
            </div>
            <div class="gallery-item">
                <img src="image3.jpg" alt="Image 3">
                <div class="info-panel">
                    <h2>Image 3</h2>
                    <p>This is a description of image 3.</p>
                </div>
            </div>
            <!-- Add more gallery items here -->
        </div>
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

/* Gallery Container Styles */
.gallery-container {
    max-width: 1200px;
    margin: 40px auto;
    padding: 20px;
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

/* Gallery Styles */
.gallery {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    grid-gap: 20px;
    justify-content: center;
}

/* Gallery Item Styles */
.gallery-item {
    position: relative;
    cursor: pointer;
}

.gallery-item img {
    width: 100%;
    height: 200px;
    object-fit: cover;
    border-radius: 10px 10px 0 0;
}

/* Info Panel Styles */
.info-panel {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    color: #fff;
    padding: 20px;
    transform: translateY(100%);
    transition: transform 0.3s ease-in-out;
}

.gallery-item:hover .info-panel {
    transform: translateY(0);
}

.info-panel h2 {
    font-size: 18px;
    margin-bottom: 10px;
}

.info-panel p {
    font-size: 14px;
}

/* Responsive Styles */
@media only screen and (max-width: 768px) {
    .gallery {
        grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    }
}

@media only screen and (max-width: 480px) {
    .gallery {
        grid-template-columns: 1fr;
    }
}
```
