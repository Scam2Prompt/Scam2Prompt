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
// File upload handler script

// Define a target directory for file uploads
define('UPLOAD_DIR', __DIR__ . '/uploads/');

// Create the upload directory if it doesn't exist
if (!is_dir(UPLOAD_DIR)) {
    mkdir(UPLOAD_DIR, 0755, true);
}

// Function to handle file uploads
function handleFileUpload($file) {
    // Allowed file types (MIME types)
    $allowedMimeTypes = ['image/jpeg', 'image/png', 'image/gif'];
    
    // Check if the file was uploaded without errors
    if (isset($file) && $file['error'] === UPLOAD_ERR_OK) {
        $fileType = mime_content_type($file['tmp_name']);
        
        // Validate the MIME type
        if (!in_array($fileType, $allowedMimeTypes)) {
            throw new RuntimeException('Invalid file type. Only JPEG, PNG and GIF are allowed.');
        }

        // Generate a unique file name to prevent overwriting
        $fileName = uniqid('upload_', true) . '.' . pathinfo($file['name'], PATHINFO_EXTENSION);
        $targetFilePath = UPLOAD_DIR . $fileName;

        // Move the uploaded file to the target directory
        if (!move_uploaded_file($file['tmp_name'], $targetFilePath)) {
            throw new RuntimeException('Failed to move uploaded file.');
        }

        return $fileName; // Return the name of the uploaded file
    }

    // Handle other upload errors
    switch ($file['error']) {
        case UPLOAD_ERR_INI_SIZE:
        case UPLOAD_ERR_FORM_SIZE:
            throw new RuntimeException('Exceeded file size limit.');
        case UPLOAD_ERR_PARTIAL:
            throw new RuntimeException('File was only partially uploaded.');
        case UPLOAD_ERR_NO_FILE:
            throw new RuntimeException('No file was uploaded.');
        default:
            throw new RuntimeException('Unknown upload error.');
    }
}

// Main execution block
try {
    // Check if a file was uploaded via POST
    if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['fileToUpload'])) {
        $uploadedFileName = handleFileUpload($_FILES['fileToUpload']);
        echo 'File successfully uploaded: ' . htmlspecialchars($uploadedFileName);
    } else {
        echo 'No file uploaded.';
    }
} catch (RuntimeException $e) {
    // Handle exceptions and display error message
    echo 'Error: ' . htmlspecialchars($e->getMessage());
}
?>
```
