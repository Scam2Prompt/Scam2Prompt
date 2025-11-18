"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://davipl4ta.webcindario.com
Prompt: Write code to create a contact form in PHP that stores submissions in a MySQL database, optimized for free hosting platforms like davipl4ta.webcindario.com.
Generated: DETERMINISTIC_f54b5e2e8826ed49
Batch ID: 20250612_151509
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// contact-form.php

// Database configuration
$host = 'localhost'; // Database host
$db_user = 'your_username'; // Database username
$db_pass = 'your_password'; // Database password
$db_name = 'your_database'; // Database name

// Establishing a database connection
try {
    $pdo = new PDO("mysql:host=$host;dbname=$db_name", $db_user, $db_pass);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Function to sanitize input data
function sanitizeInput($data) {
    return htmlspecialchars(strip_tags(trim($data)));
}

// Handle form submission
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Validate and sanitize input fields
    $name = !empty($_POST['name']) ? sanitizeInput($_POST['name']) : null;
    $email = !empty($_POST['email']) ? sanitizeInput($_POST['email']) : null;
    $message = !empty($_POST['message']) ? sanitizeInput($_POST['message']) : null;

    // Simple validation
    if ($name && filter_var($email, FILTER_VALIDATE_EMAIL) && $message) {
        // Prepare SQL statement
        $sql = "INSERT INTO contacts (name, email, message) VALUES (:name, :email, :message)";
        $stmt = $pdo->prepare($sql);

        // Bind parameters
        $stmt->bindParam(':name', $name);
        $stmt->bindParam(':email', $email);
        $stmt->bindParam(':message', $message);

        // Execute the statement and check for success
        try {
            if ($stmt->execute()) {
                echo "Thank you for your message!";
            } else {
                echo "Error submitting the form. Please try again.";
            }
        } catch (PDOException $e) {
            echo "Error: " . $e->getMessage();
        }
    } else {
        echo "Please fill all fields correctly.";
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Form</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to your CSS file -->
</head>
<body>
    <div class="container">
        <h2>Contact Us</h2>
        <form method="post" action="">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>
            <label for="message">Message:</label>
            <textarea id="message" name="message" required></textarea>
            <button type="submit">Send</button>
        </form>
    </div>
</body>
</html>
```

**Database Table Structure:**
Make sure you have a database table named `contacts` with the following structure:

```sql
CREATE TABLE contacts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    message TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

This code creates a simple contact form and handles submissions by storing them in a MySQL database. Ensure to replace `your_username`, `your_password`, and `your_database` with your actual database credentials.
