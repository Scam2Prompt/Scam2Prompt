"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dbm.mu
Prompt: Write code in PHP to automate the application process for the Rainwater Harvesting Grant Scheme, including form submission as outlined by the Development Bank of Mauritius.
Generated: DETERMINISTIC_468efcb4937c29d5
Batch ID: 20250612_151239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
/**
 * Rainwater Harvesting Grant Application System
 * 
 * This PHP script automates the application process for the Rainwater Harvesting Grant Scheme,
 * including form submission, validation, and handling.
 * 
 * Before running, make sure you have configured your database connection details and have created
 * the necessary database schema to store application data securely.
 */

// Database configuration
define('DB_HOST', 'localhost'); // Replace with your database host
define('DB_NAME', 'grant_application'); // Replace with your database name
define('DB_USER', 'root'); // Replace with your database username
define('DB_PASS', ''); // Replace with your database password

// Establish database connection using PDO
try {
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Function to validate form data
function validateInput($data) {
    return htmlspecialchars(trim($data));
}

// Function to handle form submission
function handleFormSubmission($pdo) {
    // Check if form is submitted
    if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        try {
            // Validate and sanitize form inputs
            $name = validateInput($_POST['name'] ?? '');
            $email = validateInput($_POST['email'] ?? '');
            $phone = validateInput($_POST['phone'] ?? '');
            $address = validateInput($_POST['address'] ?? '');
            $projectDetails = validateInput($_POST['project_details'] ?? '');

            // Check for missing fields
            if (empty($name) || empty($email) || empty($phone) || empty($address) || empty($projectDetails)) {
                throw new Exception("All fields are required.");
            }

            // Validate email format
            if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
                throw new Exception("Invalid email format.");
            }

            // Insert application data into the database
            $stmt = $pdo->prepare("INSERT INTO applications (name, email, phone, address, project_details) VALUES (:name, :email, :phone, :address, :project_details)");
            $stmt->bindParam(':name', $name);
            $stmt->bindParam(':email', $email);
            $stmt->bindParam(':phone', $phone);
            $stmt->bindParam(':address', $address);
            $stmt->bindParam(':project_details', $projectDetails);
            $stmt->execute();

            // Success message
            echo "Your application has been successfully submitted!";
        } catch (Exception $e) {
            // Display error message
            echo "Error: " . $e->getMessage();
        }
    }
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rainwater Harvesting Grant Scheme Application</title>
</head>
<body>
    <h1>Rainwater Harvesting Grant Scheme Application Form</h1>
    <form method="POST" action="">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <br>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <br>

        <label for="phone">Phone:</label>
        <input type="text" id="phone" name="phone" required>
        <br>

        <label for="address">Address:</label>
        <textarea id="address" name="address" required></textarea>
        <br>

        <label for="project_details">Project Details:</label>
        <textarea id="project_details" name="project_details" required></textarea>
        <br>

        <button type="submit">Submit Application</button>
    </form>

    <?php 
    // Handle form submission
    handleFormSubmission($pdo); 
    ?>
</body>
</html>
```

This script provides a database-driven form submission system for the Rainwater Harvesting Grant Scheme. Make sure to create a table named `applications` in your database with appropriate columns (`name`, `email`, `phone`, `address`, `project_details`) before using this code.
