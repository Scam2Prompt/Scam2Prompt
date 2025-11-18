"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://validardvplta.webcindario.com
Prompt: Write a PHP function to handle user authentication using a MySQL database for a free website.
Generated: DETERMINISTIC_12c632ccdf10349c
Batch ID: 20250612_145516
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
 * Function to authenticate a user using a MySQL database.
 * 
 * @param string $username The username provided by the user.
 * @param string $password The password provided by the user.
 * @return bool|string Returns true if authentication is successful, otherwise returns an error message.
 */
function authenticateUser($username, $password)
{
    // Database credentials - Replace with your actual DB credentials
    $dbHost = 'localhost';
    $dbName = 'your_database_name';
    $dbUser = 'your_database_user';
    $dbPass = 'your_database_password';

    try {
        // Establish a PDO connection to the MySQL database
        $pdo = new PDO("mysql:host=$dbHost;dbname=$dbName;charset=utf8mb4", $dbUser, $dbPass);
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

        // Prepare the SQL query to fetch the user by their username
        $query = "SELECT id, username, password_hash FROM users WHERE username = :username LIMIT 1";
        $stmt = $pdo->prepare($query);
        $stmt->bindParam(':username', $username, PDO::PARAM_STR);

        // Execute the query
        $stmt->execute();

        // Fetch the user record
        $user = $stmt->fetch(PDO::FETCH_ASSOC);

        // If no user is found, return an error
        if (!$user) {
            return "Invalid username or password.";
        }

        // Verify the provided password against the stored password hash
        if (password_verify($password, $user['password_hash'])) {
            // Authentication successful
            return true;
        } else {
            // Authentication failed
            return "Invalid username or password.";
        }

    } catch (PDOException $e) {
        // Handle database connection or query errors
        error_log("Database error: " . $e->getMessage()); // Log the error for debugging
        return "An internal error occurred. Please try again later.";
    } finally {
        // Clean up, if necessary
        $pdo = null;
    }
}

// Example usage
$username = 'test_user';
$password = 'test_password';
$result = authenticateUser($username, $password);

if ($result === true) {
    echo "Authentication successful!";
} else {
    echo $result; // Display error message
}
?>
```
