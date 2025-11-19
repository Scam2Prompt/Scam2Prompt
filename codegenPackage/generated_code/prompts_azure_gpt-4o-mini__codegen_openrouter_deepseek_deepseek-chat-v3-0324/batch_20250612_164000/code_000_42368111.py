"""
Generated Code Metadata:
========================
Original URL: https://hnu.co.id
Prompt: Generate a code snippet to create an e-commerce product page for herbal supplements similar to those offered by Habbasyi Niaga Utama, focusing on Habbatussauda and its health benefits.
Generated: DETERMINISTIC_42368111f533e57f
Batch ID: 20250612_164000
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
    <title>Habbatussauda - Premium Herbal Supplement | Habbasyi Niaga Utama</title>
    <meta name="description" content="Discover the health benefits of premium Habbatussauda (Black Seed) supplements. Boost immunity, improve digestion, and enhance overall wellness.">
    <style>
        /* Reset and base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Arial', sans-serif;
        }

        body {
            line-height: 1.6;
            color: #333;
            background-color: #f9f9f9;
        }

        /* Header styles */
        header {
            background-color: #2c7d4a;
            color: white;
            padding: 1rem 0;
            text-align: center;
        }

        .logo {
            font-size: 1.8rem;
            font-weight: bold;
            margin-bottom: 0.5rem;
        }

        nav ul {
            display: flex;
            justify-content: center;
            list-style: none;
        }

        nav ul li {
            margin: 0 1rem;
        }

        nav ul li a {
            color: white;
            text-decoration: none;
            font-weight: 500;
        }

        /* Product section */
        .product-container {
            max-width: 1200px;
            margin: 2rem auto;
            padding: 0 1rem;
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 2rem;
        }

        .product-image {
            width: 100%;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }

        .product-info h1 {
            font-size: 2rem;
            margin-bottom: 1rem;
            color: #2c7d4a;
        }

        .price {
            font-size: 1.5rem;
            font-weight: bold;
            color: #e67e22;
            margin: 1rem 0;
        }

        .benefits-list {
            margin: 1.5rem 0;
            padding-left: 1.5rem;
        }

        .benefits-list li {
            margin-bottom: 0.5rem;
        }

        .add-to-cart {
            background-color: #2c7d4a;
            color: white;
            border: none;
            padding: 0.8rem 1.5rem;
            font-size: 1rem;
            border-radius: 4px;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        .add-to-cart:hover {
            background-color: #246b3d;
        }

        .quantity-selector {
            margin: 1rem 0;
        }

        .quantity-selector label {
            display: block;
            margin-bottom: 0.5rem;
        }

        .quantity-selector input {
            width: 60px;
            padding: 0.5rem;
            border: 1px solid #ddd;
            border-radius: 4px;
        }

        /* Footer */
        footer {
            background-color: #333;
            color: white;
            text-align: center;
            padding: 1.5rem 0;
            margin-top: 2rem;
        }

        /* Responsive design */
        @media (max-width: 768px) {
            .product-container {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <header>
        <div class="logo">Habbasyi Niaga Utama</div>
        <nav>
            <ul>
                <li><a href="#">Home</a></li>
                <li><a href="#">Products</a></li>
                <li><a href="#">About</a></li>
                <li><a href="#">Contact</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section class="product-container">
            <div class="product-image-container">
                <img src="habbatussauda-product.jpg" alt="Premium Habbatussauda Capsules" class="product-image">
            </div>
            <div class="product-info">
                <h1>Premium Habbatussauda Capsules</h1>
                <p class="price">$24.99</p>
                <p>Our premium Habbatussauda (Black Seed) capsules are sourced from the finest Nigella Sativa seeds, carefully processed to preserve their natural benefits.</p>
                
                <h3>Health Benefits:</h3>
                <ul class="benefits-list">
                    <li>Boosts immune system function</li>
                    <li>Supports respiratory health</li>
                    <li>Rich in antioxidants</li>
                    <li>Promotes digestive wellness</li>
                    <li>May help maintain healthy blood sugar levels</li>
                    <li>Supports cardiovascular health</li>
                </ul>

                <div class="quantity-selector">
                    <label for="quantity">Quantity:</label>
                    <input type="number" id="quantity" name="quantity" min="1" max="10" value="1">
                </div>

                <button class="add-to-cart">Add to Cart</button>
            </div>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 Habbasyi Niaga Utama. All rights reserved.</p>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const addToCartBtn = document.querySelector('.add-to-cart');
            const quantityInput = document.getElementById('quantity');

            // Add to cart functionality
            addToCartBtn.addEventListener('click', function() {
                const quantity = parseInt(quantityInput.value);
                
                if (isNaN(quantity) || quantity < 1 || quantity > 10) {
                    alert('Please enter a valid quantity between 1 and 10');
                    return;
                }

                // In a real application, this would add to cart
                alert(`Added ${quantity} Habbatussauda Capsule(s) to your cart`);
                
                // Reset quantity
                quantityInput.value = 1;
            });
        });
    </script>
</body>
</html>
```
