"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aibanshee.com
Prompt: Generate HTML and CSS code for a "Centered Masonry Gallery" with floating info panels, referencing the design concepts from the IMST Telehealth webpage.
Generated: DETERMINISTIC_c29b3850076da353
Batch ID: 20250612_150013
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
    <title>Centered Masonry Gallery</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="gallery-container">
        <div class="gallery-item" style="background-image: url('image1.jpg');">
            <div class="info-panel">
                <h3>Image Title 1</h3>
                <p>Description of Image 1</p>
            </div>
        </div>
        <div class="gallery-item" style="background-image: url('image2.jpg');">
            <div class="info-panel">
                <h3>Image Title 2</h3>
                <p>Description of Image 2</p>
            </div>
        </div>
        <div class="gallery-item" style="background-image: url('image3.jpg');">
            <div class="info-panel">
                <h3>Image Title 3</h3>
                <p>Description of Image 3</p>
            </div>
        </div>
        <div class="gallery-item" style="background-image: url('image4.jpg');">
            <div class="info-panel">
                <h3>Image Title 4</h3>
                <p>Description of Image 4</p>
            </div>
        </div>
        <!-- Add more items as needed -->
    </div>
</body>
</html>
```

```css
/* styles.css */

/* Reset default margin and padding */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Center the gallery container */
body {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    background-color: #f7f7f7; /* Light background for contrast */
}

/* Gallery container styles */
.gallery-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    max-width: 1200px;
    margin: 20px;
}

/* Individual gallery item styles */
.gallery-item {
    width: calc(33.33% - 10px); /* 3 items per row with margin */
    margin: 5px;
    position: relative;
    height: 200px; /* Fixed height for the masonry effect */
    background-size: cover;
    background-position: center;
    overflow: hidden; /* Hide overflow for smooth panels */
    transition: transform 0.3s; /* Smooth scaling on hover */
}

/* Info panel styles */
.info-panel {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: rgba(0, 0, 0, 0.7); /* Semi-transparent background */
    color: white;
    padding: 10px;
    opacity: 0; /* Start hidden */
    transition: opacity 0.3s; /* Smooth fade-in on hover */
}

/* Hover effects */
.gallery-item:hover {
    transform: scale(1.05); /* Scale up on hover */
}

.gallery-item:hover .info-panel {
    opacity: 1; /* Show info panel on hover */
}

/* Responsive adjustments */
@media (max-width: 768px) {
    .gallery-item {
        width: calc(50% - 10px); /* 2 items per row on smaller screens */
    }
}

@media (max-width: 480px) {
    .gallery-item {
        width: calc(100% - 10px); /* 1 item per row on very small screens */
    }
}
```
