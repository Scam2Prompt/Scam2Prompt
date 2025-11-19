"""
Generated Code Metadata:
========================
Original URL: https://idgfiber.com
Prompt: Write a script to generate a quote request form for IDG Fiber products, allowing users to input quantities for items like Glass Fiber Reinforced Concrete (GFRC) and AR Fiber, and calculate the total cost.
Generated: DETERMINISTIC_ee3c5a6aacc3b424
Batch ID: 20250612_153246
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
    <title>IDG Fiber Products Quote Request</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            color: #333;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            border: 1px solid #ddd;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h1 {
            text-align: center;
            color: #2c3e50;
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        input[type="number"], input[type="text"], input[type="email"] {
            width: 100%;
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-sizing: border-box;
        }
        button {
            background-color: #3498db;
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }
        button:hover {
            background-color: #2980b9;
        }
        .result {
            margin-top: 20px;
            padding: 15px;
            background-color: #f8f9fa;
            border-radius: 4px;
            display: none;
        }
        .product-row {
            display: flex;
            justify-content: space-between;
            margin-bottom: 10px;
            padding-bottom: 10px;
            border-bottom: 1px solid #eee;
        }
        .error {
            color: #e74c3c;
            font-size: 14px;
            margin-top: 5px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>IDG Fiber Products Quote Request</h1>
        <form id="quoteForm">
            <div class="form-group">
                <label for="name">Full Name</label>
                <input type="text" id="name" name="name" required>
                <div id="nameError" class="error"></div>
            </div>
            
            <div class="form-group">
                <label for="email">Email Address</label>
                <input type="email" id="email" name="email" required>
                <div id="emailError" class="error"></div>
            </div>
            
            <div class="form-group">
                <label for="company">Company Name</label>
                <input type="text" id="company" name="company">
            </div>
            
            <div class="form-group">
                <label for="phone">Phone Number</label>
                <input type="text" id="phone" name="phone" required>
                <div id="phoneError" class="error"></div>
            </div>
            
            <h3>Product Quantities</h3>
            
            <div class="form-group">
                <label for="gfrc">Glass Fiber Reinforced Concrete (GFRC) - $45 per unit</label>
                <input type="number" id="gfrc" name="gfrc" min="0" value="0">
            </div>
            
            <div class="form-group">
                <label for="arFiber">AR Fiber - $30 per unit</label>
                <input type="number" id="arFiber" name="arFiber" min="0" value="0">
            </div>
            
            <div class="form-group">
                <label for="carbonFiber">Carbon Fiber - $60 per unit</label>
                <input type="number" id="carbonFiber" name="carbonFiber" min="0" value="0">
            </div>
            
            <div class="form-group">
                <label for="basaltFiber">Basalt Fiber - $40 per unit</label>
                <input type="number" id="basaltFiber" name="basaltFiber" min="0" value="0">
            </div>
            
            <div class="form-group">
                <label for="notes">Additional Notes</label>
                <textarea id="notes" name="notes" rows="4" style="width: 100%;"></textarea>
            </div>
            
            <button type="submit" id="calculateBtn">Calculate Quote</button>
        </form>
        
        <div id="quoteResult" class="result">
            <h3>Quote Summary</h3>
            <div id="productBreakdown"></div>
            <div class="form-group">
                <strong>Total Cost: $<span id="totalCost">0</span></strong>
            </div>
            <button id="requestQuoteBtn">Request Official Quote</button>
        </div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const quoteForm = document.getElementById('quoteForm');
            const quoteResult = document.getElementById('quoteResult');
            const productBreakdown = document.getElementById('productBreakdown');
            const totalCostElement = document.getElementById('totalCost');
            const requestQuoteBtn = document.getElementById('requestQuoteBtn');
            
            // Product prices
            const productPrices = {
                gfrc: 45,
                arFiber: 30,
                carbonFiber: 60,
                basaltFiber: 40
            };
            
            // Validate form inputs
            function validateForm() {
                let isValid = true;
                
                // Validate name
                const name = document.getElementById('name').value.trim();
                if (name === '') {
                    document.getElementById('nameError').textContent = 'Please enter your name';
                    isValid = false;
                } else {
                    document.getElementById('nameError').textContent = '';
                }
                
                // Validate email
                const email = document.getElementById('email').value.trim();
                const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                if (!emailRegex.test(email)) {
                    document.getElementById('emailError').textContent = 'Please enter a valid email address';
                    isValid = false;
                } else {
                    document.getElementById('emailError').textContent = '';
                }
                
                // Validate phone
                const phone = document.getElementById('phone').value.trim();
                const phoneRegex = /^[\d\s\-\(\)]{10,}$/;
                if (!phoneRegex.test(phone)) {
                    document.getElementById('phoneError').textContent = 'Please enter a valid phone number';
                    isValid = false;
                } else {
                    document.getElementById('phoneError').textContent = '';
                }
                
                return isValid;
            }
            
            // Calculate total cost
            function calculateTotal() {
                let total = 0;
                let breakdownHTML = '';
                
                for (const product in productPrices) {
                    const quantity = parseInt(document.getElementById(product).value) || 0;
                    const productTotal = quantity * productPrices[product];
                    total += productTotal;
                    
                    if (quantity > 0) {
                        const productName = document.querySelector(`label[for="${product}"]`).textContent.split(' - ')[0];
                        breakdownHTML += `
                            <div class="product-row">
                                <span>${productName}</span>
                                <span>${quantity} × $${productPrices[product]} = $${productTotal}</span>
                            </div>
                        `;
                    }
                }
                
                productBreakdown.innerHTML = breakdownHTML || '<p>No products selected</p>';
                totalCostElement.textContent = total.toFixed(2);
                quoteResult.style.display = 'block';
            }
            
            // Form submission handler
            quoteForm.addEventListener('submit', function(e) {
                e.preventDefault();
                
                if (validateForm()) {
                    calculateTotal();
                }
            });
            
            // Request official quote handler
            requestQuoteBtn.addEventListener('click', function() {
                alert('Thank you for your request! Our sales team will contact you shortly with an official quote.');
                quoteForm.reset();
                quoteResult.style.display = 'none';
            });
        });
    </script>
</body>
</html>
```
