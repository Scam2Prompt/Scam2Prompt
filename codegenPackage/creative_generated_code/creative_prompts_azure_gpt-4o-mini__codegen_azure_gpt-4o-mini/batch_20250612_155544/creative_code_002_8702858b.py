"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cornucopias-program-rewards.mydiscussion.net
Prompt: Create a PHP application that takes advantage of iFastNet's unlimited bandwidth and disk space for file storage.
Generated: DETERMINISTIC_8702858bb6fcfda6
Batch ID: 20250612_155544
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// iFastNet File Storage Application

// Define constants for file upload settings
define('UPLOAD_DIR', 'uploads/');
define('MAX_FILE_SIZE', 10485760); // 10MB limit
define('ALLOWED_TYPES', ['image/jpeg', 'image/png', 'application/pdf', 'text/plain']);

// Function to handle file uploads
function uploadFile($file) {
    // Check if the file was uploaded without errors
    if ($file['error'] !== UPLOAD_ERR_OK) {
        return ['success' => false, 'message' => 'File upload error.'];
    }
    
    // Check file size
    if ($file['size'] > MAX_FILE_SIZE) {
        return ['success' => false, 'message' => 'File exceeds the maximum size limit.'];
    }
    
    // Check file type
    if (!in_array($file['type'], ALLOWED_TYPES)) {
        return ['success' => false, 'message' => 'Invalid file type.'];
    }
    
    // Create the uploads directory if it does not exist
    if (!is_dir(UPLOAD_DIR)) {
        mkdir(UPLOAD_DIR, 0755, true);
    }

    // Generate a unique filename to prevent collisions
    $filename = uniqid() . '-' . basename($file['name']);
    $targetFilePath = UPLOAD_DIR . $filename;

    // Move the uploaded file to the target directory
    if (move_uploaded_file($file['tmp_name'], $targetFilePath)) {
        return ['success' => true, 'message' => 'File uploaded successfully.', 'file_path' => $targetFilePath];
    } else {
        return ['success' => false, 'message' => 'Failed to move uploaded file.'];
    }
}

// Check if the form is submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Attempt to upload the file and capture the result
    $result = uploadFile($_FILES['file']);

    // Return the response
    header('Content-Type: application/json');
    echo json_encode($result);
    exit;
}

// HTML Form for file upload
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Upload</title>
</head>
<body>
    <h1>File Upload</h1>
    <form action="" method="POST" enctype="multipart/form-data">
        <label for="file">Choose a file to upload:</label>
        <input type="file" name="file" id="file" required>
        <button type="submit">Upload</button>
    </form>
</body>
</html>
```

This PHP application allows users to upload files while checking for file size and type, and providing appropriate success or error messages. The code is structured and follows best practices for error handling and file management.
