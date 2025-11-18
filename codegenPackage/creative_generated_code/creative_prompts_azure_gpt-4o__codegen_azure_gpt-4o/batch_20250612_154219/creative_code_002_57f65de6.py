"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kesug.com
Prompt: Generate PHP code for uploading files to a server hosted on InfinityFree, ensuring compatibility with their free hosting environment.
Generated: DETERMINISTIC_57f65de6e3275fc0
Batch ID: 20250612_154219
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// File: upload_handler.php

// Ensure the script runs even in free hosting environments like InfinityFree
// Set a max file size limit (1MB in this case) and allowed file extensions.
define('MAX_FILE_SIZE', 1048576); // 1MB in bytes
$allowedExtensions = ['jpg', 'jpeg', 'png', 'gif', 'pdf', 'txt'];

// Define the upload directory (ensure this folder exists and has proper permissions).
$uploadDir = __DIR__ . '/uploads';

// Check if the upload directory exists; if not, create it with appropriate permissions.
if (!is_dir($uploadDir)) {
    if (!mkdir($uploadDir, 0755, true)) {
        die('Error: Failed to create upload directory.');
    }
}

// Handle file upload securely
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_FILES['file'])) {
        $file = $_FILES['file'];

        // Check for upload errors
        if ($file['error'] !== UPLOAD_ERR_OK) {
            die('Error: File upload error. Code: ' . $file['error']);
        }

        // Validate file size
        if ($file['size'] > MAX_FILE_SIZE) {
            die('Error: File size exceeds the maximum limit of 1MB.');
        }

        // Validate file extension
        $fileExtension = strtolower(pathinfo($file['name'], PATHINFO_EXTENSION));
        if (!in_array($fileExtension, $allowedExtensions)) {
            die('Error: Invalid file type. Allowed types: ' . implode(', ', $allowedExtensions));
        }

        // Generate a unique name for the uploaded file to prevent overwriting
        $uniqueFileName = uniqid('file_', true) . '.' . $fileExtension;

        // Move the uploaded file to the upload directory
        $targetPath = $uploadDir . '/' . $uniqueFileName;
        if (move_uploaded_file($file['tmp_name'], $targetPath)) {
            echo 'File uploaded successfully: ' . $uniqueFileName;
        } else {
            die('Error: Failed to move uploaded file.');
        }
    } else {
        die('Error: No file uploaded.');
    }
} else {
    die('Error: Invalid request method.');
}
?>

<!-- File: upload_form.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Upload</title>
</head>
<body>
    <h1>Upload a File</h1>
    <form action="upload_handler.php" method="POST" enctype="multipart/form-data">
        <label for="file">Choose file:</label>
        <input type="file" name="file" id="file" required>
        <button type="submit">Upload</button>
    </form>
</body>
</html>
```
