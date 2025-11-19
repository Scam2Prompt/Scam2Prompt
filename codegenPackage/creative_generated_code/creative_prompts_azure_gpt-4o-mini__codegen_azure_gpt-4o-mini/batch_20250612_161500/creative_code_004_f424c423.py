"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://detaljreklam.se
Prompt: Write a code example for a web form that collects customer details for printing services, ensuring it includes fields for items like brochures and roll-ups, as mentioned on Detalj Reklam's site.
Generated: DETERMINISTIC_f424c423a115bff5
Batch ID: 20250612_161500
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
    <title>Customer Details Form - Printing Services</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Customer Details Form</h1>
    <form id="printingForm" method="POST" action="submit_form.php">
        <!-- Customer Name -->
        <label for="customerName">Full Name:</label>
        <input type="text" id="customerName" name="customerName" required>
        
        <!-- Customer Email -->
        <label for="customerEmail">Email:</label>
        <input type="email" id="customerEmail" name="customerEmail" required>
        
        <!-- Customer Phone -->
        <label for="customerPhone">Phone:</label>
        <input type="tel" id="customerPhone" name="customerPhone" required>
        
        <!-- Item Selection -->
        <label for="itemType">Select Item:</label>
        <select id="itemType" name="itemType" required>
            <option value="">Please select</option>
            <option value="brochures">Brochures</option>
            <option value="roll-ups">Roll-Ups</option>
            <option value="business-cards">Business Cards</option>
            <option value="flyers">Flyers</option>
        </select>
        
        <!-- Quantity -->
        <label for="itemQuantity">Quantity:</label>
        <input type="number" id="itemQuantity" name="itemQuantity" min="1" required>
        
        <!-- Notes -->
        <label for="additionalNotes">Additional Notes:</label>
        <textarea id="additionalNotes" name="additionalNotes" rows="4" cols="50" placeholder="Any specific requests..."></textarea>
        
        <!-- Submit Button -->
        <button type="submit">Submit</button>
    </form>

    <script>
        // Handle form submission
        document.getElementById('printingForm').onsubmit = function(e) {
            // Add client-side validation if necessary
            const name = document.getElementById('customerName').value;
            const email = document.getElementById('customerEmail').value;
            const phone = document.getElementById('customerPhone').value;
            const itemType = document.getElementById('itemType').value;
            const quantity = document.getElementById('itemQuantity').value;

            if (!name || !email || !phone || !itemType || quantity <= 0) {
                alert("Please fill out all required fields correctly.");
                e.preventDefault(); // Prevent form submission
            }
        };
    </script>
</body>
</html>
```

```php
<?php
// submit_form.php

// Check if the form was submitted via POST
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Collect and sanitize input data
    $name = filter_input(INPUT_POST, 'customerName', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'customerEmail', FILTER_SANITIZE_EMAIL);
    $phone = filter_input(INPUT_POST, 'customerPhone', FILTER_SANITIZE_STRING);
    $itemType = filter_input(INPUT_POST, 'itemType', FILTER_SANITIZE_STRING);
    $quantity = filter_input(INPUT_POST, 'itemQuantity', FILTER_SANITIZE_NUMBER_INT);
    $additionalNotes = filter_input(INPUT_POST, 'additionalNotes', FILTER_SANITIZE_STRING);

    // Validate mandatory fields
    if (empty($name) || empty($email) || empty($phone) || empty($itemType) || $quantity <= 0) {
        die("Error: All fields are required and must be valid.");
    }

    // Process the data (e.g., save to database or send an email)
    // Example: save_to_database($name, $email, $phone, $itemType, $quantity, $additionalNotes);

    // Provide feedback to user
    echo "Thank you, $name! Your order for $quantity $itemType has been received.";
} else {
    // Handle the case where the script is accessed without form submission
    die("Error: Invalid request method.");
}
?>
```
