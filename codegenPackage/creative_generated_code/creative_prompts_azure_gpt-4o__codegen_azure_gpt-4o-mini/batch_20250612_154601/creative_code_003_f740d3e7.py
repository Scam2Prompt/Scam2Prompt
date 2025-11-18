"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solutechsystem.com.ng
Prompt: Write a PHP script to manage donations for an NGO website, incorporating user-friendly features inspired by Solutech System's NGO website design offerings.
Generated: DETERMINISTIC_f740d3e788372dcf
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// donation_manager.php
/**
 * Donation Manager for NGO Website
 * This script handles donations including displaying a donation form,
 * processing donations, and showing a thank you message.
 */

// Start session for user feedback and error tracking
session_start();

// Database configuration (update these with your actual database credentials)
define('DB_HOST', 'localhost');
define('DB_USER', 'username');
define('DB_PASS', 'password');
define('DB_NAME', 'ngo_donations');

// Function to connect to the database
function connectDb() {
    $connection = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
    
    // Check for connection errors
    if ($connection->connect_error) {
        die("Connection failed: " . $connection->connect_error);
    }
    return $connection;
}

// Function to handle donation processing
function processDonation($name, $email, $amount) {
    // Sanitize inputs to prevent SQL injection
    $name = htmlspecialchars(strip_tags($name));
    $email = htmlspecialchars(strip_tags($email));
    $amount = filter_var($amount, FILTER_SANITIZE_NUMBER_FLOAT, FILTER_FLAG_ALLOW_FRACTION);

    // Validate inputs
    if (empty($name) || empty($email) || !filter_var($email, FILTER_VALIDATE_EMAIL) || $amount <= 0) {
        return false; // Return false for invalid input
    }

    // Connect to the database
    $connection = connectDb();

    // Prepare SQL statement to prevent SQL injection
    $stmt = $connection->prepare("INSERT INTO donations (name, email, amount, donation_date) VALUES (?, ?, ?, NOW())");
    $stmt->bind_param("ssd", $name, $email, $amount);
    
    // Execute the statement and check for errors
    if ($stmt->execute()) {
        $stmt->close();
        $connection->close();
        return true; // Donation processed successfully
    } else {
        $stmt->close();
        $connection->close();
        return false; // Donation processing failed
    }
}

// Check if the form is submitted
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $name = $_POST['name'] ?? '';
    $email = $_POST['email'] ?? '';
    $amount = $_POST['amount'] ?? 0;

    // Process the donation
    if (processDonation($name, $email, $amount)) {
        $_SESSION['success'] = "Thank you for your generous donation!";
    } else {
        $_SESSION['error'] = "There was an error processing your donation. Please try again.";
    }

    // Redirect to the same page to prevent form resubmission
    header("Location: " . $_SERVER['PHP_SELF']);
    exit();
}

// Display any session messages
$successMessage = $_SESSION['success'] ?? '';
$errorMessage = $_SESSION['error'] ?? '';
unset($_SESSION['success'], $_SESSION['error']); // Clear messages after displaying them
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Donate to Our NGO</title>
    <link rel="stylesheet" href="styles.css"> <!-- Include your CSS file -->
</head>
<body>
    <h1>Support Our Cause</h1>

    <!-- Display success or error messages -->
    <?php if ($successMessage): ?>
        <div class="alert alert-success"><?php echo $successMessage; ?></div>
    <?php endif; ?>
    <?php if ($errorMessage): ?>
        <div class="alert alert-danger"><?php echo $errorMessage; ?></div>
    <?php endif; ?>

    <!-- Donation Form -->
    <form method="POST" action="">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>

        <label for="amount">Donation Amount ($):</label>
        <input type="number" id="amount" name="amount" step="0.01" required>

        <button type="submit">Donate</button>
    </form>
</body>
</html>
```
