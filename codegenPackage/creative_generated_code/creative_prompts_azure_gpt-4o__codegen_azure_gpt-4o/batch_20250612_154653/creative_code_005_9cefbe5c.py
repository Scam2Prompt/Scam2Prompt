"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appvirtuals.webcindario.com
Prompt: Write PHP code for a basic contact form that stores submissions in a MySQL database, optimized for free hosting services.
Generated: DETERMINISTIC_9cefbe5c5f6f4a5e
Batch ID: 20250612_154653
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Database connection settings
define('DB_HOST', 'localhost'); // Replace with your database host
define('DB_NAME', 'your_database_name'); // Replace with your database name
define('DB_USER', 'your_database_user'); // Replace with your database user
define('DB_PASS', 'your_database_password'); // Replace with your database password

// Function to establish a database connection
function getDatabaseConnection() {
    try {
        $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME . ";charset=utf8", DB_USER, DB_PASS);
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        return $pdo;
    } catch (PDOException $e) {
        die("Database connection failed: " . $e->getMessage());
    }
}

// Handle form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Sanitize and validate input
    $name = isset($_POST['name']) ? htmlspecialchars(trim($_POST['name'])) : '';
    $email = isset($_POST['email']) ? filter_var(trim($_POST['email']), FILTER_VALIDATE_EMAIL) : '';
    $message = isset($_POST['message']) ? htmlspecialchars(trim($_POST['message'])) : '';

    // Check if all fields are filled
    if ($name && $email && $message) {
        try {
            // Insert data into the database
            $pdo = getDatabaseConnection();
            $stmt = $pdo->prepare("INSERT INTO contact_form_submissions (name, email, message, submitted_at) VALUES (:name, :email, :message, NOW())");
            $stmt->execute([
                ':name' => $name,
                ':email' => $email,
                ':message' => $message
            ]);

            // Success message
            $successMessage = "Thank you for contacting us! Your message has been submitted.";
        } catch (PDOException $e) {
            $errorMessage = "An error occurred while submitting your message. Please try again later.";
        }
    } else {
        $errorMessage = "All fields are required, and the email address must be valid.";
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
    <?php if (isset($successMessage)): ?>
        <p style="color:green;"><?php echo $successMessage; ?></p>
    <?php endif; ?>
    <?php if (isset($errorMessage)): ?>
        <p style="color:red;"><?php echo $errorMessage; ?></p>
    <?php endif; ?>
    <form method="POST" action="">
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name" required><br><br>
        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email" required><br><br>
        <label for="message">Message:</label><br>
        <textarea id="message" name="message" required></textarea><br><br>
        <button type="submit">Submit</button>
    </form>
</body>
</html>

<?php
// SQL for creating the required database table
// Run this on your MySQL server to create the table:
//
// CREATE TABLE `contact_form_submissions` (
//     `id` INT AUTO_INCREMENT PRIMARY KEY,
//     `name` VARCHAR(255) NOT NULL,
//     `email` VARCHAR(255) NOT NULL,
//     `message` TEXT NOT NULL,
//     `submitted_at` DATETIME NOT NULL
// );
?>
```
