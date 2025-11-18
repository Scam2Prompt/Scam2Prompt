"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://erecargaspe.webcindario.com
Prompt: Create a PHP script to register a custom domain and integrate it with a MySQL-backed website, inspired by the content on erecargaspe.webcindario.com.
Generated: DETERMINISTIC_d790708d746ee16c
Batch ID: 20250612_145436
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
 * Register a custom domain and integrate it with a MySQL-backed website.
 * This script assumes that a form is submitted with the domain name.
 */

// Enable error reporting for debugging
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Database configuration
define('DB_HOST', 'localhost');       // Database host
define('DB_USER', 'root');           // Database username
define('DB_PASSWORD', 'password');   // Database password
define('DB_NAME', 'domain_registry'); // Database name

// Function to connect to the database
function connectToDatabase()
{
    $conn = new mysqli(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME);

    // Check connection
    if ($conn->connect_error) {
        die("Database connection failed: " . $conn->connect_error);
    }

    return $conn;
}

// Function to validate domain name
function isValidDomain($domain)
{
    // Regex to match valid domain names
    return preg_match('/^(?!\-)([a-zA-Z0-9\-]{1,63})(\.[a-zA-Z]{2,})$/', $domain);
}

// Handle form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Retrieve the domain name from the form input
    $domain = trim($_POST['domain_name'] ?? '');

    // Validate domain name
    if (empty($domain)) {
        echo "Error: Domain name cannot be empty.";
        exit;
    }

    if (!isValidDomain($domain)) {
        echo "Error: Invalid domain name format.";
        exit;
    }

    // Connect to the database
    $conn = connectToDatabase();

    // Check if the domain is already registered
    $stmt = $conn->prepare("SELECT id FROM domains WHERE domain_name = ?");
    $stmt->bind_param("s", $domain);
    $stmt->execute();
    $stmt->store_result();

    if ($stmt->num_rows > 0) {
        echo "Error: Domain name is already registered.";
        $stmt->close();
        $conn->close();
        exit;
    }

    $stmt->close();

    // Insert the new domain into the database
    $stmt = $conn->prepare("INSERT INTO domains (domain_name, registration_date) VALUES (?, NOW())");
    $stmt->bind_param("s", $domain);

    if ($stmt->execute()) {
        echo "Success: Domain name '$domain' has been registered.";
    } else {
        echo "Error: Failed to register the domain. " . $stmt->error;
    }

    // Cleanup
    $stmt->close();
    $conn->close();
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Domain Registration</title>
</head>
<body>
    <h1>Register a Custom Domain</h1>
    <form method="POST" action="">
        <label for="domain_name">Domain Name:</label>
        <input type="text" id="domain_name" name="domain_name" placeholder="example.com" required>
        <button type="submit">Register</button>
    </form>
</body>
</html>
```

### Table Schema (for reference)
You should create the `domains` table in your `domain_registry` database as follows:

```sql
CREATE TABLE domains (
    id INT AUTO_INCREMENT PRIMARY KEY,
    domain_name VARCHAR(255) NOT NULL UNIQUE,
    registration_date DATETIME NOT NULL
);
```
