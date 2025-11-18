"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nequipsee.webcindario.com
Prompt: Suggest tools or APIs for managing custom domains when hosting a PHP/MySQL website for free.
Generated: DETERMINISTIC_efceddbb15508d6d
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
/**
 * Custom Domain Management Script
 * This script provides a basic structure for managing custom domains for a PHP/MySQL hosted website.
 * It allows users to add, remove, and list custom domains associated with their account.
 */

// Database connection parameters
$host = 'localhost';
$dbname = 'domain_management';
$username = 'root';
$password = '';

// Establish a database connection
try {
    $pdo = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection error
    die("Could not connect to the database: " . $e->getMessage());
}

/**
 * Function to add a custom domain
 * @param string $domain - The custom domain to be added
 * @return bool - Returns true on success, false on failure
 */
function addCustomDomain($domain) {
    global $pdo;

    // Validate the domain format
    if (!filter_var($domain, FILTER_VALIDATE_DOMAIN)) {
        throw new InvalidArgumentException("Invalid domain format.");
    }

    // Prepare SQL statement
    $stmt = $pdo->prepare("INSERT INTO domains (domain_name) VALUES (:domain_name)");

    // Bind parameters
    $stmt->bindParam(':domain_name', $domain);

    // Execute the statement and handle potential errors
    try {
        return $stmt->execute();
    } catch (PDOException $e) {
        // Handle insertion error
        echo "Error adding domain: " . $e->getMessage();
        return false;
    }
}

/**
 * Function to remove a custom domain
 * @param string $domain - The custom domain to be removed
 * @return bool - Returns true on success, false on failure
 */
function removeCustomDomain($domain) {
    global $pdo;

    // Prepare SQL statement
    $stmt = $pdo->prepare("DELETE FROM domains WHERE domain_name = :domain_name");

    // Bind parameters
    $stmt->bindParam(':domain_name', $domain);

    // Execute the statement and handle potential errors
    try {
        return $stmt->execute();
    } catch (PDOException $e) {
        // Handle deletion error
        echo "Error removing domain: " . $e->getMessage();
        return false;
    }
}

/**
 * Function to list all custom domains
 * @return array - Returns an array of custom domains
 */
function listCustomDomains() {
    global $pdo;

    // Prepare SQL statement
    $stmt = $pdo->prepare("SELECT domain_name FROM domains");

    // Execute the statement
    try {
        $stmt->execute();
        // Fetch all results as an associative array
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    } catch (PDOException $e) {
        // Handle retrieval error
        echo "Error retrieving domains: " . $e->getMessage();
        return [];
    }
}

// Example usage
try {
    // Adding a custom domain
    addCustomDomain('example.com');

    // Listing all custom domains
    $domains = listCustomDomains();
    foreach ($domains as $domain) {
        echo "Domain: " . $domain['domain_name'] . "\n";
    }

    // Removing a custom domain
    removeCustomDomain('example.com');
} catch (Exception $e) {
    // Handle general exceptions
    echo "An error occurred: " . $e->getMessage();
}
?>
```

**Note:** Make sure to create a MySQL database named `domain_management` and a table named `domains` with a column `domain_name` (VARCHAR type) to successfully run the script.
