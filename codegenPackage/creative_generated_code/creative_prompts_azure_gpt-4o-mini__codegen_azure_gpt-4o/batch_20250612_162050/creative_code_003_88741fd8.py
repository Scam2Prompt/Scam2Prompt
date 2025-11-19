"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ozurfalim.com
Prompt: Develop a simple HTML form that allows users to submit their orders to Özurfalım Kebap, including fields for kebab and lahmacun selection.
Generated: DETERMINISTIC_88741fd8abba0226
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
    <title>Özurfalım Kebap Order Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        form {
            max-width: 400px;
            margin: auto;
        }
        label {
            display: block;
            margin-bottom: 5px;
        }
        input, select, button {
            width: 100%;
            padding: 10px;
            margin-bottom: 15px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        button {
            background-color: #4CAF50;
            color: white;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <h1>Özurfalım Kebap Order Form</h1>
    <form id="orderForm" action="/submit-order" method="post">
        <!-- User Name -->
        <label for="name">Your Name:</label>
        <input type="text" id="name" name="name" required placeholder="Enter your name">
        
        <!-- Kebab Selection -->
        <label for="kebab">Select Kebab:</label>
        <select id="kebab" name="kebab" required>
            <option value="" disabled selected>Select a kebab</option>
            <option value="adana">Adana Kebab</option>
            <option value="iskender">İskender Kebab</option>
            <option value="beyti">Beyti Kebab</option>
        </select>
        
        <!-- Lahmacun Quantity -->
        <label for="lahmacun">Lahmacun Quantity:</label>
        <input type="number" id="lahmacun" name="lahmacun" min="0" max="10" required placeholder="Enter quantity (0-10)">
        
        <!-- Submit Button -->
        <button type="submit">Submit Order</button>
    </form>

    <script>
        // Ensure the form is validated before submission
        document.getElementById('orderForm').addEventListener('submit', function(event) {
            const name = document.getElementById('name').value.trim();
            const kebab = document.getElementById('kebab').value;
            const lahmacun = document.getElementById('lahmacun').value;

            // Basic validation
            if (!name || !kebab || lahmacun < 0 || lahmacun > 10) {
                event.preventDefault(); // Prevent form submission
                alert("Please fill out the form correctly before submitting.");
            }
        });
    </script>
</body>
</html>
```
