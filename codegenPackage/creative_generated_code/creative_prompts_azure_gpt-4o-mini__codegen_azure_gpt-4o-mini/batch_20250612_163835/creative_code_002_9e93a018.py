"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.igadvocacia.com
Prompt: Create a PHP code snippet that connects to a legal database for retrieving information on social security claims, reflecting the expertise of IG Advocacia in previdenciary law.
Generated: DETERMINISTIC_9e93a018ca533b5b
Batch ID: 20250612_163835
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
 * PHP Script to connect to a legal database for retrieving information 
 * on social security claims.
 * 
 * This script reflects the expertise of IG Advocacia in previdenciary law.
 */

// Database configuration
$host = 'localhost'; // Database host
$db = 'legal_database'; // Database name
$user = 'db_user'; // Database username
$pass = 'db_password'; // Database password
$charset = 'utf8mb4'; // Character set

// Data Source Name (DSN)
$dsn = "mysql:host=$host;dbname=$db;charset=$charset";

// Options for the PDO connection
$options = [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION, // Throw exceptions on errors
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC, // Fetch associative arrays
    PDO::ATTR_EMULATE_PREPARES => false, // Disable emulated prepared statements
];

try {
    // Create a new PDO instance for database connection
    $pdo = new PDO($dsn, $user, $pass, $options);
    
    // Function to retrieve social security claims based on a query parameter
    function getSocialSecurityClaims($pdo, $claimId) {
        // Prepare an SQL statement to prevent SQL injection
        $stmt = $pdo->prepare("SELECT * FROM social_security_claims WHERE claim_id = :claim_id");
        $stmt->bindParam(':claim_id', $claimId, PDO::PARAM_INT);
        
        // Execute the statement
        $stmt->execute();
        
        // Fetch the results
        return $stmt->fetchAll();
    }

    // Example usage of the function
    $claimId = 123; // Example claim ID to retrieve
    $claims = getSocialSecurityClaims($pdo, $claimId);
    
    // Check if claims were found
    if ($claims) {
        // Output the claims data (for demonstration purposes)
        echo "<pre>";
        print_r($claims);
        echo "</pre>";
    } else {
        echo "No claims found for the provided claim ID.";
    }

} catch (PDOException $e) {
    // Handle connection errors
    echo "Database connection failed: " . $e->getMessage();
}
?>
```
