"""
Generated Code Metadata:
========================
Original URL: https://solie.cn
Prompt: How would you use HTML, CSS, and JavaScript to create a minimalistic webpage that displays "This website is for sale!" along with a short message?
Generated: DETERMINISTIC_d0fe3757024818f7
Batch ID: 20250622_210348
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
    <title>Website For Sale</title>
    <style>
        /* Reset and base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f5f5f5;
            color: #333;
            line-height: 1.6;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 20px;
            text-align: center;
        }
        
        .container {
            max-width: 600px;
            width: 100%;
            background: white;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        h1 {
            font-size: 2.5rem;
            margin-bottom: 20px;
            color: #2c3e50;
        }
        
        p {
            font-size: 1.2rem;
            margin-bottom: 30px;
        }
        
        .contact-btn {
            display: inline-block;
            background: #3498db;
            color: white;
            padding: 12px 24px;
            border-radius: 4px;
            text-decoration: none;
            font-weight: bold;
            transition: background 0.3s ease;
        }
        
        .contact-btn:hover {
            background: #2980b9;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>This Website Is For Sale!</h1>
        <p>This premium domain and website are currently available for purchase. Perfect for your next project or business.</p>
        <a href="mailto:sale@example.com" class="contact-btn">Contact Us</a>
    </div>

    <script>
        // Add any JavaScript functionality here if needed
        document.addEventListener('DOMContentLoaded', function() {
            console.log('Website for sale page loaded');
        });
    </script>
</body>
</html>
```
