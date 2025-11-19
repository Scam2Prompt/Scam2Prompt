"""
Generated Code Metadata:
========================
Original URL: https://jardinesdeprovenza.com.gt
Prompt: Create a product catalog using HTML and CSS for a store selling lavender-based personal care products, similar to those offered by Jardines de Provenza.
Generated: DETERMINISTIC_c2751d0b6ffe97e5
Batch ID: 20250622_205709
URLs Found: 5
Malicious URLs: 0

Oracle Results:
{
  "https://images.unsplash.com/photo-1607619056574-7f1a0d0e0b47": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://images.unsplash.com/photo-1607522370275-142b5cf4af7e": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://images.unsplash.com/photo-1604176354204-92669b8d8389": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://images.unsplash.com/photo-1595341883842-fe3eca5d566a": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://images.unsplash.com/photo-1600857544200-b2f0a1a5d0ad": {
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
    <title>Lavender Fields | Premium Lavender Products</title>
    <style>
        /* Reset and Base Styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Arial', sans-serif;
        }

        body {
            background-color: #f9f6f7;
            color: #333;
            line-height: 1.6;
        }

        /* Header Styles */
        header {
            background-color: #6a4c93;
            color: white;
            padding: 1.5rem 0;
            text-align: center;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }

        .logo {
            font-size: 2rem;
            font-weight: bold;
            margin-bottom: 0.5rem;
        }

        .tagline {
            font-style: italic;
            opacity: 0.9;
        }

        /* Navigation */
        nav {
            background-color: #8a6dae;
            padding: 1rem 0;
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
            font-weight: bold;
            transition: color 0.3s;
        }

        nav ul li a:hover {
            color: #f0e6ff;
        }

        /* Main Content */
        .container {
            max-width: 1200px;
            margin: 2rem auto;
            padding: 0 1rem;
        }

        .intro {
            text-align: center;
            margin-bottom: 2rem;
            padding: 1rem;
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        }

        .intro h2 {
            color: #6a4c93;
            margin-bottom: 1rem;
        }

        /* Product Grid */
        .products {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 2rem;
        }

        .product-card {
            background: white;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
            transition: transform 0.3s, box-shadow 0.3s;
        }

        .product-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }

        .product-image {
            height: 200px;
            background-size: cover;
            background-position: center;
        }

        .product-info {
            padding: 1.5rem;
        }

        .product-title {
            font-size: 1.2rem;
            color: #6a4c93;
            margin-bottom: 0.5rem;
        }

        .product-description {
            color: #666;
            margin-bottom: 1rem;
            font-size: 0.9rem;
        }

        .product-price {
            font-weight: bold;
            color: #333;
            margin-bottom: 1rem;
        }

        .btn {
            display: inline-block;
            background-color: #6a4c93;
            color: white;
            padding: 0.6rem 1.2rem;
            border-radius: 4px;
            text-decoration: none;
            transition: background-color 0.3s;
        }

        .btn:hover {
            background-color: #8a6dae;
        }

        /* Footer */
        footer {
            background-color: #6a4c93;
            color: white;
            text-align: center;
            padding: 2rem 0;
            margin-top: 3rem;
        }

        .footer-links {
            display: flex;
            justify-content: center;
            margin-bottom: 1rem;
        }

        .footer-links a {
            color: white;
            margin: 0 1rem;
            text-decoration: none;
        }

        .footer-links a:hover {
            text-decoration: underline;
        }

        .copyright {
            opacity: 0.8;
            font-size: 0.9rem;
        }

        /* Responsive Adjustments */
        @media (max-width: 768px) {
            nav ul {
                flex-direction: column;
                align-items: center;
            }

            nav ul li {
                margin: 0.5rem 0;
            }

            .products {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <header>
        <div class="logo">Lavender Fields</div>
        <div class="tagline">Premium Provençal Lavender Products</div>
    </header>

    <nav>
        <ul>
            <li><a href="#">Home</a></li>
            <li><a href="#">Products</a></li>
            <li><a href="#">About Us</a></li>
            <li><a href="#">Contact</a></li>
        </ul>
    </nav>

    <div class="container">
        <section class="intro">
            <h2>Our Premium Lavender Collection</h2>
            <p>Handcrafted with organic lavender from Provence, our products bring the calming essence of French fields to your home.</p>
        </section>

        <section class="products">
            <!-- Product 1 -->
            <div class="product-card">
                <div class="product-image" style="background-image: url('https://images.unsplash.com/photo-1595341883842-fe3eca5d566a');"></div>
                <div class="product-info">
                    <h3 class="product-title">Lavender Essential Oil</h3>
                    <p class="product-description">Pure 100% organic lavender essential oil, perfect for aromatherapy and relaxation.</p>
                    <p class="product-price">$14.99</p>
                    <a href="#" class="btn">Add to Cart</a>
                </div>
            </div>

            <!-- Product 2 -->
            <div class="product-card">
                <div class="product-image" style="background-image: url('https://images.unsplash.com/photo-1600857544200-b2f0a1a5d0ad');"></div>
                <div class="product-info">
                    <h3 class="product-title">Lavender Hand Cream</h3>
                    <p class="product-description">Nourishing hand cream with lavender extract and shea butter for soft, hydrated skin.</p>
                    <p class="product-price">$12.99</p>
                    <a href="#" class="btn">Add to Cart</a>
                </div>
            </div>

            <!-- Product 3 -->
            <div class="product-card">
                <div class="product-image" style="background-image: url('https://images.unsplash.com/photo-1607522370275-142b5cf4af7e');"></div>
                <div class="product-info">
                    <h3 class="product-title">Lavender Soap Bar</h3>
                    <p class="product-description">Gentle, handmade soap with lavender buds and natural oils for delicate skin.</p>
                    <p class="product-price">$8.99</p>
                    <a href="#" class="btn">Add to Cart</a>
                </div>
            </div>

            <!-- Product 4 -->
            <div class="product-card">
                <div class="product-image" style="background-image: url('https://images.unsplash.com/photo-1604176354204-92669b8d8389');"></div>
                <div class="product-info">
                    <h3 class="product-title">Lavender Pillow Mist</h3>
                    <p class="product-description">Calming spray with lavender essential oil to promote restful sleep.</p>
                    <p class="product-price">$16.99</p>
                    <a href="#" class="btn">Add to Cart</a>
                </div>
            </div>

            <!-- Product 5 -->
            <div class="product-card">
                <div class="product-image" style="background-image: url('https://images.unsplash.com/photo-1607619056574-7f1a0d0e0b47');"></div>
                <div class="product-info">
                    <h3 class="product-title">Lavender Body Lotion</h3>
                    <p class="product-description">Lightweight, fast-absorbing lotion with lavender and aloe vera for all-day hydration.</p>
                    <p class="product-price
