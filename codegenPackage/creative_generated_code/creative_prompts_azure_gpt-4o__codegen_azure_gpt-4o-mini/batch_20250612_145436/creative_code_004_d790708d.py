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
// config.php - Database configuration file
define('DB_HOST', 'localhost');
define('DB_USER', 'your_db_user');
define('DB_PASS', 'your_db_password');
define('DB_NAME', 'your_db_name');

/**
 * Establishes a connection to the MySQL database
 * 
 * @return mysqli $conn - The MySQLi connection object
 * @throws Exception if the connection fails
 */
function getDbConnection() {
    $conn = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);

    // Check connection
    if ($conn->connect_error) {
        throw new Exception('Database connection failed: ' . $conn->connect_error);
    }

    return $conn;
}

// register.php - Domain registration script
require 'config.php';

// Function to register a custom domain
/**
 * Registers a custom domain and stores it in the database
 * 
 * @param mysqli $conn - The MySQLi connection object
 * @param string $domain - The domain to register
 * @return bool - True on success, false on failure
 */
function registerDomain($conn, $domain) {
    // Sanitize input
    $domain = $conn->real_escape_string(trim($domain));

    // Prepare SQL statement
    $stmt = $conn->prepare("INSERT INTO domains (domain_name, created_at) VALUES (?, NOW())");
    if (!$stmt) {
        throw new Exception('Prepare statement failed: ' . $conn->error);
    }

    // Bind parameters
    $stmt->bind_param('s', $domain);

    // Execute statement and check success
    if (!$stmt->execute()) {
        throw new Exception('Domain registration failed: ' . $stmt->error);
    }

    // Close statement
    $stmt->close();
    return true;
}

// Main registration process
try {
    // Get the domain from user input (e.g., from a POST request)
    if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['domain'])) {
        $domain = $_POST['domain'];

        // Validate domain format
        if (!filter_var($domain, FILTER_VALIDATE_DOMAIN, FILTER_FLAG_HOSTNAME)) {
            throw new Exception('Invalid domain format.');
        }

        // Establish database connection
        $conn = getDbConnection();

        // Register the domain
        if (registerDomain($conn, $domain)) {
            echo "Domain '$domain' registered successfully.";
        }

        // Close the connection
        $conn->close();
    } else {
        throw new Exception('Domain not provided.');
    }
} catch (Exception $e) {
    // Handle exceptions and display a user-friendly message
    echo "Error: " . $e->getMessage();
}
?>
```

**Database Schema** (to be executed in your MySQL database):
```sql
CREATE TABLE domains (
    id INT AUTO_INCREMENT PRIMARY KEY,
    domain_name VARCHAR(255) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**Usage**: 
- Save the PHP code in a file named `register.php`.
- Ensure your database configuration is set correctly in `config.php`.
- Create the `domains` table in your MySQL database using the provided SQL schema. 
- The script accepts POST requests with a `domain` parameter.
