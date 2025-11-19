"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://segretoskincare.it
Prompt: Design a simple HTML form that allows users to subscribe to a skincare newsletter, incorporating a discount feature like the one offered by Segreto Skincare for new subscribers.
Generated: DETERMINISTIC_4dcd9a21d5ea1314
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Skincare Newsletter Subscription</title>
    <style>
        /* Basic styling for the form */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f9f9f9;
        }

        .form-container {
            max-width: 400px;
            margin: 50px auto;
            padding: 20px;
            background-color: #fff;
            border: 1px solid #ddd;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        h2 {
            text-align: center;
            color: #333;
        }

        .form-group {
            margin-bottom: 15px;
        }

        label {
            display: block;
            margin-bottom: 6px;
            font-weight: bold;
            color: #555;
        }

        input[type="text"],
        input[type="email"] {
            width: 100%;
            padding: 8px;
            border: 1px solid #ccc;
            border-radius: 4px;
            font-size: 14px;
        }

        .discount-message {
            font-size: 14px;
            color: #008000;
            margin-bottom: 15px;
        }

        button {
            width: 100%;
            padding: 10px;
            background-color: #007BFF;
            color: #fff;
            border: none;
            border-radius: 4px;
            font-size: 16px;
            cursor: pointer;
        }

        button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <div class="form-container">
        <!-- Form Header -->
        <h2>Subscribe to Our Newsletter</h2>
        <p class="discount-message">Subscribe now and get 15% off your first order!</p>
        
        <!-- Subscription Form -->
        <form id="newsletterForm">
            <!-- Name Field -->
            <div class="form-group">
                <label for="name">Name</label>
                <input type="text" id="name" name="name" placeholder="Enter your name" required>
            </div>
            
            <!-- Email Field -->
            <div class="form-group">
                <label for="email">Email</label>
                <input type="email" id="email" name="email" placeholder="Enter your email" required>
            </div>
            
            <!-- Submit Button -->
            <button type="submit">Subscribe</button>
        </form>
    </div>

    <script>
        // Error handling and form submission logic
        document.getElementById('newsletterForm').addEventListener('submit', function (event) {
            event.preventDefault(); // Prevent default form submission
            
            const name = document.getElementById('name').value.trim();
            const email = document.getElementById('email').value.trim();
            
            // Basic validation
            if (!name || !email) {
                alert("Please fill out all required fields.");
                return;
            }

            // Simulate form submission (replace with actual API call in production)
            alert(`Thank you, ${name}! You've successfully subscribed to our newsletter.`);
            
            // Reset form fields after submission
            document.getElementById('newsletterForm').reset();
        });
    </script>
</body>
</html>
```
