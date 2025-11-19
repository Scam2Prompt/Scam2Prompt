"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://illuviumprotocol.net
Prompt: Generate a code snippet that handles file uploads securely in PHP, referencing the security considerations mentioned on the PHP site.
Generated: DETERMINISTIC_45c83d8cb0382e7e
Batch ID: 20250612_155936
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Define a constant for the upload directory
define('UPLOAD_DIR', 'uploads/');

// Ensure the uploads directory exists and is writable
if (!is_dir(UPLOAD_DIR)) {
    mkdir(UPLOAD_DIR, 0755, true);
}

// Function to handle file uploads
function handleFileUpload($file) {
    // Allowed file types
    $allowedMimeTypes = ['image/jpeg', 'image/png', 'image/gif'];
    
    // Check if the file was uploaded without errors
    if ($file['error'] !== UPLOAD_ERR_OK) {
        throw new Exception('File upload error: ' . $file['error']);
    }

    // Validate the MIME type
    $finfo = finfo_open(FILEINFO_MIME_TYPE);
    $mimeType = finfo_file($finfo, $file['tmp_name']);
    finfo_close($finfo);
    
    if (!in_array($mimeType, $allowedMimeTypes)) {
        throw new Exception('Invalid file type: ' . $mimeType);
    }

    // Generate a unique file name to prevent overwriting
    $fileName = uniqid('upload_', true) . '.' . pathinfo($file['name'], PATHINFO_EXTENSION);
    $destination = UPLOAD_DIR . $fileName;

    // Move the file to the upload directory
    if (!move_uploaded_file($file['tmp_name'], $destination)) {
        throw new Exception('Failed to move uploaded file.');
    }

    return $fileName;
}

// Handle the form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    try {
        if (isset($_FILES['file'])) {
            $uploadedFileName = handleFileUpload($_FILES['file']);
            echo 'File uploaded successfully: ' . htmlspecialchars($uploadedFileName);
        } else {
            throw new Exception('No file uploaded.');
        }
    } catch (Exception $e) {
        // Log error message for debugging
        error_log($e->getMessage());
        // Display a user-friendly error message
        echo 'Error: ' . htmlspecialchars($e->getMessage());
    }
}
?>

<!-- HTML form for file upload -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Upload</title>
</head>
<body>
    <form action="" method="post" enctype="multipart/form-data">
        <input type="file" name="file" required>
        <button type="submit">Upload</button>
    </form>
</body>
</html>
```
