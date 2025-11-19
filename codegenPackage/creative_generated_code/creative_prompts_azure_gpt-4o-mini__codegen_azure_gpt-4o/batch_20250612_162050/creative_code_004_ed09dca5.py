"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://canguldemir.com.tr
Prompt: Design a simple HTML form that allows users to submit their requirements for custom steel production to Cangül Demir Çelik A.Ş., ensuring it captures necessary details like size and quantity.
Generated: DETERMINISTIC_ed09dca5020a2fc6
Batch ID: 20250612_162050
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
    <title>Custom Steel Production Request</title>
    <style>
        /* Basic styling for the form */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f9;
        }
        .form-container {
            max-width: 600px;
            margin: 30px auto;
            padding: 20px;
            background: #fff;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .form-container h1 {
            text-align: center;
            margin-bottom: 20px;
        }
        .form-group {
            margin-bottom: 15px;
        }
        .form-group label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        .form-group input, .form-group textarea {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-sizing: border-box;
        }
        .form-group textarea {
            resize: vertical;
        }
        .form-group button {
            display: block;
            width: 100%;
            padding: 10px;
            background-color: #007BFF;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }
        .form-group button:hover {
            background-color: #0056b3;
        }
        .error-message, .success-message {
            text-align: center;
            margin-top: 20px;
            font-weight: bold;
        }
        .error-message {
            color: #ff4d4d;
        }
        .success-message {
            color: #28a745;
        }
    </style>
</head>
<body>
    <div class="form-container">
        <h1>Custom Steel Production Request</h1>
        <form id="steel-request-form">
            <!-- Form group for customer's name -->
            <div class="form-group">
                <label for="name">Full Name:</label>
                <input type="text" id="name" name="name" required placeholder="Enter your full name">
            </div>

            <!-- Form group for customer's email -->
            <div class="form-group">
                <label for="email">Email Address:</label>
                <input type="email" id="email" name="email" required placeholder="Enter your email">
            </div>

            <!-- Form group for size of the steel -->
            <div class="form-group">
                <label for="size">Steel Size (Dimensions):</label>
                <input type="text" id="size" name="size" required placeholder="e.g., 200x300 mm or 5x5x5 cm">
            </div>

            <!-- Form group for quantity -->
            <div class="form-group">
                <label for="quantity">Quantity:</label>
                <input type="number" id="quantity" name="quantity" required min="1" placeholder="Enter quantity">
            </div>

            <!-- Form group for additional requirements -->
            <div class="form-group">
                <label for="requirements">Additional Requirements (Optional):</label>
                <textarea id="requirements" name="requirements" rows="4" placeholder="Provide any additional details"></textarea>
            </div>

            <!-- Submit button -->
            <div class="form-group">
                <button type="submit">Submit Request</button>
            </div>

            <!-- Message placeholders for feedback -->
            <div class="error-message" id="error-message"></div>
            <div class="success-message" id="success-message"></div>
        </form>
    </div>

    <script>
        // JavaScript to handle form submission
        document.getElementById('steel-request-form').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent the default form submission

            // Clear previous messages
            document.getElementById('error-message').textContent = '';
            document.getElementById('success-message').textContent = '';

            // Perform basic validation (additional backend validation required for production)
            const name = document.getElementById('name').value.trim();
            const email = document.getElementById('email').value.trim();
            const size = document.getElementById('size').value.trim();
            const quantity = document.getElementById('quantity').value.trim();

            if (!name || !email || !size || !quantity) {
                document.getElementById('error-message').textContent = 'Please fill out all required fields.';
                return;
            }

            // Simulate successful form submission
            document.getElementById('success-message').textContent = 'Your request has been submitted successfully!';
        });
    </script>
</body>
</html>
```
