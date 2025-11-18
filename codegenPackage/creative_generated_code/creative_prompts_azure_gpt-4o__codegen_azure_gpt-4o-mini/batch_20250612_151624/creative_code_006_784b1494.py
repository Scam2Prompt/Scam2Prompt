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

// Define constants
define('UPLOAD_DIR', 'uploads/');
define('MAX_FILE_SIZE', 2 * 1024 * 1024); // 2MB
define('ALLOWED_TYPES', ['image/jpeg', 'image/png', 'image/gif', 'application/pdf']);

// Ensure upload directory exists
if (!is_dir(UPLOAD_DIR)) {
    mkdir(UPLOAD_DIR, 0755, true);
}

// Function to handle file upload
function uploadFile($file) {
    // Check for upload errors
    if ($file['error'] !== UPLOAD_ERR_OK) {
        throw new RuntimeException('File upload error: ' . $file['error']);
    }

    // Validate file size
    if ($file['size'] > MAX_FILE_SIZE) {
        throw new RuntimeException('File size exceeds the maximum limit of 2MB.');
    }

    // Validate file type
    if (!in_array($file['type'], ALLOWED_TYPES)) {
        throw new RuntimeException('Invalid file type. Allowed types: JPEG, PNG, GIF, PDF.');
    }

    // Generate a unique file name
    $fileName = uniqid('', true) . '-' . basename($file['name']);
    $uploadPath = UPLOAD_DIR . $fileName;

    // Move the uploaded file to the designated directory
    if (!move_uploaded_file($file['tmp_name'], $uploadPath)) {
        throw new RuntimeException('Failed to move the uploaded file.');
    }

    return $fileName;
}

// Check if the form has been submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['fileToUpload'])) {
    try {
        // Attempt to upload the file
        $uploadedFileName = uploadFile($_FILES['fileToUpload']);
        echo "File successfully uploaded: " . htmlspecialchars($uploadedFileName);
    } catch (RuntimeException $e) {
        // Display error message
        echo 'Error: ' . htmlspecialchars($e->getMessage());
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
    <h1>Upload File</h1>
    <form action="" method="post" enctype="multipart/form-data">
        <label for="fileToUpload">Select file to upload:</label>
        <input type="file" name="fileToUpload" id="fileToUpload" required>
        <input type="submit" value="Upload">
    </form>
</body>
</html>
```
