"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tezwerwal.42web.io
Prompt: Create a PHP application that takes advantage of iFastNet's unlimited bandwidth and disk space for file storage.
Generated: DETERMINISTIC_8702858bb6fcfda6
Batch ID: 20250612_164316
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
define('ALLOWED_TYPES', ['image/jpeg', 'image/png', 'image/gif', 'application/pdf']);

// Function to handle file uploads
function uploadFile($file) {
    // Check for errors during the upload
    if ($file['error'] !== UPLOAD_ERR_OK) {
        throw new RuntimeException('File upload error: ' . $file['error']);
    }

    // Validate file size
    if ($file['size'] > MAX_FILE_SIZE) {
        throw new RuntimeException('File is too large. Maximum size is ' . (MAX_FILE_SIZE / 1024 / 1024) . ' MB.');
    }

    // Validate file type
    if (!in_array($file['type'], ALLOWED_TYPES)) {
        throw new RuntimeException('Invalid file type. Allowed types are: ' . implode(', ', ALLOWED_TYPES));
    }

    // Generate a unique file name to prevent collisions
    $fileName = uniqid('', true) . '-' . basename($file['name']);
    $uploadPath = UPLOAD_DIR . $fileName;

    // Move the uploaded file to the designated upload directory
    if (!move_uploaded_file($file['tmp_name'], $uploadPath)) {
        throw new RuntimeException('Failed to move uploaded file.');
    }

    return $fileName;
}

// Check if the form has been submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    try {
        // Attempt to upload the file
        $uploadedFileName = uploadFile($_FILES['file']);
        echo "File uploaded successfully: " . htmlspecialchars($uploadedFileName);
    } catch (RuntimeException $e) {
        // Handle any errors that occur during upload
        echo 'Error: ' . htmlspecialchars($e->getMessage());
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>iFastNet File Upload</title>
</head>
<body>
    <h1>Upload a File</h1>
    <form action="" method="post" enctype="multipart/form-data">
        <label for="file">Select file to upload:</label>
        <input type="file" name="file" id="file" required>
        <button type="submit">Upload</button>
    </form>
</body>
</html>
```

**Note:** Ensure that the `uploads` directory exists and is writable by the web server. Adjust the `ALLOWED_TYPES` array as needed to fit your specific requirements.
