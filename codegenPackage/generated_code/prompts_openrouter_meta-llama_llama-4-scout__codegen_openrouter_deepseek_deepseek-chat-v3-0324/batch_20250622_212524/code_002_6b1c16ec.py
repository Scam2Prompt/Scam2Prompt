"""
Generated Code Metadata:
========================
Original URL: https://avilhasdolarbraz.blogspot.com
Prompt: Generate HTML code for a simple product listing page featuring items like plastic tables, organizer boxes, and kitchen utensils.
Generated: DETERMINISTIC_6b1c16ecf1c0c26e
Batch ID: 20250622_212524
URLs Found: 6
Malicious URLs: 0

Oracle Results:
{
  "https://images.unsplash.com/photo-1556909212-d5b604d0c90d?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://images.unsplash.com/photo-1602143407151-7111542de6e8?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://images.unsplash.com/photo-1556228578-8c89e6adf883?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://images.unsplash.com/photo-1585664811087-47f65abbad64?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://images.unsplash.com/photo-1583947581924-a9d4a10a4211?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60": {
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
    <title>Home Essentials - Product Listing</title>
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
            padding: 1.5rem;
            text-align: center;
        }
        
        h1 {
            margin-bottom: 0.5rem;
        }
        
        /* Main content */
        .container {
            max-width: 1200px;
            margin: 2rem auto;
            padding: 0 1rem;
        }
        
        /* Product grid */
        .products {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 2rem;
        }
        
        /* Product card */
        .product-card {
            background: white;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
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
            padding: 1.5rem;
        }
        
        .product-title {
            font-size: 1.2rem;
            margin-bottom: 0.5rem;
            color: #2c3e50;
        }
        
        .product-price {
            font-weight: bold;
            color: #e74c3c;
            margin-bottom: 1rem;
            font-size: 1.1rem;
        }
        
        .product-description {
            color: #7f8c8d;
            margin-bottom: 1rem;
            font-size: 0.9rem;
        }
        
        .btn {
            display: inline-block;
            background: #3498db;
            color: white;
            padding: 0.5rem 1rem;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            text-decoration: none;
            transition: background 0.3s ease;
        }
        
        .btn:hover {
            background: #2980b9;
        }
        
        /* Footer */
        footer {
            background-color: #2c3e50;
            color: white;
            text-align: center;
            padding: 1.5rem;
            margin-top: 2rem;
        }
    </style>
</head>
<body>
    <header>
        <h1>Home Essentials</h1>
        <p>Quality products for your everyday needs</p>
    </header>
    
    <div class="container">
        <div class="products">
            <!-- Product 1 -->
            <div class="product-card">
                <img src="https://images.unsplash.com/photo-1556909212-d5b604d0c90d?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60" alt="Plastic Table" class="product-image">
                <div class="product-info">
                    <h3 class="product-title">Foldable Plastic Table</h3>
                    <div class="product-price">$49.99</div>
                    <p class="product-description">Durable and lightweight plastic table perfect for indoor and outdoor use. Easy to clean and foldable for storage.</p>
                    <a href="#" class="btn">Add to Cart</a>
                </div>
            </div>
            
            <!-- Product 2 -->
            <div class="product-card">
                <img src="https://images.unsplash.com/photo-1594035910387-fea47794261f?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60" alt="Organizer Box" class="product-image">
                <div class="product-info">
                    <h3 class="product-title">Stackable Organizer Box</h3>
                    <div class="product-price">$19.99</div>
                    <p class="product-description">Clear plastic organizer box with stackable design. Perfect for storing small items and keeping your space tidy.</p>
                    <a href="#" class="btn">Add to Cart</a>
                </div>
            </div>
            
            <!-- Product 3 -->
            <div class="product-card">
                <img src="https://images.unsplash.com/photo-1583947581924-a9d4a10a4211?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60" alt="Kitchen Utensils" class="product-image">
                <div class="product-info">
                    <h3 class="product-title">Kitchen Utensil Set</h3>
                    <div class="product-price">$29.99</div>
                    <p class="product-description">Complete set of 12 essential kitchen utensils made from durable plastic and stainless steel.</p>
                    <a href="#" class="btn">Add to Cart</a>
                </div>
            </div>
            
            <!-- Product 4 -->
            <div class="product-card">
                <img src="https://images.unsplash.com/photo-1556228578-8c89e6adf883?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60" alt="Plastic Chair" class="product-image">
                <div class="product-info">
                    <h3 class="product-title">Outdoor Plastic Chair</h3>
                    <div class="product-price">$24.99</div>
                    <p class="product-description">Weather-resistant plastic chair with comfortable design. Perfect for patio, garden or balcony.</p>
                    <a href="#" class="btn">Add to Cart</a>
                </div>
            </div>
            
            <!-- Product 5 -->
            <div class="product-card">
                <img src="https://images.unsplash.com/photo-1585664811087-47f65abbad64?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60" alt="Storage Bins" class="product-image">
                <div class="product-info">
                    <h3 class="product-title">Plastic Storage Bins (Set of 3)</h3>
                    <div class="product-price">$34.99</div>
                    <p class="product-description">Versatile storage bins with handles. Great for organizing toys, clothes, or pantry items.</p>
                    <a href="#" class="btn">Add to Cart</a>
                </div>
            </div>
            
            <!-- Product 6 -->
            <div class="product-card">
                <img src="https://images.unsplash.com/photo-1602143407151-7111542de6e8?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60" alt="Food Containers" class="product-image">
                <div class="product-info">
                    <h3 class="product-title">Food Storage Containers</h3>
                    <div class="product-price">$22.99</div>
                    <p class="product-description">Airtight plastic food storage containers. Microwave and dishwasher safe. Set of 5.</p>
                    <a href="#" class="btn">Add to Cart</a>
                </div>
            </div>
        </div>
    </div>
    
    <footer>
        <p>&copy; 2023 Home Essentials. All rights reserved.</p>
    </footer>
</body>
</html>
```
