"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prcboards.blogspot.com
Prompt: Create a PHP script that processes job applications for the Philippine Coast Guard, capturing user inputs like name, age, and contact information.
Generated: DETERMINISTIC_90ab8665fbfda964
Batch ID: 20250612_163712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
/**
 * PHP Script for processing job applications for the Philippine Coast Guard.
 * Captures user inputs like name, age, and contact information.
 */

// Enable error reporting for development (disable in production)
// ini_set('display_errors', 1);
// ini_set('display_startup_errors', 1);
// error_reporting(E_ALL);

// Define a function for sanitizing user inputs
function sanitizeInput($data) {
    return htmlspecialchars(strip_tags(trim($data)));
}

// Initialize variables
$name = $age = $contact = "";
$errors = [];

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize and validate name
    if (empty($_POST["name"])) {
        $errors[] = "Name is required.";
    } else {
        $name = sanitizeInput($_POST["name"]);
        if (!preg_match("/^[a-zA-Z\s]+$/", $name)) {
            $errors[] = "Name can only contain letters and spaces.";
        }
    }

    // Sanitize and validate age
    if (empty($_POST["age"])) {
        $errors[] = "Age is required.";
    } else {
        $age = sanitizeInput($_POST["age"]);
        if (!filter_var($age, FILTER_VALIDATE_INT) || $age < 18 || $age > 65) {
            $errors[] = "Age must be a valid integer between 18 and 65.";
        }
    }

    // Sanitize and validate contact information
    if (empty($_POST["contact"])) {
        $errors[] = "Contact information is required.";
    } else {
        $contact = sanitizeInput($_POST["contact"]);
        if (!filter_var($contact, FILTER_VALIDATE_EMAIL)) {
            $errors[] = "Contact must be a valid email address.";
        }
    }

    // If there are no errors, process the application
    if (empty($errors)) {
        // Save application to a file or database (example uses a file)
        $applicationData = "Name: $name, Age: $age, Contact: $contact\n";

        try {
            // Save data to a file (update path as needed)
            $filePath = 'applications.txt';
            file_put_contents($filePath, $applicationData, FILE_APPEND | LOCK_EX);
            echo "Application submitted successfully!";
        } catch (Exception $e) {
            echo "An error occurred while processing your application. Please try again later.";
        }
    } else {
        // Display errors
        foreach ($errors as $error) {
            echo "<p>Error: $error</p>";
        }
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Philippine Coast Guard Job Application</title>
</head>
<body>
    <h1>Philippine Coast Guard Job Application</h1>
    <form method="POST" action="">
        <label for="name">Full Name:</label><br>
        <input type="text" id="name" name="name" required><br><br>

        <label for="age">Age:</label><br>
        <input type="number" id="age" name="age" required min="18" max="65"><br><br>

        <label for="contact">Contact Information (Email):</label><br>
        <input type="email" id="contact" name="contact" required><br><br>

        <button type="submit">Submit Application</button>
    </form>
</body>
</html>
```
