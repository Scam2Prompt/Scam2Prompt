"""
Generated Code Metadata:
========================
Original URL: https://lagraveusenormande.fr
Prompt: Create a product catalog using HTML and CSS for an engraving company that offers customized products such as plaques, plates, and stamps.
Generated: DETERMINISTIC_64002306c52c3263
Batch ID: 20250622_210703
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
    <meta name="description" content="Product catalog for an engraving company offering customized plaques, plates, and stamps.">
    <title>Engraving Company Product Catalog</title>
    <style>
        /* General styles */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f9f9f9;
            color: #333;
        }

        header {
            background-color: #4CAF50;
            color: white;
            padding: 1rem 2rem;
            text-align: center;
        }

        h1 {
            margin: 0;
        }

        main {
            padding: 2rem;
        }

        .product-catalog {
            display: flex;
            flex-wrap: wrap;
            gap: 2rem;
            justify-content: center;
        }

        .product-card {
            background-color: white;
            border: 1px solid #ddd;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            width: 300px;
            overflow: hidden;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .product-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 6px 10px rgba(0, 0, 0, 0.15);
        }

        .product-image {
            width: 100%;
            height: 200px;
            object-fit: cover;
        }

        .product-details {
            padding: 1rem;
        }

        .product-title {
            font-size: 1.2rem;
            font-weight: bold;
            margin: 0 0 0.5rem;
        }

        .product-description {
            font-size: 0.9rem;
            margin: 0 0 1rem;
            color: #555;
        }

        .product-price {
            font-size: 1rem;
            font-weight: bold;
            color: #4CAF50;
        }

        footer {
            background-color: #333;
            color: white;
            text-align: center;
            padding: 1rem;
            margin-top: 2rem;
        }
    </style>
</head>
<body>
    <!-- Header Section -->
    <header>
        <h1>Engraving Company Product Catalog</h1>
    </header>

    <!-- Main Content -->
    <main>
        <section class="product-catalog">
            <!-- Product Card 1 -->
            <div class="product-card">
                <img src="plaque.jpg" alt="Custom Plaque" class="product-image">
                <div class="product-details">
                    <h2 class="product-title">Custom Plaque</h2>
                    <p class="product-description">Elegant plaques for awards, recognition, and memorials. Fully customizable.</p>
                    <p class="product-price">$50.00</p>
                </div>
            </div>

            <!-- Product Card 2 -->
            <div class="product-card">
                <img src="plate.jpg" alt="Engraved Plate" class="product-image">
                <div class="product-details">
                    <h2 class="product-title">Engraved Plate</h2>
                    <p class="product-description">Durable plates for labeling, signage, and decorative purposes.</p>
                    <p class="product-price">$30.00</p>
                </div>
            </div>

            <!-- Product Card 3 -->
            <div class="product-card">
                <img src="stamp.jpg" alt="Custom Stamp" class="product-image">
                <div class="product-details">
                    <h2 class="product-title">Custom Stamp</h2>
                    <p class="product-description">High-quality stamps for business or personal use. Available in various sizes.</p>
                    <p class="product-price">$20.00</p>
                </div>
            </div>
        </section>
    </main>

    <!-- Footer Section -->
    <footer>
        <p>&copy; 2023 Engraving Company. All rights reserved.</p>
    </footer>
</body>
</html>
```
