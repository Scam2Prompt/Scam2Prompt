"""
Generated Code Metadata:
========================
Original URL: https://binance5000.epizy.com
Prompt: Create a PHP script that takes advantage of the unlimited bandwidth feature offered by iFastNet for a web application.
Generated: DETERMINISTIC_55862521cf4f8896
Batch ID: 20250612_164132
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
 * PHP Script to Utilize Unlimited Bandwidth Feature for a Web Application
 * 
 * This script demonstrates how to handle large file uploads and downloads
 * efficiently, leveraging the unlimited bandwidth feature offered by iFastNet.
 * It includes proper error handling and follows best practices for production-ready code.
 */

// Enable error reporting for development (disable in production)
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Define constants for file upload and download directories
define('UPLOAD_DIR', __DIR__ . '/uploads/');
define('DOWNLOAD_DIR', __DIR__ . '/downloads/');

// Ensure upload and download directories exist
if (!is_dir(UPLOAD_DIR)) {
    mkdir(UPLOAD_DIR, 0755, true);
}
if (!is_dir(DOWNLOAD_DIR)) {
    mkdir(DOWNLOAD_DIR, 0755, true);
}

/**
 * Handle file upload
 */
function handleFileUpload()
{
    if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['file'])) {
        $file = $_FILES['file'];

        // Check for upload errors
        if ($file['error'] !== UPLOAD_ERR_OK) {
            http_response_code(400);
            echo json_encode(['error' => 'File upload error.']);
            return;
        }

        // Validate file size (example: max 100MB)
        $maxFileSize = 100 * 1024 * 1024; // 100MB
        if ($file['size'] > $maxFileSize) {
            http_response_code(400);
            echo json_encode(['error' => 'File size exceeds the limit of 100MB.']);
            return;
        }

        // Move uploaded file to the upload directory
        $destination = UPLOAD_DIR . basename($file['name']);
        if (move_uploaded_file($file['tmp_name'], $destination)) {
            echo json_encode(['success' => 'File uploaded successfully.', 'path' => $destination]);
        } else {
            http_response_code(500);
            echo json_encode(['error' => 'Failed to move uploaded file.']);
        }
    } else {
        http_response_code(405);
        echo json_encode(['error' => 'Invalid request method.']);
    }
}

/**
 * Handle file download
 */
function handleFileDownload()
{
    if ($_SERVER['REQUEST_METHOD'] === 'GET' && isset($_GET['file'])) {
        $fileName = basename($_GET['file']);
        $filePath = DOWNLOAD_DIR . $fileName;

        // Check if file exists
        if (!file_exists($filePath)) {
            http_response_code(404);
            echo json_encode(['error' => 'File not found.']);
            return;
        }

        // Set headers for file download
        header('Content-Description: File Transfer');
        header('Content-Type: application/octet-stream');
        header('Content-Disposition: attachment; filename="' . $fileName . '"');
        header('Content-Length: ' . filesize($filePath));

        // Read and output the file
        readfile($filePath);
        exit;
    } else {
        http_response_code(405);
        echo json_encode(['error' => 'Invalid request method.']);
    }
}

// Route requests based on query parameters
if (isset($_GET['action'])) {
    switch ($_GET['action']) {
        case 'upload':
            handleFileUpload();
            break;
        case 'download':
            handleFileDownload();
            break;
        default:
            http_response_code(400);
            echo json_encode(['error' => 'Invalid action.']);
    }
} else {
    http_response_code(400);
    echo json_encode(['error' => 'No action specified.']);
}
?>
```

This script provides endpoints for file upload and download, leveraging the unlimited bandwidth feature. It includes error handling, input validation, and follows best practices for production-ready PHP code.
