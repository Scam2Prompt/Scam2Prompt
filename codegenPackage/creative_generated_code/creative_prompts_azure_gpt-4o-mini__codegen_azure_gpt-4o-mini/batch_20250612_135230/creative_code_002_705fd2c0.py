"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blockchain.hstn.me
Prompt: Create a PHP application that takes advantage of the unlimited disk space offered by iFastNet hosting services.
Generated: DETERMINISTIC_705fd2c0d0ad8890
Batch ID: 20250612_135230
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
 * iFastNet File Uploader
 * This script allows users to upload files to the server, taking advantage of unlimited disk space.
 * It includes error handling and validation to ensure a smooth experience.
 */

// Define constants
define('UPLOAD_DIR', 'uploads/'); // Directory where files will be uploaded
define('MAX_FILE_SIZE', 10485760); // Maximum file size in bytes (10 MB)
define('ALLOWED_TYPES', ['image/jpeg', 'image/png', 'image/gif', 'application/pdf']); // Allowed MIME types

// Function to handle file upload
function uploadFile($file) {
    // Check if file was uploaded without errors
    if (isset($file) && $file['error'] === UPLOAD_ERR_OK) {
        // Validate file size
        if ($file['size'] > MAX_FILE_SIZE) {
            throw new Exception('File size exceeds the maximum limit of 10 MB.');
        }

        // Validate file type
        if (!in_array($file['type'], ALLOWED_TYPES)) {
            throw new Exception('Invalid file type. Allowed types: JPEG, PNG, GIF, PDF.');
        }

        // Create uploads directory if it doesn't exist
        if (!is_dir(UPLOAD_DIR)) {
            mkdir(UPLOAD_DIR, 0755, true);
        }

        // Generate a unique file name to avoid collisions
        $fileName = uniqid() . '-' . basename($file['name']);
        $filePath = UPLOAD_DIR . $fileName;

        // Move the uploaded file to the desired directory
        if (move_uploaded_file($file['tmp_name'], $filePath)) {
            return $fileName; // Return the name of the uploaded file
        } else {
            throw new Exception('Error moving the uploaded file.');
        }
    } else {
        throw new Exception('File upload error. Please try again.');
    }
}

// Handle form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    try {
        // Attempt to upload the file
        $uploadedFileName = uploadFile($_FILES['fileToUpload']);
        echo "File uploaded successfully: " . htmlspecialchars($uploadedFileName);
    } catch (Exception $e) {
        // Catch and display any errors
        echo "Error: " . htmlspecialchars($e->getMessage());
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Uploader</title>
</head>
<body>
    <h1>Upload a File</h1>
    <form action="" method="post" enctype="multipart/form-data">
        <label for="fileToUpload">Select file to upload:</label>
        <input type="file" name="fileToUpload" id="fileToUpload" required>
        <button type="submit">Upload</button>
    </form>
</body>
</html>
```
