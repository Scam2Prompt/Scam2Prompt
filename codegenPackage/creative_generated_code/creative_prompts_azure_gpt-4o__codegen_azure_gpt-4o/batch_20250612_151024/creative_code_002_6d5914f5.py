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
    <title>Quick View Example</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="product">
        <img src="product-image.jpg" alt="Product Image" class="product-image">
        <button class="quick-view-btn">Quick View</button>
    </div>

    <!-- Quick View Modal -->
    <div id="quick-view-modal" class="modal hidden">
        <div class="modal-content">
            <span class="close-btn">&times;</span>
            <img src="product-image.jpg" alt="Product Image" class="modal-product-image">
            <h2>Product Name</h2>
            <p>Short product description goes here.</p>
            <p><strong>Price:</strong> $99.99</p>
        </div>
    </div>

    <script>
        // JavaScript for handling Quick View functionality
        document.addEventListener('DOMContentLoaded', () => {
            const quickViewBtn = document.querySelector('.quick-view-btn');
            const modal = document.getElementById('quick-view-modal');
            const closeBtn = document.querySelector('.close-btn');

            // Show the modal when Quick View button is clicked
            quickViewBtn.addEventListener('click', () => {
                modal.classList.remove('hidden');
            });

            // Hide the modal when Close button is clicked
            closeBtn.addEventListener('click', () => {
                modal.classList.add('hidden');
            });

            // Hide the modal when clicking outside the modal content
            window.addEventListener('click', (event) => {
                if (event.target === modal) {
                    modal.classList.add('hidden');
                }
            });
        });
    </script>
</body>
</html>
```

```css
/* styles.css */

/* Basic Reset */
body {
    margin: 0;
    font-family: Arial, sans-serif;
}

/* Product Styling */
.product {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin: 20px;
}

.product-image {
    width: 200px;
    height: auto;
    border: 1px solid #ddd;
    border-radius: 5px;
}

.quick-view-btn {
    margin-top: 10px;
    padding: 10px 20px;
    background-color: #007BFF;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.quick-view-btn:hover {
    background-color: #0056b3;
}

/* Modal Styling */
.modal {
    display: flex;
    justify-content: center;
    align-items: center;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    z-index: 1000;
    visibility: hidden;
    opacity: 0;
    transition: visibility 0s, opacity 0.3s ease;
}

.modal.hidden {
    visibility: hidden;
    opacity: 0;
}

.modal-content {
    background-color: #fff;
    padding: 20px;
    border-radius: 10px;
    max-width: 400px;
    text-align: center;
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
}

.close-btn {
    position: absolute;
    top: 10px;
    right: 15px;
    font-size: 20px;
    font-weight: bold;
    cursor: pointer;
}

.modal-product-image {
    width: 100%;
    height: auto;
    margin-bottom: 10px;
}

/* Show Modal */
.modal:not(.hidden) {
    visibility: visible;
    opacity: 1;
}
```
