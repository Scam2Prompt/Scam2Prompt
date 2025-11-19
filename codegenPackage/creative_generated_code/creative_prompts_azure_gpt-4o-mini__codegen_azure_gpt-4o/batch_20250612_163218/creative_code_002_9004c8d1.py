"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aidsupport.rf.gd
Prompt: Create a PHP application that takes advantage of the unlimited disk space offered by iFastNet for file storage.
Generated: DETERMINISTIC_9004c8d11063ac09
Batch ID: 20250612_163218
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
 * File Storage Application
 * This script allows users to upload and retrieve files using iFastNet's unlimited disk space.
 * Ensure proper configurations and permissions are set for the `uploads/` directory.
 */

// Enable error reporting for development purposes (disable in production).
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Define upload directory (ensure it's writable).
define('UPLOAD_DIR', __DIR__ . '/uploads/');

// Check if the upload directory exists, create it if necessary.
if (!is_dir(UPLOAD_DIR)) {
    if (!mkdir(UPLOAD_DIR, 0755, true)) {
        die('Failed to create upload directory.');
    }
}

// Handle file upload.
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['file'])) {
    // Validate uploaded file.
    if ($_FILES['file']['error'] === UPLOAD_ERR_OK) {
        $fileName = basename($_FILES['file']['name']);
        $filePath = UPLOAD_DIR . $fileName;

        // Prevent overwriting files with the same name.
        if (file_exists($filePath)) {
            die('Error: A file with the same name already exists.');
        }

        // Move the uploaded file to the upload directory.
        if (move_uploaded_file($_FILES['file']['tmp_name'], $filePath)) {
            echo 'File uploaded successfully: ' . htmlspecialchars($fileName);
        } else {
            die('Error: Failed to move uploaded file.');
        }
    } else {
        die('Error: File upload failed. Code: ' . $_FILES['file']['error']);
    }
}

// Handle file retrieval.
if ($_SERVER['REQUEST_METHOD'] === 'GET' && isset($_GET['file'])) {
    $fileName = basename($_GET['file']);
    $filePath = UPLOAD_DIR . $fileName;

    // Check if the file exists.
    if (file_exists($filePath)) {
        // Serve the file to the user.
        header('Content-Type: application/octet-stream');
        header('Content-Disposition: attachment; filename="' . $fileName . '"');
        header('Content-Length: ' . filesize($filePath));
        readfile($filePath);
        exit;
    } else {
        die('Error: File not found.');
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Storage Application</title>
</head>
<body>
    <h1>File Storage Application</h1>
    <h2>Upload a File</h2>
    <form action="" method="POST" enctype="multipart/form-data">
        <input type="file" name="file" required>
        <button type="submit">Upload</button>
    </form>

    <h2>Retrieve a File</h2>
    <form action="" method="GET">
        <input type="text" name="file" placeholder="Enter file name" required>
        <button type="submit">Download</button>
    </form>
</body>
</html>
```

### Notes:
- Ensure the `uploads/` directory is writable (`chmod 775 uploads/`).
- Remove error reporting in production: `error_reporting(0)` and `ini_set('display_errors', 0)`.
- Ideally, additional authentication and security checks should be implemented for production.
