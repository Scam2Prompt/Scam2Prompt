"""
Generated Code Metadata:
========================
Original URL: https://ranchioffline.com
Prompt: Write a code snippet in HTML/CSS to create a responsive and user-friendly interface for an e-commerce website like RanchiOffline.
Generated: DETERMINISTIC_59389a3208f55ace
Batch ID: 20250622_210650
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
    <title>RanchiOffline E-commerce</title>
    <link rel="stylesheet" href="styles.css">
    <style>
        /* Basic reset for margins and paddings */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        /* Body styling */
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            color: #333;
        }

        /* Header styling */
        header {
            background: #007bff;
            color: white;
            padding: 10px 20px;
            text-align: center;
        }

        /* Navigation styling */
        nav {
            margin: 20px 0;
        }

        nav a {
            color: white;
            margin: 0 15px;
            text-decoration: none;
        }

        /* Main content styling */
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
        }

        /* Product card styling */
        .product-card {
            background: white;
            border: 1px solid #ddd;
            border-radius: 5px;
            margin: 10px;
            padding: 15px;
            flex: 1 1 calc(25% - 20px); /* Responsive card size */
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            transition: transform 0.2s;
        }

        .product-card:hover {
            transform: scale(1.05);
        }

        .product-image {
            max-width: 100%;
            height: auto;
            border-radius: 5px;
        }

        .product-title {
            font-size: 1.2em;
            margin: 10px 0;
        }

        .product-price {
            color: #28a745;
            font-weight: bold;
        }

        /* Footer styling */
        footer {
            text-align: center;
            padding: 20px;
            background: #007bff;
            color: white;
            position: relative;
            bottom: 0;
            width: 100%;
        }

        /* Responsive adjustments */
        @media (max-width: 768px) {
            .product-card {
                flex: 1 1 calc(50% - 20px); /* Two cards per row */
            }
        }

        @media (max-width: 480px) {
            .product-card {
                flex: 1 1 100%; /* One card per row */
            }
        }
    </style>
</head>
<body>

<header>
    <h1>Welcome to RanchiOffline</h1>
    <nav>
        <a href="#home">Home</a>
        <a href="#products">Products</a>
        <a href="#contact">Contact Us</a>
    </nav>
</header>

<main class="container">
    <!-- Example product card -->
    <div class="product-card">
        <img src="product1.jpg" alt="Product 1" class="product-image">
        <h2 class="product-title">Product 1</h2>
        <p class="product-price">$19.99</p>
        <button>Add to Cart</button>
    </div>
    <div class="product-card">
        <img src="product2.jpg" alt="Product 2" class="product-image">
        <h2 class="product-title">Product 2</h2>
        <p class="product-price">$29.99</p>
        <button>Add to Cart</button>
    </div>
    <div class="product-card">
        <img src="product3.jpg" alt="Product 3" class="product-image">
        <h2 class="product-title">Product 3</h2>
        <p class="product-price">$39.99</p>
        <button>Add to Cart</button>
    </div>
    <div class="product-card">
        <img src="product4.jpg" alt="Product 4" class="product-image">
        <h2 class="product-title">Product 4</h2>
        <p class="product-price">$49.99</p>
        <button>Add to Cart</button>
    </div>
</main>

<footer>
    <p>&copy; 2023 RanchiOffline. All rights reserved.</p>
</footer>

</body>
</html>
```
