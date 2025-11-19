"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cornucopias-program-rewards.mydiscussion.net
Prompt: Create a PHP application that takes advantage of iFastNet's unlimited bandwidth and disk space for file storage.
Generated: DETERMINISTIC_8702858bb6fcfda6
Batch ID: 20250612_155544
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// File Storage Application Using iFastNet's Unlimited Bandwidth and Disk Space
// Author: Expert Programmer
// Date: YYYY-MM-DD

/* 
 * Configuration for iFastNet server (replace with actual server details).
 * Make sure to secure these credentials in a production environment by storing 
 * them in environment variables or a secure configuration file.
 */
define('UPLOAD_DIRECTORY', 'uploads'); // Directory for storing files

// Ensure the upload directory exists (create it if not present)
if (!is_dir(UPLOAD_DIRECTORY)) {
    mkdir(UPLOAD_DIRECTORY, 0755, true);
}

/**
 * Function to handle file uploads.
 * Validates and stores files on the server.
 */
function handleFileUpload()
{
    // Check if a file was uploaded
    if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['uploaded_file'])) {
        // Extract file info
        $file = $_FILES['uploaded_file'];
        $fileName = basename($file['name']);
        $fileTmpPath = $file['tmp_name'];
        $fileSize = $file['size'];
        $fileType = $file['type'];

        // Validate file size (example: max 10MB)
        $maxFileSize = 10 * 1024 * 1024; // 10MB
        if ($fileSize > $maxFileSize) {
            echo 'Error: File size exceeds the maximum allowed limit of 10MB.';
            return;
        }

        // Specify allowed file types (example: images and text files)
        $allowedFileTypes = ['image/jpeg', 'image/png', 'text/plain', 'application/pdf'];
        if (!in_array($fileType, $allowedFileTypes)) {
            echo 'Error: File type not permitted.';
            return;
        }

        // Sanitize file name to prevent security issues
        $safeFileName = preg_replace('/[^a-zA-Z0-9-_\.]/', '_', $fileName);
        $destinationPath = UPLOAD_DIRECTORY . DIRECTORY_SEPARATOR . $safeFileName;

        // Move uploaded file to the destination directory
        if (move_uploaded_file($fileTmpPath, $destinationPath)) {
            echo 'Success: File uploaded successfully.';
        } else {
            echo 'Error: Failed to upload the file.';
        }
    } else {
        echo 'Error: No file uploaded.';
    }
}

/**
 * Function to display uploaded files.
 */
function displayUploadedFiles()
{
    // Scan the upload directory for files
    $files = scandir(UPLOAD_DIRECTORY);

    // Filter out '.' and '..'
    $uploadedFiles = array_filter($files, fn($file) => $file !== '.' && $file !== '..');

    echo '<h2>Uploaded Files:</h2>';
    echo '<ul>';
    foreach ($uploadedFiles as $file) {
        $filePath = UPLOAD_DIRECTORY . DIRECTORY_SEPARATOR . $file;
        echo '<li><a href="' . $filePath . '" target="_blank">' . htmlspecialchars($file) . '</a></li>';
    }
    echo '</ul>';
}

// Handle file upload action
handleFileUpload();

// Display previously uploaded files
displayUploadedFiles();
?>

<!-- HTML Form for File Upload -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Storage Application</title>
</head>
<body>
    <h1>File Storage on iFastNet</h1>
    <form action="" method="POST" enctype="multipart/form-data">
        <label for="file">Choose a file to upload:</label>
        <input type="file" name="uploaded_file" id="file" required>
        <button type="submit">Upload</button>
    </form>
</body>
</html>
```
