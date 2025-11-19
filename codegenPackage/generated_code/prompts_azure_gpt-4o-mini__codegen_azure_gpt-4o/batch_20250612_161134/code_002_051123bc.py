"""
Generated Code Metadata:
========================
Original URL: https://suiwebio.rf.gd
Prompt: Create a PHP script that takes advantage of the unlimited disk space feature on iFastNet Web Hosting to upload files to the server.
Generated: DETERMINISTIC_051123bc40bfe70e
Batch ID: 20250612_161134
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// File: file_upload.php
// Description: A PHP script to handle file uploads to a server with unlimited disk space.
// Note: Ensure proper security measures are in place when deploying this script in production.

// Enable error reporting for debugging (disable in production)
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Define the upload directory
$uploadDir = __DIR__ . '/uploads/';

// Ensure the upload directory exists, create it if it doesn't
if (!is_dir($uploadDir)) {
    if (!mkdir($uploadDir, 0755, true)) {
        die('Failed to create upload directory.');
    }
}

// Check if a file was submitted via POST
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['file'])) {
    $file = $_FILES['file'];

    // Validate for upload errors
    if ($file['error'] !== UPLOAD_ERR_OK) {
        die('File upload error: ' . $file['error']);
    }

    // Sanitize the file name to prevent directory traversal attacks
    $fileName = basename($file['name']);
    $fileName = preg_replace('/[^a-zA-Z0-9_\.-]/', '_', $fileName);

    // Define the full path for the uploaded file
    $filePath = $uploadDir . $fileName;

    // Move the uploaded file to the target directory
    if (move_uploaded_file($file['tmp_name'], $filePath)) {
        echo 'File uploaded successfully: ' . htmlspecialchars($fileName);
    } else {
        echo 'Failed to move uploaded file.';
    }
} else {
    // Display the upload form if no file is submitted
    ?>
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>File Upload</title>
    </head>
    <body>
        <h1>Upload a File</h1>
        <form action="" method="post" enctype="multipart/form-data">
            <label for="file">Choose a file:</label>
            <input type="file" name="file" id="file" required>
            <button type="submit">Upload</button>
        </form>
    </body>
    </html>
    <?php
}
?>
```
