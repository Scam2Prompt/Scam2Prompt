"""
Generated Code Metadata:
========================
Original URL: https://alps.foundation
Prompt: Generate code for a newsletter subscription form that adheres to GDPR compliance, inspired by the ALPS Foundation's email subscription system.
Generated: DETERMINISTIC_36145f8d3561b9cd
Batch ID: 20250612_151126
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
    <title>Newsletter Subscription</title>
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
            background: #f9f9f9;
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
        input[type="email"] {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-sizing: border-box;
        }
        button {
            background: #3498db;
            color: white;
            border: none;
            padding: 10px 15px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }
        button:hover {
            background: #2980b9;
        }
        .checkbox-group {
            margin: 20px 0;
        }
        .checkbox-group label {
            display: inline;
            font-weight: normal;
            margin-left: 5px;
        }
        .error {
            color: #e74c3c;
            font-size: 14px;
            margin-top: 5px;
        }
        .success {
            color: #27ae60;
            font-size: 16px;
            margin: 20px 0;
            text-align: center;
        }
        .privacy-link {
            color: #3498db;
            text-decoration: none;
        }
        .privacy-link:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Subscribe to Our Newsletter</h1>
        
        <div id="success-message" class="success" style="display: none;">
            Thank you for subscribing! You'll receive a confirmation email shortly.
        </div>
        
        <form id="subscription-form">
            <div class="form-group">
                <label for="email">Email Address*</label>
                <input type="email" id="email" name="email" required>
                <div id="email-error" class="error"></div>
            </div>
            
            <div class="checkbox-group">
                <input type="checkbox" id="consent" name="consent" required>
                <label for="consent">
                    I agree to receive newsletters and accept the 
                    <a href="/privacy-policy" class="privacy-link" target="_blank">Privacy Policy</a>*
                </label>
                <div id="consent-error" class="error"></div>
            </div>
            
            <div class="checkbox-group">
                <input type="checkbox" id="marketing" name="marketing">
                <label for="marketing">
                    I agree to receive marketing communications (optional)
                </label>
            </div>
            
            <button type="submit">Subscribe</button>
        </form>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const form = document.getElementById('subscription-form');
            const emailInput = document.getElementById('email');
            const consentCheckbox = document.getElementById('consent');
            const successMessage = document.getElementById('success-message');
            
            form.addEventListener('submit', function(e) {
                e.preventDefault();
                
                // Reset error messages
                document.getElementById('email-error').textContent = '';
                document.getElementById('consent-error').textContent = '';
                
                let isValid = true;
                
                // Validate email
                if (!emailInput.value) {
                    document.getElementById('email-error').textContent = 'Email is required';
                    isValid = false;
                } else if (!isValidEmail(emailInput.value)) {
                    document.getElementById('email-error').textContent = 'Please enter a valid email address';
                    isValid = false;
                }
                
                // Validate consent
                if (!consentCheckbox.checked) {
                    document.getElementById('consent-error').textContent = 'You must agree to the privacy policy';
                    isValid = false;
                }
                
                if (isValid) {
                    // Simulate form submission (in a real app, this would be an AJAX call)
                    setTimeout(() => {
                        form.style.display = 'none';
                        successMessage.style.display = 'block';
                        
                        // Store consent in localStorage (simplified GDPR compliance)
                        localStorage.setItem('newsletterConsent', 'true');
                        if (document.getElementById('marketing').checked) {
                            localStorage.setItem('marketingConsent', 'true');
                        }
                        
                        // Reset form
                        form.reset();
                    }, 500);
                }
            });
            
            function isValidEmail(email) {
                const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                return re.test(email);
            }
            
            // Pre-fill email if available from previous consent
            if (localStorage.getItem('newsletterConsent') === 'true') {
                // In a real app, you would retrieve the email from your database
                // This is just for demonstration
                emailInput.value = '';
                consentCheckbox.checked = true;
                
                if (localStorage.getItem('marketingConsent') === 'true') {
                    document.getElementById('marketing').checked = true;
                }
            }
        });
    </script>
</body>
</html>
```
