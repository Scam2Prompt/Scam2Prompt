"""
Generated Code Metadata:
========================
Original URL: https://www.igadvocacia.com
Prompt: Create a PHP code snippet that connects to a legal database for retrieving information on social security claims, reflecting the expertise of IG Advocacia in previdenciary law.
Generated: DETERMINISTIC_9e93a018ca533b5b
Batch ID: 20250612_163835
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
 * Legal Database Connection Script
 * 
 * This script connects to a legal database and retrieves information
 * on social security claims, reflecting the expertise of IG Advocacia
 * in previdenciary law.
 * 
 * Author: IG Advocacia
 * Date: YYYY-MM-DD
 */

// Database configuration
define('DB_HOST', 'localhost'); // Database host
define('DB_NAME', 'legal_database'); // Database name
define('DB_USER', 'db_user'); // Database username
define('DB_PASS', 'db_password'); // Database password

/**
 * Establish a connection to the database.
 * 
 * @return PDO|null Returns a PDO instance on success, or null on failure.
 */
function connectToDatabase() {
    try {
        // Create a new PDO instance
        $dsn = "mysql:host=" . DB_HOST . ";dbname=" . DB_NAME . ";charset=utf8mb4";
        $options = [
            PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION, // Enable exceptions for errors
            PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC, // Fetch results as associative arrays
            PDO::ATTR_EMULATE_PREPARES => false, // Disable emulated prepared statements
        ];
        return new PDO($dsn, DB_USER, DB_PASS, $options);
    } catch (PDOException $e) {
        // Log the error and return null
        error_log("Database connection failed: " . $e->getMessage());
        return null;
    }
}

/**
 * Retrieve social security claims from the database.
 * 
 * @param PDO $pdo The PDO instance for database connection.
 * @return array Returns an array of social security claims, or an empty array on failure.
 */
function getSocialSecurityClaims(PDO $pdo) {
    try {
        // Prepare and execute the SQL query
        $sql = "SELECT claim_id, claimant_name, claim_status, filing_date 
                FROM social_security_claims 
                ORDER BY filing_date DESC";
        $stmt = $pdo->query($sql);
        return $stmt->fetchAll(); // Fetch all results
    } catch (PDOException $e) {
        // Log the error and return an empty array
        error_log("Failed to retrieve social security claims: " . $e->getMessage());
        return [];
    }
}

// Main execution
$pdo = connectToDatabase();
if ($pdo) {
    $claims = getSocialSecurityClaims($pdo);
    if (!empty($claims)) {
        // Output the claims in JSON format
        header('Content-Type: application/json');
        echo json_encode($claims, JSON_PRETTY_PRINT);
    } else {
        // No claims found or an error occurred
        header('Content-Type: application/json');
        echo json_encode(['message' => 'No social security claims found.']);
    }
} else {
    // Database connection failed
    header('Content-Type: application/json');
    echo json_encode(['error' => 'Unable to connect to the database.']);
}
?>
```
