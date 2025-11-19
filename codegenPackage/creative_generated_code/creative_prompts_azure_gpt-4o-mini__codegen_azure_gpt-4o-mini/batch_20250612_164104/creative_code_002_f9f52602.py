"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapps-walletconnet-validation.rf.gd
Prompt: Create a PHP script that utilizes the unlimited bandwidth feature of iFastNet for a file upload service.
Generated: DETERMINISTIC_f9f526029063e938
Batch ID: 20250612_164104
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// File upload script for iFastNet hosting utilizing unlimited bandwidth feature

// Define the target directory for uploaded files
define('UPLOAD_DIR', __DIR__ . '/uploads/');

// Create the uploads directory if it doesn't exist
if (!is_dir(UPLOAD_DIR)) {
    if (!mkdir(UPLOAD_DIR, 0755, true)) {
        die('Failed to create upload directory.');
    }
}

/**
 * Validates the uploaded file.
 *
 * @param array $file The uploaded file information from $_FILES.
 * @return array An associative array containing the validation result and message.
 */
function validateFile($file) {
    $allowedMimeTypes = ['image/jpeg', 'image/png', 'image/gif', 'application/pdf'];
    $maxFileSize = 5 * 1024 * 1024; // 5 MB

    // Check for upload errors
    if ($file['error'] !== UPLOAD_ERR_OK) {
        return ['success' => false, 'message' => 'File upload error.'];
    }

    // Check for valid file size
    if ($file['size'] > $maxFileSize) {
        return ['success' => false, 'message' => 'File size exceeds the maximum limit of 5 MB.'];
    }

    // Check for valid MIME type
    if (!in_array(mime_content_type($file['tmp_name']), $allowedMimeTypes)) {
        return ['success' => false, 'message' => 'Invalid file type. Only JPG, PNG, GIF, and PDF are allowed.'];
    }

    return ['success' => true];
}

/**
 * Handles the file upload process.
 *
 * @param array $file The uploaded file information from $_FILES.
 * @return string The upload result message.
 */
function uploadFile($file) {
    $validation = validateFile($file);
    
    if (!$validation['success']) {
        return $validation['message'];
    }

    // Sanitize the file name and create a unique file path
    $fileName = basename($file['name']);
    $targetFilePath = UPLOAD_DIR . uniqid('', true) . '-' . $fileName;

    // Move the uploaded file to the target directory
    if (move_uploaded_file($file['tmp_name'], $targetFilePath)) {
        return 'File uploaded successfully: ' . htmlspecialchars($targetFilePath);
    } else {
        return 'Failed to move uploaded file.';
    }
}

// Check if a file has been uploaded
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['fileToUpload'])) {
    $uploadResult = uploadFile($_FILES['fileToUpload']);
} else {
    $uploadResult = 'No file uploaded.';
}

// Output the result message
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
        <label for="fileToUpload">Choose a file to upload:</label>
        <input type="file" name="fileToUpload" id="fileToUpload" required>
        <input type="submit" value="Upload">
    </form>
    <p><?php echo htmlspecialchars($uploadResult); ?></p>
</body>
</html>
```
