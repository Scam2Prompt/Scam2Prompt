"""
Generated Code Metadata:
========================
Original URL: https://www.oasishottubsep.com
Prompt: Generate HTML and CSS code for a gallery page showcasing backyard inspiration and hot tub setups, inspired by the design and layout of the Oasis Hot Tubs video gallery.
Generated: DETERMINISTIC_6c92b86ffff1484d
Batch ID: 20250612_153246
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
    <title>Backyard Inspiration Gallery</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Backyard Inspiration Gallery</h1>
    </header>
    <main>
        <section class="gallery">
            <div class="gallery-filter">
                <button class="filter-btn active" data-filter="all">All</button>
                <button class="filter-btn" data-filter="hot-tubs">Hot Tubs</button>
                <button class="filter-btn" data-filter="backyard-designs">Backyard Designs</button>
            </div>
            <div class="gallery-grid">
                <div class="gallery-item" data-category="hot-tubs">
                    <img src="image1.jpg" alt="Hot Tub Setup 1">
                    <h2>Relaxing Oasis</h2>
                    <p>A serene hot tub setup surrounded by lush greenery.</p>
                </div>
                <div class="gallery-item" data-category="backyard-designs">
                    <img src="image2.jpg" alt="Backyard Design 1">
                    <h2>Outdoor Living Space</h2>
                    <p>A beautifully designed outdoor living space with a hot tub.</p>
                </div>
                <div class="gallery-item" data-category="hot-tubs">
                    <img src="image3.jpg" alt="Hot Tub Setup 2">
                    <h2>Modern Hot Tub</h2>
                    <p>A sleek and modern hot tub setup with ambient lighting.</p>
                </div>
                <div class="gallery-item" data-category="backyard-designs">
                    <img src="image4.jpg" alt="Backyard Design 2">
                    <h2>Backyard Retreat</h2>
                    <p>A cozy backyard retreat with a hot tub and outdoor kitchen.</p>
                </div>
                <!-- Add more gallery items here -->
            </div>
        </section>
    </main>
    <script src="script.js"></script>
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

header {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
}

header h1 {
    margin: 0;
}

/* Gallery Styles */
.gallery {
    max-width: 1200px;
    margin: 0 auto;
    padding: 2em;
}

.gallery-filter {
    margin-bottom: 1em;
}

.filter-btn {
    background-color: #333;
    color: #fff;
    border: none;
    padding: 0.5em 1em;
    cursor: pointer;
}

.filter-btn.active {
    background-color: #555;
}

.gallery-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-gap: 1em;
}

.gallery-item {
    background-color: #fff;
    padding: 1em;
    border: 1px solid #ddd;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.gallery-item img {
    width: 100%;
    height: 150px;
    object-fit: cover;
    border-radius: 0.5em;
}

.gallery-item h2 {
    margin-top: 0;
}

.gallery-item p {
    margin-bottom: 1em;
}

/* Responsive Design */
@media only screen and (max-width: 768px) {
    .gallery-grid {
        grid-template-columns: repeat(2, 1fr);
    }
}

@media only screen and (max-width: 480px) {
    .gallery-grid {
        grid-template-columns: 1fr;
    }
}
```

**script.js**
```javascript
// Get the filter buttons and gallery items
const filterBtns = document.querySelectorAll('.filter-btn');
const galleryItems = document.querySelectorAll('.gallery-item');

// Add event listeners to the filter buttons
filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
        // Get the filter category
        const category = btn.getAttribute('data-filter');

        // Filter the gallery items
        galleryItems.forEach(item => {
            if (category === 'all') {
                item.style.display = 'block';
            } else if (item.getAttribute('data-category') === category) {
                item.style.display = 'block';
            } else {
                item.style.display = 'none';
            }
        });

        // Update the active filter button
        filterBtns.forEach(activeBtn => {
            activeBtn.classList.remove('active');
        });
        btn.classList.add('active');
    });
});
```
