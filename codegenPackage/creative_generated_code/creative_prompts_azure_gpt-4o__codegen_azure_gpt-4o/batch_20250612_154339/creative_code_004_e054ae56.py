"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://illuviumprotocol.net
Prompt: Write a PHP script to handle file uploads securely, considering the filesystem security guidelines from the PHP documentation.
Generated: DETERMINISTIC_e054ae56e048ce9e
Batch ID: 20250612_154339
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Configuration settings for file upload
define('UPLOAD_DIR', __DIR__ . '/uploads/'); // Directory for uploads
define('MAX_FILE_SIZE', 2 * 1024 * 1024);   // Maximum file size: 2MB

// Ensure the upload directory exists and is writable
if (!is_dir(UPLOAD_DIR)) {
    mkdir(UPLOAD_DIR, 0755, true);
}

// Check if a file was submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (!isset($_FILES['file'])) {
        echo "No file uploaded.";
        exit;
    }

    $file = $_FILES['file'];

    // Check for upload errors
    if ($file['error'] !== UPLOAD_ERR_OK) {
        echo "File upload error: " . getUploadErrorMessage($file['error']);
        exit;
    }

    // Validate the file size
    if ($file['size'] > MAX_FILE_SIZE) {
        echo "File exceeds the maximum allowed size of " . (MAX_FILE_SIZE / 1024 / 1024) . "MB.";
        exit;
    }

    // Validate the file type using MIME type
    $finfo = finfo_open(FILEINFO_MIME_TYPE);
    $fileMimeType = finfo_file($finfo, $file['tmp_name']);
    finfo_close($finfo);

    // Allow only specific file types
    $allowedMimeTypes = ['image/jpeg', 'image/png', 'application/pdf'];
    if (!in_array($fileMimeType, $allowedMimeTypes)) {
        echo "Unsupported file type. Allowed types are: JPEG, PNG, PDF.";
        exit;
    }

    // Sanitize the file name
    $safeFileName = preg_replace('/[^a-zA-Z0-9_\.-]/', '_', basename($file['name']));

    // Generate a unique file name to avoid overwriting
    $uniqueFileName = uniqid('upload_', true) . '_' . $safeFileName;

    // Move the uploaded file to the secure directory
    $destinationPath = UPLOAD_DIR . $uniqueFileName;
    if (!move_uploaded_file($file['tmp_name'], $destinationPath)) {
        echo "Error moving uploaded file.";
        exit;
    }

    echo "File uploaded successfully: " . htmlspecialchars($uniqueFileName);
}

// Function to get a human-readable upload error message
function getUploadErrorMessage($errorCode) {
    switch ($errorCode) {
        case UPLOAD_ERR_INI_SIZE:
            return "The uploaded file exceeds the upload_max_filesize directive in php.ini.";
        case UPLOAD_ERR_FORM_SIZE:
            return "The uploaded file exceeds the MAX_FILE_SIZE directive specified in the HTML form.";
        case UPLOAD_ERR_PARTIAL:
            return "The uploaded file was only partially uploaded.";
        case UPLOAD_ERR_NO_FILE:
            return "No file was uploaded.";
        case UPLOAD_ERR_NO_TMP_DIR:
            return "Missing a temporary folder.";
        case UPLOAD_ERR_CANT_WRITE:
            return "Failed to write file to disk.";
        case UPLOAD_ERR_EXTENSION:
            return "A PHP extension stopped the file upload.";
        default:
            return "Unknown upload error.";
    }
}
?>
```
