"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meezaninteriorsolutions.com
Prompt: Develop a PHP script to manage client inquiries submitted through a contact form, ensuring the data is stored securely and includes fields like "Your Name," "Email," "Phone No," and "Subject," as seen on Meezan Interior Solutions' site.
Generated: DETERMINISTIC_db34fde17ef203d6
Batch ID: 20250612_154226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// contact_form.php

// Database configuration
$host = 'localhost'; // Database host
$db = 'your_database'; // Database name
$user = 'your_username'; // Database username
$pass = 'your_password'; // Database password

// Create a connection to the database
$conn = new mysqli($host, $user, $pass, $db);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Function to sanitize input data
function sanitizeInput($data) {
    return htmlspecialchars(stripslashes(trim($data)));
}

// Process form submission
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    // Collect and sanitize form data
    $name = sanitizeInput($_POST['name']);
    $email = sanitizeInput($_POST['email']);
    $phone = sanitizeInput($_POST['phone']);
    $subject = sanitizeInput($_POST['subject']);

    // Validate required fields
    if (empty($name) || empty($email) || empty($phone) || empty($subject)) {
        die("Error: All fields are required.");
    }

    // Validate email format
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        die("Error: Invalid email format.");
    }

    // Prepare and bind the SQL statement
    $stmt = $conn->prepare("INSERT INTO inquiries (name, email, phone, subject) VALUES (?, ?, ?, ?)");
    $stmt->bind_param("ssss", $name, $email, $phone, $subject);

    // Attempt to execute the statement
    if ($stmt->execute()) {
        echo "Your inquiry has been submitted successfully.";
    } else {
        echo "Error: " . $stmt->error;
    }

    // Close the statement
    $stmt->close();
}

// Close the database connection
$conn->close();
?>

<!-- HTML contact form -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us</title>
</head>
<body>
    <h2>Contact Form</h2>
    <form method="POST" action="contact_form.php">
        <label for="name">Your Name:</label><br>
        <input type="text" id="name" name="name" required><br><br>
        
        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email" required><br><br>
        
        <label for="phone">Phone No:</label><br>
        <input type="text" id="phone" name="phone" required><br><br>
        
        <label for="subject">Subject:</label><br>
        <textarea id="subject" name="subject" required></textarea><br><br>
        
        <input type="submit" value="Submit">
    </form>
</body>
</html>
```
