"""
Generated Code Metadata:
========================
Original URL: https://mail.dexodoor.com
Prompt: "Design a simple web application using HTML, CSS, and JavaScript to showcase different styles of UPVC blinds, curtains, and shutters."
Generated: DETERMINISTIC_62e40ebf3ac77b04
Batch ID: 20250622_210038
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
    <title>UPVC Blinds, Curtains, and Shutters Showcase</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>UPVC Blinds, Curtains, and Shutters Showcase</h1>
    </header>
    <main>
        <section id="gallery">
            <h2>Our Collection</h2>
            <div class="card" onclick="showDetails('blinds')">
                <img src="images/blinds.jpg" alt="UPVC Blinds">
                <h3>UPVC Blinds</h3>
                <p>Stylish and functional blinds for every room.</p>
            </div>
            <div class="card" onclick="showDetails('curtains')">
                <img src="images/curtains.jpg" alt="UPVC Curtains">
                <h3>UPVC Curtains</h3>
                <p>Elegant curtains that enhance your decor.</p>
            </div>
            <div class="card" onclick="showDetails('shutters')">
                <img src="images/shutters.jpg" alt="UPVC Shutters">
                <h3>UPVC Shutters</h3>
                <p>Durable shutters for added privacy and style.</p>
            </div>
        </section>
        <section id="details" class="hidden">
            <h2>Details</h2>
            <div id="details-content"></div>
            <button onclick="hideDetails()">Close</button>
        </section>
    </main>
    <footer>
        <p>&copy; 2023 UPVC Showcase. All rights reserved.</p>
    </footer>
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

/* Body styles */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    background-color: #f4f4f4;
}

/* Header styles */
header {
    background: #35424a;
    color: #ffffff;
    padding: 20px 0;
    text-align: center;
}

/* Main section styles */
main {
    padding: 20px;
}

/* Gallery styles */
#gallery {
    display: flex;
    justify-content: space-around;
    flex-wrap: wrap;
}

/* Card styles */
.card {
    background: #ffffff;
    border: 1px solid #dddddd;
    border-radius: 5px;
    margin: 10px;
    padding: 15px;
    text-align: center;
    cursor: pointer;
    transition: transform 0.2s;
}

.card:hover {
    transform: scale(1.05);
}

/* Hidden class for details section */
.hidden {
    display: none;
}

/* Footer styles */
footer {
    text-align: center;
    padding: 10px 0;
    background: #35424a;
    color: #ffffff;
    position: relative;
    bottom: 0;
    width: 100%;
}
```

```javascript
// script.js

/**
 * Displays the details of the selected item.
 * @param {string} type - The type of item to display (blinds, curtains, shutters).
 */
function showDetails(type) {
    const detailsContent = document.getElementById('details-content');
    const detailsSection = document.getElementById('details');

    // Clear previous content
    detailsContent.innerHTML = '';

    // Set content based on the selected type
    switch (type) {
        case 'blinds':
            detailsContent.innerHTML = '<h3>UPVC Blinds</h3><p>Our UPVC blinds are available in various styles and colors, perfect for any room.</p>';
            break;
        case 'curtains':
            detailsContent.innerHTML = '<h3>UPVC Curtains</h3><p>Elegant and stylish, our UPVC curtains add a touch of sophistication to your home.</p>';
            break;
        case 'shutters':
            detailsContent.innerHTML = '<h3>UPVC Shutters</h3><p>Durable and stylish, our UPVC shutters provide privacy and enhance your home’s aesthetic.</p>';
            break;
        default:
            detailsContent.innerHTML = '<p>Details not available.</p>';
    }

    // Show the details section
    detailsSection.classList.remove('hidden');
}

/**
 * Hides the details section.
 */
function hideDetails() {
    const detailsSection = document.getElementById('details');
    detailsSection.classList.add('hidden');
}
```
