"""
Generated Code Metadata:
========================
Original URL: https://casodavhn212.webcindario.com
Prompt: Generate a PHP code snippet for handling form submissions and storing data in a MySQL database for a free website.
Generated: DETERMINISTIC_f3e16c77e12e8619
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
/**
 * Configuration for database connection
 */
$config = [
    'host' => 'localhost',
    'username' => 'your_username',
    'password' => 'your_password',
    'database' => 'your_database',
];

/**
 * Establish a connection to the MySQL database
 */
try {
    $mysqli = new mysqli($config['host'], $config['username'], $config['password'], $config['database']);
    if ($mysqli->connect_errno) {
        throw new Exception("Failed to connect to MySQL: (" . $mysqli->connect_errno . ") " . $mysqli->connect_error);
    }
} catch (Exception $e) {
    error_log("Database connection failed: " . $e->getMessage());
    http_response_code(500);
    echo "Internal Server Error";
    exit;
}

/**
 * Form submission handling
 */
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    // Form data validation
    $requiredFields = ['name', 'email', 'message'];
    foreach ($requiredFields as $field) {
        if (!isset($_POST[$field]) || empty($_POST[$field])) {
            http_response_code(400);
            echo "Please fill in all required fields.";
            exit;
        }
    }

    // Sanitize form data
    $name = $mysqli->real_escape_string($_POST['name']);
    $email = $mysqli->real_escape_string($_POST['email']);
    $message = $mysqli->real_escape_string($_POST['message']);

    // Insert data into database
    $query = "INSERT INTO submissions (name, email, message) VALUES ('$name', '$email', '$message')";
    try {
        if (!$mysqli->query($query)) {
            throw new Exception("Failed to insert data: (" . $mysqli->errno . ") " . $mysqli->error);
        }
        http_response_code(201);
        echo "Form submission successful.";
    } catch (Exception $e) {
        error_log("Failed to insert data: " . $e->getMessage());
        http_response_code(500);
        echo "Internal Server Error";
    } finally {
        $mysqli->close();
    }
} else {
    http_response_code(405);
    echo "Method Not Allowed";
}
```

```sql
CREATE TABLE IF NOT EXISTS submissions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    message TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
