"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fenceguys4u.com
Prompt: Generate code to create a web form for requesting a free quote for fence, deck, or pergola installation, including fields for dimensions, material preferences, and project type, as described on "The Fence Guys" website.
Generated: DETERMINISTIC_9a9140750a9942f5
Batch ID: 20250612_153246
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
    <title>Free Quote Request Form</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Request a Free Quote</h1>
        <form id="quoteForm" method="POST" action="submit_quote.php">
            <!-- Project Type Selection -->
            <label for="projectType">Select Project Type:</label>
            <select id="projectType" name="projectType" required>
                <option value="" disabled selected>Select one</option>
                <option value="fence">Fence Installation</option>
                <option value="deck">Deck Installation</option>
                <option value="pergola">Pergola Installation</option>
            </select>

            <!-- Dimensions Input -->
            <label for="dimensions">Dimensions (Length x Width in feet):</label>
            <input type="text" id="dimensions" name="dimensions" placeholder="e.g., 20 x 10" required pattern="^\d+\s*x\s*\d+$" title="Format: Length x Width (e.g., 20 x 10)">

            <!-- Material Preferences -->
            <label for="material">Material Preferences:</label>
            <select id="material" name="material" required>
                <option value="" disabled selected>Select material</option>
                <option value="wood">Wood</option>
                <option value="vinyl">Vinyl</option>
                <option value="aluminum">Aluminum</option>
                <option value="composite">Composite</option>
            </select>

            <!-- Additional Notes -->
            <label for="notes">Additional Notes:</label>
            <textarea id="notes" name="notes" rows="4" placeholder="Any additional details or requests..."></textarea>

            <!-- Submit Button -->
            <button type="submit">Request Quote</button>
        </form>
    </div>

    <script>
        // Basic form validation
        document.getElementById('quoteForm').addEventListener('submit', function(event) {
            const dimensions = document.getElementById('dimensions').value;
            const regex = /^\d+\s*x\s*\d+$/;

            if (!regex.test(dimensions)) {
                alert("Please enter dimensions in the correct format: Length x Width (e.g., 20 x 10)");
                event.preventDefault(); // Prevent form submission
            }
        });
    </script>
</body>
</html>
```

```php
<?php
// submit_quote.php

// Check if the form was submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize input data
    $projectType = filter_input(INPUT_POST, 'projectType', FILTER_SANITIZE_STRING);
    $dimensions = filter_input(INPUT_POST, 'dimensions', FILTER_SANITIZE_STRING);
    $material = filter_input(INPUT_POST, 'material', FILTER_SANITIZE_STRING);
    $notes = filter_input(INPUT_POST, 'notes', FILTER_SANITIZE_STRING);

    // Validate required fields
    if (empty($projectType) || empty($dimensions) || empty($material)) {
        die("Error: Please fill in all required fields.");
    }

    // Prepare data for storage or email (example)
    $to = "info@thefenceguys.com";
    $subject = "New Quote Request";
    $message = "Project Type: $projectType\nDimensions: $dimensions\nMaterial: $material\nNotes: $notes";
    $headers = "From: no-reply@thefenceguys.com";

    // Send the email
    if (mail($to, $subject, $message, $headers)) {
        echo "Quote request submitted successfully!";
    } else {
        echo "Error: Unable to send email. Please try again later.";
    }
} else {
    echo "Error: Invalid request method.";
}
?>
```

```css
/* styles.css */

body {
    font-family: Arial, sans-serif;
    background-color: #f9f9f9;
    margin: 0;
    padding: 20px;
}

.container {
    max-width: 600px;
    margin: auto;
    background: #fff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

h1 {
    text-align: center;
}

label {
    display: block;
    margin: 12px 0 4px;
}

input[type="text"],
select,
textarea {
    width: 100%;
    padding: 8px;
    margin: 4px 0 12px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    background-color: #4CAF50;
    color: white;
    padding: 10px 15px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    width: 100%;
}

button:hover {
    background-color: #45a049;
}
```
