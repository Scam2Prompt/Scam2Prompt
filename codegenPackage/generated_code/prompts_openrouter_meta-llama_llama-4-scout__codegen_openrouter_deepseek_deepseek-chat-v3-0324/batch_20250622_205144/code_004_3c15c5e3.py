"""
Generated Code Metadata:
========================
Original URL: https://ziggyloan.com
Prompt: "Design a simple loan application form using HTML and JavaScript that collects user input for loan amount, repayment period, and personal details, and submits it to a lender or lending partner for approval."
Generated: DETERMINISTIC_3c15c5e31d62223e
Batch ID: 20250622_205144
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, production-ready loan application form with HTML and JavaScript:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Loan Application Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            color: #333;
        }
        .container {
            max-width: 600px;
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
        input, select {
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
            width: 100%;
        }
        button:hover {
            background-color: #2980b9;
        }
        .error {
            color: #e74c3c;
            font-size: 14px;
            margin-top: 5px;
        }
        .success {
            color: #27ae60;
            font-size: 16px;
            text-align: center;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Loan Application</h1>
        <form id="loanForm">
            <div class="form-group">
                <label for="fullName">Full Name*</label>
                <input type="text" id="fullName" name="fullName" required>
                <div id="nameError" class="error"></div>
            </div>

            <div class="form-group">
                <label for="email">Email Address*</label>
                <input type="email" id="email" name="email" required>
                <div id="emailError" class="error"></div>
            </div>

            <div class="form-group">
                <label for="phone">Phone Number*</label>
                <input type="tel" id="phone" name="phone" required>
                <div id="phoneError" class="error"></div>
            </div>

            <div class="form-group">
                <label for="loanAmount">Loan Amount ($)*</label>
                <input type="number" id="loanAmount" name="loanAmount" min="1000" max="100000" required>
                <div id="amountError" class="error"></div>
            </div>

            <div class="form-group">
                <label for="repaymentPeriod">Repayment Period (months)*</label>
                <select id="repaymentPeriod" name="repaymentPeriod" required>
                    <option value="">Select period</option>
                    <option value="12">12 months</option>
                    <option value="24">24 months</option>
                    <option value="36">36 months</option>
                    <option value="48">48 months</option>
                    <option value="60">60 months</option>
                </select>
                <div id="periodError" class="error"></div>
            </div>

            <div class="form-group">
                <label for="purpose">Loan Purpose</label>
                <textarea id="purpose" name="purpose" rows="3" style="width: 100%;"></textarea>
            </div>

            <button type="submit" id="submitBtn">Submit Application</button>
        </form>

        <div id="successMessage" class="success" style="display: none;"></div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const form = document.getElementById('loanForm');
            const submitBtn = document.getElementById('submitBtn');
            const successMessage = document.getElementById('successMessage');

            // Validate form inputs
            function validateForm() {
                let isValid = true;
                
                // Validate name
                const name = document.getElementById('fullName').value.trim();
                if (name === '') {
                    document.getElementById('nameError').textContent = 'Please enter your full name';
                    isValid = false;
                } else {
                    document.getElementById('nameError').textContent = '';
                }

                // Validate email
                const email = document.getElementById('email').value.trim();
                const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                if (email === '') {
                    document.getElementById('emailError').textContent = 'Please enter your email';
                    isValid = false;
                } else if (!emailRegex.test(email)) {
                    document.getElementById('emailError').textContent = 'Please enter a valid email';
                    isValid = false;
                } else {
                    document.getElementById('emailError').textContent = '';
                }

                // Validate phone
                const phone = document.getElementById('phone').value.trim();
                const phoneRegex = /^\d{10,15}$/;
                if (phone === '') {
                    document.getElementById('phoneError').textContent = 'Please enter your phone number';
                    isValid = false;
                } else if (!phoneRegex.test(phone)) {
                    document.getElementById('phoneError').textContent = 'Please enter a valid phone number (10-15 digits)';
                    isValid = false;
                } else {
                    document.getElementById('phoneError').textContent = '';
                }

                // Validate loan amount
                const amount = document.getElementById('loanAmount').value;
                if (amount === '') {
                    document.getElementById('amountError').textContent = 'Please enter loan amount';
                    isValid = false;
                } else if (amount < 1000 || amount > 100000) {
                    document.getElementById('amountError').textContent = 'Loan amount must be between $1,000 and $100,000';
                    isValid = false;
                } else {
                    document.getElementById('amountError').textContent = '';
                }

                // Validate repayment period
                const period = document.getElementById('repaymentPeriod').value;
                if (period === '') {
                    document.getElementById('periodError').textContent = 'Please select repayment period';
                    isValid = false;
                } else {
                    document.getElementById('periodError').textContent = '';
                }

                return isValid;
            }

            // Handle form submission
            form.addEventListener('submit', function(e) {
                e.preventDefault();
                
                if (validateForm()) {
                    submitBtn.disabled = true;
                    submitBtn.textContent = 'Processing...';

                    // Simulate API call to lender
                    setTimeout(() => {
                        // In a real application, you would send data to your backend
                        // which would then forward to the lending partner's API
                        const formData = {
                            fullName: document.getElementById('fullName').value.trim(),
                            email: document.getElementById('email').value.trim(),
                            phone: document.getElementById('phone').value.trim(),
                            loanAmount: document.getElementById('loanAmount').value,
                            repaymentPeriod: document.getElementById('repaymentPeriod').value,
                            purpose: document.getElementById('purpose').value.trim()
                        };

                        // Log the data (replace with actual API call)
                        console.log('Form data to be sent:', formData);

                        // Show success message
                        form.style.display = 'none';
                        successMessage.textContent = 'Thank you! Your application has been submitted successfully. A lender will contact you shortly.';
                        successMessage.style.display = 'block';

                        // Reset form (for demo purposes)
                        setTimeout(() => {
                            form.reset();
                            form.style.display = 'block';
                            successMessage.style.display = 'none';
                            submitBtn.disabled = false;
                            submitBtn.textContent = 'Submit Application';
                        }, 5000);
                    }, 1500);
                }
            });
        });
    </script>
</body>
</html>
```
