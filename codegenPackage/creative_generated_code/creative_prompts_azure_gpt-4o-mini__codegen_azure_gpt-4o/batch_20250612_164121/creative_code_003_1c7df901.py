"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beltsmania.com
Prompt: Develop a code snippet in PHP that processes a customer’s order for a custom belt, including validation for logo uploads and title inputs as described by Belts Mania.
Generated: DETERMINISTIC_1c7df901b48b1bba
Batch ID: 20250612_164121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// File: process_order.php

// Enable error reporting for debugging during development (disable in production)
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Function to validate uploaded logo file
function validateLogoUpload($file) {
    $allowedTypes = ['image/jpeg', 'image/png', 'image/gif'];
    $maxFileSize = 2 * 1024 * 1024; // 2 MB

    if (!isset($file['error']) || is_array($file['error'])) {
        throw new RuntimeException('Invalid file parameters.');
    }

    // Check file upload error
    switch ($file['error']) {
        case UPLOAD_ERR_OK:
            break;
        case UPLOAD_ERR_NO_FILE:
            throw new RuntimeException('No file sent.');
        case UPLOAD_ERR_INI_SIZE:
        case UPLOAD_ERR_FORM_SIZE:
            throw new RuntimeException('Exceeded file size limit.');
        default:
            throw new RuntimeException('Unknown error during upload.');
    }

    // Validate file size
    if ($file['size'] > $maxFileSize) {
        throw new RuntimeException('File exceeds maximum allowed size of 2 MB.');
    }

    // Validate file type
    if (!in_array($file['type'], $allowedTypes)) {
        throw new RuntimeException('Invalid file type. Allowed types: JPEG, PNG, GIF.');
    }

    return true;
}

// Function to validate customer-provided title
function validateTitle($title) {
    $maxLength = 50;

    if (empty($title)) {
        throw new RuntimeException('Title cannot be empty.');
    }

    if (strlen($title) > $maxLength) {
        throw new RuntimeException("Title exceeds maximum length of {$maxLength} characters.");
    }

    return true;
}

// Function to process the belt order
function processOrder($title, $logoFile) {
    try {
        // Validate title input
        validateTitle($title);

        // Validate logo upload
        validateLogoUpload($logoFile);

        // Move uploaded logo file to a permanent directory
        $uploadDir = __DIR__ . '/uploads/';
        if (!is_dir($uploadDir)) {
            mkdir($uploadDir, 0755, true);
        }

        $fileName = basename($logoFile['name']);
        $targetPath = $uploadDir . $fileName;

        if (!move_uploaded_file($logoFile['tmp_name'], $targetPath)) {
            throw new RuntimeException('Failed to move uploaded file.');
        }

        // Simulate saving order details to a database (replace with actual database logic)
        $orderDetails = [
            'title' => $title,
            'logoPath' => $targetPath,
            'orderDate' => date('Y-m-d H:i:s')
        ];

        // Return success response
        return [
            'success' => true,
            'message' => 'Order processed successfully.',
            'orderDetails' => $orderDetails
        ];
    } catch (RuntimeException $e) {
        // Return error response
        return [
            'success' => false,
            'message' => $e->getMessage()
        ];
    }
}

// Example usage (replace $_POST and $_FILES with actual inputs from your application)
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $title = $_POST['title'] ?? '';
    $logoFile = $_FILES['logo'] ?? null;

    $result = processOrder($title, $logoFile);

    // Output the result (replace with actual response handling logic)
    header('Content-Type: application/json');
    echo json_encode($result);
}
?>
```
