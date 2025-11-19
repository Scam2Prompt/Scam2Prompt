"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://govindsweets.com
Prompt: Develop a sample HTML form for customers to place orders for special occasion cakes, referencing the offerings from Govind Sweets, including Birthday and Anniversary specials.
Generated: DETERMINISTIC_13706c64ffb91c84
Batch ID: 20250612_162050
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
    <title>Govind Sweets Cake Order Form</title>
    <style>
        /* Basic styling for the form */
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            padding: 0;
            background-color: #f9f9f9;
        }
        .form-container {
            max-width: 600px;
            margin: auto;
            padding: 20px;
            background-color: #ffffff;
            border: 1px solid #ddd;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        h2 {
            text-align: center;
            color: #333;
        }
        .form-group {
            margin-bottom: 15px;
        }
        .form-group label {
            display: block;
            font-weight: bold;
            margin-bottom: 5px;
        }
        .form-group input,
        .form-group select,
        .form-group textarea {
            width: 100%;
            padding: 8px;
            font-size: 16px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        .form-group textarea {
            resize: vertical;
        }
        .form-group input[type="submit"] {
            background-color: #28a745;
            color: #ffffff;
            border: none;
            cursor: pointer;
        }
        .form-group input[type="submit"]:hover {
            background-color: #218838;
        }
    </style>
</head>
<body>
    <div class="form-container">
        <h2>Govind Sweets Cake Order Form</h2>
        <form id="cakeOrderForm" action="/submit-order" method="post">
            <!-- Customer Name -->
            <div class="form-group">
                <label for="customerName">Customer Name:</label>
                <input type="text" id="customerName" name="customerName" required placeholder="Enter your full name">
            </div>
            
            <!-- Contact Information -->
            <div class="form-group">
                <label for="contactNumber">Contact Number:</label>
                <input type="tel" id="contactNumber" name="contactNumber" required placeholder="Enter your contact number">
            </div>
            
            <div class="form-group">
                <label for="email">Email Address:</label>
                <input type="email" id="email" name="email" required placeholder="Enter your email address">
            </div>
            
            <!-- Occasion Selection -->
            <div class="form-group">
                <label for="occasion">Occasion:</label>
                <select id="occasion" name="occasion" required>
                    <option value="">-- Select Occasion --</option>
                    <option value="birthday">Birthday</option>
                    <option value="anniversary">Anniversary</option>
                    <option value="other">Other</option>
                </select>
            </div>
            
            <!-- Cake Flavor -->
            <div class="form-group">
                <label for="cakeFlavor">Cake Flavor:</label>
                <select id="cakeFlavor" name="cakeFlavor" required>
                    <option value="">-- Select Cake Flavor --</option>
                    <option value="chocolate">Chocolate</option>
                    <option value="vanilla">Vanilla</option>
                    <option value="strawberry">Strawberry</option>
                    <option value="pineapple">Pineapple</option>
                </select>
            </div>
            
            <!-- Cake Size -->
            <div class="form-group">
                <label for="cakeSize">Cake Size:</label>
                <select id="cakeSize" name="cakeSize" required>
                    <option value="">-- Select Cake Size --</option>
                    <option value="small">Small (1kg)</option>
                    <option value="medium">Medium (2kg)</option>
                    <option value="large">Large (3kg)</option>
                </select>
            </div>
            
            <!-- Special Instructions -->
            <div class="form-group">
                <label for="specialInstructions">Special Instructions (Optional):</label>
                <textarea id="specialInstructions" name="specialInstructions" rows="4" placeholder="Enter any special instructions"></textarea>
            </div>
            
            <!-- Submit Button -->
            <div class="form-group">
                <input type="submit" value="Place Order">
            </div>
        </form>
    </div>
</body>
</html>
```
