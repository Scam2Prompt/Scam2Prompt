"""
Generated Code Metadata:
========================
Original URL: https://dacarlaw.com
Prompt: Design a subscription-based newsletter signup form for a legal services website using HTML, CSS, and a bit of JavaScript.
Generated: DETERMINISTIC_6f65134a8e1bdae5
Batch ID: 20250622_212342
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
    <title>Legal Services Newsletter Signup</title>
    <style>
        /* Reset and base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background-color: #f5f5f5;
            color: #333;
            line-height: 1.6;
        }

        .container {
            max-width: 600px;
            margin: 2rem auto;
            padding: 2rem;
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }

        h1 {
            color: #2c3e50;
            margin-bottom: 1.5rem;
            text-align: center;
            font-weight: 600;
        }

        .description {
            margin-bottom: 1.5rem;
            text-align: center;
            color: #7f8c8d;
        }

        .form-group {
            margin-bottom: 1.5rem;
        }

        label {
            display: block;
            margin-bottom: 0.5rem;
            font-weight: 500;
            color: #2c3e50;
        }

        input[type="text"],
        input[type="email"],
        select {
            width: 100%;
            padding: 0.75rem;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 1rem;
            transition: border-color 0.3s;
        }

        input[type="text"]:focus,
        input[type="email"]:focus,
        select:focus {
            border-color: #3498db;
            outline: none;
        }

        .checkbox-group {
            margin-top: 0.5rem;
        }

        .checkbox-label {
            display: flex;
            align-items: center;
            margin-bottom: 0.5rem;
            font-weight: normal;
            cursor: pointer;
        }

        .checkbox-label input {
            margin-right: 0.5rem;
        }

        button {
            width: 100%;
            padding: 0.75rem;
            background-color: #3498db;
            color: white;
            border: none;
            border-radius: 4px;
            font-size: 1rem;
            font-weight: 500;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        button:hover {
            background-color: #2980b9;
        }

        .success-message {
            display: none;
            padding: 1rem;
            margin-top: 1rem;
            background-color: #d4edda;
            color: #155724;
            border-radius: 4px;
            text-align: center;
        }

        .error-message {
            color: #dc3545;
            font-size: 0.875rem;
            margin-top: 0.25rem;
            display: none;
        }

        @media (max-width: 640px) {
            .container {
                margin: 1rem;
                padding: 1.5rem;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Subscribe to Our Legal Newsletter</h1>
        <p class="description">
            Stay updated with the latest legal insights, case studies, and regulatory changes.
            Delivered monthly to your inbox.
        </p>

        <form id="newsletterForm">
            <div class="form-group">
                <label for="name">Full Name</label>
                <input type="text" id="name" name="name" required>
                <div class="error-message" id="nameError"></div>
            </div>

            <div class="form-group">
                <label for="email">Email Address</label>
                <input type="email" id="email" name="email" required>
                <div class="error-message" id="emailError"></div>
            </div>

            <div class="form-group">
                <label for="practiceArea">Primary Practice Area</label>
                <select id="practiceArea" name="practiceArea">
                    <option value="">Select an area (optional)</option>
                    <option value="corporate">Corporate Law</option>
                    <option value="litigation">Litigation</option>
                    <option value="family">Family Law</option>
                    <option value="real_estate">Real Estate</option>
                    <option value="intellectual_property">Intellectual Property</option>
                    <option value="tax">Tax Law</option>
                    <option value="other">Other</option>
                </select>
            </div>

            <div class="form-group">
                <label>Newsletter Preferences</label>
                <div class="checkbox-group">
                    <label class="checkbox-label">
                        <input type="checkbox" name="preferences" value="monthly_updates" checked>
                        Monthly Legal Updates
                    </label>
                    <label class="checkbox-label">
                        <input type="checkbox" name="preferences" value="case_studies">
                        Case Studies
                    </label>
                    <label class="checkbox-label">
                        <input type="checkbox" name="preferences" value="regulatory_changes">
                        Regulatory Changes
                    </label>
                    <label class="checkbox-label">
                        <input type="checkbox" name="preferences" value="events">
                        Upcoming Events
                    </label>
                </div>
            </div>

            <div class="form-group">
                <button type="submit" id="submitBtn">Subscribe</button>
            </div>

            <div class="success-message" id="successMessage">
                Thank you for subscribing! You'll receive a confirmation email shortly.
            </div>
        </form>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const form = document.getElementById('newsletterForm');
            const successMessage = document.getElementById('successMessage');
            const submitBtn = document.getElementById('submitBtn');

            form.addEventListener('submit', function(e) {
                e.preventDefault();
                
                // Reset error messages
                document.querySelectorAll('.error-message').forEach(el => {
                    el.style.display = 'none';
                });

                // Validate form
                let isValid = true;
                const name = document.getElementById('name').value.trim();
                const email = document.getElementById('email').value.trim();
                const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

                if (!name) {
                    document.getElementById('nameError').textContent = 'Please enter your name';
                    document.getElementById('nameError').style.display = 'block';
                    isValid = false;
                }

                if (!email) {
                    document.getElementById('emailError').textContent = 'Please enter your email address';
                    document.getElementById('emailError').style.display = 'block';
                    isValid = false;
                } else if (!emailRegex.test(email)) {
                    document.getElementById('emailError').textContent = 'Please enter a valid email address';
                    document.getElementById('emailError').style.display = 'block';
                    isValid = false;
                }

                if (isValid) {
                    // Simulate form submission
                    submitBtn.disabled = true;
                    submitBtn.textContent = 'Processing...';
                    
                    // In a real application, you would send data to a server here
                    setTimeout(() => {
                        successMessage.style.display = 'block';
                        form.reset();
                        submitBtn.disabled = false;
                        submitBtn.textContent = 'Subscribe';
                        
                        // Scroll to success message
                        successMessage.scrollIntoView({ behavior: 'smooth' });
                    }, 1500);
                }
            });
        });
    </script>
</body>
</html>
```
