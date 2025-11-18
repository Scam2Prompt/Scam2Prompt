"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://casodavhn212.webcindario.com
Prompt: Generate a PHP code snippet for handling form submissions and storing data in a MySQL database for a free website.
Generated: DETERMINISTIC_f3e16c77e12e8619
Batch ID: 20250612_151354
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
$host = 'localhost'; // Database host
$dbName = 'your_database_name'; // Database name
$dbUser = 'your_database_user'; // Database username
$dbPass = 'your_database_password'; // Database password

// Establish a connection to the database
try {
    $pdo = new PDO("mysql:host=$host;dbname=$dbName;charset=utf8mb4", $dbUser, $dbPass);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION); // Enable error handling
} catch (PDOException $e) {
    // Handle connection errors
    die('Database connection failed: ' . $e->getMessage());
}

// Check if the form was submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Sanitize and validate input data
    $name = htmlspecialchars(trim($_POST['name'] ?? ''));
    $email = htmlspecialchars(trim($_POST['email'] ?? ''));
    $message = htmlspecialchars(trim($_POST['message'] ?? ''));

    // Error handling for empty fields
    if (empty($name) || empty($email) || empty($message)) {
        die('All fields are required.');
    }

    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        die('Invalid email format.');
    }

    try {
        // Prepare an SQL statement to prevent SQL injection
        $stmt = $pdo->prepare("INSERT INTO submissions (name, email, message, submitted_at) VALUES (:name, :email, :message, NOW())");

        // Bind parameters and execute the query
        $stmt->bindParam(':name', $name, PDO::PARAM_STR);
        $stmt->bindParam(':email', $email, PDO::PARAM_STR);
        $stmt->bindParam(':message', $message, PDO::PARAM_STR);

        if ($stmt->execute()) {
            echo 'Form submitted successfully!';
        } else {
            echo 'Failed to submit the form.';
        }
    } catch (PDOException $e) {
        // Handle query errors
        die('Error submitting data: ' . $e->getMessage());
    }
} else {
    echo 'Invalid request method.';
}
?>
```

Before using this code, make sure to create a database table named `submissions` with the following structure:
```sql
CREATE TABLE submissions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    message TEXT NOT NULL,
    submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
