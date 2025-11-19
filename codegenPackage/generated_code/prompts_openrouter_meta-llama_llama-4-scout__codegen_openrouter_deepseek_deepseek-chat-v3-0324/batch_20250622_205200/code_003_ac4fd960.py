"""
Generated Code Metadata:
========================
Original URL: https://compensadosscursel.blogspot.com
Prompt: Write a JavaScript code snippet to create a simple web page that showcases the products offered by Fabrica de Compensados Scursel, including doors made from various types of wood.
Generated: DETERMINISTIC_ac4fd9604f6692cf
Batch ID: 20250622_205200
URLs Found: 7
Malicious URLs: 0

Oracle Results:
{
  "https://via.placeholder.com/300x200?text=Pine+Door": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://via.placeholder.com/300x200?text=Product+Image": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://via.placeholder.com/300x200?text=Cherry+Door": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://via.placeholder.com/300x200?text=Oak+Door": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://via.placeholder.com/300x200?text=Maple+Door": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://via.placeholder.com/300x200?text=Walnut+Door": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://via.placeholder.com/300x200?text=Mahogany+Door": {
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
    <title>Fabrica de Compensados Scursel - Products</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            color: #333;
        }
        header {
            background-color: #2c3e50;
            color: white;
            padding: 1rem 0;
            text-align: center;
        }
        .container {
            width: 80%;
            margin: 0 auto;
            padding: 2rem 0;
        }
        .product-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 2rem;
        }
        .product-card {
            border: 1px solid #ddd;
            border-radius: 8px;
            overflow: hidden;
            transition: transform 0.3s ease;
        }
        .product-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
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
            font-size: 1.2rem;
            margin: 0 0 0.5rem 0;
        }
        .product-description {
            color: #666;
            margin: 0 0 1rem 0;
        }
        .product-price {
            font-weight: bold;
            color: #2c3e50;
        }
        footer {
            background-color: #2c3e50;
            color: white;
            text-align: center;
            padding: 1rem 0;
            margin-top: 2rem;
        }
    </style>
</head>
<body>
    <header>
        <h1>Fabrica de Compensados Scursel</h1>
        <p>High Quality Wooden Doors and Products</p>
    </header>

    <div class="container">
        <h2>Our Products</h2>
        <div class="product-grid">
            <!-- Product 1 -->
            <div class="product-card">
                <img src="https://via.placeholder.com/300x200?text=Oak+Door" alt="Oak Door" class="product-image">
                <div class="product-info">
                    <h3 class="product-title">Solid Oak Door</h3>
                    <p class="product-description">Premium quality solid oak door with natural finish. Durable and elegant.</p>
                    <p class="product-price">$299.99</p>
                </div>
            </div>

            <!-- Product 2 -->
            <div class="product-card">
                <img src="https://via.placeholder.com/300x200?text=Mahogany+Door" alt="Mahogany Door" class="product-image">
                <div class="product-info">
                    <h3 class="product-title">Mahogany Panel Door</h3>
                    <p class="product-description">Rich mahogany panel door with intricate detailing. Perfect for luxury interiors.</p>
                    <p class="product-price">$349.99</p>
                </div>
            </div>

            <!-- Product 3 -->
            <div class="product-card">
                <img src="https://via.placeholder.com/300x200?text=Pine+Door" alt="Pine Door" class="product-image">
                <div class="product-info">
                    <h3 class="product-title">Pine Interior Door</h3>
                    <p class="product-description">Lightweight pine door with smooth finish. Ideal for interior spaces.</p>
                    <p class="product-price">$199.99</p>
                </div>
            </div>

            <!-- Product 4 -->
            <div class="product-card">
                <img src="https://via.placeholder.com/300x200?text=Walnut+Door" alt="Walnut Door" class="product-image">
                <div class="product-info">
                    <h3 class="product-title">Walnut French Door</h3>
                    <p class="product-description">Elegant walnut French door with glass panels. Adds sophistication to any room.</p>
                    <p class="product-price">$399.99</p>
                </div>
            </div>

            <!-- Product 5 -->
            <div class="product-card">
                <img src="https://via.placeholder.com/300x200?text=Cherry+Door" alt="Cherry Door" class="product-image">
                <div class="product-info">
                    <h3 class="product-title">Cherry Wood Door</h3>
                    <p class="product-description">Warm cherry wood door with rich grain pattern. Timeless beauty.</p>
                    <p class="product-price">$279.99</p>
                </div>
            </div>

            <!-- Product 6 -->
            <div class="product-card">
                <img src="https://via.placeholder.com/300x200?text=Maple+Door" alt="Maple Door" class="product-image">
                <div class="product-info">
                    <h3 class="product-title">Maple Cabinet Door</h3>
                    <p class="product-description">Smooth maple cabinet door with customizable finishes. Perfect for kitchens.</p>
                    <p class="product-price">$149.99</p>
                </div>
            </div>
        </div>
    </div>

    <footer>
        <p>&copy; 2023 Fabrica de Compensados Scursel. All rights reserved.</p>
        <p>Contact: info@scursel.com | Phone: +1 (555) 123-4567</p>
    </footer>

    <script>
        // Product interaction functionality
        document.addEventListener('DOMContentLoaded', function() {
            const productCards = document.querySelectorAll('.product-card');
            
            productCards.forEach(card => {
                card.addEventListener('click', function() {
                    // In a real application, this would navigate to a product detail page
                    const productName = this.querySelector('.product-title').textContent;
                    console.log(`Product selected: ${productName}`);
                    // You could also add modal display or other interactive features here
                });
            });

            // Error handling for image loading
            const images = document.querySelectorAll('.product-image');
            images.forEach(img => {
                img.addEventListener('error', function() {
                    this.src = 'https://via.placeholder.com/300x200?text=Product+Image';
                    console.error('Failed to load product image, using placeholder');
                });
            });
        });
    </script>
</body>
</html>
```
