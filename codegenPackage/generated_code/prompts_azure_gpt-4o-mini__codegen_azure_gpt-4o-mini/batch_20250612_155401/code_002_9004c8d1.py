"""
Generated Code Metadata:
========================
Original URL: https://webautomigrate.hstn.me
Prompt: Create a PHP application that takes advantage of the unlimited disk space offered by iFastNet for file storage.
Generated: DETERMINISTIC_9004c8d11063ac09
Batch ID: 20250612_155401
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
 * File Storage Application
 * This application allows users to upload files to the server using iFastNet's unlimited disk space.
 * It includes error handling, file validation, and secure file storage practices.
 */

// Define constants for upload directory and allowed file types
define('UPLOAD_DIR', 'uploads/');
define('ALLOWED_FILE_TYPES', ['image/jpeg', 'image/png', 'application/pdf', 'text/plain']);
define('MAX_FILE_SIZE', 5 * 1024 * 1024); // 5 MB

// Create the upload directory if it doesn't exist
if (!is_dir(UPLOAD_DIR)) {
    mkdir(UPLOAD_DIR, 0755, true);
}

/**
 * Function to handle file upload
 *
 * @return void
 */
function handleFileUpload() {
    // Check if a file was uploaded
    if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['file'])) {
        $file = $_FILES['file'];

        // Validate file upload
        if ($file['error'] !== UPLOAD_ERR_OK) {
            echo "Error during file upload: " . getUploadError($file['error']);
            return;
        }

        // Check file size
        if ($file['size'] > MAX_FILE_SIZE) {
            echo "File size exceeds the maximum limit of 5 MB.";
            return;
        }

        // Check file type
        if (!in_array($file['type'], ALLOWED_FILE_TYPES)) {
            echo "Invalid file type. Allowed types: " . implode(', ', ALLOWED_FILE_TYPES);
            return;
        }

        // Generate a unique file name to prevent overwriting
        $fileName = uniqid() . '-' . basename($file['name']);
        $targetFilePath = UPLOAD_DIR . $fileName;

        // Move the uploaded file to the target directory
        if (move_uploaded_file($file['tmp_name'], $targetFilePath)) {
            echo "File uploaded successfully: " . htmlspecialchars($fileName);
        } else {
            echo "Error moving the uploaded file.";
        }
    }
}

/**
 * Function to get a user-friendly error message for file upload errors
 *
 * @param int $errorCode
 * @return string
 */
function getUploadError($errorCode) {
    switch ($errorCode) {
        case UPLOAD_ERR_INI_SIZE:
        case UPLOAD_ERR_FORM_SIZE:
            return "File is too large.";
        case UPLOAD_ERR_PARTIAL:
            return "File was only partially uploaded.";
        case UPLOAD_ERR_NO_FILE:
            return "No file was uploaded.";
        case UPLOAD_ERR_NO_TMP_DIR:
            return "Missing a temporary folder.";
        case UPLOAD_ERR_CANT_WRITE:
            return "Failed to write file to disk.";
        case UPLOAD_ERR_EXTENSION:
            return "File upload stopped by a PHP extension.";
        default:
            return "Unknown upload error.";
    }
}

// Call the file upload handler
handleFileUpload();
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
        <input type="file" name="file" required>
        <button type="submit">Upload</button>
    </form>
</body>
</html>
```
