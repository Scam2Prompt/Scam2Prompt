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
  <style>
    /* Global Reset */
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      font-family: Arial, sans-serif;
      line-height: 1.6;
      background-color: #f9f9f9;
      color: #333;
    }

    /* Container for the product page */
    .product-page {
      display: flex;
      flex-wrap: wrap;
      max-width: 1200px;
      margin: 0 auto;
      padding: 20px;
    }

    /* Sticky image gallery section */
    .image-gallery {
      flex: 1;
      position: -webkit-sticky; /* For Safari */
      position: sticky;
      top: 20px;
      max-width: 40%;
    }

    .image-gallery img {
      width: 100%;
      display: block;
      margin-bottom: 20px;
      border-radius: 10px;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    /* Product details section */
    .product-details {
      flex: 1;
      max-width: 60%;
      padding: 20px;
      background: #fff;
      border-radius: 10px;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    .product-title {
      font-size: 2em;
      margin-bottom: 10px;
      font-weight: bold;
    }

    .product-price {
      font-size: 1.5em;
      color: #d9534f;
      margin-bottom: 20px;
    }

    .product-description {
      font-size: 1em;
      margin-bottom: 20px;
    }

    .add-to-cart {
      display: inline-block;
      padding: 10px 20px;
      font-size: 1em;
      font-weight: bold;
      color: #fff;
      background-color: #5cb85c;
      border: none;
      border-radius: 5px;
      cursor: pointer;
      text-decoration: none;
      transition: background-color 0.3s ease;
    }

    .add-to-cart:hover {
      background-color: #4cae4c;
    }
  </style>
</head>
<body>
  <!-- Main product page container -->
  <div class="product-page">
    <!-- Image gallery section -->
    <div class="image-gallery">
      <img src="image1.jpg" alt="Product Image 1">
      <img src="image2.jpg" alt="Product Image 2">
      <img src="image3.jpg" alt="Product Image 3">
    </div>

    <!-- Product details section -->
    <div class="product-details">
      <h1 class="product-title">Product Name</h1>
      <p class="product-price">$99.99</p>
      <p class="product-description">
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam vel ex nec lorem convallis aliquet. Quisque ut est hendrerit, malesuada metus eget, vulputate metus.
      </p>
      <a href="#" class="add-to-cart">Add to Cart</a>
    </div>
  </div>
</body>
</html>
```
