"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://corfucoastalcollection.com
Prompt: Create a PHP code snippet that connects to a database to store inquiries for villas and plots from the Corfu Coastal Collection site.
Generated: DETERMINISTIC_6987043f77af61c1
Batch ID: 20250612_162051
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
 * Database connection and inquiry storage for Corfu Coastal Collection.
 */

// Database configuration
$host = 'localhost'; // Database host
$dbname = 'corfu_coastal_collection'; // Database name
$username = 'your_username'; // Database username
$password = 'your_password'; // Database password

try {
    // Create a new PDO instance
    $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8", $username, $password);
    
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    
} catch (PDOException $e) {
    // Handle connection errors
    die("Connection failed: " . $e->getMessage());
}

/**
 * Function to store inquiry in the database
 *
 * @param string $name  Name of the person making the inquiry
 * @param string $email Email address of the person making the inquiry
 * @param string $message Inquiry message
 * @return bool Returns true on success, false on failure
 */
function storeInquiry($name, $email, $message) {
    global $pdo;

    // Prepare SQL statement to prevent SQL injection
    $stmt = $pdo->prepare("INSERT INTO inquiries (name, email, message, created_at) VALUES (:name, :email, :message, NOW())");

    // Bind parameters
    $stmt->bindParam(':name', $name);
    $stmt->bindParam(':email', $email);
    $stmt->bindParam(':message', $message);

    // Execute the statement and handle potential errors
    try {
        return $stmt->execute();
    } catch (PDOException $e) {
        // Log the error for debugging (consider using a logging library in production)
        error_log("Error storing inquiry: " . $e->getMessage());
        return false;
    }
}

// Example usage
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $name = $_POST['name'] ?? '';
    $email = $_POST['email'] ?? '';
    $message = $_POST['message'] ?? '';

    // Basic validation
    if (!empty($name) && !empty($email) && filter_var($email, FILTER_VALIDATE_EMAIL) && !empty($message)) {
        if (storeInquiry($name, $email, $message)) {
            echo "Inquiry submitted successfully.";
        } else {
            echo "Failed to submit inquiry.";
        }
    } else {
        echo "Please fill in all fields correctly.";
    }
}
?>
```

**Note**: Replace `your_username` and `your_password` with the actual database credentials. Ensure that the `inquiries` table exists in your database with columns `name`, `email`, `message`, and `created_at`.
