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

Here is production-ready code for an interactive gallery in JavaScript, HTML, and CSS:

### `index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Indological India Gallery</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Indological India Gallery</h1>
        <p>Explore our campaigns and activities through vibrant imagery.</p>
    </header>

    <main>
        <div id="gallery" class="gallery-container">
            <!-- Images will be dynamically loaded here -->
        </div>
    </main>

    <footer>
        <p>&copy; 2023 Indological India</p>
    </footer>

    <script src="script.js"></script>
</body>
</html>
```

---

### `styles.css`
```css
/* General styles */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    color: #333;
    background-color: #f9f9f9;
}

/* Header styles */
header {
    text-align: center;
    padding: 20px;
    background-color: #004d99;
    color: white;
}

/* Gallery container */
.gallery-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    padding: 20px;
    gap: 20px;
}

/* Individual gallery item */
.gallery-item {
    position: relative;
    width: 250px;
    height: 250px;
    overflow: hidden;
    border: 1px solid #ddd;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease-in-out;
}

.gallery-item:hover {
    transform: scale(1.05);
}

/* Image styles */
.gallery-item img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

/* Caption overlay */
.caption {
    position: absolute;
    bottom: 0;
    background: rgba(0, 0, 0, 0.6);
    color: white;
    width: 100%;
    padding: 10px;
    text-align: center;
    opacity: 0;
    transition: opacity 0.3s ease-in-out;
}

.gallery-item:hover .caption {
    opacity: 1;
}

/* Footer styles */
footer {
    text-align: center;
    padding: 10px;
    background-color: #004d99;
    color: white;
}
```

---

### `script.js`
```javascript
// Sample data for gallery images
const galleryData = [
    {
        src: 'images/campaign1.jpg',
        caption: 'Campaign for Rural Education'
    },
    {
        src: 'images/campaign2.jpg',
        caption: 'Women Empowerment Initiatives'
    },
    {
        src: 'images/campaign3.jpg',
        caption: 'Environmental Conservation Drive'
    },
    {
        src: 'images/campaign4.jpg',
        caption: 'Cultural Heritage Preservation'
    },
    {
        src: 'images/campaign5.jpg',
        caption: 'Healthcare Awareness Programs'
    }
];

/**
 * Function to dynamically render gallery items
 */
function renderGallery() {
    const galleryContainer = document.getElementById('gallery');
    
    // Ensure the container is cleared before rendering
    galleryContainer.innerHTML = '';

    // Iterate over the gallery data and create elements
    galleryData.forEach(item => {
        const galleryItem = document.createElement('div');
        galleryItem.className = 'gallery-item';

        // Create the image element
        const image = document.createElement('img');
        image.src = item.src;
        image.alt = item.caption;

        // Create the caption overlay
        const caption = document.createElement('div');
        caption.className = 'caption';
        caption.textContent = item.caption;

        // Append image and caption to the gallery item
        galleryItem.appendChild(image);
        galleryItem.appendChild(caption);

        // Append gallery item to the container
        galleryContainer.appendChild(galleryItem);
    });
}

/**
 * Error handling for image loading
 */
window.addEventListener('error', (e) => {
    if (e.target.tagName === 'IMG') {
        e.target.src = 'images/placeholder.jpg'; // Fallback image
        console.error(`Failed to load image: ${e.target.src}`);
    }
});

/**
 * Initialize the gallery on page load
 */
document.addEventListener('DOMContentLoaded', renderGallery);
```

### Notes:
1. Place images (`campaign1.jpg`, `campaign2.jpg`, etc.) in a folder named `images`.
2. Include a `placeholder.jpg` in the `images` folder for fallback purposes.
