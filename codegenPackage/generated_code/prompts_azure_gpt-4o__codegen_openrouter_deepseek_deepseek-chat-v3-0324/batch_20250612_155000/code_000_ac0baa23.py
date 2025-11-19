"""
Generated Code Metadata:
========================
Original URL: https://la-guarida.com.ar
Prompt: Write code for a basic e-commerce website using HTML, CSS, and JavaScript, incorporating features mentioned by La Guarida, such as product listings and a shopping cart.
Generated: DETERMINISTIC_ac0baa230ac21b4c
Batch ID: 20250612_155000
URLs Found: 6
Malicious URLs: 0

Oracle Results:
{
  "https://images.unsplash.com/photo-1603366615917-1fa6dad5c4fa?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://images.unsplash.com/photo-1560345573-9f453083c335?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://images.unsplash.com/photo-1594035910387-fea47794261f?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://images.unsplash.com/photo-1571115177098-24ec42ed204d?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://images.unsplash.com/photo-1517705008128-361805f42e86?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://images.unsplash.com/photo-1587049352851-8d4e89133924?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>La Guarida - E-commerce</title>
    <style>
        /* Reset and base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Arial', sans-serif;
        }

        body {
            background-color: #f5f5f5;
            color: #333;
            line-height: 1.6;
        }

        /* Header styles */
        header {
            background-color: #2c3e50;
            color: white;
            padding: 1rem;
            text-align: center;
        }

        .logo {
            font-size: 2rem;
            font-weight: bold;
            margin-bottom: 0.5rem;
        }

        /* Navigation */
        nav {
            background-color: #34495e;
            padding: 0.5rem;
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
            padding: 0.5rem;
            transition: color 0.3s;
        }

        nav ul li a:hover {
            color: #f39c12;
        }

        /* Main content */
        .container {
            max-width: 1200px;
            margin: 2rem auto;
            padding: 0 1rem;
            display: grid;
            grid-template-columns: 3fr 1fr;
            gap: 2rem;
        }

        /* Product grid */
        .products {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 1.5rem;
        }

        .product-card {
            background: white;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s;
        }

        .product-card:hover {
            transform: translateY(-5px);
        }

        .product-image {
            width: 100%;
            height: 200px;
            object-fit: cover;
        }

        .product-info {
            padding: 1rem;
        }

        .product-title {
            font-size: 1.1rem;
            margin-bottom: 0.5rem;
        }

        .product-price {
            font-weight: bold;
            color: #e74c3c;
            margin-bottom: 1rem;
        }

        .add-to-cart {
            background-color: #3498db;
            color: white;
            border: none;
            padding: 0.5rem 1rem;
            border-radius: 4px;
            cursor: pointer;
            width: 100%;
            transition: background-color 0.3s;
        }

        .add-to-cart:hover {
            background-color: #2980b9;
        }

        /* Shopping cart */
        .cart {
            background: white;
            border-radius: 8px;
            padding: 1rem;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            position: sticky;
            top: 1rem;
        }

        .cart-title {
            font-size: 1.2rem;
            margin-bottom: 1rem;
            padding-bottom: 0.5rem;
            border-bottom: 1px solid #eee;
        }

        .cart-items {
            margin-bottom: 1rem;
        }

        .cart-item {
            display: flex;
            justify-content: space-between;
            margin-bottom: 0.5rem;
            padding-bottom: 0.5rem;
            border-bottom: 1px solid #eee;
        }

        .cart-item-name {
            flex: 2;
        }

        .cart-item-price {
            flex: 1;
            text-align: right;
        }

        .cart-total {
            font-weight: bold;
            text-align: right;
            margin-top: 1rem;
            padding-top: 1rem;
            border-top: 1px solid #eee;
        }

        .checkout-btn {
            background-color: #27ae60;
            color: white;
            border: none;
            padding: 0.75rem;
            border-radius: 4px;
            cursor: pointer;
            width: 100%;
            margin-top: 1rem;
            transition: background-color 0.3s;
        }

        .checkout-btn:hover {
            background-color: #219653;
        }

        /* Footer */
        footer {
            background-color: #2c3e50;
            color: white;
            text-align: center;
            padding: 1rem;
            margin-top: 2rem;
        }

        /* Responsive adjustments */
        @media (max-width: 768px) {
            .container {
                grid-template-columns: 1fr;
            }

            .cart {
                position: static;
                margin-top: 2rem;
            }
        }
    </style>
</head>
<body>
    <header>
        <div class="logo">La Guarida</div>
        <p>Your favorite e-commerce store</p>
    </header>

    <nav>
        <ul>
            <li><a href="#">Home</a></li>
            <li><a href="#">Products</a></li>
            <li><a href="#">About</a></li>
            <li><a href="#">Contact</a></li>
        </ul>
    </nav>

    <div class="container">
        <main class="products">
            <!-- Product cards will be dynamically inserted here -->
        </main>

        <aside class="cart">
            <h2 class="cart-title">Your Cart</h2>
            <div class="cart-items">
                <!-- Cart items will be dynamically inserted here -->
            </div>
            <div class="cart-total">Total: $0.00</div>
            <button class="checkout-btn">Proceed to Checkout</button>
        </aside>
    </div>

    <footer>
        <p>&copy; 2023 La Guarida. All rights reserved.</p>
    </footer>

    <script>
        // Sample product data
        const products = [
            {
                id: 1,
                name: "Premium Coffee Beans",
                price: 12.99,
                image: "https://images.unsplash.com/photo-1517705008128-361805f42e86?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
            },
            {
                id: 2,
                name: "Organic Tea Selection",
                price: 9.99,
                image: "https://images.unsplash.com/photo-1560345573-9f453083c335?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
            },
            {
                id: 3,
                name: "Artisanal Chocolate Box",
                price: 18.50,
                image: "https://images.unsplash.com/photo-1571115177098-24ec42ed204d?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
            },
            {
                id: 4,
                name: "Gourmet Spice Set",
                price: 15.75,
                image: "https://images.unsplash.com/photo-1603366615917-1fa6dad5c4fa?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
            },
            {
                id: 5,
                name: "Handcrafted Olive Oil",
                price: 22.00,
                image: "https://images.unsplash.com/photo-1594035910387-fea47794261f?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
            },
            {
                id: 6,
                name: "Specialty Honey Jar",
                price: 8.99,
                image: "https://images.unsplash.com/photo-1587049352851-8d4e89133924?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
            }
        ];

        // Shopping cart state
        let cart = [];

        // DOM elements
        const productsContainer = document.querySelector('.products');
        const cartItemsContainer = document.querySelector('.cart-items');
        const cartTotalElement = document.querySelector('.cart-total');

        // Initialize the app
        document.addEventListener('DOMContentLoaded', () => {
            renderProducts();
            renderCart();
        });

        // Render product listings
        function renderProducts
