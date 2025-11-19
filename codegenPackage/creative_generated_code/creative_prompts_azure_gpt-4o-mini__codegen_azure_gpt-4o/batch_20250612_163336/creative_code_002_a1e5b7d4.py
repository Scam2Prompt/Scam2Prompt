"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pancakeswap.epizy.com
Prompt: Create a PHP script that takes advantage of the unlimited disk space offered by iFastNet for file uploads.
Generated: DETERMINISTIC_a1e5b7d4cd13fdca
Batch ID: 20250612_163336
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// File Upload Script for iFastNet's Unlimited Disk Space

// Enable error reporting for debugging purposes. Disable in production.
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Define the directory to store uploaded files
define('UPLOAD_DIR', __DIR__ . '/uploads/');

// Ensure the upload directory exists; create it if not
if (!is_dir(UPLOAD_DIR)) {
    if (!mkdir(UPLOAD_DIR, 0755, true)) {
        die('Failed to create upload directory.');
    }
}

// Maximum file size in bytes (e.g., 100 MB)
// Set higher limits if necessary to utilize unlimited disk space
define('MAX_FILE_SIZE', 100 * 1024 * 1024);

// Allowed file types for upload
$allowedFileTypes = ['image/jpeg', 'image/png', 'application/pdf', 'text/plain'];

// Handle file upload
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['file'])) {
    $file = $_FILES['file'];

    // Check if the upload encountered errors
    if ($file['error'] !== UPLOAD_ERR_OK) {
        die('File upload encountered an error. Code: ' . $file['error']);
    }

    // Check file size
    if ($file['size'] > MAX_FILE_SIZE) {
        die('File exceeds maximum allowed size of ' . MAX_FILE_SIZE / (1024 * 1024) . ' MB.');
    }

    // Check file type
    if (!in_array($file['type'], $allowedFileTypes)) {
        die('File type not allowed. Allowed types are: ' . implode(', ', $allowedFileTypes));
    }

    // Generate a unique name for the file to avoid overwriting
    $uniqueFileName = uniqid('', true) . '-' . basename($file['name']);

    // Define the complete path for the uploaded file
    $destination = UPLOAD_DIR . $uniqueFileName;

    // Move the uploaded file to the destination directory
    if (!move_uploaded_file($file['tmp_name'], $destination)) {
        die('Failed to move uploaded file.');
    }

    // Success message
    echo 'File uploaded successfully! Location: ' . $destination;
} else {
    // Display the upload form if the request is not a POST
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
