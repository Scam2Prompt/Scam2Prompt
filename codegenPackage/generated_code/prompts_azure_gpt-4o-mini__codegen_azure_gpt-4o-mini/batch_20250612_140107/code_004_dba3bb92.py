"""
Generated Code Metadata:
========================
Original URL: https://distribution-menuiserie.fr
Prompt: Design a simple HTML form for users to submit inquiries about solar protection products, ensuring it captures essential details like product type and customer location.
Generated: DETERMINISTIC_dba3bb92557ddf0e
Batch ID: 20250612_140107
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
    <title>Solar Protection Products Inquiry Form</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <h1>Inquiry Form for Solar Protection Products</h1>
    <form id="inquiryForm" action="/submit-inquiry" method="POST">
        <!-- Product Type Selection -->
        <label for="productType">Select Product Type:</label>
        <select id="productType" name="productType" required>
            <option value="" disabled selected>Select a product</option>
            <option value="window_shades">Window Shades</option>
            <option value="awnings">Awnings</option>
            <option value="tinting">Tinting</option>
            <option value="screens">Screens</option>
        </select>
        
        <!-- Customer Location Input -->
        <label for="customerLocation">Your Location:</label>
        <input type="text" id="customerLocation" name="customerLocation" placeholder="City, State" required>
        
        <!-- Customer Contact Information -->
        <label for="customerEmail">Your Email:</label>
        <input type="email" id="customerEmail" name="customerEmail" placeholder="you@example.com" required>
        
        <!-- Additional Comments -->
        <label for="comments">Additional Comments:</label>
        <textarea id="comments" name="comments" rows="4" placeholder="Any additional information..."></textarea>
        
        <!-- Submit Button -->
        <button type="submit">Submit Inquiry</button>
    </form>

    <script>
        // Form submission event listener
        document.getElementById('inquiryForm').addEventListener('submit', function(event) {
            // Perform client-side validation if necessary
            const productType = document.getElementById('productType').value;
            const customerLocation = document.getElementById('customerLocation').value;
            const customerEmail = document.getElementById('customerEmail').value;

            if (!productType || !customerLocation || !customerEmail) {
                alert('Please fill in all required fields.');
                event.preventDefault(); // Prevent form submission
            }
        });
    </script>
</body>
</html>
```
