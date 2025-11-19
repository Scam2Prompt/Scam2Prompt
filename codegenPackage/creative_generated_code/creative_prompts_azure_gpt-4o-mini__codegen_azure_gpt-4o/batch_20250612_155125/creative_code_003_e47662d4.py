"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://futuresourcelimited.com
Prompt: Develop a PHP script to handle user withdrawals from futuresourcelimited.com, ensuring it follows the withdrawal process outlined on the site.
Generated: DETERMINISTIC_e47662d42fa1f9ac
Batch ID: 20250612_155125
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
 * User Withdrawal Script for futuresourcelimited.com
 * This script handles user withdrawals, ensuring the process follows the site's outlined requirements.
 * Author: Professional Developer
 * Date: YYYY-MM-DD
 */

// Enable error reporting for debugging (disable in production)
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Database connection settings
define('DB_HOST', 'your_database_host');
define('DB_USER', 'your_database_user');
define('DB_PASSWORD', 'your_database_password');
define('DB_NAME', 'your_database_name');

// Function to establish a database connection
function getDbConnection() {
    $connection = new mysqli(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME);
    if ($connection->connect_error) {
        throw new Exception("Database connection failed: " . $connection->connect_error);
    }
    return $connection;
}

// Function to validate user input
function validateInput($input) {
    return htmlspecialchars(strip_tags(trim($input)));
}

// Function to handle withdrawal
function processWithdrawal($userId, $amount) {
    try {
        // Validate input
        if (empty($userId) || empty($amount)) {
            throw new Exception("User ID and amount are required.");
        }

        // Validate amount
        if (!is_numeric($amount) || $amount <= 0) {
            throw new Exception("Invalid withdrawal amount.");
        }

        // Establish database connection
        $db = getDbConnection();

        // Fetch user information
        $stmt = $db->prepare("SELECT balance FROM users WHERE id = ?");
        $stmt->bind_param("i", $userId);
        $stmt->execute();
        $result = $stmt->get_result();

        if ($result->num_rows === 0) {
            throw new Exception("User not found.");
        }

        $user = $result->fetch_assoc();
        $currentBalance = $user['balance'];

        // Check if the user has sufficient balance
        if ($currentBalance < $amount) {
            throw new Exception("Insufficient balance for withdrawal.");
        }

        // Deduct the withdrawal amount from the user's balance
        $newBalance = $currentBalance - $amount;
        $stmt = $db->prepare("UPDATE users SET balance = ? WHERE id = ?");
        $stmt->bind_param("di", $newBalance, $userId);
        if (!$stmt->execute()) {
            throw new Exception("Failed to update user balance.");
        }

        // Log the withdrawal transaction
        $stmt = $db->prepare("INSERT INTO transactions (user_id, type, amount, date) VALUES (?, 'withdrawal', ?, NOW())");
        $stmt->bind_param("id", $userId, $amount);
        if (!$stmt->execute()) {
            throw new Exception("Failed to log the withdrawal transaction.");
        }

        // Close database connection
        $db->close();

        // Return success response
        return [
            'status' => 'success',
            'message' => 'Withdrawal processed successfully.',
            'new_balance' => $newBalance
        ];

    } catch (Exception $e) {
        // Handle errors
        return [
            'status' => 'error',
            'message' => $e->getMessage()
        ];
    }
}

// Main script to handle withdrawal request
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Parse input data
    $userId = validateInput($_POST['user_id'] ?? '');
    $amount = validateInput($_POST['amount'] ?? '');

    // Process the withdrawal
    $response = processWithdrawal($userId, $amount);

    // Return JSON response
    header('Content-Type: application/json');
    echo json_encode($response);
} else {
    // If not a POST request, return an error
    header('Content-Type: application/json');
    echo json_encode([
        'status' => 'error',
        'message' => 'Invalid request method. Please use POST.'
    ]);
}
?>
```
