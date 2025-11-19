"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gautamindustries.com
Prompt: Develop a simple HTML form that allows users to request a quote for decorative wood veneer sheets, incorporating the pricing information provided by Gautam Industries.
Generated: DETERMINISTIC_5c95dde93cb2ffc4
Batch ID: 20250612_163540
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
    <title>Decorative Wood Veneer Sheets Quote Request</title>
    <style>
        /* Basic styling for the form */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }

        .container {
            max-width: 600px;
            margin: 50px auto;
            padding: 20px;
            background: #fff;
            border: 1px solid #ddd;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }

        h1 {
            text-align: center;
            color: #333;
        }

        form {
            display: flex;
            flex-direction: column;
        }

        label {
            margin: 10px 0 5px;
            font-weight: bold;
        }

        input, select, textarea, button {
            padding: 10px;
            margin-bottom: 20px;
            border: 1px solid #ddd;
            border-radius: 4px;
            width: 100%;
        }

        button {
            background-color: #007bff;
            color: #fff;
            cursor: pointer;
            border: none;
        }

        button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Request a Quote</h1>
        <form id="quoteForm">
            <!-- Name field -->
            <label for="name">Full Name</label>
            <input type="text" id="name" name="name" required placeholder="Enter your name">

            <!-- Email field -->
            <label for="email">Email Address</label>
            <input type="email" id="email" name="email" required placeholder="Enter your email">

            <!-- Phone field -->
            <label for="phone">Phone Number</label>
            <input type="tel" id="phone" name="phone" required placeholder="Enter your phone number">

            <!-- Veneer type selection -->
            <label for="veneerType">Veneer Type</label>
            <select id="veneerType" name="veneerType" required>
                <option value="" disabled selected>Select a veneer type</option>
                <option value="oak">Oak</option>
                <option value="walnut">Walnut</option>
                <option value="mahogany">Mahogany</option>
                <option value="birch">Birch</option>
            </select>

            <!-- Quantity selection -->
            <label for="quantity">Quantity (Sheets)</label>
            <input type="number" id="quantity" name="quantity" required min="1" placeholder="Enter quantity">

            <!-- Additional notes -->
            <label for="notes">Additional Notes</label>
            <textarea id="notes" name="notes" placeholder="Add any specific requirements"></textarea>

            <!-- Submit button -->
            <button type="submit">Submit Request</button>
        </form>
    </div>

    <!-- JavaScript for handling form submission -->
    <script>
        // Attach a submit event listener to the form
        document.getElementById('quoteForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent the default form submission

            // Gather form data
            const formData = {
                name: document.getElementById('name').value,
                email: document.getElementById('email').value,
                phone: document.getElementById('phone').value,
                veneerType: document.getElementById('veneerType').value,
                quantity: document.getElementById('quantity').value,
                notes: document.getElementById('notes').value
            };

            // Basic validation (optional, backend validation still needed)
            if (!formData.name || !formData.email || !formData.phone || !formData.veneerType || !formData.quantity) {
                alert('Please fill in all the required fields.');
                return;
            }

            // Simulate form submission (replace with actual API call in production)
            console.log('Quote request submitted:', formData);
            alert('Thank you! Your request has been submitted.');

            // Reset the form
            document.getElementById('quoteForm').reset();
        });
    </script>
</body>
</html>
```
