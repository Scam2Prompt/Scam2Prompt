"""
Generated Code Metadata:
========================
Original URL: https://www.apos.cl
Prompt: "Create a simple product catalog using HTML, CSS, and JavaScript that showcases different types of paper rolls, including thermal rolls, with pricing and contact information for a Chilean business."
Generated: DETERMINISTIC_98673a3ebbd56e10
Batch ID: 20250622_205138
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
    <title>Paper Roll Catalog - Chilean Business</title>
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

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }

        header {
            background-color: #2c3e50;
            color: white;
            padding: 20px 0;
            text-align: center;
            margin-bottom: 30px;
        }

        h1 {
            font-size: 2.5rem;
            margin-bottom: 10px;
        }

        .tagline {
            font-size: 1.2rem;
            opacity: 0.9;
        }

        .products {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 25px;
            margin-bottom: 40px;
        }

        .product-card {
            background: white;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease;
        }

        .product-card:hover {
            transform: translateY(-5px);
        }

        .product-image {
            height: 200px;
            background-color: #eee;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.5rem;
            color: #666;
        }

        .product-info {
            padding: 20px;
        }

        .product-title {
            font-size: 1.4rem;
            margin-bottom: 10px;
            color: #2c3e50;
        }

        .product-description {
            margin-bottom: 15px;
            color: #666;
        }

        .product-price {
            font-size: 1.3rem;
            font-weight: bold;
            color: #e74c3c;
            margin-bottom: 15px;
        }

        .contact-section {
            background-color: #2c3e50;
            color: white;
            padding: 30px;
            border-radius: 8px;
            margin-top: 30px;
        }

        .contact-title {
            font-size: 1.8rem;
            margin-bottom: 20px;
            text-align: center;
        }

        .contact-info {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-around;
            gap: 20px;
        }

        .contact-method {
            flex: 1;
            min-width: 250px;
            text-align: center;
        }

        .contact-method h3 {
            margin-bottom: 10px;
            font-size: 1.3rem;
        }

        .contact-method p {
            margin-bottom: 5px;
        }

        footer {
            text-align: center;
            padding: 20px;
            margin-top: 40px;
            background-color: #34495e;
            color: white;
        }

        @media (max-width: 768px) {
            .products {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <header>
        <div class="container">
            <h1>Paper Roll Solutions</h1>
            <p class="tagline">High-quality paper rolls for your business needs</p>
        </div>
    </header>

    <div class="container">
        <div class="products" id="products-container">
            <!-- Products will be loaded here via JavaScript -->
        </div>

        <div class="contact-section">
            <h2 class="contact-title">Contact Us</h2>
            <div class="contact-info">
                <div class="contact-method">
                    <h3>Phone</h3>
                    <p>+56 9 1234 5678</p>
                </div>
                <div class="contact-method">
                    <h3>Email</h3>
                    <p>contact@paperrolls.cl</p>
                </div>
                <div class="contact-method">
                    <h3>Address</h3>
                    <p>Santiago, Chile</p>
                </div>
            </div>
        </div>
    </div>

    <footer>
        <p>&copy; 2023 Paper Roll Solutions. All rights reserved.</p>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            // Product data
            const products = [
                {
                    id: 1,
                    title: "Thermal Paper Roll 80mm",
                    description: "High-quality thermal paper rolls for POS systems. 80mm width, 60mm diameter.",
                    price: "CLP $12,500",
                    imageText: "Thermal 80mm"
                },
                {
                    id: 2,
                    title: "Thermal Paper Roll 57mm",
                    description: "Standard thermal paper rolls for receipt printers. 57mm width, 40mm diameter.",
                    price: "CLP $9,800",
                    imageText: "Thermal 57mm"
                },
                {
                    id: 3,
                    title: "Bond Paper Roll A4",
                    description: "Premium bond paper rolls for office printers. A4 size, 500 sheets per roll.",
                    price: "CLP $15,200",
                    imageText: "Bond A4"
                },
                {
                    id: 4,
                    title: "Kraft Paper Roll 50cm",
                    description: "Eco-friendly kraft paper rolls for packaging. 50cm width, 30m length.",
                    price: "CLP $18,750",
                    imageText: "Kraft 50cm"
                },
                {
                    id: 5,
                    title: "Thermal Paper Roll 110mm",
                    description: "Large format thermal paper for industrial printers. 110mm width, 80mm diameter.",
                    price: "CLP $22,300",
                    imageText: "Thermal 110mm"
                },
                {
                    id: 6,
                    title: "Carbonless Paper Roll",
                    description: "Multi-part carbonless paper rolls for forms. Custom sizes available.",
                    price: "CLP $14,900",
                    imageText: "Carbonless"
                }
            ];

            // Render products
            const productsContainer = document.getElementById('products-container');
            
            products.forEach(product => {
                const productCard = document.createElement('div');
                productCard.className = 'product-card';
                
                productCard.innerHTML = `
                    <div class="product-image">${product.imageText}</div>
                    <div class="product-info">
                        <h3 class="product-title">${product.title}</h3>
                        <p class="product-description">${product.description}</p>
                        <p class="product-price">${product.price}</p>
                    </div>
                `;
                
                productsContainer.appendChild(productCard);
            });

            // Error handling for product rendering
            if (products.length === 0) {
                productsContainer.innerHTML = '<p>No products available at the moment. Please check back later.</p>';
            }
        });
    </script>
</body>
</html>
```
