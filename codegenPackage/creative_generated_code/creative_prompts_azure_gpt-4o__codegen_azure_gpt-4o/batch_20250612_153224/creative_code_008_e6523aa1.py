"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://naikreatif.com
Prompt: Write PHP code to handle form submissions for downloading resources like the restaurant grand opening checklist offered by Naikreatif.
Generated: DETERMINISTIC_e6523aa12d1b76e4
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Enable error reporting for debugging purposes (disable in production)
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Function to sanitize user input
function sanitizeInput($input) {
    return htmlspecialchars(stripslashes(trim($input)));
}

// Check if the form was submitted
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    // Collect and sanitize form data
    $name = isset($_POST['name']) ? sanitizeInput($_POST['name']) : '';
    $email = isset($_POST['email']) ? sanitizeInput($_POST['email']) : '';

    // Initialize an array to hold error messages
    $errors = [];

    // Validate name (required)
    if (empty($name)) {
        $errors[] = "Name is required.";
    }

    // Validate email (required and should be a valid email format)
    if (empty($email)) {
        $errors[] = "Email is required.";
    } elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $errors[] = "Invalid email format.";
    }

    // If there are no errors, process the download logic
    if (empty($errors)) {
        // Log submission (could be replaced with database storage or email notification)
        file_put_contents('submissions.log', date('Y-m-d H:i:s') . " - Name: $name, Email: $email\n", FILE_APPEND);

        // Set headers to trigger file download
        $file = 'restaurant_grand_opening_checklist.pdf'; // Path to the resource file
        if (file_exists($file)) {
            header('Content-Description: File Transfer');
            header('Content-Type: application/pdf');
            header('Content-Disposition: attachment; filename="' . basename($file) . '"');
            header('Content-Length: ' . filesize($file));
            readfile($file);
            exit; // Ensure no further code runs after file download
        } else {
            $errors[] = "The requested resource could not be found.";
        }
    }

    // Display errors if any
    if (!empty($errors)) {
        foreach ($errors as $error) {
            echo "<p style='color:red;'>$error</p>";
        }
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Download Resource</title>
</head>
<body>
    <h1>Download the Restaurant Grand Opening Checklist</h1>
    <form method="POST" action="">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <br><br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <br><br>
        <button type="submit">Download</button>
    </form>
</body>
</html>
```
