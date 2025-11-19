"""
Generated Code Metadata:
========================
Original URL: https://baliauthenticcoffeeandgallery.com
Prompt: "Develop a customer newsletter subscription system using PHP and MySQL for a WordPress site like baliauthenticcoffeeandgallery.com, including functionality for product announcements and offers."
Generated: DETERMINISTIC_5be5af27d897df4e
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// newsletter_subscription.php

// Database configuration
$host = 'localhost'; // Database host
$dbname = 'your_database_name'; // Database name
$username = 'your_username'; // Database username
$password = 'your_password'; // Database password

// Create a connection to the database
try {
    $pdo = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection error
    die("Connection failed: " . $e->getMessage());
}

// Function to subscribe a user to the newsletter
function subscribeUser($email) {
    global $pdo;

    // Validate email format
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        return "Invalid email format.";
    }

    // Check if the email is already subscribed
    $stmt = $pdo->prepare("SELECT * FROM newsletter_subscribers WHERE email = :email");
    $stmt->execute(['email' => $email]);
    
    if ($stmt->rowCount() > 0) {
        return "This email is already subscribed.";
    }

    // Insert the email into the database
    $stmt = $pdo->prepare("INSERT INTO newsletter_subscribers (email, subscribed_at) VALUES (:email, NOW())");
    if ($stmt->execute(['email' => $email])) {
        return "Subscription successful!";
    } else {
        return "Subscription failed. Please try again.";
    }
}

// Handle form submission
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $email = trim($_POST['email']);
    $message = subscribeUser($email);
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Newsletter Subscription</title>
    <link rel="stylesheet" href="style.css"> <!-- Link to your CSS file -->
</head>
<body>
    <div class="subscription-form">
        <h2>Subscribe to Our Newsletter</h2>
        <?php if (isset($message)) : ?>
            <p><?php echo htmlspecialchars($message); ?></p>
        <?php endif; ?>
        <form action="" method="POST">
            <input type="email" name="email" placeholder="Enter your email" required>
            <button type="submit">Subscribe</button>
        </form>
    </div>
</body>
</html>
```

```sql
-- SQL script to create the newsletter_subscribers table

CREATE TABLE newsletter_subscribers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    subscribed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Notes:
- Replace `your_database_name`, `your_username`, and `your_password` with your actual database credentials.
- Ensure that the database connection is secure and that you handle sensitive information appropriately.
- The HTML form is basic; you may want to style it further with CSS.
- This code assumes you have a MySQL database set up and accessible from your PHP environment.
