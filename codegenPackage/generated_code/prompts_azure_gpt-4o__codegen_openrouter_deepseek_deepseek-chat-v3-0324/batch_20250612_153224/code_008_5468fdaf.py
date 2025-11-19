"""
Generated Code Metadata:
========================
Original URL: https://www.navkarfurniture.com
Prompt: Generate code to integrate a newsletter subscription form into a furniture retailer's website, allowing users to receive updates about special offers, similar to Navkar Furniture's "Join Our Newsletter" feature.
Generated: DETERMINISTIC_5468fdafa565356e
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
    <title>Furniture Store - Newsletter</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        
        .newsletter-container {
            background-color: #f9f9f9;
            border: 1px solid #ddd;
            border-radius: 5px;
            padding: 30px;
            margin: 20px 0;
            text-align: center;
        }
        
        .newsletter-title {
            font-size: 24px;
            margin-bottom: 15px;
            color: #2c3e50;
        }
        
        .newsletter-description {
            margin-bottom: 20px;
            color: #7f8c8d;
        }
        
        .newsletter-form {
            display: flex;
            flex-direction: column;
            max-width: 500px;
            margin: 0 auto;
        }
        
        .form-group {
            margin-bottom: 15px;
            text-align: left;
        }
        
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        
        input[type="text"],
        input[type="email"] {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 16px;
        }
        
        .checkbox-group {
            display: flex;
            align-items: center;
            margin-bottom: 15px;
        }
        
        input[type="checkbox"] {
            margin-right: 10px;
        }
        
        button {
            background-color: #3498db;
            color: white;
            border: none;
            padding: 12px 20px;
            font-size: 16px;
            border-radius: 4px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        
        button:hover {
            background-color: #2980b9;
        }
        
        .success-message {
            color: #27ae60;
            margin-top: 15px;
            display: none;
        }
        
        .error-message {
            color: #e74c3c;
            margin-top: 15px;
            display: none;
        }
    </style>
</head>
<body>
    <div class="newsletter-container">
        <h2 class="newsletter-title">Join Our Newsletter</h2>
        <p class="newsletter-description">
            Subscribe to receive updates on new arrivals, special offers, and furniture trends.
        </p>
        
        <form id="newsletterForm" class="newsletter-form" novalidate>
            <div class="form-group">
                <label for="name">Name</label>
                <input type="text" id="name" name="name" placeholder="Your name" required>
            </div>
            
            <div class="form-group">
                <label for="email">Email Address</label>
                <input type="email" id="email" name="email" placeholder="Your email address" required>
            </div>
            
            <div class="checkbox-group">
                <input type="checkbox" id="consent" name="consent" required>
                <label for="consent">I agree to receive marketing emails from Furniture Store</label>
            </div>
            
            <button type="submit">Subscribe</button>
            
            <div id="successMessage" class="success-message">
                Thank you for subscribing! You'll receive our next newsletter.
            </div>
            
            <div id="errorMessage" class="error-message">
                There was an error processing your subscription. Please try again.
            </div>
        </form>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const form = document.getElementById('newsletterForm');
            const successMessage = document.getElementById('successMessage');
            const errorMessage = document.getElementById('errorMessage');
            
            form.addEventListener('submit', function(e) {
                e.preventDefault();
                
                // Hide previous messages
                successMessage.style.display = 'none';
                errorMessage.style.display = 'none';
                
                // Validate form
                if (!form.checkValidity()) {
                    form.reportValidity();
                    return;
                }
                
                // Get form data
                const formData = new FormData(form);
                const data = {
                    name: formData.get('name'),
                    email: formData.get('email'),
                    consent: formData.get('consent') === 'on'
                };
                
                // Simulate API call (replace with actual API call in production)
                simulateApiCall(data)
                    .then(response => {
                        if (response.success) {
                            successMessage.style.display = 'block';
                            form.reset();
                        } else {
                            errorMessage.style.display = 'block';
                        }
                    })
                    .catch(error => {
                        console.error('Error:', error);
                        errorMessage.style.display = 'block';
                    });
            });
            
            // Simulate API call function (replace with actual fetch/axios call)
            function simulateApiCall(data) {
                return new Promise((resolve) => {
                    setTimeout(() => {
                        // Simulate random success/failure for demo
                        const success = Math.random() > 0.2;
                        resolve({ success });
                    }, 1000);
                });
            }
        });
    </script>
</body>
</html>
```
