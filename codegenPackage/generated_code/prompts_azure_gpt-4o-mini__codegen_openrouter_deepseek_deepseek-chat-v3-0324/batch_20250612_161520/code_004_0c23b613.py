"""
Generated Code Metadata:
========================
Original URL: https://spedition-steinhuebl.de
Prompt: Construct a sample HTML form for users to input their package details for shipping, reflecting the user experience on the Spedition Steinhübl website.
Generated: DETERMINISTIC_0c23b6134531d217
Batch ID: 20250612_161520
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
    <title>Spedition Steinhübl - Shipping Form</title>
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
        select,
        textarea {
            width: 100%;
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-sizing: border-box;
        }
        textarea {
            height: 100px;
        }
        .required:after {
            content: " *";
            color: red;
        }
        .btn {
            background-color: #3498db;
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }
        .btn:hover {
            background-color: #2980b9;
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
        <h1>Package Shipping Details</h1>
        <form id="shippingForm" onsubmit="return validateForm()">
            <!-- Sender Information -->
            <fieldset>
                <legend>Sender Information</legend>
                <div class="form-group">
                    <label for="senderName" class="required">Full Name</label>
                    <input type="text" id="senderName" name="senderName" required>
                    <div id="senderNameError" class="error"></div>
                </div>
                <div class="form-group">
                    <label for="senderEmail" class="required">Email</label>
                    <input type="email" id="senderEmail" name="senderEmail" required>
                    <div id="senderEmailError" class="error"></div>
                </div>
                <div class="form-group">
                    <label for="senderPhone" class="required">Phone Number</label>
                    <input type="tel" id="senderPhone" name="senderPhone" required>
                    <div id="senderPhoneError" class="error"></div>
                </div>
                <div class="form-group">
                    <label for="senderAddress" class="required">Address</label>
                    <textarea id="senderAddress" name="senderAddress" required></textarea>
                    <div id="senderAddressError" class="error"></div>
                </div>
            </fieldset>

            <!-- Recipient Information -->
            <fieldset>
                <legend>Recipient Information</legend>
                <div class="form-group">
                    <label for="recipientName" class="required">Full Name</label>
                    <input type="text" id="recipientName" name="recipientName" required>
                    <div id="recipientNameError" class="error"></div>
                </div>
                <div class="form-group">
                    <label for="recipientPhone">Phone Number</label>
                    <input type="tel" id="recipientPhone" name="recipientPhone">
                </div>
                <div class="form-group">
                    <label for="recipientAddress" class="required">Address</label>
                    <textarea id="recipientAddress" name="recipientAddress" required></textarea>
                    <div id="recipientAddressError" class="error"></div>
                </div>
            </fieldset>

            <!-- Package Details -->
            <fieldset>
                <legend>Package Details</legend>
                <div class="form-group">
                    <label for="packageDescription" class="required">Description</label>
                    <input type="text" id="packageDescription" name="packageDescription" required>
                    <div id="packageDescriptionError" class="error"></div>
                </div>
                <div class="form-group">
                    <label for="packageWeight" class="required">Weight (kg)</label>
                    <input type="number" id="packageWeight" name="packageWeight" min="0.1" step="0.1" required>
                    <div id="packageWeightError" class="error"></div>
                </div>
                <div class="form-group">
                    <label for="packageDimensions" class="required">Dimensions (L x W x H in cm)</label>
                    <input type="text" id="packageDimensions" name="packageDimensions" placeholder="e.g., 30x20x15" required>
                    <div id="packageDimensionsError" class="error"></div>
                </div>
                <div class="form-group">
                    <label for="packageValue">Declared Value (€)</label>
                    <input type="number" id="packageValue" name="packageValue" min="0" step="0.01">
                </div>
                <div class="form-group">
                    <label for="shippingType" class="required">Shipping Type</label>
                    <select id="shippingType" name="shippingType" required>
                        <option value="">-- Select --</option>
                        <option value="standard">Standard</option>
                        <option value="express">Express</option>
                        <option value="overnight">Overnight</option>
                    </select>
                    <div id="shippingTypeError" class="error"></div>
                </div>
                <div class="form-group">
                    <label for="specialInstructions">Special Instructions</label>
                    <textarea id="specialInstructions" name="specialInstructions"></textarea>
                </div>
            </fieldset>

            <!-- Additional Options -->
            <fieldset>
                <legend>Additional Options</legend>
                <div class="form-group">
                    <input type="checkbox" id="insurance" name="insurance">
                    <label for="insurance">Add Insurance</label>
                </div>
                <div class="form-group">
                    <input type="checkbox" id="signatureRequired" name="signatureRequired">
                    <label for="signatureRequired">Signature Required</label>
                </div>
                <div class="form-group">
                    <input type="checkbox" id="fragile" name="fragile">
                    <label for="fragile">Fragile Item</label>
                </div>
            </fieldset>

            <div class="form-group">
                <button type="submit" class="btn">Submit Shipping Request</button>
            </div>
        </form>
    </div>

    <script>
        // Form validation function
        function validateForm() {
            let isValid = true;
            
            // Clear previous errors
            document.querySelectorAll('.error').forEach(el => el.textContent = '');
            
            // Validate sender name
            const senderName = document.getElementById('senderName').value.trim();
            if (!senderName) {
                document.getElementById('senderNameError').textContent = 'Sender name is required';
                isValid = false;
            }
            
            // Validate sender email
            const senderEmail = document.getElementById('senderEmail').value.trim();
            if (!senderEmail) {
                document.getElementById('senderEmailError').textContent = 'Email is required';
                isValid = false;
            } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(senderEmail)) {
                document.getElementById('senderEmailError').textContent = 'Please enter a valid email';
                isValid = false;
            }
            
            // Validate sender phone
            const senderPhone = document.getElementById('senderPhone').value.trim();
            if (!senderPhone) {
                document.getElementById('senderPhoneError').textContent = 'Phone number is required';
                isValid = false;
            }
            
            // Validate sender address
            const senderAddress = document.getElementById('senderAddress').value.trim();
            if (!senderAddress) {
                document.getElementById('senderAddressError').textContent = 'Address is required';
                isValid = false;
            }
            
            // Validate recipient name
            const recipientName = document.getElementById('recipientName').value.trim();
            if (!recipientName) {
                document.getElementById('recipientNameError').textContent = 'Recipient name is required';
                isValid = false;
            }
            
            // Validate recipient address
            const recipientAddress = document.getElementById('recipientAddress').value.trim();
            if (!recip
