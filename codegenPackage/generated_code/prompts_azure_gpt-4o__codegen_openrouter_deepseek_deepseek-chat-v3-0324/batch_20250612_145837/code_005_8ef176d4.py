"""
Generated Code Metadata:
========================
Original URL: https://unisawpv3.com
Prompt: Write a PHP script that interacts with a server running Apache 2.4.62 and PHP 8.3.14 to approve and log user actions, similar to the functionality implied by `approve.php`.
Generated: DETERMINISTIC_8ef176d47c522733
Batch ID: 20250612_145837
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
 * approve.php - User action approval and logging system
 * 
 * This script handles the approval of user actions and logs them to a database.
 * It requires Apache 2.4.62 and PHP 8.3.14 or higher.
 */

declare(strict_types=1);

// Database configuration
const DB_HOST = 'localhost';
const DB_NAME = 'approval_system';
const DB_USER = 'approval_user';
const DB_PASS = 'secure_password';
const DB_CHARSET = 'utf8mb4';

// Action status constants
const STATUS_PENDING = 'pending';
const STATUS_APPROVED = 'approved';
const STATUS_REJECTED = 'rejected';

// Initialize response array
$response = [
    'success' => false,
    'message' => '',
    'data' => []
];

try {
    // Check if script is accessed via POST
    if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
        throw new RuntimeException('Invalid request method. Only POST is allowed.');
    }

    // Validate required parameters
    $requiredParams = ['action_id', 'approver_id', 'decision'];
    foreach ($requiredParams as $param) {
        if (!isset($_POST[$param]) || empty($_POST[$param])) {
            throw new InvalidArgumentException("Missing required parameter: $param");
        }
    }

    // Sanitize input
    $actionId = filter_var($_POST['action_id'], FILTER_SANITIZE_NUMBER_INT);
    $approverId = filter_var($_POST['approver_id'], FILTER_SANITIZE_NUMBER_INT);
    $decision = strtolower(filter_var($_POST['decision'], FILTER_SANITIZE_STRING));

    // Validate decision
    if (!in_array($decision, [STATUS_APPROVED, STATUS_REJECTED])) {
        throw new InvalidArgumentException('Invalid decision. Must be either "approved" or "rejected".');
    }

    // Create database connection
    $dsn = "mysql:host=" . DB_HOST . ";dbname=" . DB_NAME . ";charset=" . DB_CHARSET;
    $options = [
        PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
        PDO::ATTR_EMULATE_PREPARES   => false,
    ];

    $pdo = new PDO($dsn, DB_USER, DB_PASS, $options);

    // Begin transaction
    $pdo->beginTransaction();

    try {
        // Check if action exists and is pending
        $stmt = $pdo->prepare("SELECT * FROM user_actions WHERE id = ? AND status = ?");
        $stmt->execute([$actionId, STATUS_PENDING]);
        $action = $stmt->fetch();

        if (!$action) {
            throw new RuntimeException('Action not found or already processed.');
        }

        // Update action status
        $updateStmt = $pdo->prepare("UPDATE user_actions SET status = ?, approver_id = ?, processed_at = NOW() WHERE id = ?");
        $updateStmt->execute([$decision, $approverId, $actionId]);

        // Log the approval
        $logStmt = $pdo->prepare("INSERT INTO approval_logs (action_id, approver_id, decision, logged_at) VALUES (?, ?, ?, NOW())");
        $logStmt->execute([$actionId, $approverId, $decision]);

        // Commit transaction
        $pdo->commit();

        // Prepare success response
        $response['success'] = true;
        $response['message'] = "Action successfully $decision.";
        $response['data'] = [
            'action_id' => $actionId,
            'status' => $decision,
            'processed_at' => date('Y-m-d H:i:s')
        ];

    } catch (Exception $e) {
        // Rollback transaction on error
        $pdo->rollBack();
        throw $e;
    }

} catch (InvalidArgumentException $e) {
    $response['message'] = $e->getMessage();
    http_response_code(400);
} catch (RuntimeException $e) {
    $response['message'] = $e->getMessage();
    http_response_code(404);
} catch (PDOException $e) {
    $response['message'] = 'Database error: ' . $e->getMessage();
    http_response_code(500);
} catch (Exception $e) {
    $response['message'] = 'An unexpected error occurred: ' . $e->getMessage();
    http_response_code(500);
}

// Set content type and return JSON response
header('Content-Type: application/json');
echo json_encode($response);
```
