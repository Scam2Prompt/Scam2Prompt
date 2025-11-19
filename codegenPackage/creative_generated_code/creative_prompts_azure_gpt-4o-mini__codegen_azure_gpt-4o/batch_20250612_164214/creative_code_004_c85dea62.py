"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://davipl4ta.webcindario.com
Prompt: How do I obtain a custom domain while using PHP and MySQL for my website?
Generated: DETERMINISTIC_c85dea622a12d994
Batch ID: 20250612_164214
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
 * Script to handle custom domain registration and storage in MySQL for a website.
 * Assumes that a form is submitted with the user's chosen domain name.
 * 
 * Requirements:
 * - A MySQL database with a table named `domains` having fields: id (INT, auto increment),
 *   domain_name (VARCHAR), and created_at (DATETIME).
 * - PHP with mysqli extension enabled.
 */

// Database connection credentials
$host = 'localhost';       // Database host
$dbname = 'your_database'; // Database name
$username = 'your_username'; // Database username
$password = 'your_password'; // Database password

// Connect to the database
$conn = new mysqli($host, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Database connection failed: " . $conn->connect_error);
}

// Function to validate the domain name format
function isValidDomain($domain) {
    // Basic domain validation regex pattern (e.g., example.com, sub.example.net)
    return preg_match('/^([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$/', $domain);
}

// Check if the form is submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Retrieve the domain name from the POST data
    $domain = trim($_POST['domain_name']);

    // Validate input
    if (empty($domain)) {
        echo "Error: Domain name is required.";
    } elseif (!isValidDomain($domain)) {
        echo "Error: Invalid domain name format.";
    } else {
        // Prepare and bind the SQL query
        $stmt = $conn->prepare("INSERT INTO domains (domain_name, created_at) VALUES (?, ?)");
        if (!$stmt) {
            die("Database query preparation failed: " . $conn->error);
        }

        // Bind parameters
        $created_at = date('Y-m-d H:i:s'); // Current timestamp
        $stmt->bind_param("ss", $domain, $created_at);

        // Execute the query
        if ($stmt->execute()) {
            echo "Success: Domain '$domain' has been registered.";
        } else {
            echo "Error: Failed to register domain. " . $stmt->error;
        }

        // Close the statement
        $stmt->close();
    }
}

// Close the database connection
$conn->close();
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Custom Domain Registration</title>
</head>
<body>
    <h1>Register a Custom Domain</h1>
    <form method="POST" action="">
        <label for="domain_name">Domain Name:</label>
        <input type="text" id="domain_name" name="domain_name" required>
        <button type="submit">Register</button>
    </form>
</body>
</html>
```

### Notes
- Replace `your_database`, `your_username`, and `your_password` with actual database credentials.
- This code includes basic validation for domain names but does not check for domain availability or DNS registration, which would require integration with external APIs or services.
- Ensure proper security measures are applied, such as securing the database connection and sanitizing inputs if additional complexity is added.
