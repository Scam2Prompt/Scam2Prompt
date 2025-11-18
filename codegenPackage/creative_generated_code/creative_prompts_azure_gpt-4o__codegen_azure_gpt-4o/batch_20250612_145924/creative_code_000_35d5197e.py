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
 * approve_request.php
 *
 * This script processes user approval requests.
 * Compatible with PHP 8.3.14.
 * 
 * Ensure the database configuration and table structure match your requirements.
 */

declare(strict_types=1);

// Configuration - Replace values with your actual database credentials
const DB_HOST = 'localhost';
const DB_NAME = 'your_database_name';
const DB_USER = 'your_database_user';
const DB_PASS = 'your_database_password';

try {
    // Establish a database connection using PDO
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS, [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION, // Throw exceptions on errors
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC, // Fetch data as associative arrays
    ]);
} catch (PDOException $e) {
    // Handle database connection errors
    http_response_code(500); // Internal Server Error
    echo json_encode(['error' => 'Database connection failed: ' . $e->getMessage()]);
    exit;
}

// Validate request method
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405); // Method Not Allowed
    echo json_encode(['error' => 'Invalid request method. Use POST.']);
    exit;
}

// Parse and validate incoming JSON payload
$requestBody = file_get_contents('php://input');
$data = json_decode($requestBody, true);

if (json_last_error() !== JSON_ERROR_NONE || !is_array($data)) {
    http_response_code(400); // Bad Request
    echo json_encode(['error' => 'Invalid JSON payload.']);
    exit;
}

// Ensure required fields are provided and valid
if (empty($data['user_id']) || !is_int($data['user_id'])) {
    http_response_code(400); // Bad Request
    echo json_encode(['error' => 'Missing or invalid user_id.']);
    exit;
}

try {
    // Prepare SQL statement to update user approval status
    $stmt = $pdo->prepare(
        "UPDATE users SET approved = 1 WHERE id = :user_id"
    );

    // Bind parameters and execute statement
    $stmt->bindValue(':user_id', $data['user_id'], PDO::PARAM_INT);

    if ($stmt->execute()) {
        // Check if a row was actually updated
        if ($stmt->rowCount() === 1) {
            http_response_code(200); // OK
            echo json_encode(['message' => 'User approved successfully.']);
        } else {
            http_response_code(404); // Not Found
            echo json_encode(['error' => 'User not found or already approved.']);
        }
    } else {
        throw new RuntimeException('Failed to execute query.');
    }
} catch (PDOException | RuntimeException $e) {
    // Handle SQL errors
    http_response_code(500); // Internal Server Error
    echo json_encode(['error' => 'An error occurred: ' . $e->getMessage()]);
    exit;
}
```
