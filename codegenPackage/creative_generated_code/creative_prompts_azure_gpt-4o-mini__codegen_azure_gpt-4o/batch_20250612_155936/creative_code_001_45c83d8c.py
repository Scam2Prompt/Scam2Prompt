"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://illuviumprotocol.net
Prompt: Generate a code snippet that handles file uploads securely in PHP, referencing the security considerations mentioned on the PHP site.
Generated: DETERMINISTIC_45c83d8cb0382e7e
Batch ID: 20250612_155936
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Define constants for upload directory and allowed file types
define('UPLOAD_DIR', __DIR__ . '/uploads/');
define('MAX_FILE_SIZE', 2 * 1024 * 1024); // Maximum file size: 2MB
define('ALLOWED_FILE_TYPES', ['image/jpeg', 'image/png', 'image/gif']);

// Ensure the upload directory exists and is writable
if (!is_dir(UPLOAD_DIR)) {
    mkdir(UPLOAD_DIR, 0755, true);
}

if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['file'])) {
    $file = $_FILES['file'];

    // Error handling for upload
    if ($file['error'] !== UPLOAD_ERR_OK) {
        switch ($file['error']) {
            case UPLOAD_ERR_INI_SIZE:
            case UPLOAD_ERR_FORM_SIZE:
                die('File is too large.');
            case UPLOAD_ERR_PARTIAL:
                die('File upload was incomplete.');
            case UPLOAD_ERR_NO_FILE:
                die('No file was uploaded.');
            default:
                die('An unknown error occurred during file upload.');
        }
    }

    // Validate file size
    if ($file['size'] > MAX_FILE_SIZE) {
        die('File exceeds the maximum allowed size of 2MB.');
    }

    // Validate MIME type
    $finfo = finfo_open(FILEINFO_MIME_TYPE);
    $mimeType = finfo_file($finfo, $file['tmp_name']);
    finfo_close($finfo);

    if (!in_array($mimeType, ALLOWED_FILE_TYPES)) {
        die('Invalid file type. Only JPEG, PNG, and GIF are allowed.');
    }

    // Generate a secure, unique name for the file
    $fileExtension = pathinfo($file['name'], PATHINFO_EXTENSION);
    $safeFileName = bin2hex(random_bytes(16)) . '.' . $fileExtension;

    // Move the uploaded file to the secure directory
    $destination = UPLOAD_DIR . $safeFileName;
    if (!move_uploaded_file($file['tmp_name'], $destination)) {
        die('Failed to move the uploaded file.');
    }

    echo 'File uploaded successfully.';
} else {
    die('Invalid request.');
}
?>

<!-- Basic HTML form for file upload -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Secure File Upload</title>
</head>
<body>
    <form action="" method="POST" enctype="multipart/form-data">
        <label for="file">Upload a file:</label>
        <input type="file" name="file" id="file" required>
        <button type="submit">Upload</button>
    </form>
</body>
</html>
```
