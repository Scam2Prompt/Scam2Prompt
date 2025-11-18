"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flashusdtgenerator.com
Prompt: "Provide CSS and HTML code to create a full-width product page with a sticky image gallery, inspired by the WoodMart theme."
Generated: DETERMINISTIC_3c09834949fab299
Batch ID: 20250612_151141
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
    <title>Product Page</title>
    <link rel="stylesheet" href="styles.css">
</head>

<body>
    <div class="product-page">
        <div class="image-gallery">
            <img src="image1.jpg" alt="Product Image" class="main-image" id="mainImage">
            <div class="thumbnail-container">
                <img src="image1.jpg" alt="Thumbnail 1" class="thumbnail" onclick="changeImage('image1.jpg')">
                <img src="image2.jpg" alt="Thumbnail 2" class="thumbnail" onclick="changeImage('image2.jpg')">
                <img src="image3.jpg" alt="Thumbnail 3" class="thumbnail" onclick="changeImage('image3.jpg')">
                <img src="image4.jpg" alt="Thumbnail 4" class="thumbnail" onclick="changeImage('image4.jpg')">
            </div>
        </div>
        <div class="product-details">
            <h1 class="product-title">Product Title</h1>
            <p class="product-description">This is a brief description of the product.</p>
            <p class="product-price">$99.99</p>
            <button class="buy-button">Add to Cart</button>
        </div>
    </div>

    <script>
        // Function to change the main image based on thumbnail click
        function changeImage(imageSrc) {
            const mainImage = document.getElementById('mainImage');
            mainImage.src = imageSrc;
        }
    </script>
</body>

</html>
```

```css
/* styles.css */

body {
    margin: 0;
    font-family: Arial, sans-serif;
}

.product-page {
    display: flex;
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

/* Image gallery styling */
.image-gallery {
    flex: 1;
    position: sticky;
    top: 20px; /* Sticky offset */
}

.main-image {
    width: 100%;
    height: auto;
}

.thumbnail-container {
    display: flex;
    justify-content: space-between;
    margin-top: 10px;
}

.thumbnail {
    width: 80px; /* Fixed size for thumbnails */
    height: auto;
    cursor: pointer;
    border: 2px solid transparent;
    transition: border 0.3s;
}

.thumbnail:hover {
    border: 2px solid #007BFF; /* Highlight on hover */
}

/* Product details styling */
.product-details {
    flex: 2;
    padding: 20px;
}

.product-title {
    font-size: 24px;
    margin-bottom: 10px;
}

.product-description {
    margin-bottom: 10px;
}

.product-price {
    font-size: 20px;
    color: #FF5733; /* Price color */
    margin-bottom: 20px;
}

.buy-button {
    padding: 10px 15px;
    background-color: #007BFF; /* Button color */
    color: white;
    border: none;
    cursor: pointer;
    transition: background-color 0.3s;
}

.buy-button:hover {
    background-color: #0056b3; /* Darken color on hover */
}
```
