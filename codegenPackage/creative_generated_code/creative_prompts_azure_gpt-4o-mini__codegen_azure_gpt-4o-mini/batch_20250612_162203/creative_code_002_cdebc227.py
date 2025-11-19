"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://openseaaward-program.epizy.com
Prompt: Create a PHP script that utilizes the unlimited bandwidth feature of iFastNet hosting for a file upload service.
Generated: DETERMINISTIC_cdebc227954df6dd
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// file_upload.php

/**
 * File Upload Service
 *
 * This script allows users to upload files to the server utilizing the unlimited bandwidth feature of iFastNet hosting.
 * It includes error handling, file type validation, and secure upload practices.
 */

// Define allowed file types
$allowedFileTypes = ['image/jpeg', 'image/png', 'image/gif', 'application/pdf', 'text/plain'];

// Define maximum file size (e.g., 10 MB)
$maxFileSize = 10 * 1024 * 1024; // 10 MB in bytes

// Function to handle file upload
function uploadFile($file)
{
    global $allowedFileTypes, $maxFileSize;

    // Check if file was uploaded without errors
    if (isset($file) && $file['error'] === UPLOAD_ERR_OK) {
        // Validate file type
        if (!in_array($file['type'], $allowedFileTypes)) {
            return "Error: Unsupported file type. Allowed types: " . implode(', ', $allowedFileTypes);
        }

        // Validate file size
        if ($file['size'] > $maxFileSize) {
            return "Error: File size exceeds the maximum limit of " . ($maxFileSize / 1024 / 1024) . " MB.";
        }

        // Specify the upload directory
        $uploadDirectory = 'uploads/';

        // Check if the upload directory exists, if not create it
        if (!is_dir($uploadDirectory)) {
            mkdir($uploadDirectory, 0755, true);
        }

        // Generate a unique file name to prevent overwriting
        $fileName = uniqid('', true) . '-' . basename($file['name']);
        $uploadFilePath = $uploadDirectory . $fileName;

        // Attempt to move the uploaded file to the specified directory
        if (move_uploaded_file($file['tmp_name'], $uploadFilePath)) {
            return "File uploaded successfully: " . htmlspecialchars($uploadFilePath);
        } else {
            return "Error: Failed to move uploaded file.";
        }
    } else {
        return "Error: No file uploaded or there was an upload error.";
    }
}

// Check if a file is posted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Call the upload function and capture the response
    $response = uploadFile($_FILES['file']);
    echo $response;
} else {
    // Display the file upload form when accessed via GET
    ?>
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>File Upload</title>
    </head>
    <body>
        <h1>Upload File</h1>
        <form action="" method="post" enctype="multipart/form-data">
            <label for="file">Choose file:</label>
            <input type="file" name="file" id="file" required>
            <input type="submit" value="Upload">
        </form>
    </body>
    </html>
    <?php
}
?>
```
