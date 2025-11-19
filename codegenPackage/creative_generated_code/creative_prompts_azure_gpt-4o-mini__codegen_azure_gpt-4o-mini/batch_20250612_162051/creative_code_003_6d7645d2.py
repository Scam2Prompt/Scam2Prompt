"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scout.kz
Prompt: Develop a PHP script that allows users to submit a request for a customized tractor offer from SCOUT, including their specific requirements and budget.
Generated: DETERMINISTIC_6d7645d2421a3680
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Start the session to store user data
session_start();

// Constants for database connection
define('DB_SERVER', 'localhost');
define('DB_USERNAME', 'username');
define('DB_PASSWORD', 'password');
define('DB_DATABASE', 'database');

// Create a function to establish a database connection
function getDatabaseConnection() {
    $conn = new mysqli(DB_SERVER, DB_USERNAME, DB_PASSWORD, DB_DATABASE);

    // Check for connection errors
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }
    return $conn;
}

// Function to handle form submission
function handleRequestForm($data) {
    // Validate input data
    $requiredFields = ['name', 'email', 'requirements', 'budget'];
    foreach ($requiredFields as $field) {
        if (empty($data[$field])) {
            throw new Exception("The field '$field' is required.");
        }
    }

    // Sanitize input data
    $name = htmlspecialchars($data['name']);
    $email = htmlspecialchars($data['email']);
    $requirements = htmlspecialchars($data['requirements']);
    $budget = floatval($data['budget']);

    // Establish database connection
    $conn = getDatabaseConnection();

    // Prepare and bind the SQL statement
    $stmt = $conn->prepare("INSERT INTO tractor_requests (name, email, requirements, budget) VALUES (?, ?, ?, ?)");
    if (!$stmt) {
        throw new Exception("Database preparation failed: " . $conn->error);
    }
    $stmt->bind_param("sssd", $name, $email, $requirements, $budget);

    // Execute the statement and check for errors
    if (!$stmt->execute()) {
        throw new Exception("Database execution failed: " . $stmt->error);
    }

    // Close the statement and connection
    $stmt->close();
    $conn->close();

    // Return success message
    return "Your request has been submitted successfully!";
}

// Handle POST request to submit the form
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    try {
        $message = handleRequestForm($_POST);
        $_SESSION['success_message'] = $message;
    } catch (Exception $e) {
        $_SESSION['error_message'] = $e->getMessage();
    }
    // Redirect to the form page to show the result
    header("Location: request_form.php");
    exit();
}
?>

<!-- HTML Form for User Input -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Request Customized Tractor Offer</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Request a Customized Tractor Offer</h1>
    <?php
    // Display success or error messages
    if (isset($_SESSION['success_message'])) {
        echo "<p class='success'>" . $_SESSION['success_message'] . "</p>";
        unset($_SESSION['success_message']);
    }
    if (isset($_SESSION['error_message'])) {
        echo "<p class='error'>" . $_SESSION['error_message'] . "</p>";
        unset($_SESSION['error_message']);
    }
    ?>
    <form method="POST" action="">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>

        <label for="requirements">Requirements:</label>
        <textarea id="requirements" name="requirements" required></textarea>

        <label for="budget">Budget:</label>
        <input type="number" id="budget" name="budget" step="0.01" required>

        <button type="submit">Submit Request</button>
    </form>
</body>
</html>
```
