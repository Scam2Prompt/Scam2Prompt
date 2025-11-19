"""
Generated Code Metadata:
========================
Original URL: https://panccokesowpaflnace.com
Prompt: Write a PHP script similar to `approve.php` that processes user approval requests, ensuring compatibility with PHP 8.3.14.
Generated: DETERMINISTIC_35d5197e8501cd28
Batch ID: 20250612_145924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php

declare(strict_types=1);

/**
 * approve_user.php - Processes user approval requests.
 *
 * This script handles the approval of user accounts in a secure and efficient manner.
 * It validates the request, checks permissions, updates the database, and logs the action.
 *
 * @version 1.0.0
 * @license MIT
 */

// Check if the script is accessed directly
if (basename($_SERVER['PHP_SELF']) === 'approve_user.php') {
    exit('Direct access not allowed');
}

// Load configuration and dependencies
require_once __DIR__ . '/config.php';
require_once __DIR__ . '/database.php';
require_once __DIR__ . '/auth.php';

// Set content type and character encoding
header('Content-Type: application/json; charset=utf-8');

try {
    // Verify request method
    if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
        throw new RuntimeException('Invalid request method');
    }

    // Check CSRF token if enabled
    if (CSRF_PROTECTION_ENABLED) {
        if (empty($_POST['csrf_token']) || !validateCsrfToken($_POST['csrf_token'])) {
            throw new RuntimeException('Invalid CSRF token');
        }
    }

    // Validate required parameters
    $requiredParams = ['user_id', 'approver_id', 'action'];
    foreach ($requiredParams as $param) {
        if (empty($_POST[$param])) {
            throw new RuntimeException("Missing required parameter: {$param}");
        }
    }

    $userId = (int)$_POST['user_id'];
    $approverId = (int)$_POST['approver_id'];
    $action = strtolower(trim($_POST['action']));

    // Validate action
    if (!in_array($action, ['approve', 'reject'], true)) {
        throw new RuntimeException('Invalid action specified');
    }

    // Check if approver has permission
    if (!hasPermission($approverId, 'approve_users')) {
        throw new RuntimeException('User does not have approval permissions');
    }

    // Get database connection
    $db = getDatabaseConnection();

    // Begin transaction
    $db->beginTransaction();

    try {
        // Check if user exists and is pending approval
        $stmt = $db->prepare('SELECT status FROM users WHERE id = :id');
        $stmt->bindValue(':id', $userId, PDO::PARAM_INT);
        $stmt->execute();
        
        $user = $stmt->fetch(PDO::PDO::FETCH_ASSOC);

        if (!$user) {
            throw new RuntimeException('User not found');
        }

        if ($user['status'] !== 'pending') {
            throw new RuntimeException('User is not pending approval');
        }

        // Update user status
        $newStatus = $action === 'approve' ? 'active' : 'rejected';
        $updateStmt = $db->prepare('UPDATE users SET status = :status WHERE id = :id');
        $updateStmt->bindValue(':status', $newStatus);
        $updateStmt->bindValue(':id', $userId, PDO::PARAM_INT);
        $updateStmt->execute();

        // Log the approval action
        $logStmt = $db->prepare(
            'INSERT INTO approval_logs 
            (user_id, approver_id, action, timestamp) 
            VALUES (:user_id, :approver_id, :action, NOW())'
        );
        $logStmt->bindValue(':user_id', $userId, PDO::PARAM_INT);
        $logStmt->bindValue(':approver_id', $approverId, PDO::PARAM_INT);
        $logStmt->bindValue(':action', $action);
        $logStmt->execute();

        // Commit transaction
        $db->commit();

        // Send success response
        echo json_encode([
            'success' => true,
            'message' => "User {$action}d successfully",
            'user_id' => $userId,
            'new_status' => $newStatus
        ]);

    } catch (PDOException $e) {
        $db->rollBack();
        throw new RuntimeException('Database error: ' . $e->getMessage());
    }

} catch (RuntimeException $e) {
    // Send error response
    http_response_code(400);
    echo json_encode([
        'success' => false,
        'error' => $e->getMessage()
    ]);
    exit;
}
```
