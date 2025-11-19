"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-cryptosoft-pro.com
Prompt: Develop a PHP application that allows users to report fraudulent investment schemes, similar to the actions taken against the platform discussed on thecryptosoft-pro.com.
Generated: DETERMINISTIC_519450bc0c62ee0e
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// fraud_report.php

// Start a new session or resume the existing session
session_start();

// Database connection settings
$host = 'localhost';
$db = 'fraud_reports';
$user = 'root';
$pass = 'password';

// Create a new PDO instance for database connection with error handling
try {
    $pdo = new PDO("mysql:host=$host;dbname=$db", $user, $pass);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Function to sanitize user input
function sanitizeInput($data) {
    return htmlspecialchars(strip_tags(trim($data)));
}

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Collect and sanitize form data
    $reporter_name = sanitizeInput($_POST['reporter_name']);
    $email = sanitizeInput($_POST['email']);
    $scheme_details = sanitizeInput($_POST['scheme_details']);
    
    // Validate input data
    if (empty($reporter_name) || empty($email) || empty($scheme_details)) {
        $error_message = "All fields are required.";
    } elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $error_message = "Invalid email format.";
    } else {
        // Prepare and execute SQL statement to insert report into the database
        try {
            $stmt = $pdo->prepare("INSERT INTO reports (reporter_name, email, scheme_details, created_at) VALUES (?, ?, ?, NOW())");
            $stmt->execute([$reporter_name, $email, $scheme_details]);
            $success_message = "Report submitted successfully.";
        } catch (PDOException $e) {
            $error_message = "Error submitting report: " . $e->getMessage();
        }
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Report Fraudulent Investment Scheme</title>
    <link rel="stylesheet" href="styles.css"> <!-- Include your CSS file -->
</head>
<body>
    <h1>Report Fraudulent Investment Scheme</h1>

    <?php
    // Display success or error messages
    if (isset($success_message)) {
        echo "<p class='success'>$success_message</p>";
    }
    if (isset($error_message)) {
        echo "<p class='error'>$error_message</p>";
    }
    ?>

    <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="POST">
        <label for="reporter_name">Your Name:</label>
        <input type="text" id="reporter_name" name="reporter_name" required>

        <label for="email">Your Email:</label>
        <input type="email" id="email" name="email" required>

        <label for="scheme_details">Details of the Scheme:</label>
        <textarea id="scheme_details" name="scheme_details" required></textarea>

        <button type="submit">Submit Report</button>
    </form>
</body>
</html>
```

### SQL Table Creation Script
Make sure to create the following table in your MySQL database.

```sql
CREATE TABLE reports (
    id INT AUTO_INCREMENT PRIMARY KEY,
    reporter_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    scheme_details TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Notes
- Ensure that your database connection credentials are correct.
- The `styles.css` file should be created to style the form and messages as needed.
- Always ensure that you have the necessary security measures in place when handling user input, such as prepared statements and data sanitization.
