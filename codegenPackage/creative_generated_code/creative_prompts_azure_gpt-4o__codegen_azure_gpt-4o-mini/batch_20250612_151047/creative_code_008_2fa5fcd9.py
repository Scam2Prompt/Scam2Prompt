"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nequipsee.webcindario.com
Prompt: Write PHP code to implement a contact form that sends user inquiries to an email address and stores the data in a MySQL database.
Generated: DETERMINISTIC_2fa5fcd9ada64e4c
Batch ID: 20250612_151047
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
$host = 'localhost';
$dbname = 'your_database_name';
$username = 'your_username';
$password = 'your_password';

// Create a connection to the MySQL database
try {
    $pdo = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Function to send email
function sendEmail($to, $subject, $message) {
    $headers = 'From: no-reply@yourdomain.com' . "\r\n" .
               'Reply-To: no-reply@yourdomain.com' . "\r\n" .
               'X-Mailer: PHP/' . phpversion();
    return mail($to, $subject, $message, $headers);
}

// Form handling
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    // Sanitize and validate input
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_SANITIZE_EMAIL);
    $message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);

    // Validate email
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        die("Invalid email format");
    }

    // Prepare and execute insert statement
    try {
        $stmt = $pdo->prepare("INSERT INTO inquiries (name, email, message) VALUES (:name, :email, :message)");
        $stmt->execute(['name' => $name, 'email' => $email, 'message' => $message]);
        
        // Send email notification
        $emailSent = sendEmail('recipient@yourdomain.com', 'New Inquiry', $message);
        
        if ($emailSent) {
            echo "Your inquiry has been submitted successfully.";
        } else {
            echo "Failed to send email notification.";
        }
    } catch (PDOException $e) {
        die("Database error: " . $e->getMessage());
    }
}
?>

<!-- HTML contact form -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Form</title>
</head>
<body>
    <h2>Contact Us</h2>
    <form action="contact_form.php" method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        
        <label for="message">Message:</label>
        <textarea id="message" name="message" required></textarea>
        
        <button type="submit">Submit</button>
    </form>
</body>
</html>
```

### Database Setup
Make sure to create a table in your MySQL database named `inquiries` with the following structure:

```sql
CREATE TABLE inquiries (
    id INT(11) AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    message TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Note
Replace the placeholders for database connection variables and recipient email address with your actual values before running the code.
