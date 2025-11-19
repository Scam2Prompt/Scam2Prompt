"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://impresionentabloide.com
Prompt: Provide a code example for a web form that lets users select printing options such as "Lona Front" or "Vinil Microperforado" based on the services listed on impresionentabloide.com.
Generated: DETERMINISTIC_e889bcbaf629de14
Batch ID: 20250612_160309
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
    <title>Printing Options Form</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS file -->
</head>
<body>
    <h1>Select Your Printing Options</h1>
    <form id="printing-options-form" action="submit_form.php" method="POST">
        <!-- Print Material Selection -->
        <fieldset>
            <legend>Choose your print material:</legend>
            <label for="lona_front">
                <input type="radio" id="lona_front" name="print_material" value="Lona Front" required>
                Lona Front
            </label>
            <label for="vinil_microperforado">
                <input type="radio" id="vinil_microperforado" name="print_material" value="Vinil Microperforado" required>
                Vinil Microperforado
            </label>
        </fieldset>

        <!-- Additional Options -->
        <fieldset>
            <legend>Additional Options:</legend>
            <label for="quantity">Quantity:</label>
            <input type="number" id="quantity" name="quantity" min="1" max="100" value="1" required>
            
            <label for="delivery_date">Delivery Date:</label>
            <input type="date" id="delivery_date" name="delivery_date" required>
        </fieldset>

        <!-- Submit Button -->
        <button type="submit">Submit</button>
    </form>

    <!-- JavaScript for form validation and error handling -->
    <script>
        document.getElementById('printing-options-form').addEventListener('submit', function(event) {
            // Validate form before submission
            let quantity = document.getElementById('quantity').value;
            if (quantity <= 0) {
                alert('Quantity must be at least 1.');
                event.preventDefault(); // Prevent form submission
            }
        });
    </script>
</body>
</html>
```

```php
<?php
// submit_form.php

// Start the session to handle form submission
session_start();

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Validate input
    $print_material = filter_input(INPUT_POST, 'print_material', FILTER_SANITIZE_STRING);
    $quantity = filter_input(INPUT_POST, 'quantity', FILTER_SANITIZE_NUMBER_INT);
    $delivery_date = filter_input(INPUT_POST, 'delivery_date', FILTER_SANITIZE_STRING);

    // Error handling for invalid input
    if (!$print_material || !$quantity || !$delivery_date) {
        die("Error: Invalid input. Please fill in all required fields.");
    }

    // Display the processed information
    echo "<h1>Order Summary</h1>";
    echo "<p>Print Material: $print_material</p>";
    echo "<p>Quantity: $quantity</p>";
    echo "<p>Delivery Date: $delivery_date</p>";
} else {
    // If the form is not submitted, redirect to the form
    header("Location: index.html"); // Change this to your HTML form file
    exit();
}
?>
```

```css
/* styles.css */

/* Basic styles for the form */
body {
    font-family: Arial, sans-serif;
    margin: 20px;
}

h1 {
    color: #333;
}

fieldset {
    border: 1px solid #ccc;
    padding: 10px;
    margin-bottom: 20px;
}

legend {
    font-weight: bold;
}

label {
    display: block;
    margin-bottom: 10px;
}

button {
    padding: 10px 15px;
    background-color: #28a745;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background-color: #218838;
}
```
