"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://emareels.se
Prompt: Write code to display detailed images and specifications for Emanuelson Reels models, such as "Trout 1 Large" and "Salmon," in a mobile-friendly web application.
Generated: DETERMINISTIC_5a7e93885673c3f2
Batch ID: 20250612_153224
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
    <title>Emanuelson Reels Models</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
    <script src="script.js" defer></script> <!-- Load JavaScript file at the end of the body -->
</head>
<body>
    <header>
        <h1>Emanuelson Reels Models</h1>
        <nav>
            <ul>
                <li><a href="#trout">Trout 1 Large</a></li>
                <li><a href="#salmon">Salmon</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section id="trout">
            <h2>Trout 1 Large</h2>
            <img src="images/trout1-large.jpg" alt="Emanuelson Trout 1 Large Reel" class="responsive-img">
            <div class="specifications">
                <h3>Specifications:</h3>
                <ul>
                    <li>Weight: 250 grams</li>
                    <li>Material: Aluminum</li>
                    <li>Drag System: Smooth drag with adjustable tension</li>
                    <li>Line Capacity: 200 yards of 20 lb test</li>
                </ul>
            </div>
        </section>
        <section id="salmon">
            <h2>Salmon Reel</h2>
            <img src="images/salmon-reel.jpg" alt="Emanuelson Salmon Reel" class="responsive-img">
            <div class="specifications">
                <h3>Specifications:</h3>
                <ul>
                    <li>Weight: 300 grams</li>
                    <li>Material: Carbon Fiber</li>
                    <li>Drag System: High-performance drag system</li>
                    <li>Line Capacity: 250 yards of 30 lb test</li>
                </ul>
            </div>
        </section>
    </main>
    <footer>
        <p>&copy; 2023 Emanuelson Reels. All rights reserved.</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* Basic styling for body and text */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    margin: 0;
    padding: 0;
}

/* Header styling */
header {
    background: #007BFF;
    color: white;
    padding: 10px 0;
    text-align: center;
}

/* Navigation list styling */
nav ul {
    list-style-type: none;
    padding: 0;
}

/* Navigation link styling */
nav a {
    color: white;
    text-decoration: none;
    margin: 0 15px;
}

/* Main section styling */
main {
    padding: 20px;
}

/* Image responsiveness */
.responsive-img {
    max-width: 100%;
    height: auto;
}

/* Specifications list styling */
.specifications {
    margin-top: 10px;
}

/* Footer styling */
footer {
    background: #333;
    color: white;
    text-align: center;
    padding: 10px 0;
    position: relative;
    bottom: 0;
    width: 100%;
}
```

```javascript
// script.js

// Function to initialize the application
document.addEventListener("DOMContentLoaded", () => {
    // Check if images are loaded successfully
    const images = document.querySelectorAll('img');
    images.forEach((img) => {
        img.onerror = () => {
            console.error(`Error loading image: ${img.src}`);
            img.alt = "Image not available"; // Set alt text if image fails to load
        };
    });
});
```
