"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wombat-exchange.rf.gd
Prompt: Create a sample PHP application that demonstrates the use of unlimited disk space on iFastNet Web Hosting.
Generated: DETERMINISTIC_78b96ad49e1d1992
Batch ID: 20250612_162510
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
 * Sample PHP application to demonstrate file storage on unlimited disk space
 * using iFastNet Web Hosting.
 * 
 * Please ensure that your hosting plan has unlimited disk space enabled and 
 * that server limits (such as max execution time, file upload size, etc.) are reviewed.
 */

// Configuration
define('UPLOAD_DIRECTORY', __DIR__ . '/uploads'); // Upload directory

// Create the upload directory if it doesn't exist
if (!is_dir(UPLOAD_DIRECTORY)) {
    if (!mkdir(UPLOAD_DIRECTORY, 0755, true)) {
        die('Failed to create upload directory.');
    }
}

// Error handling for file upload
function handleUploadError($errorCode) {
    $errors = [
        UPLOAD_ERR_INI_SIZE => 'The uploaded file exceeds the upload_max_filesize directive in php.ini.',
        UPLOAD_ERR_FORM_SIZE => 'The uploaded file exceeds the MAX_FILE_SIZE directive in the HTML form.',
        UPLOAD_ERR_PARTIAL => 'The uploaded file was only partially uploaded.',
        UPLOAD_ERR_NO_FILE => 'No file was uploaded.',
        UPLOAD_ERR_NO_TMP_DIR => 'Missing a temporary folder.',
        UPLOAD_ERR_CANT_WRITE => 'Failed to write file to disk.',
        UPLOAD_ERR_EXTENSION => 'A PHP extension stopped the file upload.',
    ];

    return $errors[$errorCode] ?? 'Unknown upload error.';
}

// File upload processing
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['file'])) {
    $uploadedFile = $_FILES['file'];

    if ($uploadedFile['error'] !== UPLOAD_ERR_OK) {
        die('File upload error: ' . handleUploadError($uploadedFile['error']));
    }

    $destinationPath = UPLOAD_DIRECTORY . '/' . basename($uploadedFile['name']);

    // Move uploaded file to the upload directory
    if (!move_uploaded_file($uploadedFile['tmp_name'], $destinationPath)) {
        die('Failed to move uploaded file.');
    }

    echo 'File uploaded successfully!<br>';
    echo 'File path: ' . $destinationPath;
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Unlimited Disk Space Demo</title>
</head>
<body>
    <h1>Unlimited Disk Space Demonstration</h1>
    <form action="" method="POST" enctype="multipart/form-data">
        <label for="file">Choose a file to upload:</label>
        <input type="file" id="file" name="file" required>
        <button type="submit">Upload</button>
    </form>
    <p>Uploaded files are stored in the server's "uploads" directory.</p>
</body>
</html>
```
