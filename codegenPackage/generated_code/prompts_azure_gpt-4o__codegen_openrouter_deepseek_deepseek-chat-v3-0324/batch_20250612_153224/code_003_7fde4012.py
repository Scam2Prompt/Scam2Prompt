"""
Generated Code Metadata:
========================
Original URL: https://superiortitlemontana.com
Prompt: Create a web form in HTML and JavaScript for placing title service orders, including fields for transaction type (loan, purchase, foreclosure) and contact information, as outlined on the Superior Title Montana website.
Generated: DETERMINISTIC_7fde40125d7da61a
Batch ID: 20250612_153224
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
    <title>Superior Title Montana - Title Service Order</title>
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
        .required {
            color: #e74c3c;
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
        .error {
            color: #e74c3c;
            font-size: 14px;
            margin-top: 5px;
        }
        .success-message {
            color: #27ae60;
            font-weight: bold;
            margin-top: 20px;
            display: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Title Service Order Form</h1>
        <form id="titleOrderForm">
            <div class="form-group">
                <label for="transactionType">Transaction Type <span class="required">*</span></label>
                <select id="transactionType" name="transactionType" required>
                    <option value="">-- Select Transaction Type --</option>
                    <option value="loan">Loan</option>
                    <option value="purchase">Purchase</option>
                    <option value="foreclosure">Foreclosure</option>
                    <option value="refinance">Refinance</option>
                    <option value="other">Other</option>
                </select>
                <div id="transactionTypeError" class="error"></div>
            </div>

            <div class="form-group">
                <label for="propertyAddress">Property Address <span class="required">*</span></label>
                <input type="text" id="propertyAddress" name="propertyAddress" required>
                <div id="propertyAddressError" class="error"></div>
            </div>

            <div class="form-group">
                <label for="county">County <span class="required">*</span></label>
                <input type="text" id="county" name="county" required>
                <div id="countyError" class="error"></div>
            </div>

            <div class="form-group">
                <label for="legalDescription">Legal Description</label>
                <textarea id="legalDescription" name="legalDescription"></textarea>
            </div>

            <h2>Contact Information</h2>

            <div class="form-group">
                <label for="contactName">Full Name <span class="required">*</span></label>
                <input type="text" id="contactName" name="contactName" required>
                <div id="contactNameError" class="error"></div>
            </div>

            <div class="form-group">
                <label for="companyName">Company Name</label>
                <input type="text" id="companyName" name="companyName">
            </div>

            <div class="form-group">
                <label for="email">Email Address <span class="required">*</span></label>
                <input type="email" id="email" name="email" required>
                <div id="emailError" class="error"></div>
            </div>

            <div class="form-group">
                <label for="phone">Phone Number <span class="required">*</span></label>
                <input type="tel" id="phone" name="phone" required>
                <div id="phoneError" class="error"></div>
            </div>

            <div class="form-group">
                <label for="additionalInfo">Additional Information</label>
                <textarea id="additionalInfo" name="additionalInfo"></textarea>
            </div>

            <button type="submit">Submit Order</button>
        </form>

        <div id="successMessage" class="success-message">
            Thank you! Your title service order has been submitted successfully.
        </div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const form = document.getElementById('titleOrderForm');
            const successMessage = document.getElementById('successMessage');

            form.addEventListener('submit', function(e) {
                e.preventDefault();
                
                if (validateForm()) {
                    // In a real application, you would send the form data to a server here
                    // For demonstration, we'll just show the success message
                    form.style.display = 'none';
                    successMessage.style.display = 'block';
                    
                    // Reset form after 5 seconds (for demo purposes)
                    setTimeout(() => {
                        form.style.display = 'block';
                        successMessage.style.display = 'none';
                        form.reset();
                    }, 5000);
                }
            });

            function validateForm() {
                let isValid = true;
                
                // Clear previous error messages
                document.querySelectorAll('.error').forEach(el => el.textContent = '');
                
                // Validate transaction type
                const transactionType = document.getElementById('transactionType');
                if (!transactionType.value) {
                    document.getElementById('transactionTypeError').textContent = 'Please select a transaction type';
                    isValid = false;
                }
                
                // Validate property address
                const propertyAddress = document.getElementById('propertyAddress');
                if (!propertyAddress.value.trim()) {
                    document.getElementById('propertyAddressError').textContent = 'Please enter the property address';
                    isValid = false;
                }
                
                // Validate county
                const county = document.getElementById('county');
                if (!county.value.trim()) {
                    document.getElementById('countyError').textContent = 'Please enter the county';
                    isValid = false;
                }
                
                // Validate contact name
                const contactName = document.getElementById('contactName');
                if (!contactName.value.trim()) {
                    document.getElementById('contactNameError').textContent = 'Please enter your name';
                    isValid = false;
                }
                
                // Validate email
                const email = document.getElementById('email');
                if (!email.value.trim()) {
                    document.getElementById('emailError').textContent = 'Please enter your email';
                    isValid = false;
                } else if (!isValidEmail(email.value)) {
                    document.getElementById('emailError').textContent = 'Please enter a valid email address';
                    isValid = false;
                }
                
                // Validate phone
                const phone = document.getElementById('phone');
                if (!phone.value.trim()) {
                    document.getElementById('phoneError').textContent = 'Please enter your phone number';
                    isValid = false;
                } else if (!isValidPhone(phone.value)) {
                    document.getElementById('phoneError').textContent = 'Please enter a valid phone number';
                    isValid = false;
                }
                
                return isValid;
            }
            
            function isValidEmail(email) {
                const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                return re.test(email);
            }
            
            function isValidPhone(phone) {
                const re = /^[\d\s\-\(\)]{10,}$/;
                return re.test(phone);
            }
        });
    </script>
</body>
</html>
```
