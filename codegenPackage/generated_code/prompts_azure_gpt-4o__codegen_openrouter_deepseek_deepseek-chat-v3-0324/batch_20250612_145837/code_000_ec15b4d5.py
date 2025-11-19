"""
Generated Code Metadata:
========================
Original URL: https://unisawpv3.com
Prompt: Write a PHP script that uses functionality similar to `approve.php` from a server running Apache 2.4.62 and PHP 8.3.14 to validate user input and log the results in a directory like `logs/`.
Generated: DETERMINISTIC_ec15b4d5d0a5b241
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
 * approve.php - Validates user input and logs results.
 *
 * @package    UserApprovalSystem
 * @version    1.0.0
 * @author     Your Name <your.email@example.com>
 * @license    MIT
 */

declare(strict_types=1);

// Configuration constants
const LOG_DIR = __DIR__ . '/logs/';
const MAX_INPUT_LENGTH = 255;
const ALLOWED_ACTIONS = ['approve', 'reject', 'pending'];
const DATE_FORMAT = 'Y-m-d H:i:s';

// Ensure logs directory exists
if (!file_exists(LOG_DIR) && !mkdir(LOG_DIR, 0755, true) && !is_dir(LOG_DIR)) {
    throw new RuntimeException(sprintf('Directory "%s" could not be created', LOG_DIR));
}

// Set content type and character encoding
header('Content-Type: application/json; charset=utf-8');

try {
    // Validate request method
    if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
        throw new InvalidArgumentException('Only POST requests are allowed', 405);
    }

    // Get and validate input
    $input = json_decode(file_get_contents('php://input'), true, 512, JSON_THROW_ON_ERROR);
    
    if (!isset($input['action'], $input['user_id'], $input['reason'])) {
        throw new InvalidArgumentException('Missing required fields', 400);
    }

    // Sanitize and validate input
    $action = trim($input['action']);
    $userId = filter_var($input['user_id'], FILTER_VALIDATE_INT);
    $reason = trim($input['reason']);

    if (!in_array($action, ALLOWED_ACTIONS, true)) {
        throw new InvalidArgumentException('Invalid action specified', 400);
    }

    if ($userId === false || $userId <= 0) {
        throw new InvalidArgumentException('Invalid user ID', 400);
    }

    if (empty($reason) || strlen($reason) > MAX_INPUT_LENGTH) {
        throw new InvalidArgumentException('Reason must be between 1 and ' . MAX_INPUT_LENGTH . ' characters', 400);
    }

    // Prepare log data
    $logData = [
        'timestamp' => date(DATE_FORMAT),
        'action' => $action,
        'user_id' => $userId,
        'reason' => $reason,
        'ip_address' => $_SERVER['REMOTE_ADDR'] ?? 'unknown'
    ];

    // Write to log file
    $logFile = LOG_DIR . 'approval_log_' . date('Y-m-d') . '.log';
    $logLine = json_encode($logData, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE) . PHP_EOL;

    if (file_put_contents($logFile, $logLine, FILE_APPEND | LOCK_EX) === false) {
        throw new RuntimeException('Failed to write to log file', 500);
    }

    // Return success response
    echo json_encode([
        'status' => 'success',
        'message' => 'Action logged successfully',
        'data' => $logData
    ], JSON_THROW_ON_ERROR);

} catch (InvalidArgumentException $e) {
    http_response_code($e->getCode() ?: 400);
    echo json_encode([
        'status' => 'error',
        'message' => $e->getMessage()
    ], JSON_THROW_ON_ERROR);
} catch (RuntimeException $e) {
    http_response_code($e->getCode() ?: 500);
    echo json_encode([
        'status' => 'error',
        'message' => $e->getMessage()
    ], JSON_THROW_ON_ERROR);
} catch (JsonException $e) {
    http_response_code(400);
    echo json_encode([
        'status' => 'error',
        'message' => 'Invalid JSON data'
    ], JSON_THROW_ON_ERROR);
} catch (Throwable $e) {
    http_response_code(500);
    echo json_encode([
        'status' => 'error',
        'message' => 'An unexpected error occurred'
    ], JSON_THROW_ON_ERROR);
}
```
