"""
Generated Code Metadata:
========================
Original URL: https://yourpalmreading.com
Prompt: Write code in PHP to handle file uploads (e.g., hand images) and validate the file type and size before storing them, similar to the functionality described on YourPalmReading.com.
Generated: DETERMINISTIC_3d22ebe5cdb2664e
Batch ID: 20250612_154021
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
 * Handles file uploads, validates file type and size, and stores them.
 */

// Configuration
const MAX_FILE_SIZE = 5 * 1024 * 1024; // 5MB
const ALLOWED_MIME_TYPES = ['image/jpeg', 'image/png', 'image/gif'];
const UPLOAD_DIRECTORY = 'uploads';

/**
 * Handles file upload and validation.
 *
 * @param array $file The uploaded file.
 * @return array|false
 */
function handleFileUpload(array $file)
{
    // Check if file was uploaded without errors
    if ($file['error'] !== UPLOAD_ERR_OK) {
        throw new Exception('File upload failed with error code ' . $file['error']);
    }

    // Validate file size
    if ($file['size'] > MAX_FILE_SIZE) {
        throw new Exception('File size exceeds the maximum allowed size of ' . MAX_FILE_SIZE . ' bytes');
    }

    // Validate file type
    $finfo = finfo_open(FILEINFO_MIME_TYPE);
    $mimeType = finfo_file($finfo, $file['tmp_name']);
    finfo_close($finfo);

    if (!in_array($mimeType, ALLOWED_MIME_TYPES)) {
        throw new Exception('File type is not allowed. Only ' . implode(', ', ALLOWED_MIME_TYPES) . ' are allowed');
    }

    // Store file
    $filename = pathinfo($file['name'], PATHINFO_FILENAME) . '_' . uniqid() . '.' . pathinfo($file['name'], PATHINFO_EXTENSION);
    $uploadPath = UPLOAD_DIRECTORY . DIRECTORY_SEPARATOR . $filename;

    if (!is_dir(UPLOAD_DIRECTORY)) {
        mkdir(UPLOAD_DIRECTORY, 0755, true);
    }

    if (!move_uploaded_file($file['tmp_name'], $uploadPath)) {
        throw new Exception('Failed to move uploaded file to ' . $uploadPath);
    }

    return [
        'filename' => $filename,
        'path' => $uploadPath,
        'mime_type' => $mimeType,
    ];
}

// Example usage
try {
    if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        if (!empty($_FILES['file'])) {
            $file = $_FILES['file'];
            $result = handleFileUpload($file);
            echo json_encode($result, JSON_PRETTY_PRINT);
        } else {
            throw new Exception('No file provided');
        }
    } else {
        throw new Exception('Invalid request method');
    }
} catch (Exception $e) {
    http_response_code(400);
    echo json_encode(['error' => $e->getMessage()], JSON_PRETTY_PRINT);
}

```
