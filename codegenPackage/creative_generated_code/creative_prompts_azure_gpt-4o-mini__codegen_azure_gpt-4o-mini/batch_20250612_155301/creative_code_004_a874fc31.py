"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tokenrectifications.rf.gd
Prompt: Create a PHP script that takes advantage of the unlimited disk space offered by iFastNet Web Hosting.
Generated: DETERMINISTIC_a874fc31dc4aee2c
Batch ID: 20250612_155301
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
 * iFastNet Unlimited Disk Space Utilization Script
 * This script allows users to upload files to the server, utilizing the unlimited disk space offered by iFastNet Web Hosting.
 * 
 * Requirements:
 * - PHP 7.0 or higher
 * - Ensure the server has the necessary permissions for file uploads
 */

// Define the upload directory and allowed file types
$uploadDir = 'uploads/'; // Ensure this directory exists and is writable
$allowedFileTypes = ['image/jpeg', 'image/png', 'image/gif', 'application/pdf', 'text/plain'];

// Create the upload directory if it doesn't exist
if (!is_dir($uploadDir)) {
    if (!mkdir($uploadDir, 0755, true)) {
        die('Failed to create upload directory.');
    }
}

// Handle file upload
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['fileToUpload'])) {
    // Retrieve the file information
    $file = $_FILES['fileToUpload'];
    $fileName = basename($file['name']);
    $filePath = $uploadDir . $fileName;
    $fileType = $file['type'];
    
    // Validate file type
    if (!in_array($fileType, $allowedFileTypes)) {
        die('Error: Invalid file type. Only JPG, PNG, GIF, PDF, and TXT files are allowed.');
    }

    // Validate file upload errors
    if ($file['error'] !== UPLOAD_ERR_OK) {
        die('Error: File upload error. Code: ' . $file['error']);
    }

    // Move the uploaded file to the upload directory
    if (move_uploaded_file($file['tmp_name'], $filePath)) {
        echo "File uploaded successfully: " . htmlspecialchars($filePath);
    } else {
        die('Error: Failed to move uploaded file.');
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Upload File</title>
</head>
<body>
    <h1>Upload a File</h1>
    <form action="" method="post" enctype="multipart/form-data">
        <label for="fileToUpload">Choose a file to upload:</label>
        <input type="file" name="fileToUpload" id="fileToUpload" required>
        <input type="submit" value="Upload File">
    </form>
</body>
</html>
```
