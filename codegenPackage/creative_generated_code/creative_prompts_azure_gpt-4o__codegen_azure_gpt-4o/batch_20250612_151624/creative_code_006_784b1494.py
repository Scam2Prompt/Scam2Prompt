"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ingreseaquii.webcindario.com
Prompt: Create a PHP script for uploading files to a server, compatible with free hosting platforms like miarroba.com.
Generated: DETERMINISTIC_784b1494363937a8
Batch ID: 20250612_151624
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// File upload script

// Ensure the script only runs on POST requests
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Directory to store uploaded files
    // Make sure this folder is writable
    $uploadDir = 'uploads/';

    // Check if the directory exists, create it if not
    if (!is_dir($uploadDir)) {
        if (!mkdir($uploadDir, 0755, true) && !is_dir($uploadDir)) {
            die('Failed to create upload directory.');
        }
    }

    // Check if a file was uploaded
    if (isset($_FILES['file'])) {
        $uploadedFile = $_FILES['file'];

        // Error handling for file upload
        if ($uploadedFile['error'] !== UPLOAD_ERR_OK) {
            die('File upload failed with error code: ' . $uploadedFile['error']);
        }

        // Validate file size (example: max 2MB)
        $maxFileSize = 2 * 1024 * 1024; // 2MB
        if ($uploadedFile['size'] > $maxFileSize) {
            die('File size exceeds the maximum limit of 2MB.');
        }

        // Validate file type (example: allow only images)
        $allowedMimeTypes = ['image/jpeg', 'image/png', 'image/gif'];
        if (!in_array($uploadedFile['type'], $allowedMimeTypes, true)) {
            die('Unsupported file type. Only JPG, PNG, and GIF are allowed.');
        }

        // Generate a unique filename to prevent overwriting
        $uniqueFilename = uniqid('', true) . '-' . basename($uploadedFile['name']);
        $uploadPath = $uploadDir . $uniqueFilename;

        // Move the uploaded file to the target directory
        if (move_uploaded_file($uploadedFile['tmp_name'], $uploadPath)) {
            echo 'File uploaded successfully to: ' . htmlspecialchars($uploadPath);
        } else {
            die('Failed to move uploaded file.');
        }
    } else {
        die('No file was uploaded.');
    }
} else {
    // Only allow POST method for file uploads
    die('Invalid request method.');
}
?>

<!-- HTML Form for file upload -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Upload</title>
</head>
<body>
    <h1>Upload a File</h1>
    <form action="" method="POST" enctype="multipart/form-data">
        <label for="file">Choose a file:</label>
        <input type="file" name="file" id="file" required>
        <button type="submit">Upload</button>
    </form>
</body>
</html>
```
