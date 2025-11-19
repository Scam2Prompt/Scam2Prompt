"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://powerfivesolar.com
Prompt: Develop a simple web form that collects user information for solar consultation, similar to the form provided by PowerFive Solar, ensuring it captures property type and roof type.
Generated: DETERMINISTIC_05d3ed08e3c9da22
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
    <title>Solar Consultation Form</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to an external stylesheet -->
</head>
<body>
    <h1>Solar Consultation Request Form</h1>
    <form id="consultationForm" action="submit_form.php" method="POST">
        <label for="name">Full Name:</label>
        <input type="text" id="name" name="name" required>
        
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        
        <label for="phone">Phone Number:</label>
        <input type="tel" id="phone" name="phone" required>
        
        <label for="propertyType">Property Type:</label>
        <select id="propertyType" name="propertyType" required>
            <option value="">Select Property Type</option>
            <option value="Residential">Residential</option>
            <option value="Commercial">Commercial</option>
            <option value="Industrial">Industrial</option>
        </select>
        
        <label for="roofType">Roof Type:</label>
        <select id="roofType" name="roofType" required>
            <option value="">Select Roof Type</option>
            <option value="Flat">Flat</option>
            <option value="Gabled">Gabled</option>
            <option value="Hip">Hip</option>
            <option value="Mansard">Mansard</option>
            <option value="Gambrel">Gambrel</option>
        </select>
        
        <button type="submit">Submit</button>
    </form>

    <script>
        // Function to handle form submission
        document.getElementById('consultationForm').addEventListener('submit', function(event) {
            // Perform any client-side validation here
            
            // Example: Confirm before submission
            if (!confirm('Are you sure you want to submit your information?')) {
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
// This script handles the form submission for solar consultation requests

// Check if the form was submitted via POST
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    // Sanitize and validate user inputs
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
    $phone = filter_input(INPUT_POST, 'phone', FILTER_SANITIZE_STRING);
    $propertyType = filter_input(INPUT_POST, 'propertyType', FILTER_SANITIZE_STRING);
    $roofType = filter_input(INPUT_POST, 'roofType', FILTER_SANITIZE_STRING);

    // Check for validation errors
    if (!$name || !$email || !$phone || !$propertyType || !$roofType) {
        die("Invalid input. Please fill out all fields correctly.");
    }

    // Here you would typically save the data to a database or send an email
    // For demonstration, let's just echo the received data
    echo "Thank you for your request, $name!<br>";
    echo "We will contact you at $email or $phone regarding your $propertyType property with a $roofType roof.";
} else {
    // If the form is accessed directly (not via POST), redirect or show an error
    header("Location: index.html");
    exit();
}
?>
```
