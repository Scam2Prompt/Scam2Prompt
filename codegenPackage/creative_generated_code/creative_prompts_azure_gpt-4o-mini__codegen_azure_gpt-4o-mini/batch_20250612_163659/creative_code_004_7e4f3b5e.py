"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pancakeswap.kesug.com
Prompt: Create a PHP code example that demonstrates how to utilize the unlimited disk space feature on iFastNet hosting.
Generated: DETERMINISTIC_7e4f3b5eec396520
Batch ID: 20250612_163659
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
 * A simple script to demonstrate how to utilize the unlimited disk space feature
 * on iFastNet hosting by uploading files to the server.
 * 
 * This example allows users to upload a file and saves it to a specified directory.
 * Note: Ensure that the target directory has the correct permissions.
 */

// Define the target directory for uploads
define('UPLOAD_DIR', __DIR__ . '/uploads/');

// Create the uploads directory if it doesn't exist
if (!is_dir(UPLOAD_DIR)) {
    if (!mkdir(UPLOAD_DIR, 0755, true)) {
        die('Failed to create upload directory: ' . UPLOAD_DIR);
    }
}

// Check if a file was uploaded
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['fileToUpload'])) {
    $file = $_FILES['fileToUpload'];

    // Validate file upload
    if ($file['error'] !== UPLOAD_ERR_OK) {
        die('File upload error: ' . $file['error']);
    }

    // Sanitize file name
    $fileName = basename($file['name']);
    $targetFilePath = UPLOAD_DIR . $fileName;

    // Move uploaded file to the target directory
    if (move_uploaded_file($file['tmp_name'], $targetFilePath)) {
        echo "File uploaded successfully: " . htmlspecialchars($fileName);
    } else {
        die('Failed to move uploaded file.');
    }
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Upload Example</title>
</head>
<body>
    <h1>Upload a File</h1>
    <form action="" method="post" enctype="multipart/form-data">
        <label for="fileToUpload">Select file to upload:</label>
        <input type="file" name="fileToUpload" id="fileToUpload" required>
        <button type="submit">Upload File</button>
    </form>
</body>
</html>
```
