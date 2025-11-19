"""
Generated Code Metadata:
========================
Original URL: https://cakco.com
Prompt: "Design a product page for a French soft waxy vegetable-tanned cowhide shoulder bag with a retro handheld design."
Generated: DETERMINISTIC_fda03acc56ed1520
Batch ID: 20250622_205302
URLs Found: 5
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/bag-thumb2.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/bag-thumb4.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/bag-thumb1.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/bag-thumb3.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/bag-main.jpg": {
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
    <title>French Soft Waxy Vegetable-Tanned Cowhide Shoulder Bag</title>
    <style>
        /* Reset and base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Helvetica Neue', Arial, sans-serif;
        }
        
        body {
            background-color: #f9f9f9;
            color: #333;
            line-height: 1.6;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        
        /* Product section */
        .product {
            display: flex;
            flex-wrap: wrap;
            gap: 30px;
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            padding: 30px;
            margin-top: 20px;
        }
        
        .product-images {
            flex: 1;
            min-width: 300px;
        }
        
        .main-image {
            width: 100%;
            height: 400px;
            object-fit: cover;
            border-radius: 4px;
            margin-bottom: 15px;
        }
        
        .thumbnail-container {
            display: flex;
            gap: 10px;
        }
        
        .thumbnail {
            width: 80px;
            height: 80px;
            object-fit: cover;
            border-radius: 4px;
            cursor: pointer;
            border: 1px solid #ddd;
        }
        
        .thumbnail:hover {
            border-color: #888;
        }
        
        .product-details {
            flex: 1;
            min-width: 300px;
        }
        
        .product-title {
            font-size: 28px;
            margin-bottom: 10px;
            color: #222;
        }
        
        .product-subtitle {
            font-size: 18px;
            color: #666;
            margin-bottom: 20px;
            font-weight: 300;
        }
        
        .price {
            font-size: 24px;
            font-weight: bold;
            color: #333;
            margin: 20px 0;
        }
        
        .description {
            margin: 20px 0;
            line-height: 1.7;
        }
        
        .features {
            margin: 20px 0;
        }
        
        .features li {
            margin-bottom: 8px;
            list-style-position: inside;
        }
        
        .color-selector {
            margin: 20px 0;
        }
        
        .color-option {
            display: inline-block;
            width: 30px;
            height: 30px;
            border-radius: 50%;
            margin-right: 10px;
            cursor: pointer;
            border: 2px solid transparent;
        }
        
        .color-option.selected {
            border-color: #333;
        }
        
        .quantity-selector {
            margin: 20px 0;
        }
        
        .quantity-selector select {
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        
        .add-to-cart {
            background-color: #000;
            color: white;
            border: none;
            padding: 12px 30px;
            font-size: 16px;
            cursor: pointer;
            border-radius: 4px;
            transition: background-color 0.3s;
            margin-top: 20px;
        }
        
        .add-to-cart:hover {
            background-color: #333;
        }
        
        .delivery-info {
            margin-top: 30px;
            padding: 15px;
            background-color: #f5f5f5;
            border-radius: 4px;
        }
        
        /* Responsive adjustments */
        @media (max-width: 768px) {
            .product {
                flex-direction: column;
            }
            
            .main-image {
                height: 300px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="product">
            <div class="product-images">
                <img id="mainImage" src="https://example.com/bag-main.jpg" alt="French Soft Waxy Vegetable-Tanned Cowhide Shoulder Bag" class="main-image">
                <div class="thumbnail-container">
                    <img src="https://example.com/bag-thumb1.jpg" alt="Bag front view" class="thumbnail" onclick="changeImage(this)">
                    <img src="https://example.com/bag-thumb2.jpg" alt="Bag side view" class="thumbnail" onclick="changeImage(this)">
                    <img src="https://example.com/bag-thumb3.jpg" alt="Bag back view" class="thumbnail" onclick="changeImage(this)">
                    <img src="https://example.com/bag-thumb4.jpg" alt="Bag detail" class="thumbnail" onclick="changeImage(this)">
                </div>
            </div>
            
            <div class="product-details">
                <h1 class="product-title">French Soft Waxy Vegetable-Tanned Cowhide Shoulder Bag</h1>
                <h2 class="product-subtitle">Retro Handheld Design</h2>
                
                <div class="price">$249.00</div>
                
                <div class="description">
                    <p>This exquisite shoulder bag is crafted from premium French soft waxy vegetable-tanned cowhide, offering both durability and a luxurious feel. The retro handheld design combines timeless elegance with modern functionality.</p>
                </div>
                
                <ul class="features">
                    <li>100% vegetable-tanned French cowhide leather</li>
                    <li>Soft waxy finish that develops a beautiful patina over time</li>
                    <li>Retro handheld design with detachable shoulder strap</li>
                    <li>Spacious main compartment with interior pockets</li>
                    <li>Handcrafted by skilled artisans in France</li>
                    <li>Dimensions: 12" x 9" x 5" (30cm x 23cm x 13cm)</li>
                </ul>
                
                <div class="color-selector">
                    <p>Color:</p>
                    <div class="color-option selected" style="background-color: #8B4513;" title="Chestnut" onclick="selectColor(this)"></div>
                    <div class="color-option" style="background-color: #5C4033;" title="Dark Brown" onclick="selectColor(this)"></div>
                    <div class="color-option" style="background-color: #D2B48C;" title="Tan" onclick="selectColor(this)"></div>
                </div>
                
                <div class="quantity-selector">
                    <label for="quantity">Quantity:</label>
                    <select id="quantity">
                        <option value="1">1</option>
                        <option value="2">2</option>
                        <option value="3">3</option>
                        <option value="4">4</option>
                        <option value="5">5</option>
                    </select>
                </div>
                
                <button class="add-to-cart" onclick="addToCart()">Add to Cart</button>
                
                <div class="delivery-info">
                    <p><strong>Free shipping</strong> on all orders over $100</p>
                    <p>Estimated delivery: 3-5 business days</p>
                    <p>Returns accepted within 30 days</p>
                </div>
            </div>
        </div>
    </div>
    
    <script>
        // Change main image when thumbnail is clicked
        function changeImage(element) {
            document.getElementById('mainImage').src = element.src;
        }
        
        // Select color option
        function selectColor(element) {
            const colors = document.querySelectorAll('.color-option');
            colors.forEach(color => color.classList.remove('selected'));
            element.classList.add('selected');
        }
        
        // Add to cart functionality
        function addToCart() {
            const quantity = document.getElementById('quantity').value;
            const selectedColor = document.querySelector('.color-option.selected').title;
            
            // In a real application, this would send data to your backend
            alert(`Added ${quantity} ${selectedColor} bag(s) to your cart`);
            
            // Here you would typically:
            // 1. Validate inputs
            // 2. Send data to server
            // 3. Update cart UI
            // 4. Handle errors if they occur
        }
    </script>
</body>
</html>
```
