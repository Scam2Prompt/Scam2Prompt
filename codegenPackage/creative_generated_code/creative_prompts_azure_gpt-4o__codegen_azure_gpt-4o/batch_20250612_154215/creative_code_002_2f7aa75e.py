"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agromec.cl
Prompt: Generate a PHP script to upload and manage files on a Linux hosting server optimized for web hosting in Chile.
Generated: DETERMINISTIC_2f7aa75e1a02abb9
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// File: file_manager.php

// Configuration for file upload
define('UPLOAD_DIR', __DIR__ . '/uploads/');
define('MAX_FILE_SIZE', 5 * 1024 * 1024); // Maximum file size: 5MB
define('ALLOWED_FILE_TYPES', ['image/jpeg', 'image/png', 'application/pdf']); // Allowed MIME types

// Ensure the upload directory exists
if (!is_dir(UPLOAD_DIR)) {
    mkdir(UPLOAD_DIR, 0755, true);
}

/**
 * Handles file uploads and validation.
 *
 * @return void
 */
function handleFileUpload()
{
    if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['file'])) {
        $file = $_FILES['file'];

        // Check for errors during upload
        if ($file['error'] !== UPLOAD_ERR_OK) {
            echo "Error uploading file: " . getUploadErrorMessage($file['error']);
            return;
        }

        // Validate file size
        if ($file['size'] > MAX_FILE_SIZE) {
            echo "Error: File size exceeds the maximum limit of " . (MAX_FILE_SIZE / (1024 * 1024)) . "MB.";
            return;
        }

        // Validate file type
        if (!in_array($file['type'], ALLOWED_FILE_TYPES)) {
            echo "Error: Unsupported file type.";
            return;
        }

        // Generate a unique name for the file to avoid overwriting
        $uniqueFileName = uniqid('', true) . '-' . basename($file['name']);

        // Move the uploaded file to the upload directory
        if (move_uploaded_file($file['tmp_name'], UPLOAD_DIR . $uniqueFileName)) {
            echo "File uploaded successfully: " . $uniqueFileName;
        } else {
            echo "Error: Failed to move uploaded file.";
        }
    }
}

/**
 * Provides a human-readable error message for upload errors.
 *
 * @param int $errorCode The error code returned by the upload.
 * @return string The corresponding error message.
 */
function getUploadErrorMessage($errorCode)
{
    $errorMessages = [
        UPLOAD_ERR_OK => 'No error.',
        UPLOAD_ERR_INI_SIZE => 'The uploaded file exceeds the upload_max_filesize directive in php.ini.',
        UPLOAD_ERR_FORM_SIZE => 'The uploaded file exceeds the MAX_FILE_SIZE directive that was specified in the HTML form.',
        UPLOAD_ERR_PARTIAL => 'The uploaded file was only partially uploaded.',
        UPLOAD_ERR_NO_FILE => 'No file was uploaded.',
        UPLOAD_ERR_NO_TMP_DIR => 'Missing a temporary folder.',
        UPLOAD_ERR_CANT_WRITE => 'Failed to write file to disk.',
        UPLOAD_ERR_EXTENSION => 'A PHP extension stopped the file upload.',
    ];

    return $errorMessages[$errorCode] ?? 'Unknown error.';
}

/**
 * Displays the list of uploaded files.
 *
 * @return void
 */
function displayUploadedFiles()
{
    $files = array_diff(scandir(UPLOAD_DIR), ['.', '..']); // Exclude '.' and '..'

    if (empty($files)) {
        echo "No files uploaded yet.";
        return;
    }

    echo "<ul>";
    foreach ($files as $file) {
        echo "<li><a href='uploads/$file' target='_blank'>$file</a></li>";
    }
    echo "</ul>";
}

// Main execution logic
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Upload Manager</title>
</head>
<body>
    <h1>File Upload Manager</h1>

    <!-- File upload form -->
    <form action="" method="post" enctype="multipart/form-data">
        <label for="file">Select file to upload:</label>
        <input type="file" name="file" id="file" required>
        <button type="submit">Upload File</button>
    </form>

    <h2>Uploaded Files</h2>
    <?php
    // Process file upload
    handleFileUpload();

    // Display uploaded files
    displayUploadedFiles();
    ?>
</body>
</html>
```
