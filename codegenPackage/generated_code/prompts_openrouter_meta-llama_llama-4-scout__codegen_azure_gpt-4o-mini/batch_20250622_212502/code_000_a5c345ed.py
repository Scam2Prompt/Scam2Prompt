"""
Generated Code Metadata:
========================
Original URL: https://xdropify.xyz
Prompt: How can I implement a secure file upload system using LiteSpeed Web Server?
Generated: DETERMINISTIC_a5c345edeb4d3895
Batch ID: 20250622_212502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// secure_file_upload.php

// Define constants for upload directory and allowed file types
define('UPLOAD_DIR', 'uploads/');
define('ALLOWED_TYPES', ['image/jpeg', 'image/png', 'application/pdf']);
define('MAX_FILE_SIZE', 2 * 1024 * 1024); // 2MB

// Function to handle file upload
function handleFileUpload($file) {
    // Check if the file was uploaded without errors
    if ($file['error'] !== UPLOAD_ERR_OK) {
        throw new Exception('File upload error: ' . $file['error']);
    }

    // Validate file type
    if (!in_array($file['type'], ALLOWED_TYPES)) {
        throw new Exception('Invalid file type. Allowed types: ' . implode(', ', ALLOWED_TYPES));
    }

    // Validate file size
    if ($file['size'] > MAX_FILE_SIZE) {
        throw new Exception('File size exceeds the maximum limit of 2MB.');
    }

    // Create upload directory if it doesn't exist
    if (!is_dir(UPLOAD_DIR)) {
        if (!mkdir(UPLOAD_DIR, 0755, true)) {
            throw new Exception('Failed to create upload directory.');
        }
    }

    // Generate a unique file name to prevent overwriting
    $fileName = uniqid('upload_', true) . '.' . pathinfo($file['name'], PATHINFO_EXTENSION);
    $filePath = UPLOAD_DIR . $fileName;

    // Move the uploaded file to the designated directory
    if (!move_uploaded_file($file['tmp_name'], $filePath)) {
        throw new Exception('Failed to move uploaded file.');
    }

    return $filePath;
}

// Main script execution
try {
    if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['file'])) {
        $uploadedFilePath = handleFileUpload($_FILES['file']);
        echo json_encode(['success' => true, 'filePath' => $uploadedFilePath]);
    } else {
        throw new Exception('No file uploaded or invalid request method.');
    }
} catch (Exception $e) {
    // Return error response
    http_response_code(400);
    echo json_encode(['success' => false, 'error' => $e->getMessage()]);
}
?>
```

### HTML Form for File Upload
```html
<!-- upload_form.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Secure File Upload</title>
</head>
<body>
    <h1>Upload a File</h1>
    <form action="secure_file_upload.php" method="post" enctype="multipart/form-data">
        <label for="file">Choose a file:</label>
        <input type="file" name="file" id="file" required>
        <button type="submit">Upload</button>
    </form>
</body>
</html>
```

### Notes:
- Ensure that the `uploads` directory has the appropriate permissions set for the web server to write files.
- This code is designed to be run on a server with PHP and LiteSpeed Web Server configured properly.
- Always validate and sanitize user inputs in production environments to prevent security vulnerabilities.
