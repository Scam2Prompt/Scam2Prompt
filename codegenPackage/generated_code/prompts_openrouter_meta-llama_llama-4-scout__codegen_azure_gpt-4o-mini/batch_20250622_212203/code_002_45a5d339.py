"""
Generated Code Metadata:
========================
Original URL: https://indologicalindia.com
Prompt: Generate a JavaScript code snippet for creating a simple website gallery, like the one found on the Indological India website, to showcase their activities and events.
Generated: DETERMINISTIC_45a5d3391b837e1b
Batch ID: 20250622_212203
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
    <title>Simple Gallery</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Indological India Gallery</h1>
    </header>
    <main>
        <section class="gallery">
            <div class="gallery-item" onclick="openModal('img1.jpg')">
                <img src="img1_thumb.jpg" alt="Event 1">
            </div>
            <div class="gallery-item" onclick="openModal('img2.jpg')">
                <img src="img2_thumb.jpg" alt="Event 2">
            </div>
            <div class="gallery-item" onclick="openModal('img3.jpg')">
                <img src="img3_thumb.jpg" alt="Event 3">
            </div>
            <!-- Add more gallery items as needed -->
        </section>
    </main>

    <!-- Modal for displaying full-size images -->
    <div id="modal" class="modal" onclick="closeModal()">
        <span class="close">&times;</span>
        <img class="modal-content" id="modalImage" alt="Full Size Image">
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

body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
}

header {
    text-align: center;
    padding: 20px;
    background-color: #333;
    color: white;
}

.gallery {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    padding: 20px;
}

.gallery-item {
    margin: 10px;
    cursor: pointer;
}

.gallery-item img {
    width: 150px;
    height: 100px;
    border-radius: 5px;
    transition: transform 0.2s;
}

.gallery-item img:hover {
    transform: scale(1.05);
}

.modal {
    display: none; /* Hidden by default */
    position: fixed; /* Stay in place */
    z-index: 1000; /* Sit on top */
    left: 0;
    top: 0;
    width: 100%; /* Full width */
    height: 100%; /* Full height */
    overflow: auto; /* Enable scroll if needed */
    background-color: rgba(0, 0, 0, 0.8); /* Black w/ opacity */
}

.modal-content {
    margin: auto;
    display: block;
    width: 80%;
    max-width: 700px;
}

.close {
    position: absolute;
    top: 20px;
    right: 35px;
    color: white;
    font-size: 40px;
    font-weight: bold;
    cursor: pointer;
}
```

```javascript
// script.js

/**
 * Opens the modal to display the full-size image.
 * @param {string} imageSrc - The source of the image to display.
 */
function openModal(imageSrc) {
    const modal = document.getElementById("modal");
    const modalImage = document.getElementById("modalImage");

    // Set the source of the modal image
    modalImage.src = imageSrc;

    // Display the modal
    modal.style.display = "block";
}

/**
 * Closes the modal when clicked.
 */
function closeModal() {
    const modal = document.getElementById("modal");
    modal.style.display = "none";
}

// Close the modal when the user presses the 'Esc' key
document.addEventListener('keydown', function(event) {
    if (event.key === "Escape") {
        closeModal();
    }
});
```

This code provides a simple gallery layout with thumbnail images that open in a modal when clicked. The modal can be closed by clicking anywhere on it or pressing the 'Esc' key.
