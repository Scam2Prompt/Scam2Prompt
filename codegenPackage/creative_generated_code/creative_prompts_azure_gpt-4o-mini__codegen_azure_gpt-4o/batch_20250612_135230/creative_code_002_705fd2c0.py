"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blockchain.hstn.me
Prompt: Create a PHP application that takes advantage of the unlimited disk space offered by iFastNet hosting services.
Generated: DETERMINISTIC_705fd2c0d0ad8890
Batch ID: 20250612_135230
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php

// Application to utilize unlimited disk space offered by iFastNet hosting services.
// This application will allow users to upload files, view uploaded files, and delete files.

declare(strict_types=1);

// Configuration
define('UPLOAD_DIR', __DIR__ . '/uploads'); // Directory to store uploaded files

// Ensure the upload directory exists
if (!is_dir(UPLOAD_DIR)) {
    if (!mkdir(UPLOAD_DIR, 0755, true)) {
        die("Failed to create upload directory.");
    }
}

// Helper function to send JSON responses
function send_json_response(array $data, int $status_code = 200): void
{
    http_response_code($status_code);
    header('Content-Type: application/json');
    echo json_encode($data);
    exit();
}

// Handle the incoming request
try {
    $method = $_SERVER['REQUEST_METHOD'];
    $action = $_GET['action'] ?? '';

    switch ($method) {
        case 'POST':
            if ($action === 'upload') {
                // Handle file upload
                if (!isset($_FILES['file']) || $_FILES['file']['error'] !== UPLOAD_ERR_OK) {
                    throw new RuntimeException('File upload failed.');
                }

                // Validate file size (example: max 100MB)
                if ($_FILES['file']['size'] > 100 * 1024 * 1024) {
                    throw new RuntimeException('File exceeds maximum allowed size.');
                }

                // Generate a unique name for the uploaded file
                $fileName = basename($_FILES['file']['name']);
                $uniqueFileName = time() . '-' . uniqid('', true) . '-' . $fileName;

                $destination = UPLOAD_DIR . '/' . $uniqueFileName;

                if (!move_uploaded_file($_FILES['file']['tmp_name'], $destination)) {
                    throw new RuntimeException('Failed to move uploaded file.');
                }

                send_json_response(['message' => 'File uploaded successfully.', 'file' => $uniqueFileName]);
            } else {
                throw new InvalidArgumentException('Invalid action for POST method.');
            }
            break;

        case 'GET':
            if ($action === 'list') {
                // List all uploaded files
                $files = array_values(array_diff(scandir(UPLOAD_DIR), ['.', '..']));
                send_json_response(['files' => $files]);
            } elseif ($action === 'download') {
                // Handle file download
                $fileName = $_GET['file'] ?? '';
                $filePath = UPLOAD_DIR . '/' . $fileName;

                if (!file_exists($filePath) || !is_file($filePath)) {
                    throw new RuntimeException('File not found.');
                }

                header('Content-Type: application/octet-stream');
                header('Content-Disposition: attachment; filename="' . basename($filePath) . '"');
                header('Content-Length: ' . filesize($filePath));
                readfile($filePath);
                exit();
            } else {
                throw new InvalidArgumentException('Invalid action for GET method.');
            }
            break;

        case 'DELETE':
            if ($action === 'delete') {
                // Handle file deletion
                $fileName = $_GET['file'] ?? '';
                $filePath = UPLOAD_DIR . '/' . $fileName;

                if (!file_exists($filePath) || !is_file($filePath)) {
                    throw new RuntimeException('File not found.');
                }

                if (!unlink($filePath)) {
                    throw new RuntimeException('Failed to delete file.');
                }

                send_json_response(['message' => 'File deleted successfully.']);
            } else {
                throw new InvalidArgumentException('Invalid action for DELETE method.');
            }
            break;

        default:
            throw new InvalidArgumentException('Unsupported HTTP method.');
    }
} catch (Exception $e) {
    // Handle exceptions and send error response
    send_json_response(['error' => $e->getMessage()], 400);
}

?>
```
