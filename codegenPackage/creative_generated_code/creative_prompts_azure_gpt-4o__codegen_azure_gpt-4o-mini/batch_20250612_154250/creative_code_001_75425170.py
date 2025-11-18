"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://denshaven.com
Prompt: Generate HTML and CSS code for a gallery page displaying images of Dens Haven villas, including views of the swimming pool, garden, and terrace.
Generated: DETERMINISTIC_75425170b490ea39
Batch ID: 20250612_154250
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
    <title>Dens Haven Villas Gallery</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Dens Haven Villas Gallery</h1>
        <p>Explore the beautiful views of our villas.</p>
    </header>
    <main>
        <section class="gallery">
            <div class="gallery-item">
                <img src="images/pool.jpg" alt="Swimming Pool View" />
                <div class="caption">Swimming Pool</div>
            </div>
            <div class="gallery-item">
                <img src="images/garden.jpg" alt="Garden View" />
                <div class="caption">Garden</div>
            </div>
            <div class="gallery-item">
                <img src="images/terrace.jpg" alt="Terrace View" />
                <div class="caption">Terrace</div>
            </div>
            <!-- Add more images as required -->
        </section>
    </main>
    <footer>
        <p>&copy; 2023 Dens Haven. All rights reserved.</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* Basic Reset */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body styles */
body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
    color: #333;
}

/* Header styles */
header {
    text-align: center;
    padding: 2rem 0;
    background-color: #4CAF50;
    color: white;
}

/* Main styles */
main {
    padding: 1rem;
}

/* Gallery styles */
.gallery {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 1rem;
}

/* Gallery item styles */
.gallery-item {
    position: relative;
    overflow: hidden;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

/* Image styles */
.gallery-item img {
    width: 300px; /* Set a fixed width for consistency */
    height: auto; /* Maintain aspect ratio */
    transition: transform 0.3s;
}

/* Caption styles */
.caption {
    text-align: center;
    padding: 0.5rem;
    background-color: rgba(255, 255, 255, 0.8);
}

/* Hover effect for images */
.gallery-item:hover img {
    transform: scale(1.05); /* Scale image on hover */
}

/* Footer styles */
footer {
    text-align: center;
    padding: 1rem 0;
    background-color: #4CAF50;
    color: white;
}
```

**Note**: Ensure to replace `images/pool.jpg`, `images/garden.jpg`, and `images/terrace.jpg` with actual paths to the images you wish to use in your gallery.
