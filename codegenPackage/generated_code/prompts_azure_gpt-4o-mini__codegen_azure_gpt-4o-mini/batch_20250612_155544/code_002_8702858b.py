"""
Generated Code Metadata:
========================
Original URL: https://cornucopias-program-rewards.mydiscussion.net
Prompt: Create a PHP application that takes advantage of iFastNet's unlimited bandwidth and disk space for file storage.
Generated: DETERMINISTIC_8702858bb6fcfda6
Batch ID: 20250612_155544
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
 * File Storage Application using iFastNet's Unlimited Bandwidth and Disk Space
 * 
 * This application allows users to upload files to the server and manage their uploads.
 * It includes error handling, file validation, and basic security measures.
 */

// Define constants for upload directory and allowed file types
define('UPLOAD_DIR', 'uploads/');
define('ALLOWED_FILE_TYPES', ['image/jpeg', 'image/png', 'application/pdf', 'text/plain']);
define('MAX_FILE_SIZE', 5 * 1024 * 1024); // 5 MB

// Create the upload directory if it doesn't exist
if (!is_dir(UPLOAD_DIR)) {
    mkdir(UPLOAD_DIR, 0755, true);
}

/**
 * Function to handle file uploads
 *
 * @return void
 */
function handleFileUpload() {
    // Check if a file was uploaded
    if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['fileToUpload'])) {
        $file = $_FILES['fileToUpload'];

        // Validate file size
        if ($file['size'] > MAX_FILE_SIZE) {
            echo "Error: File size exceeds the maximum limit of 5 MB.";
            return;
        }

        // Validate file type
        if (!in_array($file['type'], ALLOWED_FILE_TYPES)) {
            echo "Error: Invalid file type. Only JPEG, PNG, PDF, and TXT files are allowed.";
            return;
        }

        // Generate a unique file name to prevent overwriting
        $targetFile = UPLOAD_DIR . uniqid('', true) . '-' . basename($file['name']);

        // Attempt to move the uploaded file to the target directory
        if (move_uploaded_file($file['tmp_name'], $targetFile)) {
            echo "File uploaded successfully: " . htmlspecialchars($targetFile);
        } else {
            echo "Error: There was a problem uploading your file.";
        }
    }
}

// Call the file upload handler
handleFileUpload();
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
        <label for="fileToUpload">Choose file to upload:</label>
        <input type="file" name="fileToUpload" id="fileToUpload" required>
        <input type="submit" value="Upload File">
    </form>
</body>
</html>
```
