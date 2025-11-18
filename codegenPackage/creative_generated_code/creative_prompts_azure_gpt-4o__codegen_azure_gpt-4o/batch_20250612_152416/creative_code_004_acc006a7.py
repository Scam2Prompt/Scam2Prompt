"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inicioseguridad6.webcindario.com
Prompt: Create a PHP-based contact form that sends user-submitted data to a MySQL database and displays a confirmation message.
Generated: DETERMINISTIC_acc006a7e1be7a67
Batch ID: 20250612_152416
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Ensure this script is executed when the form is submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Database credentials
    $dbHost = 'localhost';  // Replace with your database host
    $dbUser = 'root';       // Replace with your database username
    $dbPass = '';           // Replace with your database password
    $dbName = 'contact_form'; // Replace with your database name

    try {
        // Establish connection to MySQL database using PDO
        $pdo = new PDO("mysql:host=$dbHost;dbname=$dbName", $dbUser, $dbPass);
        // Set error mode to exception for proper error reporting
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

        // Sanitize and retrieve form data
        $name = htmlspecialchars(trim($_POST['name']));
        $email = htmlspecialchars(trim($_POST['email']));
        $message = htmlspecialchars(trim($_POST['message']));

        // Basic validation
        if (empty($name) || empty($email) || empty($message)) {
            throw new Exception('All fields are required.');
        }
        if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
            throw new Exception('Invalid email format.');
        }

        // Prepare SQL query to insert data into the database
        $stmt = $pdo->prepare("INSERT INTO contacts (name, email, message) VALUES (:name, :email, :message)");
        $stmt->bindParam(':name', $name, PDO::PARAM_STR);
        $stmt->bindParam(':email', $email, PDO::PARAM_STR);
        $stmt->bindParam(':message', $message, PDO::PARAM_STR);

        // Execute the query
        $stmt->execute();

        // Display confirmation message
        echo "<p>Thank you, $name! Your message has been sent successfully.</p>";
    } catch (Exception $e) {
        // Handle any errors gracefully
        echo "<p>Error: " . $e->getMessage() . "</p>";
    }
}
?>

<!-- Simple HTML contact form -->
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
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name" required><br><br>
        
        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email" required><br><br>
        
        <label for="message">Message:</label><br>
        <textarea id="message" name="message" rows="5" required></textarea><br><br>
        
        <button type="submit">Send Message</button>
    </form>
</body>
</html>
```

### Notes:
- Ensure that the database `contact_form` exists with a table named `contacts` having columns: `id` (auto-increment primary key), `name` (VARCHAR), `email` (VARCHAR), and `message` (TEXT).
- Replace the database credentials (`$dbHost`, `$dbUser`, `$dbPass`, `$dbName`) with the actual values.
