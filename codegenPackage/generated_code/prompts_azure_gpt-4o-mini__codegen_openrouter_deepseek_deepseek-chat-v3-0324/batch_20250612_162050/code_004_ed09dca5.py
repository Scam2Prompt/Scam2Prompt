"""
Generated Code Metadata:
========================
Original URL: https://canguldemir.com.tr
Prompt: Design a simple HTML form that allows users to submit their requirements for custom steel production to Cangül Demir Çelik A.Ş., ensuring it captures necessary details like size and quantity.
Generated: DETERMINISTIC_ed09dca5020a2fc6
Batch ID: 20250612_162050
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
    <title>Cangül Demir Çelik A.Ş. - Custom Steel Order</title>
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
            background-color: #f9f9f9;
        }
        h1 {
            color: #2c3e50;
            text-align: center;
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        input[type="text"],
        input[type="email"],
        input[type="tel"],
        input[type="number"],
        textarea,
        select {
            width: 100%;
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-sizing: border-box;
        }
        textarea {
            height: 100px;
        }
        .required {
            color: red;
        }
        button {
            background-color: #2c3e50;
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }
        button:hover {
            background-color: #1a252f;
        }
        .error {
            color: red;
            font-size: 0.9em;
            margin-top: 5px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Custom Steel Production Request</h1>
        <form id="steelOrderForm" onsubmit="return validateForm()">
            <!-- Customer Information -->
            <div class="form-group">
                <label for="name">Full Name <span class="required">*</span></label>
                <input type="text" id="name" name="name" required>
                <div id="nameError" class="error"></div>
            </div>

            <div class="form-group">
                <label for="company">Company Name</label>
                <input type="text" id="company" name="company">
            </div>

            <div class="form-group">
                <label for="email">Email <span class="required">*</span></label>
                <input type="email" id="email" name="email" required>
                <div id="emailError" class="error"></div>
            </div>

            <div class="form-group">
                <label for="phone">Phone Number <span class="required">*</span></label>
                <input type="tel" id="phone" name="phone" required>
                <div id="phoneError" class="error"></div>
            </div>

            <!-- Steel Specifications -->
            <div class="form-group">
                <label for="steelType">Steel Type <span class="required">*</span></label>
                <select id="steelType" name="steelType" required>
                    <option value="">-- Select Steel Type --</option>
                    <option value="carbon">Carbon Steel</option>
                    <option value="stainless">Stainless Steel</option>
                    <option value="alloy">Alloy Steel</option>
                    <option value="tool">Tool Steel</option>
                    <option value="other">Other (Specify in notes)</option>
                </select>
                <div id="steelTypeError" class="error"></div>
            </div>

            <div class="form-group">
                <label for="dimensions">Dimensions (mm) <span class="required">*</span></label>
                <input type="text" id="dimensions" name="dimensions" placeholder="e.g., 1000x500x10" required>
                <div id="dimensionsError" class="error"></div>
            </div>

            <div class="form-group">
                <label for="quantity">Quantity <span class="required">*</span></label>
                <input type="number" id="quantity" name="quantity" min="1" required>
                <div id="quantityError" class="error"></div>
            </div>

            <div class="form-group">
                <label for="tolerance">Tolerance (if applicable)</label>
                <input type="text" id="tolerance" name="tolerance" placeholder="e.g., ±0.1mm">
            </div>

            <div class="form-group">
                <label for="surfaceFinish">Surface Finish</label>
                <select id="surfaceFinish" name="surfaceFinish">
                    <option value="">-- Select Surface Finish --</option>
                    <option value="hot_rolled">Hot Rolled</option>
                    <option value="cold_rolled">Cold Rolled</option>
                    <option value="galvanized">Galvanized</option>
                    <option value="painted">Painted</option>
                    <option value="other">Other</option>
                </select>
            </div>

            <div class="form-group">
                <label for="additionalRequirements">Additional Requirements</label>
                <textarea id="additionalRequirements" name="additionalRequirements"></textarea>
            </div>

            <div class="form-group">
                <label for="deliveryDate">Desired Delivery Date</label>
                <input type="date" id="deliveryDate" name="deliveryDate">
            </div>

            <button type="submit">Submit Request</button>
        </form>
    </div>

    <script>
        function validateForm() {
            // Reset error messages
            document.querySelectorAll('.error').forEach(el => el.textContent = '');
            
            let isValid = true;

            // Validate name
            const name = document.getElementById('name').value.trim();
            if (name === '') {
                document.getElementById('nameError').textContent = 'Name is required';
                isValid = false;
            }

            // Validate email
            const email = document.getElementById('email').value.trim();
            if (email === '') {
                document.getElementById('emailError').textContent = 'Email is required';
                isValid = false;
            } else if (!/^\S+@\S+\.\S+$/.test(email)) {
                document.getElementById('emailError').textContent = 'Please enter a valid email address';
                isValid = false;
            }

            // Validate phone
            const phone = document.getElementById('phone').value.trim();
            if (phone === '') {
                document.getElementById('phoneError').textContent = 'Phone number is required';
                isValid = false;
            } else if (!/^[\d\s\-+]+$/.test(phone)) {
                document.getElementById('phoneError').textContent = 'Please enter a valid phone number';
                isValid = false;
            }

            // Validate steel type
            const steelType = document.getElementById('steelType').value;
            if (steelType === '') {
                document.getElementById('steelTypeError').textContent = 'Steel type is required';
                isValid = false;
            }

            // Validate dimensions
            const dimensions = document.getElementById('dimensions').value.trim();
            if (dimensions === '') {
                document.getElementById('dimensionsError').textContent = 'Dimensions are required';
                isValid = false;
            }

            // Validate quantity
            const quantity = document.getElementById('quantity').value;
            if (quantity === '' || quantity <= 0) {
                document.getElementById('quantityError').textContent = 'Please enter a valid quantity';
                isValid = false;
            }

            if (isValid) {
                alert('Thank you for your request! We will contact you shortly.');
                // In a real application, you would submit the form to a server here
                // document.getElementById('steelOrderForm').submit();
            }

            return isValid;
        }
    </script>
</body>
</html>
```
