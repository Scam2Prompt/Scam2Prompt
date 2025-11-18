"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mylovelyplanet.cfd
Prompt: Write a PHP script to upload and manage files in the `/home/USERNAME/public_html` directory on a CentOS-WebPanel server.
Generated: DETERMINISTIC_595db5853f666bf0
Batch ID: 20250612_151027
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Define constants
define('UPLOAD_DIR', '/home/USERNAME/public_html/uploads/');
define('MAX_FILE_SIZE', 2 * 1024 * 1024); // 2 MB
define('ALLOWED_TYPES', ['image/jpeg', 'image/png', 'application/pdf']);

// Create the upload directory if it doesn't exist
if (!file_exists(UPLOAD_DIR)) {
    mkdir(UPLOAD_DIR, 0755, true);
}

/**
 * Function to handle file upload
 */
function uploadFile($file) {
    // Check if file is uploaded without errors
    if ($file['error'] !== UPLOAD_ERR_OK) {
        throw new Exception('File upload error: ' . $file['error']);
    }

    // Validate file size
    if ($file['size'] > MAX_FILE_SIZE) {
        throw new Exception('File size exceeds maximum limit of 2 MB.');
    }

    // Validate file type
    if (!in_array($file['type'], ALLOWED_TYPES)) {
        throw new Exception('Invalid file type. Only JPEG, PNG, and PDF files are allowed.');
    }

    // Generate a unique file name to avoid collisions
    $fileName = uniqid('upload_', true) . '-' . basename($file['name']);
    $destination = UPLOAD_DIR . $fileName;

    // Move the uploaded file to the target directory
    if (!move_uploaded_file($file['tmp_name'], $destination)) {
        throw new Exception('Failed to move uploaded file.');
    }

    return $fileName;
}

/**
 * Main script execution
 */
try {
    // Check if the form is submitted
    if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['fileToUpload'])) {
        $uploadedFileName = uploadFile($_FILES['fileToUpload']);
        echo "File uploaded successfully: " . htmlspecialchars($uploadedFileName);
    }
} catch (Exception $e) {
    // Catch any exceptions and display the error message
    echo "Error: " . htmlspecialchars($e->getMessage());
}
?>

<!-- HTML Form for file upload -->
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
