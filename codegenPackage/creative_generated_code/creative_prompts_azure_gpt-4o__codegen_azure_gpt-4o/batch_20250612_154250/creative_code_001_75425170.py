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
    <meta name="description" content="Gallery page for Dens Haven villas showcasing views of the swimming pool, garden, and terrace.">
    <title>Dens Haven Villas Gallery</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Gallery Wrapper -->
    <div class="gallery-container">
        <header>
            <h1>Dens Haven Villas Gallery</h1>
            <p>Explore stunning views of our swimming pool, garden, and terrace.</p>
        </header>
        <main>
            <!-- Image Grid -->
            <div class="image-grid">
                <!-- Swimming Pool Images -->
                <div class="image-category">
                    <h2>Swimming Pool</h2>
                    <img src="images/pool1.jpg" alt="Swimming pool view 1" class="gallery-image">
                    <img src="images/pool2.jpg" alt="Swimming pool view 2" class="gallery-image">
                </div>
                <!-- Garden Images -->
                <div class="image-category">
                    <h2>Garden</h2>
                    <img src="images/garden1.jpg" alt="Garden view 1" class="gallery-image">
                    <img src="images/garden2.jpg" alt="Garden view 2" class="gallery-image">
                </div>
                <!-- Terrace Images -->
                <div class="image-category">
                    <h2>Terrace</h2>
                    <img src="images/terrace1.jpg" alt="Terrace view 1" class="gallery-image">
                    <img src="images/terrace2.jpg" alt="Terrace view 2" class="gallery-image">
                </div>
            </div>
        </main>
        <footer>
            <p>&copy; 2023 Dens Haven Villas. All Rights Reserved.</p>
        </footer>
    </div>
</body>
</html>
```

```css
/* styles.css */

/* Reset some default browser styles */
body, h1, h2, p {
    margin: 0;
    padding: 0;
}

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    background-color: #f9f9f9;
    color: #333;
}

/* Center and style the gallery container */
.gallery-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

/* Header styling */
header {
    text-align: center;
    margin-bottom: 20px;
}

header h1 {
    font-size: 2rem;
    margin-bottom: 10px;
}

header p {
    font-size: 1rem;
    color: #555;
}

/* Image grid styling */
.image-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 20px;
}

/* Each category section */
.image-category h2 {
    font-size: 1.5rem;
    margin-bottom: 10px;
    text-align: center;
    color: #444;
}

/* Gallery images styling */
.gallery-image {
    width: 100%;
    height: auto;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

/* Hover effect for images */
.gallery-image:hover {
    transform: scale(1.05);
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}

/* Footer styling */
footer {
    text-align: center;
    margin-top: 20px;
    font-size: 0.9rem;
    color: #777;
}
```
