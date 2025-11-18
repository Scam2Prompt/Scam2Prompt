"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://grupo-virtual.webcindario.com
Prompt: Write PHP code for a contact form that stores submissions in a MySQL database, optimized for free hosting environments.
Generated: DETERMINISTIC_938573e98c89e0dd
Batch ID: 20250612_154740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Database configuration
$host = 'localhost'; // Typically localhost for free hosting
$dbname = 'your_database_name'; // Replace with your database name
$username = 'your_username'; // Replace with your database username
$password = 'your_password'; // Replace with your database password

try {
    // Establish a database connection using PDO
    $pdo = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection errors
    die("Connection failed: " . $e->getMessage());
}

// Check if the form has been submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Validate input fields
    $name = trim($_POST['name']);
    $email = trim($_POST['email']);
    $message = trim($_POST['message']);
    
    // Validate that required fields are not empty
    if (empty($name) || empty($email) || empty($message)) {
        die("Error: All fields are required.");
    }

    // Validate email address
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        die("Error: Invalid email format.");
    }

    try {
        // Prepare SQL query to insert form data into the database
        $stmt = $pdo->prepare("INSERT INTO contact_form_submissions (name, email, message) VALUES (:name, :email, :message)");

        // Bind parameters to the query
        $stmt->bindParam(':name', $name);
        $stmt->bindParam(':email', $email);
        $stmt->bindParam(':message', $message);

        // Execute the query
        if ($stmt->execute()) {
            echo "Thank you for your submission!";
        } else {
            echo "Error: Unable to submit your form. Please try again.";
        }
    } catch (PDOException $e) {
        // Handle query errors
        die("Error: " . $e->getMessage());
    }
}
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
    <form method="post" action="">
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name" required><br>
        
        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email" required><br>
        
        <label for="message">Message:</label><br>
        <textarea id="message" name="message" required></textarea><br>
        
        <input type="submit" value="Submit">
    </form>
</body>
</html>
```
