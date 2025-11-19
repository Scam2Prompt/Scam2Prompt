"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nellyservis.sk
Prompt: Construct a simple HTML form for customers to submit their requirements for window and door installations, similar to the request process at NellyServis.
Generated: DETERMINISTIC_eadc41ed7c9100f2
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
    <title>Window and Door Installation Request Form</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <h1>Request a Window and Door Installation</h1>
    <form id="installationRequestForm" action="submit_form.php" method="POST">
        <label for="customerName">Full Name:</label>
        <input type="text" id="customerName" name="customerName" required placeholder="Enter your full name">

        <label for="customerEmail">Email Address:</label>
        <input type="email" id="customerEmail" name="customerEmail" required placeholder="Enter your email">

        <label for="installationType">Type of Installation:</label>
        <select id="installationType" name="installationType" required>
            <option value="">Select Installation Type</option>
            <option value="window">Window</option>
            <option value="door">Door</option>
            <option value="both">Both</option>
        </select>

        <label for="installationDate">Preferred Installation Date:</label>
        <input type="date" id="installationDate" name="installationDate" required>

        <label for="projectDetails">Project Details:</label>
        <textarea id="projectDetails" name="projectDetails" rows="4" required placeholder="Provide additional details about your project"></textarea>

        <button type="submit">Submit Request</button>
    </form>

    <script>
        // Client-side form validation
        document.getElementById('installationRequestForm').addEventListener('submit', function(event) {
            const emailField = document.getElementById('customerEmail');
            if (!validateEmail(emailField.value)) {
                alert('Please enter a valid email address.');
                event.preventDefault(); // Prevent form submission
            }
        });

        // Function to validate email format
        function validateEmail(email) {
            const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            return re.test(String(email).toLowerCase());
        }
    </script>
</body>
</html>
```

```php
<?php
// submit_form.php

// Function to sanitize user input
function sanitizeInput($data) {
    return htmlspecialchars(stripslashes(trim($data)));
}

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    try {
        // Sanitize form inputs
        $name = sanitizeInput($_POST['customerName']);
        $email = sanitizeInput($_POST['customerEmail']);
        $installationType = sanitizeInput($_POST['installationType']);
        $installationDate = sanitizeInput($_POST['installationDate']);
        $projectDetails = sanitizeInput($_POST['projectDetails']);

        // Validate email format
        if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
            throw new Exception("Invalid email format");
        }

        // Here you would typically save the data to a database or send an email
        // For demonstration, we will just echo the sanitized inputs
        echo "Request submitted successfully.<br>";
        echo "Name: $name<br>";
        echo "Email: $email<br>";
        echo "Installation Type: $installationType<br>";
        echo "Installation Date: $installationDate<br>";
        echo "Project Details: $projectDetails<br>";
    } catch (Exception $e) {
        // Log error to a file (not shown) and display a user-friendly message
        echo 'Error: ' . $e->getMessage();
    }
} else {
    // Handle the case of an invalid request
    echo "Invalid request method.";
}
?>
```
