"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://glisten.site
Prompt: Generate HTML and CSS code to replicate the "Quick View" functionality for product previews, as seen on the "Glisten" website.
Generated: DETERMINISTIC_6d5914f55d7d65ad
Batch ID: 20250612_151024
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
    <title>Product Quick View</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Main Product Display -->
    <div class="product-container">
        <img src="product-image.jpg" alt="Product Image" class="product-image" />
        <button class="quick-view-btn" onclick="openQuickView()">Quick View</button>
    </div>

    <!-- Quick View Modal -->
    <div id="quickViewModal" class="modal">
        <div class="modal-content">
            <span class="close" onclick="closeQuickView()">&times;</span>
            <h2>Product Title</h2>
            <img src="product-image.jpg" alt="Product Image" class="modal-image" />
            <p>Product description goes here. It can include details like material, size, and other specifications.</p>
            <p class="price">$99.99</p>
            <button class="add-to-cart-btn">Add to Cart</button>
        </div>
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

/* Styling for product container */
.product-container {
    position: relative;
    display: inline-block;
}

/* Image styles */
.product-image {
    width: 300px;
    height: 300px;
    object-fit: cover;
}

/* Quick view button styles */
.quick-view-btn {
    position: absolute;
    bottom: 10px;
    left: 10px;
    padding: 10px 20px;
    background-color: #007BFF;
    color: white;
    border: none;
    cursor: pointer;
    transition: background-color 0.3s;
}

.quick-view-btn:hover {
    background-color: #0056b3;
}

/* Modal styles */
.modal {
    display: none; /* Hidden by default */
    position: fixed; /* Stay in place */
    z-index: 1; /* Sit on top */
    left: 0;
    top: 0;
    width: 100%; /* Full width */
    height: 100%; /* Full height */
    overflow: auto; /* Enable scroll if needed */
    background-color: rgba(0, 0, 0, 0.7); /* Black w/ opacity */
}

/* Modal content styles */
.modal-content {
    background-color: white;
    margin: 15% auto; /* 15% from the top and centered */
    padding: 20px;
    border: 1px solid #888;
    width: 80%; /* Could be more or less, depending on screen size */
}

/* Close button styles */
.close {
    color: #aaa;
    float: right;
    font-size: 28px;
    font-weight: bold;
}

.close:hover,
.close:focus {
    color: black;
    text-decoration: none;
    cursor: pointer;
}

/* Price styling */
.price {
    font-size: 24px;
    font-weight: bold;
}

/* Add to cart button styles */
.add-to-cart-btn {
    padding: 10px 20px;
    background-color: #28A745;
    color: white;
    border: none;
    cursor: pointer;
    transition: background-color 0.3s;
}

.add-to-cart-btn:hover {
    background-color: #218838;
}
```

```javascript
// script.js

/**
 * Opens the Quick View modal.
 */
function openQuickView() {
    const modal = document.getElementById("quickViewModal");
    if (modal) {
        modal.style.display = "block";
    } else {
        console.error("Modal element not found.");
    }
}

/**
 * Closes the Quick View modal.
 */
function closeQuickView() {
    const modal = document.getElementById("quickViewModal");
    if (modal) {
        modal.style.display = "none";
    } else {
        console.error("Modal element not found.");
    }
}

// Close the modal when clicking anywhere outside of it
window.onclick = function(event) {
    const modal = document.getElementById("quickViewModal");
    if (event.target === modal) {
        closeQuickView();
    }
};
```
