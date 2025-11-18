"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://panccokesowpaflnace.com
Prompt: Write a PHP script similar to `approve.php` that processes user approval requests, ensuring compatibility with PHP 8.3.14.
Generated: DETERMINISTIC_35d5197e8501cd28
Batch ID: 20250612_145924
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
 * approve.php
 * 
 * This script processes user approval requests. It validates the request, 
 * checks the user status, and updates the approval status in the database.
 * 
 * PHP version 8.3.14
 */

// Enable error reporting for development (remove or adjust in production)
error_reporting(E_ALL);
ini_set('display_errors', '1');

// Database connection parameters
$host = 'localhost';
$db = 'your_database_name';
$user = 'your_username';
$pass = 'your_password';

try {
    // Create a new PDO instance for database connection
    $pdo = new PDO("mysql:host=$host;dbname=$db;charset=utf8mb4", $user, $pass);
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection errors
    die("Database connection failed: " . $e->getMessage());
}

// Check if the request method is POST
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Validate required parameters
    if (isset($_POST['user_id']) && !empty($_POST['user_id'])) {
        $userId = filter_var($_POST['user_id'], FILTER_VALIDATE_INT);
        
        // Proceed if user ID is valid
        if ($userId !== false) {
            try {
                // Begin a transaction
                $pdo->beginTransaction();

                // Check if user exists and is pending approval
                $stmt = $pdo->prepare("SELECT status FROM users WHERE id = :user_id FOR UPDATE");
                $stmt->execute(['user_id' => $userId]);
                $user = $stmt->fetch(PDO::FETCH_ASSOC);

                if ($user) {
                    // Check if user status is pending approval
                    if ($user['status'] === 'pending') {
                        // Update user status to approved
                        $updateStmt = $pdo->prepare("UPDATE users SET status = 'approved' WHERE id = :user_id");
                        $updateStmt->execute(['user_id' => $userId]);

                        // Commit the transaction
                        $pdo->commit();
                        echo json_encode(['success' => true, 'message' => 'User approved successfully.']);
                    } else {
                        echo json_encode(['success' => false, 'message' => 'User is not pending approval.']);
                    }
                } else {
                    echo json_encode(['success' => false, 'message' => 'User not found.']);
                }
            } catch (PDOException $e) {
                // Roll back the transaction on error
                $pdo->rollBack();
                echo json_encode(['success' => false, 'message' => 'Error processing request: ' . $e->getMessage()]);
            }
        } else {
            echo json_encode(['success' => false, 'message' => 'Invalid user ID.']);
        }
    } else {
        echo json_encode(['success' => false, 'message' => 'User ID is required.']);
    }
} else {
    echo json_encode(['success' => false, 'message' => 'Invalid request method.']);
}
?>
```
