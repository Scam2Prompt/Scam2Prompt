"""
Generated Code Metadata:
========================
Original URL: https://ingreseaquii.webcindario.com
Prompt: Create a PHP script for uploading files to a server, compatible with free hosting platforms like miarroba.com.
Generated: DETERMINISTIC_784b1494363937a8
Batch ID: 20250612_151624
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
 * File Upload Script
 * 
 * This script allows users to upload files to a server. It is designed to be compatible with free hosting platforms like miarroba.com.
 */

// Configuration
$allowed_file_types = array('image/jpeg', 'image/png', 'application/pdf'); // allowed file types
$max_file_size = 1024 * 1024 * 2; // 2MB
$upload_dir = 'uploads/'; // upload directory

// Check if upload directory exists
if (!is_dir($upload_dir)) {
    mkdir($upload_dir, 0755, true);
}

// Function to handle file upload
function upload_file($file, $upload_dir, $allowed_file_types, $max_file_size) {
    // Check if file was uploaded successfully
    if ($file['error'] !== UPLOAD_ERR_OK) {
        throw new Exception('File upload failed with error code ' . $file['error']);
    }

    // Check file type
    if (!in_array($file['type'], $allowed_file_types)) {
        throw new Exception('File type not allowed');
    }

    // Check file size
    if ($file['size'] > $max_file_size) {
        throw new Exception('File size exceeds the maximum allowed size of ' . ($max_file_size / 1024 / 1024) . 'MB');
    }

    // Generate unique filename
    $filename = uniqid() . '_' . basename($file['name']);
    $filepath = $upload_dir . $filename;

    // Move uploaded file to upload directory
    if (!move_uploaded_file($file['tmp_name'], $filepath)) {
        throw new Exception('Failed to move uploaded file');
    }

    return $filename;
}

// Handle file upload
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    try {
        // Check if file was provided
        if (!isset($_FILES['file'])) {
            throw new Exception('No file provided');
        }

        $uploaded_filename = upload_file($_FILES['file'], $upload_dir, $allowed_file_types, $max_file_size);
        echo "File uploaded successfully: $uploaded_filename";
    } catch (Exception $e) {
        http_response_code(400);
        echo "Error: " . $e->getMessage();
    }
} else {
    // Display upload form
    ?>
    <form action="" method="post" enctype="multipart/form-data">
        <input type="file" name="file" />
        <button type="submit">Upload File</button>
    </form>
    <?php
}
```
