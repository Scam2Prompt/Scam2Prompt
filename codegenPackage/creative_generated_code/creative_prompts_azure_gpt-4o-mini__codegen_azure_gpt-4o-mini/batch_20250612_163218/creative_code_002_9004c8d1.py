"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aidsupport.rf.gd
Prompt: Create a PHP application that takes advantage of the unlimited disk space offered by iFastNet for file storage.
Generated: DETERMINISTIC_9004c8d11063ac09
Batch ID: 20250612_163218
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// File: FileStorage.php

/**
 * A simple PHP application for managing file uploads to unlimited disk space
 * offered by iFastNet.
 */
class FileStorage
{
    private $uploadDir;

    // Constructor to set the upload directory
    public function __construct($uploadDir)
    {
        // Set the upload directory and create it if it doesn't exist
        $this->uploadDir = rtrim($uploadDir, '/') . '/';
        if (!is_dir($this->uploadDir) && !mkdir($this->uploadDir, 0755, true)) {
            throw new Exception("Failed to create upload directory: " . $this->uploadDir);
        }
    }

    /**
     * Upload a file to the server.
     * 
     * @param array $file The file data from the $_FILES superglobal.
     * @return string The path to the uploaded file.
     * @throws Exception If the upload fails.
     */
    public function uploadFile($file)
    {
        // Validate the file array
        if (!isset($file['error']) || is_array($file['error'])) {
            throw new InvalidArgumentException('Invalid file upload.');
        }

        // Check for upload errors
        switch ($file['error']) {
            case UPLOAD_ERR_OK:
                break;
            case UPLOAD_ERR_NO_FILE:
                throw new Exception('No file was uploaded.');
            case UPLOAD_ERR_INI_SIZE:
            case UPLOAD_ERR_FORM_SIZE:
                throw new Exception('File is too large.');
            default:
                throw new Exception('Unknown error occurred during file upload.');
        }

        // Validate file type and size if necessary (optional)
        $this->validateFile($file);

        // Generate a unique filename and move the uploaded file
        $filename = uniqid('', true) . '-' . basename($file['name']);
        $destination = $this->uploadDir . $filename;

        if (!move_uploaded_file($file['tmp_name'], $destination)) {
            throw new Exception('Failed to move uploaded file.');
        }

        return $destination; // Return the path to the uploaded file
    }

    /**
     * Validate the uploaded file type and size.
     * 
     * @param array $file The file data from the $_FILES superglobal.
     * @throws Exception If the file validation fails.
     */
    private function validateFile($file)
    {
        // Example: Restrict to specific file types (optional)
        $allowedMimeTypes = ['image/jpeg', 'image/png', 'application/pdf'];
        $fileMimeType = mime_content_type($file['tmp_name']);

        if (!in_array($fileMimeType, $allowedMimeTypes)) {
            throw new Exception('File type not allowed.');
        }

        // Example: Check file size (optional)
        if ($file['size'] > 5 * 1024 * 1024) { // Limit to 5MB
            throw new Exception('File size exceeds limit.');
        }
    }
}

// Usage example
try {
    // Set the upload directory
    $uploadDir = __DIR__ . '/uploads';
    $fileStorage = new FileStorage($uploadDir);

    // Handle file upload
    if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['fileToUpload'])) {
        $uploadedFilePath = $fileStorage->uploadFile($_FILES['fileToUpload']);
        echo "File uploaded successfully: " . htmlspecialchars($uploadedFilePath);
    }
} catch (Exception $e) {
    // Handle exceptions and display error message
    echo "Error: " . htmlspecialchars($e->getMessage());
}
?>

<!-- HTML Form for File Upload -->
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
        <input type="file" name="fileToUpload" required>
        <button type="submit">Upload</button>
    </form>
</body>
</html>
```
