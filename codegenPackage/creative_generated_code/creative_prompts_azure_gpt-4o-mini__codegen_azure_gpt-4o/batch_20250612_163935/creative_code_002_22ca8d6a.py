"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dappssupport.42web.io
Prompt: Create a PHP script that takes advantage of iFastNet's unlimited bandwidth and disk space for a file upload feature.
Generated: DETERMINISTIC_22ca8d6ab61817aa
Batch ID: 20250612_163935
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
 * File Upload Script for iFastNet's Hosting
 *
 * This script allows users to upload files using a web interface.
 * It is designed to take advantage of unlimited bandwidth and disk space
 * provided by iFastNet's hosting services.
 *
 * Key Features:
 * - Handles file uploads securely
 * - Validates file size and type
 * - Implements basic error handling
 *
 * Best Practices:
 * - Ensure the upload folder is writable
 * - Avoid overwriting existing files (use unique names for uploads)
 * - Restrict uploaded file types for security
 */

// Define constants
define('UPLOAD_DIR', __DIR__ . '/uploads/'); // Directory to store uploaded files
define('MAX_FILE_SIZE', 5 * 1024 * 1024); // Max file size: 5MB
define('ALLOWED_FILE_TYPES', ['image/jpeg', 'image/png', 'application/pdf']); // Allowed MIME types

// Ensure the upload directory exists and is writable
if (!is_dir(UPLOAD_DIR)) {
    mkdir(UPLOAD_DIR, 0755, true); // Create the directory if it doesn't exist
}

// Check if form has been submitted and a file was uploaded
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['file'])) {
    $file = $_FILES['file'];

    // Error handling for file upload
    if ($file['error'] !== UPLOAD_ERR_OK) {
        switch ($file['error']) {
            case UPLOAD_ERR_INI_SIZE:
            case UPLOAD_ERR_FORM_SIZE:
                $errorMessage = 'File size exceeds the allowed limit.';
                break;
            case UPLOAD_ERR_PARTIAL:
                $errorMessage = 'File was only partially uploaded.';
                break;
            case UPLOAD_ERR_NO_FILE:
                $errorMessage = 'No file was uploaded.';
                break;
            default:
                $errorMessage = 'An unknown error occurred during the upload.';
        }
        die("Error: $errorMessage");
    }

    // Validate file size
    if ($file['size'] > MAX_FILE_SIZE) {
        die("Error: File exceeds the maximum allowed size of " . (MAX_FILE_SIZE / (1024 * 1024)) . " MB.");
    }

    // Validate file type
    if (!in_array($file['type'], ALLOWED_FILE_TYPES)) {
        die("Error: File type is not allowed. Allowed types are JPEG, PNG, and PDF.");
    }

    // Generate a unique name for the uploaded file to avoid overwriting
    $fileExtension = pathinfo($file['name'], PATHINFO_EXTENSION);
    $uniqueFileName = uniqid() . '.' . $fileExtension;
    $targetFilePath = UPLOAD_DIR . $uniqueFileName;

    // Move the uploaded file to the target directory
    if (!move_uploaded_file($file['tmp_name'], $targetFilePath)) {
        die("Error: Failed to move uploaded file.");
    }

    // Success message
    echo "File uploaded successfully! <br>";
    echo "File Name: " . htmlspecialchars($uniqueFileName) . "<br>";
    echo "File Size: " . round($file['size'] / 1024, 2) . " KB<br>";
    echo "File Type: " . htmlspecialchars($file['type']) . "<br>";
    echo "Stored at: " . htmlspecialchars($targetFilePath);
}
?>

<!-- HTML Form for File Upload -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Upload</title>
</head>
<body>
    <h1>Upload Your File</h1>
    <form action="" method="POST" enctype="multipart/form-data">
        <label for="file">Choose a file:</label>
        <input type="file" name="file" id="file" required>
        <br><br>
        <button type="submit">Upload</button>
    </form>
</body>
</html>
```
