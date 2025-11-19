"""
Generated Code Metadata:
========================
Original URL: https://aidsupport.rf.gd
Prompt: Create a PHP application that takes advantage of the unlimited disk space offered by iFastNet for file storage.
Generated: DETERMINISTIC_9004c8d11063ac09
Batch ID: 20250612_163218
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
 * @param array $file The uploaded file information from $_FILES
 * @return string|false The path to the uploaded file or false on failure
 */
function uploadFile($file) {
    // Check for upload errors
    if ($file['error'] !== UPLOAD_ERR_OK) {
        return false;
    }

    // Validate file type
    if (!in_array($file['type'], ALLOWED_FILE_TYPES)) {
        return false;
    }

    // Validate file size
    if ($file['size'] > MAX_FILE_SIZE) {
        return false;
    }

    // Generate a unique file name to prevent overwriting
    $fileName = uniqid('', true) . '-' . basename($file['name']);
    $targetPath = UPLOAD_DIR . $fileName;

    // Move the uploaded file to the target directory
    if (move_uploaded_file($file['tmp_name'], $targetPath)) {
        return $targetPath;
    }

    return false;
}

// Check if a file has been uploaded
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['fileToUpload'])) {
    $uploadedFilePath = uploadFile($_FILES['fileToUpload']);

    if ($uploadedFilePath) {
        echo "File uploaded successfully: " . htmlspecialchars($uploadedFilePath);
    } else {
        echo "File upload failed. Please check the file type and size.";
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
        <label for="fileToUpload">Select file to upload:</label>
        <input type="file" name="fileToUpload" id="fileToUpload" required>
        <input type="submit" value="Upload File">
    </form>
</body>
</html>
```
