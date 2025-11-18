"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hubfix.rf.gd
Prompt: Create a PHP script to manage file uploads on a hosting service with unlimited disk space and no daily hit limit, as described on iFastNet.
Generated: DETERMINISTIC_13435ab0cfb9e64b
Batch ID: 20250612_154236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
/**
 * File Upload Manager Script
 * Author: [Your Name]
 * Date: [Today's Date]
 * Description: This script is designed for a hosting service with unlimited disk space
 * and no daily hit limit, allowing users to upload files securely.
 */

// Define constants
define('UPLOAD_DIR', __DIR__ . '/uploads/'); // Directory where files will be uploaded
define('MAX_FILE_SIZE', 10 * 1024 * 1024);  // Max file size (10 MB)

/**
 * Ensure the upload directory exists and is writable.
 */
if (!is_dir(UPLOAD_DIR)) {
    if (!mkdir(UPLOAD_DIR, 0755, true)) {
        die('Failed to create upload directory.');
    }
}

if (!is_writable(UPLOAD_DIR)) {
    die('Upload directory is not writable.');
}

/**
 * Handle the file upload process.
 */
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['file'])) {
    $file = $_FILES['file'];
    
    try {
        // Validate upload errors
        if ($file['error'] !== UPLOAD_ERR_OK) {
            throw new RuntimeException('File upload error: ' . $file['error']);
        }

        // Validate file size
        if ($file['size'] > MAX_FILE_SIZE) {
            throw new RuntimeException('File size exceeds the maximum limit of ' . (MAX_FILE_SIZE / 1024 / 1024) . ' MB.');
        }

        // Validate file type (optional, add your allowed mime types here)
        $allowedMimeTypes = ['image/jpeg', 'image/png', 'application/pdf'];
        $finfo = new finfo(FILEINFO_MIME_TYPE);
        $mimeType = $finfo->file($file['tmp_name']);
        if (!in_array($mimeType, $allowedMimeTypes)) {
            throw new RuntimeException('Invalid file type.');
        }

        // Generate a unique name for the file
        $fileExtension = pathinfo($file['name'], PATHINFO_EXTENSION);
        $fileName = uniqid('file_', true) . '.' . $fileExtension;

        // Move the uploaded file to the target directory
        $filePath = UPLOAD_DIR . $fileName;
        if (!move_uploaded_file($file['tmp_name'], $filePath)) {
            throw new RuntimeException('Failed to move uploaded file.');
        }

        // Success response
        echo json_encode([
            'status' => 'success',
            'message' => 'File uploaded successfully.',
            'file_path' => $filePath
        ]);
    } catch (RuntimeException $e) {
        // Error response
        http_response_code(400);
        echo json_encode([
            'status' => 'error',
            'message' => $e->getMessage()
        ]);
    }
} else {
    // Display a basic HTML form (optional)
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
    <?php
}
?>
```
