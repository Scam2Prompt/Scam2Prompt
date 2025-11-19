"""
Generated Code Metadata:
========================
Original URL: https://solutechsystem.com.ng
Prompt: Write a PHP script to manage donations for an NGO website, incorporating user-friendly features inspired by Solutech System's NGO website design offerings.
Generated: DETERMINISTIC_f740d3e788372dcf
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// donation_manager.php

// Start the session to manage user data
session_start();

// Database connection parameters
$host = 'localhost';
$db = 'ngo_donations';
$user = 'root';
$pass = 'password'; // Change this to your database password

// Create a connection to the database
try {
    $pdo = new PDO("mysql:host=$host;dbname=$db", $user, $pass);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Function to handle donation submission
function submitDonation($name, $email, $amount) {
    global $pdo;

    // Validate input
    if (empty($name) || empty($email) || empty($amount) || !is_numeric($amount) || $amount <= 0) {
        throw new InvalidArgumentException("Invalid input data.");
    }

    // Prepare SQL statement to insert donation
    $stmt = $pdo->prepare("INSERT INTO donations (name, email, amount, donation_date) VALUES (:name, :email, :amount, NOW())");

    // Bind parameters and execute
    $stmt->bindParam(':name', $name);
    $stmt->bindParam(':email', $email);
    $stmt->bindParam(':amount', $amount);

    if ($stmt->execute()) {
        return true;
    } else {
        throw new Exception("Failed to record donation.");
    }
}

// Handle form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    try {
        // Retrieve and sanitize input data
        $name = htmlspecialchars(trim($_POST['name']));
        $email = htmlspecialchars(trim($_POST['email']));
        $amount = htmlspecialchars(trim($_POST['amount']));

        // Submit the donation
        submitDonation($name, $email, $amount);

        // Set success message
        $_SESSION['message'] = "Thank you for your generous donation!";
        header("Location: thank_you.php");
        exit();
    } catch (Exception $e) {
        // Set error message
        $_SESSION['error'] = $e->getMessage();
        header("Location: donation_form.php");
        exit();
    }
}

// HTML form for donation submission
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Donate to Our NGO</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to your CSS file -->
</head>
<body>
    <div class="container">
        <h1>Make a Donation</h1>
        <?php
        // Display error or success messages
        if (isset($_SESSION['error'])) {
            echo "<div class='error'>{$_SESSION['error']}</div>";
            unset($_SESSION['error']);
        }
        if (isset($_SESSION['message'])) {
            echo "<div class='success'>{$_SESSION['message']}</div>";
            unset($_SESSION['message']);
        }
        ?>
        <form action="donation_manager.php" method="POST">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>

            <label for="amount">Donation Amount:</label>
            <input type="number" id="amount" name="amount" required min="1">

            <button type="submit">Donate</button>
        </form>
    </div>
</body>
</html>
```

**Note:** Ensure you have a database named `ngo_donations` with a table `donations` structured as follows:

```sql
CREATE TABLE donations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    donation_date DATETIME NOT NULL
);
```

Make sure to adjust the database connection parameters as needed for your environment.
