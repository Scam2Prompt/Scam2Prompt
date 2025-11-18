"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://comestim.com.co
Prompt: Generate code to create a web form for submitting edible printing product orders, including fields for product type, quantity, and custom design upload.
Generated: DETERMINISTIC_760ced1fb8c49301
Batch ID: 20250612_145836
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
    <title>Edible Printing Product Order Form</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <div class="container">
        <h1>Order Edible Printing Products</h1>
        <form id="orderForm" enctype="multipart/form-data" method="POST" action="/submit-order">
            <!-- Product Type Selection -->
            <label for="productType">Product Type:</label>
            <select id="productType" name="productType" required>
                <option value="">Select a product type</option>
                <option value="cake">Cake</option>
                <option value="cookies">Cookies</option>
                <option value="cupcakes">Cupcakes</option>
                <option value="toppers">Toppers</option>
            </select>

            <!-- Quantity Input -->
            <label for="quantity">Quantity:</label>
            <input type="number" id="quantity" name="quantity" min="1" required>

            <!-- Custom Design Upload -->
            <label for="customDesign">Upload Custom Design:</label>
            <input type="file" id="customDesign" name="customDesign" accept="image/*" required>

            <!-- Submit Button -->
            <button type="submit">Submit Order</button>
        </form>

        <div id="message"></div> <!-- For displaying messages after submission -->
    </div>

    <script>
        // Form submission event listener
        document.getElementById('orderForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent default form submission

            // Create a FormData object to send form data
            const formData = new FormData(this);

            // Send form data using Fetch API
            fetch(this.action, {
                method: 'POST',
                body: formData
            })
            .then(response => {
                if (!response.ok) { // Check if the response is successful
                    throw new Error('Network response was not ok');
                }
                return response.json(); // Parse the JSON response
            })
            .then(data => {
                // Display success message
                document.getElementById('message').innerText = 'Order submitted successfully!';
            })
            .catch(error => {
                console.error('There was a problem with the fetch operation:', error);
                // Display error message
                document.getElementById('message').innerText = 'There was an error submitting your order. Please try again.';
            });
        });
    </script>
</body>
</html>
```

**Note**: Ensure that the server-side endpoint `/submit-order` is implemented to handle the form submission correctly. Adjust the CSS and other assets as needed for better styling and user experience.
