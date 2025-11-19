"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pancakeswap.kesug.com
Prompt: Create a PHP code example that demonstrates how to utilize the unlimited disk space feature on iFastNet hosting.
Generated: DETERMINISTIC_7e4f3b5eec396520
Batch ID: 20250612_163659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// File: upload_file.php

// Description:
// This script demonstrates how to utilize the unlimited disk space feature on iFastNet hosting
// by allowing users to upload files to the server. Proper error handling and security measures
// have been implemented to make it production-ready.

// Configuration: Set the directory for file storage.
define('UPLOAD_DIR', __DIR__ . '/uploads');

// Ensure the upload directory exists and is writable.
if (!is_dir(UPLOAD_DIR)) {
    if (!mkdir(UPLOAD_DIR, 0755, true)) {
        die('Error: Failed to create upload directory.');
    }
}

// Handle file upload request.
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Check if a file was uploaded.
    if (isset($_FILES['file']) && $_FILES['file']['error'] === UPLOAD_ERR_OK) {
        $uploadedFile = $_FILES['file'];
        
        // Sanitize the original file name to prevent security risks (e.g., directory traversal).
        $originalFileName = basename($uploadedFile['name']);
        $safeFileName = preg_replace('/[^a-zA-Z0-9_\.-]/', '_', $originalFileName);
        
        // Define the full path for the uploaded file in the 'uploads' directory.
        $destination = UPLOAD_DIR . '/' . $safeFileName;

        // Check if the file already exists.
        if (file_exists($destination)) {
            echo 'Error: A file with the same name already exists.';
            exit;
        }

        // Move the uploaded file to the destination.
        if (move_uploaded_file($uploadedFile['tmp_name'], $destination)) {
            echo 'Success: File uploaded successfully.';
        } else {
            echo 'Error: Failed to move uploaded file.';
        }
    } else {
        // Handle upload errors.
        switch ($_FILES['file']['error']) {
            case UPLOAD_ERR_INI_SIZE:
            case UPLOAD_ERR_FORM_SIZE:
                echo 'Error: File size exceeds limit.';
                break;
            case UPLOAD_ERR_PARTIAL:
                echo 'Error: File upload was incomplete.';
                break;
            case UPLOAD_ERR_NO_FILE:
                echo 'Error: No file was uploaded.';
                break;
            default:
                echo 'Error: An unknown error occurred during file upload.';
                break;
        }
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Upload</title>
</head>
<body>
    <h1>File Upload Form</h1>
    <!-- A simple HTML form for file uploads -->
    <form action="upload_file.php" method="post" enctype="multipart/form-data">
        <label for="file">Choose a file to upload:</label>
        <input type="file" name="file" id="file" required>
        <button type="submit">Upload File</button>
    </form>
</body>
</html>
```
