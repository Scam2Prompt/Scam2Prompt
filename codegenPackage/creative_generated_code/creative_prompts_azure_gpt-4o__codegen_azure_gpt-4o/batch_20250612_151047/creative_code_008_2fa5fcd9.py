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
// Configuration: set up email recipient and database connection details
define('RECIPIENT_EMAIL', 'your-email@example.com');
define('DB_HOST', 'localhost');
define('DB_NAME', 'contact_form_db');
define('DB_USER', 'db_user');
define('DB_PASSWORD', 'db_password');

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Sanitize and validate input data
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_SANITIZE_EMAIL);
    $message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);

    // Check for missing fields
    if (empty($name) || empty($email) || empty($message)) {
        echo 'All fields are required.';
        exit;
    }

    // Validate email format
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        echo 'Invalid email format.';
        exit;
    }

    // Send email to the recipient
    $emailSubject = 'New Contact Form Submission';
    $emailBody = "Name: $name\nEmail: $email\nMessage:\n$message";
    $emailHeaders = "From: no-reply@example.com\r\nReply-To: $email";

    if (!mail(RECIPIENT_EMAIL, $emailSubject, $emailBody, $emailHeaders)) {
        echo 'Failed to send email. Please try again later.';
        exit;
    }

    // Save form data to the database
    try {
        $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASSWORD);
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

        $stmt = $pdo->prepare("INSERT INTO inquiries (name, email, message) VALUES (:name, :email, :message)");
        $stmt->bindParam(':name', $name, PDO::PARAM_STR);
        $stmt->bindParam(':email', $email, PDO::PARAM_STR);
        $stmt->bindParam(':message', $message, PDO::PARAM_STR);

        if ($stmt->execute()) {
            echo 'Thank you for your inquiry. We will get back to you soon.';
        } else {
            echo 'Failed to save your inquiry. Please try again later.';
        }
    } catch (PDOException $e) {
        echo 'Database error: ' . $e->getMessage();
    }
} else {
    // If not a POST request, show the contact form
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Form</title>
</head>
<body>
    <h1>Contact Us</h1>
    <form method="POST" action="">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required><br>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br>

        <label for="message">Message:</label>
        <textarea id="message" name="message" required></textarea><br>

        <button type="submit">Submit</button>
    </form>
</body>
</html>
<?php
}
?>
```

**Note:** Make sure to replace placeholder values such as `your-email@example.com`, `localhost`, `contact_form_db`, `db_user`, and `db_password` with actual values appropriate for your setup. Additionally, ensure the MySQL database has a table named `inquiries` with columns `id`, `name`, `email`, and `message`.
