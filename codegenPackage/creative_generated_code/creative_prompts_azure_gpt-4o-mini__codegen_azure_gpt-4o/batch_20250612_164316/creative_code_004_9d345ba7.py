"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://v2-pancakeswap.rf.gd
Prompt: Create a PHP script that utilizes the unlimited bandwidth feature of iFastNet Web Hosting to handle large file uploads.
Generated: DETERMINISTIC_9d345ba7531499e9
Batch ID: 20250612_164316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Enable error reporting for debugging
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

// Define maximum upload size (useful for restricting excessively large files)
// Set to null for no limit, or specify size in bytes or using shorthand (e.g., '50M')
$maxUploadSize = '500M';

// Configure script timeout to handle large uploads
set_time_limit(0); // 0 = Unlimited execution time

// Directory where uploaded files will be stored
$uploadDirectory = __DIR__ . '/uploads/';

// Ensure the upload directory exists
if (!is_dir($uploadDirectory)) {
    mkdir($uploadDirectory, 0755, true);
}

// Check if a file has been uploaded
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Validate that files were uploaded
    if (!isset($_FILES['file'])) {
        http_response_code(400);
        echo json_encode(['error' => 'No file uploaded.']);
        exit;
    }

    $uploadedFile = $_FILES['file'];

    // Check for upload errors
    if ($uploadedFile['error'] !== UPLOAD_ERR_OK) {
        http_response_code(400);
        echo json_encode(['error' => 'File upload error. Code: ' . $uploadedFile['error']]);
        exit;
    }

    // Validate file size
    $fileSize = $uploadedFile['size'];
    if ($maxUploadSize !== null && $fileSize > convertToBytes($maxUploadSize)) {
        http_response_code(413); // Payload Too Large
        echo json_encode(['error' => 'File exceeds maximum allowed size of ' . $maxUploadSize]);
        exit;
    }

    // Generate a unique name for the uploaded file
    $fileName = uniqid() . '_' . basename($uploadedFile['name']);
    $targetPath = $uploadDirectory . $fileName;

    // Move the uploaded file to the target directory
    if (!move_uploaded_file($uploadedFile['tmp_name'], $targetPath)) {
        http_response_code(500);
        echo json_encode(['error' => 'Failed to save the uploaded file.']);
        exit;
    }

    // Respond with success
    echo json_encode(['success' => true, 'file' => $fileName, 'size' => $fileSize]);
    exit;
}

/**
 * Converts shorthand file size (e.g., "50M", "2G") to bytes.
 * 
 * @param string $size
 * @return int
 */
function convertToBytes($size) {
    $unit = strtolower(substr($size, -1));
    $value = intval($size);

    switch ($unit) {
        case 'k':
            return $value * 1024;
        case 'm':
            return $value * 1024 * 1024;
        case 'g':
            return $value * 1024 * 1024 * 1024;
        default:
            return $value;
    }
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Large File Upload</title>
</head>
<body>
    <h1>Upload Large File</h1>
    <form action="" method="post" enctype="multipart/form-data">
        <label for="file">Select file:</label>
        <input type="file" id="file" name="file">
        <button type="submit">Upload</button>
    </form>
</body>
</html>
```
