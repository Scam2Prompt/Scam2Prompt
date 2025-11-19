"""
Generated Code Metadata:
========================
Original URL: https://hubfix.rf.gd
Prompt: Create a PHP script to manage file uploads on a hosting service with unlimited disk space and no daily hit limit, as described on iFastNet.
Generated: DETERMINISTIC_13435ab0cfb9e64b
Batch ID: 20250612_154236
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
 * File Upload Management Script
 * 
 * This script handles file uploads to a hosting service with unlimited disk space.
 * It includes error handling, file type validation, and secure file storage.
 */

// Define upload directory
define('UPLOAD_DIR', 'uploads/');

// Create upload directory if it doesn't exist
if (!is_dir(UPLOAD_DIR)) {
    mkdir(UPLOAD_DIR, 0755, true);
}

/**
 * Function to handle file upload
 *
 * @param array $file The uploaded file information from $_FILES
 * @return string|false The path to the uploaded file or false on failure
 */
function uploadFile($file) {
    // Check for upload errors
    if ($file['error'] !== UPLOAD_ERR_OK) {
        return false; // Return false on error
    }

    // Validate file type (allow only specific types)
    $allowedTypes = ['image/jpeg', 'image/png', 'image/gif', 'application/pdf'];
    if (!in_array($file['type'], $allowedTypes)) {
        return false; // Return false if file type is not allowed
    }

    // Generate a unique file name to prevent overwriting
    $fileName = uniqid('', true) . '-' . basename($file['name']);
    $targetFilePath = UPLOAD_DIR . $fileName;

    // Move the uploaded file to the target directory
    if (move_uploaded_file($file['tmp_name'], $targetFilePath)) {
        return $targetFilePath; // Return the path of the uploaded file
    }

    return false; // Return false if the move operation failed
}

// Check if a file has been uploaded
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['fileToUpload'])) {
    $uploadedFilePath = uploadFile($_FILES['fileToUpload']);

    if ($uploadedFilePath) {
        echo "File uploaded successfully: " . htmlspecialchars($uploadedFilePath);
    } else {
        echo "File upload failed. Please check the file type and try again.";
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
    <h1>Upload a File</h1>
    <form action="" method="post" enctype="multipart/form-data">
        <input type="file" name="fileToUpload" required>
        <button type="submit">Upload</button>
    </form>
</body>
</html>
```
