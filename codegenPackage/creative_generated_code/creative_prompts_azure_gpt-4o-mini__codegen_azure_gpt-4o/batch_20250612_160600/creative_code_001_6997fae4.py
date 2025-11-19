"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbasepromo.webcindario.com
Prompt: What are the steps to set up a custom domain for a free website using PHP and MySQL?
Generated: DETERMINISTIC_6997fae470478fb7
Batch ID: 20250612_160600
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
 * Script for setting up a custom domain for a free website using PHP and MySQL
 * Assumes you already have a MySQL database setup and a web server configured
 * This example uses PDO for database interaction and follows best practices
 */

// Database configuration
define('DB_HOST', 'localhost'); // Replace with your database host
define('DB_NAME', 'custom_domain_db'); // Replace with your database name
define('DB_USER', 'root'); // Replace with your database user
define('DB_PASS', 'password'); // Replace with your database password

try {
    // Create a connection to the database using PDO
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle database connection errors
    die("Database connection failed: " . $e->getMessage());
}

// Function to add a new custom domain for a website
function addCustomDomain($websiteId, $domainName) {
    global $pdo;

    try {
        // Validate inputs
        if (empty($websiteId) || empty($domainName)) {
            throw new Exception("Website ID and domain name are required.");
        }

        // Check if the domain name already exists
        $stmt = $pdo->prepare("SELECT * FROM domains WHERE domain_name = :domain_name");
        $stmt->execute(['domain_name' => $domainName]);
        if ($stmt->rowCount() > 0) {
            throw new Exception("The domain is already in use.");
        }

        // Insert the new domain into the database
        $stmt = $pdo->prepare("INSERT INTO domains (website_id, domain_name) VALUES (:website_id, :domain_name)");
        $stmt->execute(['website_id' => $websiteId, 'domain_name' => $domainName]);

        return "Custom domain added successfully.";
    } catch (Exception $e) {
        // Handle errors gracefully and return a user-friendly message
        return "Error: " . $e->getMessage();
    }
}

// Example usage
$websiteId = 1; // Replace with the actual website ID
$domainName = "example.com"; // Replace with the desired custom domain

$result = addCustomDomain($websiteId, $domainName);
echo $result;

?>
```

**Database Schema (MySQL)**:
```sql
CREATE TABLE websites (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE domains (
    id INT AUTO_INCREMENT PRIMARY KEY,
    website_id INT NOT NULL,
    domain_name VARCHAR(255) NOT NULL,
    FOREIGN KEY (website_id) REFERENCES websites(id),
    UNIQUE (domain_name)
);
```
rId = 123; // Typically retrieved from session or authentication system
$customDomain = "mycustomdomain.com"; // Provided by the user (e.g., via a form)

// Call the function and display the result
$result = configureCustomDomain($userId, $customDomain);
echo $result;

?>
```

### Key Points:
- Replace `DB_HOST`, `DB_USER`, `DB_PASSWORD`, and `DB_NAME` with your actual database credentials.
- Set up a database table named `domain_mapping` as described in the comments.
- The script includes proper validation for domain format and checks for domain uniqueness.
- Error handling is implemented for database connection and SQL queries.
