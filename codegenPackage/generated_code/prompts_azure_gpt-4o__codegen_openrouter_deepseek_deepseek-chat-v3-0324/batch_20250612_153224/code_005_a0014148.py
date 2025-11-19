"""
Generated Code Metadata:
========================
Original URL: https://digistrategy.in
Prompt: Write HTML and CSS code for a "Get A Quote" form, like the one featured on digistrategy.in, with a modern and professional design.
Generated: DETERMINISTIC_a001414804152df2
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
    <title>Get A Quote</title>
    <style>
        /* Reset and base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background-color: #f8f9fa;
            color: #333;
            line-height: 1.6;
        }

        /* Form container */
        .quote-container {
            max-width: 600px;
            margin: 40px auto;
            padding: 30px;
            background: white;
            border-radius: 8px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        }

        .quote-container h2 {
            text-align: center;
            margin-bottom: 25px;
            color: #2c3e50;
            font-size: 28px;
        }

        /* Form elements */
        .form-group {
            margin-bottom: 20px;
        }

        .form-group label {
            display: block;
            margin-bottom: 8px;
            font-weight: 600;
            color: #2c3e50;
        }

        .form-control {
            width: 100%;
            padding: 12px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 16px;
            transition: border-color 0.3s;
        }

        .form-control:focus {
            outline: none;
            border-color: #3498db;
        }

        textarea.form-control {
            min-height: 120px;
            resize: vertical;
        }

        /* Submit button */
        .submit-btn {
            display: block;
            width: 100%;
            padding: 14px;
            background-color: #3498db;
            color: white;
            border: none;
            border-radius: 4px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        .submit-btn:hover {
            background-color: #2980b9;
        }

        /* Responsive adjustments */
        @media (max-width: 768px) {
            .quote-container {
                margin: 20px;
                padding: 20px;
            }
        }
    </style>
</head>
<body>
    <div class="quote-container">
        <h2>Get A Quote</h2>
        <form id="quoteForm">
            <div class="form-group">
                <label for="name">Full Name</label>
                <input type="text" id="name" class="form-control" required>
            </div>
            
            <div class="form-group">
                <label for="email">Email Address</label>
                <input type="email" id="email" class="form-control" required>
            </div>
            
            <div class="form-group">
                <label for="phone">Phone Number</label>
                <input type="tel" id="phone" class="form-control" required>
            </div>
            
            <div class="form-group">
                <label for="service">Service Interested In</label>
                <select id="service" class="form-control" required>
                    <option value="" disabled selected>Select a service</option>
                    <option value="web-development">Web Development</option>
                    <option value="mobile-app">Mobile App Development</option>
                    <option value="digital-marketing">Digital Marketing</option>
                    <option value="seo">SEO Services</option>
                    <option value="consulting">Business Consulting</option>
                </select>
            </div>
            
            <div class="form-group">
                <label for="message">Project Details</label>
                <textarea id="message" class="form-control" placeholder="Tell us about your project..." required></textarea>
            </div>
            
            <button type="submit" class="submit-btn">Submit Request</button>
        </form>
    </div>

    <script>
        document.getElementById('quoteForm').addEventListener('submit', function(e) {
            e.preventDefault();
            // Form validation and submission logic would go here
            alert('Thank you for your request! We will contact you shortly.');
            this.reset();
        });
    </script>
</body>
</html>
```
