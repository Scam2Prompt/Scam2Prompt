"""
Generated Code Metadata:
========================
Original URL: https://superiortitlemontana.com
Prompt: Create a web form using HTML and JavaScript that allows users to request a free consultation and price estimate for title insurance services, similar to the one provided on Superior Title Montana's website.
Generated: DETERMINISTIC_7803488aad2d092d
Batch ID: 20250622_210655
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
    <title>Title Insurance Consultation Request</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            color: #333;
            background-color: #f9f9f9;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background: #fff;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #2c3e50;
            text-align: center;
            margin-bottom: 30px;
        }
        .form-group {
            margin-bottom: 20px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        input[type="text"],
        input[type="email"],
        input[type="tel"],
        select,
        textarea {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 16px;
        }
        textarea {
            height: 120px;
        }
        .required {
            color: #e74c3c;
        }
        button {
            background: #3498db;
            color: white;
            border: none;
            padding: 12px 20px;
            font-size: 16px;
            cursor: pointer;
            border-radius: 4px;
            width: 100%;
            transition: background 0.3s;
        }
        button:hover {
            background: #2980b9;
        }
        .error {
            color: #e74c3c;
            font-size: 14px;
            margin-top: 5px;
        }
        .success-message {
            display: none;
            background: #2ecc71;
            color: white;
            padding: 20px;
            border-radius: 4px;
            text-align: center;
            margin-bottom: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Free Title Insurance Consultation</h1>
        
        <div id="successMessage" class="success-message">
            Thank you for your request! We'll contact you shortly with your consultation and price estimate.
        </div>
        
        <form id="consultationForm">
            <div class="form-group">
                <label for="firstName">First Name <span class="required">*</span></label>
                <input type="text" id="firstName" name="firstName" required>
                <div id="firstNameError" class="error"></div>
            </div>
            
            <div class="form-group">
                <label for="lastName">Last Name <span class="required">*</span></label>
                <input type="text" id="lastName" name="lastName" required>
                <div id="lastNameError" class="error"></div>
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
            
            <div class="form-group">
                <label for="propertyType">Property Type <span class="required">*</span></label>
                <select id="propertyType" name="propertyType" required>
                    <option value="">Select Property Type</option>
                    <option value="single-family">Single Family Home</option>
                    <option value="condo">Condo</option>
                    <option value="multi-family">Multi-Family</option>
                    <option value="commercial">Commercial</option>
                    <option value="land">Land</option>
                </select>
                <div id="propertyTypeError" class="error"></div>
            </div>
            
            <div class="form-group">
                <label for="propertyAddress">Property Address <span class="required">*</span></label>
                <textarea id="propertyAddress" name="propertyAddress" required></textarea>
                <div id="propertyAddressError" class="error"></div>
            </div>
            
            <div class="form-group">
                <label for="purchasePrice">Estimated Purchase Price ($) <span class="required">*</span></label>
                <input type="text" id="purchasePrice" name="purchasePrice" required>
                <div id="purchasePriceError" class="error"></div>
            </div>
            
            <div class="form-group">
                <label for="loanAmount">Loan Amount (if applicable)</label>
                <input type="text" id="loanAmount" name="loanAmount">
            </div>
            
            <div class="form-group">
                <label for="closingDate">Estimated Closing Date</label>
                <input type="text" id="closingDate" name="closingDate" placeholder="MM/DD/YYYY">
            </div>
            
            <div class="form-group">
                <label for="additionalInfo">Additional Information</label>
                <textarea id="additionalInfo" name="additionalInfo"></textarea>
            </div>
            
            <button type="submit">Request Free Consultation</button>
        </form>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const form = document.getElementById('consultationForm');
            const successMessage = document.getElementById('successMessage');
            
            form.addEventListener('submit', function(e) {
                e.preventDefault();
                
                if (validateForm()) {
                    // In a real application, you would send the form data to a server here
                    // For demonstration, we'll just show the success message
                    form.reset();
                    form.style.display = 'none';
                    successMessage.style.display = 'block';
                    
                    // Scroll to success message
                    successMessage.scrollIntoView({ behavior: 'smooth' });
                }
            });
            
            function validateForm() {
                let isValid = true;
                
                // Clear previous errors
                const errorElements = document.querySelectorAll('.error');
                errorElements.forEach(el => el.textContent = '');
                
                // Validate required fields
                const requiredFields = [
                    'firstName', 'lastName', 'email', 'phone', 
                    'propertyType', 'propertyAddress', 'purchasePrice'
                ];
                
                requiredFields.forEach(fieldId => {
                    const field = document.getElementById(fieldId);
                    if (!field.value.trim()) {
                        document.getElementById(`${fieldId}Error`).textContent = 'This field is required';
                        isValid = false;
                    }
                });
                
                // Validate email format
                const email = document.getElementById('email');
                if (email.value && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value)) {
                    document.getElementById('emailError').textContent = 'Please enter a valid email address';
                    isValid = false;
                }
                
                // Validate phone format
                const phone = document.getElementById('phone');
                if (phone.value && !/^\d{10,}$/.test(phone.value.replace(/\D/g, ''))) {
                    document.getElementById('phoneError').textContent = 'Please enter a valid phone number';
                    isValid = false;
                }
                
                // Validate purchase price is numeric
                const purchasePrice = document.getElementById('purchasePrice');
                if (purchasePrice.value && !/^\d+$/.test(purchasePrice.value.replace(/[$,]/g, ''))) {
                    document.getElementById('purchasePriceError').textContent = 'Please enter a valid amount';
                    isValid = false;
                }
                
                // Validate loan amount is numeric if provided
                const loanAmount = document.getElementById('loanAmount');
                if (loanAmount.value && !/^\d+$/.test(loanAmount.value.replace(/[$,]/g, ''))) {
                    document.getElementById('loanAmountError').textContent = 'Please enter a valid amount';
                    isValid = false;
                }
                
                return isValid;
            }
            
            // Format phone number as user types
            const phoneInput = document.getElementById('phone');
            phoneInput.addEventListener('input', function(e) {
                const x = e.target.value.replace(/\D/g, '').match(/(\d{0,3})(\d{0,3})(\d{0,4})/);
                e.target.value = !x[2] ? x[1] : '(' + x[1] + ') ' + x[2] +
