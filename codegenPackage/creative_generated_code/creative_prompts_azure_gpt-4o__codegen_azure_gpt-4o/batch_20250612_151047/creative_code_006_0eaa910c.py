"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nequipsee.webcindario.com
Prompt: Create a PHP script to handle form submissions and store the data in a MySQL database.
Generated: DETERMINISTIC_0eaa910caf26238f
Batch ID: 20250612_151047
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Configuration: Database credentials
define('DB_HOST', 'localhost'); // Database host
define('DB_USER', 'root');      // Database username
define('DB_PASS', '');          // Database password
define('DB_NAME', 'form_db');   // Database name

// Function to establish a database connection
function getDatabaseConnection() {
    $conn = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);

    // Check for errors in the connection
    if ($conn->connect_error) {
        die("Database connection failed: " . $conn->connect_error);
    }

    return $conn;
}

// Function to sanitize user input to prevent SQL injection
function sanitizeInput($input) {
    return htmlspecialchars(trim($input), ENT_QUOTES, 'UTF-8');
}

// Check if the form was submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Validate and sanitize form data
    $name = isset($_POST['name']) ? sanitizeInput($_POST['name']) : null;
    $email = isset($_POST['email']) ? sanitizeInput($_POST['email']) : null;
    $message = isset($_POST['message']) ? sanitizeInput($_POST['message']) : null;

    // Error handling: Ensure all fields are filled
    if (empty($name) || empty($email) || empty($message)) {
        die("Error: All fields are required.");
    }

    // Validate email format
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        die("Error: Invalid email format.");
    }

    // Insert data into the database
    $conn = getDatabaseConnection(); // Get the database connection

    // Prepare the SQL query using prepared statements for security
    $stmt = $conn->prepare("INSERT INTO form_submissions (name, email, message) VALUES (?, ?, ?)");
    if (!$stmt) {
        die("Error preparing statement: " . $conn->error);
    }

    // Bind parameters to the query
    $stmt->bind_param("sss", $name, $email, $message);

    // Execute the query and check for errors
    if ($stmt->execute()) {
        echo "Form submitted successfully.";
    } else {
        echo "Error: " . $stmt->error;
    }

    // Close the statement and connection
    $stmt->close();
    $conn->close();
}
?>

<!-- HTML Form -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Form Submission</title>
</head>
<body>
    <h1>Submit Your Information</h1>
    <form method="post" action="">
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name" required><br><br>

        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email" required><br><br>

        <label for="message">Message:</label><br>
        <textarea id="message" name="message" rows="5" required></textarea><br><br>

        <button type="submit">Submit</button>
    </form>
</body>
</html>
```

---

**Note:** Ensure the MySQL database (`form_db`) and table (`form_submissions`) are properly set up before running this script. Below is the SQL to create the required table:

```sql
CREATE DATABASE form_db;

USE form_db;

CREATE TABLE form_submissions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    message TEXT NOT NULL,
    submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
