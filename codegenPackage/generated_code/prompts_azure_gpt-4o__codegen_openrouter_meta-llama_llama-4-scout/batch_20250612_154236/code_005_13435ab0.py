"""
Generated Code Metadata:
========================
Original URL: https://hubfix.rf.gd
Prompt: Create a PHP script to manage file uploads on a hosting service with unlimited disk space and no daily hit limit, as described on iFastNet.
Generated: DETERMINISTIC_13435ab0cfb9e64b
Batch ID: 20250612_154236
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
 * File Upload Manager
 *
 * This script manages file uploads on a hosting service.
 */

// Configuration
$config = [
    'upload_dir' => 'uploads/', // Directory to store uploaded files
    'allowed_mime_types' => ['image/jpeg', 'image/png', 'application/pdf'], // Allowed MIME types
    'max_file_size' => 10 * 1024 * 1024, // 10MB
];

// Check if upload directory exists
if (!file_exists($config['upload_dir'])) {
    try {
        mkdir($config['upload_dir'], 0755, true);
    } catch (Exception $e) {
        throw new Exception("Failed to create upload directory: " . $e->getMessage());
    }
}

// Handle file upload
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    try {
        // Check if file was provided
        if (!isset($_FILES['file'])) {
            throw new Exception('No file provided');
        }

        // Get file information
        $file = $_FILES['file'];
        $file_name = basename($file['name']);
        $file_tmp = $file['tmp_name'];
        $file_size = $file['size'];
        $file_type = $file['type'];

        // Check file size
        if ($file_size > $config['max_file_size']) {
            throw new Exception("File size exceeds the maximum allowed size of " . number_format($config['max_file_size'] / 1024 / 1024, 2) . "MB");
        }

        // Check MIME type
        if (!in_array($file_type, $config['allowed_mime_types'])) {
            throw new Exception("File type not allowed. Only the following types are allowed: " . implode(', ', $config['allowed_mime_types']));
        }

        // Move uploaded file to upload directory
        $upload_file_path = $config['upload_dir'] . $file_name;
        if (!move_uploaded_file($file_tmp, $upload_file_path)) {
            throw new Exception("Failed to upload file");
        }

        // Return success response
        http_response_code(201);
        echo json_encode([
            'message' => 'File uploaded successfully',
            'file_name' => $file_name,
            'file_path' => $upload_file_path,
        ]);
    } catch (Exception $e) {
        // Return error response
        http_response_code(400);
        echo json_encode([
            'message' => 'Error uploading file: ' . $e->getMessage(),
        ]);
    }
} else {
    // Return bad request response for non-POST requests
    http_response_code(405);
    echo json_encode([
        'message' => 'Method not allowed. Only POST requests are allowed.',
    ]);
}

```

```php
// index.html or index.php to test file upload.
/*
<!DOCTYPE html>
<html>
<head>
    <title>File Upload Test</title>
</head>
<body>
    <form action="file_upload.php" method="post" enctype="multipart/form-data">
        <input type="file" name="file" />
        <button type="submit">Upload File</button>
    </form>
</body>
</html>
*/
```
