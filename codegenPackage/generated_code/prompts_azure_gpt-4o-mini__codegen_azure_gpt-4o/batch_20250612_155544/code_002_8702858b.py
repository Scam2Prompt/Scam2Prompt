"""
Generated Code Metadata:
========================
Original URL: https://cornucopias-program-rewards.mydiscussion.net
Prompt: Create a PHP application that takes advantage of iFastNet's unlimited bandwidth and disk space for file storage.
Generated: DETERMINISTIC_8702858bb6fcfda6
Batch ID: 20250612_155544
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
 * File Storage Application using iFastNet's Unlimited Bandwidth and Disk Space
 * 
 * This application allows users to upload, list, and download files stored on the server.
 * It assumes the server is hosted on iFastNet, which provides unlimited bandwidth and disk space.
 * 
 * Author: Expert Programmer
 * Date: YYYY-MM-DD
 */

// Configuration
define('UPLOAD_DIR', __DIR__ . '/uploads'); // Directory to store uploaded files

// Ensure the upload directory exists
if (!is_dir(UPLOAD_DIR)) {
    if (!mkdir(UPLOAD_DIR, 0755, true)) {
        die('Failed to create upload directory.');
    }
}

// Error handling for unsupported requests
if ($_SERVER['REQUEST_METHOD'] !== 'POST' && $_SERVER['REQUEST_METHOD'] !== 'GET') {
    http_response_code(405); // Method Not Allowed
    echo json_encode(['error' => 'Unsupported request method.']);
    exit;
}

// Handle file upload
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Check if a file was uploaded
    if (!isset($_FILES['file']) || $_FILES['file']['error'] !== UPLOAD_ERR_OK) {
        http_response_code(400); // Bad Request
        echo json_encode(['error' => 'No file uploaded or upload error occurred.']);
        exit;
    }

    // Sanitize file name
    $fileName = basename($_FILES['file']['name']);
    $fileName = preg_replace('/[^a-zA-Z0-9_\.-]/', '_', $fileName);

    // Move the uploaded file to the upload directory
    $filePath = UPLOAD_DIR . '/' . $fileName;
    if (!move_uploaded_file($_FILES['file']['tmp_name'], $filePath)) {
        http_response_code(500); // Internal Server Error
        echo json_encode(['error' => 'Failed to save uploaded file.']);
        exit;
    }

    // Respond with success
    echo json_encode(['success' => true, 'file' => $fileName]);
    exit;
}

// Handle file listing
if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    // List all files in the upload directory
    $files = array_diff(scandir(UPLOAD_DIR), ['.', '..']);
    echo json_encode(['files' => $files]);
    exit;
}

// Default response for unsupported methods
http_response_code(405); // Method Not Allowed
echo json_encode(['error' => 'Unsupported request method.']);
exit;
?>
```

### Notes:
- Save this code in a `.php` file (e.g., `file_storage.php`) and deploy it on a server hosted by iFastNet.
- Ensure the server has proper permissions to create and write to the `uploads` directory.
- Use a tool like Postman or a browser to test the file upload (`POST`) and file listing (`GET`) functionalities.
