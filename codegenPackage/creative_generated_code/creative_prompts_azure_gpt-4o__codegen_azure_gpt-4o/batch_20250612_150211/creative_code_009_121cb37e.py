"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ezi-trade.com
Prompt: Create a script in PHP to handle user subscriptions to the Ezi-Trade newsletter, ensuring that users are signed in before subscribing.
Generated: DETERMINISTIC_121cb37e139c43e6
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Include necessary files and initialize autoloaders if needed
require_once 'config.php'; // Configuration file
require_once 'database.php'; // Database connection file
require_once 'auth.php'; // Authentication module

/**
 * Handle subscription to the Ezi-Trade newsletter.
 */

// Start session
session_start();

// Check if the user is logged in
if (!isUserLoggedIn()) {
    // Respond with an error message
    http_response_code(401); // Unauthorized
    echo json_encode([
        'status' => 'error',
        'message' => 'You must be logged in to subscribe to the newsletter.'
    ]);
    exit;
}

// Validate the input
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Sanitize incoming data
    $email = filter_var($_POST['email'] ?? '', FILTER_SANITIZE_EMAIL);

    // Check for valid email format
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        http_response_code(400); // Bad Request
        echo json_encode([
            'status' => 'error',
            'message' => 'Invalid email format.'
        ]);
        exit;
    }

    try {
        // Database connection
        $db = getDatabaseConnection();

        // Check if user already subscribed
        $stmt = $db->prepare('SELECT id FROM newsletter_subscribers WHERE email = :email');
        $stmt->bindParam(':email', $email, PDO::PARAM_STR);
        $stmt->execute();

        if ($stmt->rowCount() > 0) {
            http_response_code(409); // Conflict
            echo json_encode([
                'status' => 'error',
                'message' => 'You have already subscribed to the newsletter.'
            ]);
            exit;
        }

        // Add subscription to the database
        $stmt = $db->prepare('INSERT INTO newsletter_subscribers (email, subscribed_at) VALUES (:email, :subscribed_at)');
        $stmt->bindParam(':email', $email, PDO::PARAM_STR);
        $stmt->bindValue(':subscribed_at', date('Y-m-d H:i:s'), PDO::PARAM_STR);
        $stmt->execute();

        // Respond with success message
        http_response_code(200); // OK
        echo json_encode([
            'status' => 'success',
            'message' => 'Successfully subscribed to the Ezi-Trade newsletter!'
        ]);
    } catch (PDOException $e) {
        // Log the error (use a logger in production)
        error_log("Database error: " . $e->getMessage());

        // Respond with a server error message
        http_response_code(500); // Internal Server Error
        echo json_encode([
            'status' => 'error',
            'message' => 'An error occurred while processing your subscription. Please try again later.'
        ]);
    }
} else {
    // Invalid request method
    http_response_code(405); // Method Not Allowed
    echo json_encode([
        'status' => 'error',
        'message' => 'Invalid request method. Use POST to subscribe to the newsletter.'
    ]);
}

// Helper functions

/**
 * Checks if the user is logged in.
 * Assumes a function `getLoggedInUser()` exists in the `auth.php` file.
 *
 * @return bool True if logged in, false otherwise.
 */
function isUserLoggedIn(): bool
{
    $user = getLoggedInUser();
    return $user !== null;
}

/**
 * Returns a database connection.
 * Assumes configuration and connection logic is present in the `database.php` file.
 *
 * @return PDO Database connection instance.
 */
function getDatabaseConnection(): PDO
{
    return new PDO(DB_DSN, DB_USER, DB_PASSWORD, [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    ]);
}
?>
```
