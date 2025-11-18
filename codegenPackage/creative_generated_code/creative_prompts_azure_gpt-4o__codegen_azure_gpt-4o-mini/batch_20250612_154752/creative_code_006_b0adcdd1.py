"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://indologicalindia.com
Prompt: Write code to create an interactive gallery for "Indological India" that dynamically displays images of their campaigns and activities with captions.
Generated: DETERMINISTIC_b0adcdd1db77d347
Batch ID: 20250612_154752
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
    <title>Indological India Gallery</title>
    <link rel="stylesheet" href="styles.css">
    <script src="script.js" defer></script>
</head>
<body>
    <header>
        <h1>Indological India Campaign Gallery</h1>
    </header>
    <main>
        <section id="gallery" class="gallery"></section>
    </main>
    <footer>
        <p>&copy; 2023 Indological India. All Rights Reserved.</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* Basic reset */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body styling */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
}

/* Header styling */
header {
    text-align: center;
    padding: 20px;
    background-color: #007BFF;
    color: white;
}

/* Gallery styling */
.gallery {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 15px;
    padding: 20px;
}

/* Individual image container */
.gallery-item {
    position: relative;
    overflow: hidden;
    border-radius: 8px;
}

/* Image styling */
.gallery-item img {
    width: 100%;
    height: auto;
    transition: transform 0.3s;
}

/* Caption styling */
.gallery-item caption {
    position: absolute;
    bottom: 0;
    background: rgba(0, 0, 0, 0.7);
    color: white;
    width: 100%;
    text-align: center;
    padding: 10px;
    opacity: 0;
    transition: opacity 0.3s;
}

/* Show caption on hover */
.gallery-item:hover img {
    transform: scale(1.05);
}

.gallery-item:hover caption {
    opacity: 1;
}
```

```javascript
// script.js

// Define the image data
const imageData = [
    {
        src: 'images/campaign1.jpg',
        caption: 'Campaign 1: Promoting Cultural Awareness'
    },
    {
        src: 'images/campaign2.jpg',
        caption: 'Campaign 2: Preserving Traditional Arts'
    },
    {
        src: 'images/campaign3.jpg',
        caption: 'Campaign 3: Education and Community Support'
    }
    // Add more images as needed
];

// Function to create image elements for the gallery
function createGallery() {
    const gallery = document.getElementById('gallery');
    
    // Check if gallery exists
    if (!gallery) {
        console.error('Gallery element not found');
        return;
    }

    // Loop through image data and create elements
    imageData.forEach(image => {
        const item = document.createElement('div');
        item.classList.add('gallery-item');

        const img = document.createElement('img');
        img.src = image.src;
        img.alt = image.caption;

        const caption = document.createElement('caption');
        caption.textContent = image.caption;

        // Append image and caption to the gallery item
        item.appendChild(img);
        item.appendChild(caption);

        // Append the gallery item to the gallery
        gallery.appendChild(item);
    });
}

// Handle potential errors during gallery creation
try {
    createGallery();
} catch (error) {
    console.error('Error creating gallery:', error);
}
```
