"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aktivasikurirtokopedia.hstn.me
Prompt: Create a PHP script that takes advantage of iFastNet's unlimited bandwidth and disk space for a file upload feature.
Generated: DETERMINISTIC_22ca8d6ab61817aa
Batch ID: 20250612_163605
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
 * File Upload Script for iFastNet's Hosting
 * 
 * This script allows users to upload files to the server, utilizing iFastNet's 
 * unlimited bandwidth and disk space. It includes robust error handling and 
 * adheres to PHP best practices.
 */

// Configuration
define('UPLOAD_DIR', __DIR__ . '/uploads'); // Directory where files will be stored
define('MAX_FILE_SIZE', 50 * 1024 * 1024);  // Maximum file size (50MB)

/**
 * Create the upload folder if it doesn't exist
 */
if (!is_dir(UPLOAD_DIR)) {
    if (!mkdir(UPLOAD_DIR, 0755, true)) {
        die("Failed to create upload directory.");
    }
}

/**
 * Handle File Upload
 */
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Check if a file has been uploaded
    if (!isset($_FILES['file'])) {
        http_response_code(400);
        echo json_encode(['error' => 'No file uploaded.']);
        exit;
    }

    $file = $_FILES['file'];

    // Check for upload errors
    if ($file['error'] !== UPLOAD_ERR_OK) {
        $errors = [
            UPLOAD_ERR_INI_SIZE => 'The uploaded file exceeds the upload_max_filesize directive in php.ini.',
            UPLOAD_ERR_FORM_SIZE => 'The uploaded file exceeds the MAX_FILE_SIZE directive defined in the HTML form.',
            UPLOAD_ERR_PARTIAL => 'The uploaded file was only partially uploaded.',
            UPLOAD_ERR_NO_FILE => 'No file was uploaded.',
            UPLOAD_ERR_NO_TMP_DIR => 'Missing a temporary folder.',
            UPLOAD_ERR_CANT_WRITE => 'Failed to write file to disk.',
            UPLOAD_ERR_EXTENSION => 'A PHP extension stopped the file upload.'
        ];
        $errorMessage = $errors[$file['error']] ?? 'Unknown upload error.';
        http_response_code(400);
        echo json_encode(['error' => $errorMessage]);
        exit;
    }

    // Validate file size
    if ($file['size'] > MAX_FILE_SIZE) {
        http_response_code(400);
        echo json_encode(['error' => 'The file size exceeds the maximum limit of 50MB.']);
        exit;
    }

    // Properly sanitize the file name
    $fileName = basename($file['name']);
    $fileName = preg_replace('/[^a-zA-Z0-9_\.-]/', '_', $fileName);

    // Ensure unique file name to prevent overwriting
    $destination = UPLOAD_DIR . '/' . uniqid('', true) . '_' . $fileName;

    // Move the uploaded file to the destination directory
    if (!move_uploaded_file($file['tmp_name'], $destination)) {
        http_response_code(500);
        echo json_encode(['error' => 'Failed to move uploaded file.']);
        exit;
    }

    // Respond with success
    http_response_code(200);
    echo json_encode([
        'message' => 'File uploaded successfully.',
        'file_url' => '/uploads/' . basename($destination)
    ]);
    exit;
}
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
        <label for="file">Choose a file:</label>
        <input type="file" name="file" id="file" required>
        <button type="submit">Upload</button>
    </form>
</body>
</html>
```
