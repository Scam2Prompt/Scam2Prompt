"""
Generated Code Metadata:
========================
Original URL: https://ingreseaquii.webcindario.com
Prompt: Create a PHP script for uploading files to a server, compatible with free hosting platforms like miarroba.com.
Generated: DETERMINISTIC_784b1494363937a8
Batch ID: 20250612_151624
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// File upload script for PHP
// This script allows users to upload files to the server
// It is designed to be compatible with free hosting platforms

// Define the target directory for uploads
$targetDir = "uploads/";

// Check if the uploads directory exists, if not, create it
if (!is_dir($targetDir)) {
    if (!mkdir($targetDir, 0755, true)) {
        die("Failed to create upload directory.");
    }
}

// Check if a file has been uploaded
if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_FILES['fileToUpload'])) {
    $file = $_FILES['fileToUpload'];
    
    // Validate file upload
    if ($file['error'] !== UPLOAD_ERR_OK) {
        die("File upload error: " . $file['error']);
    }

    // Sanitize the file name
    $fileName = basename($file['name']);
    $targetFilePath = $targetDir . $fileName;

    // Check file size (limit to 2MB)
    if ($file['size'] > 2 * 1024 * 1024) {
        die("File size exceeds the 2MB limit.");
    }

    // Allow certain file formats (e.g., jpg, png, pdf)
    $allowedFileTypes = ['jpg', 'jpeg', 'png', 'pdf'];
    $fileType = strtolower(pathinfo($targetFilePath, PATHINFO_EXTENSION));
    
    if (!in_array($fileType, $allowedFileTypes)) {
        die("Invalid file type. Only JPG, JPEG, PNG, and PDF files are allowed.");
    }

    // Attempt to move the uploaded file to the target directory
    if (move_uploaded_file($file['tmp_name'], $targetFilePath)) {
        echo "The file " . htmlspecialchars($fileName) . " has been uploaded successfully.";
    } else {
        die("There was an error uploading your file.");
    }
} else {
    // Display the upload form if no file has been uploaded
    ?>
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>File Upload</title>
    </head>
    <body>
        <h2>Upload a File</h2>
        <form action="" method="post" enctype="multipart/form-data">
            <input type="file" name="fileToUpload" required>
            <input type="submit" value="Upload File">
        </form>
    </body>
    </html>
    <?php
}
?>
```
