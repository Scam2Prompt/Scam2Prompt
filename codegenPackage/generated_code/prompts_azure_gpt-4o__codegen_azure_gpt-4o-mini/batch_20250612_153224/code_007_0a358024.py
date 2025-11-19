"""
Generated Code Metadata:
========================
Original URL: https://rupakparajuli.com.np
Prompt: Generate code to implement a responsive gallery feature for travel photos on a WordPress blog using JavaScript and CSS.
Generated: DETERMINISTIC_0a358024c14e060b
Batch ID: 20250612_153224
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
    <title>Responsive Travel Photo Gallery</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="gallery">
        <div class="gallery-item">
            <img src="photo1.jpg" alt="Travel Photo 1" />
        </div>
        <div class="gallery-item">
            <img src="photo2.jpg" alt="Travel Photo 2" />
        </div>
        <div class="gallery-item">
            <img src="photo3.jpg" alt="Travel Photo 3" />
        </div>
        <!-- Add more photos as needed -->
    </div>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* Basic reset for margins and paddings */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Gallery container styles */
.gallery {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 10px;
    padding: 10px;
}

/* Individual gallery item styles */
.gallery-item {
    overflow: hidden;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

/* Image styles */
.gallery-item img {
    width: 100%;
    height: auto;
    display: block;
    transition: transform 0.3s ease;
}

/* Image hover effect */
.gallery-item img:hover {
    transform: scale(1.05);
}
```

```javascript
// script.js

// Function to initialize the gallery
function initGallery() {
    const galleryItems = document.querySelectorAll('.gallery-item img');

    // Add click event listener to each gallery item
    galleryItems.forEach(item => {
        item.addEventListener('click', () => {
            openLightbox(item.src);
        });
    });
}

// Function to open a lightbox with the clicked image
function openLightbox(src) {
    const lightbox = document.createElement('div');
    lightbox.classList.add('lightbox');

    const img = document.createElement('img');
    img.src = src;
    img.alt = 'Lightbox Image';

    // Close lightbox on click
    lightbox.addEventListener('click', () => {
        lightbox.remove();
    });

    lightbox.appendChild(img);
    document.body.appendChild(lightbox);
}

// Initialize the gallery on DOMContentLoaded
document.addEventListener('DOMContentLoaded', initGallery);
```

```css
/* Additional styles for lightbox functionality */
.lightbox {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.8);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
}

.lightbox img {
    max-width: 90%;
    max-height: 90%;
}
```

This code provides a responsive gallery feature for travel photos on a WordPress blog, complete with a lightbox effect for viewing images.
