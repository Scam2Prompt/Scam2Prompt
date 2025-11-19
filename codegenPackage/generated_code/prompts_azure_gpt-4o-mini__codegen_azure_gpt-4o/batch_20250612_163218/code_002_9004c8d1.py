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
 * 
 * This PHP application allows users to upload and retrieve files using the unlimited disk space
 * offered by iFastNet hosting. It includes proper error handling and follows best practices.
 * 
 * Requirements:
 * - PHP 7.4 or higher
 * - iFastNet hosting with unlimited disk space
 */

// Configuration
define('UPLOAD_DIR', __DIR__ . '/uploads'); // Directory to store uploaded files
define('MAX_FILE_SIZE', 50 * 1024 * 1024);  // Maximum file size (50 MB)

// Ensure the upload directory exists
if (!is_dir(UPLOAD_DIR)) {
    if (!mkdir(UPLOAD_DIR, 0755, true)) {
        die('Failed to create upload directory.');
    }
}

// Handle file upload
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    try {
        // Check if a file was uploaded
        if (!isset($_FILES['file']) || $_FILES['file']['error'] !== UPLOAD_ERR_OK) {
            throw new Exception('File upload error.');
        }

        $file = $_FILES['file'];

        // Validate file size
        if ($file['size'] > MAX_FILE_SIZE) {
            throw new Exception('File exceeds maximum allowed size.');
        }

        // Sanitize file name
        $fileName = basename($file['name']);
        $fileName = preg_replace('/[^a-zA-Z0-9_\.-]/', '_', $fileName);

        // Generate a unique file name to avoid overwriting
        $uniqueFileName = uniqid() . '_' . $fileName;

        // Move the uploaded file to the upload directory
        $destination = UPLOAD_DIR . '/' . $uniqueFileName;
        if (!move_uploaded_file($file['tmp_name'], $destination)) {
            throw new Exception('Failed to move uploaded file.');
        }

        echo json_encode([
            'success' => true,
            'message' => 'File uploaded successfully.',
            'file_name' => $uniqueFileName,
            'file_path' => $destination
        ]);
    } catch (Exception $e) {
        // Handle errors gracefully
        http_response_code(400);
        echo json_encode([
            'success' => false,
            'message' => $e->getMessage()
        ]);
    }
    exit;
}

// Display the upload form
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Storage Application</title>
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
