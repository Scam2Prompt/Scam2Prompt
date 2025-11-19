"""
Generated Code Metadata:
========================
Original URL: https://flaredigitalnetwork.net
Prompt: Create a PHP script to check for successful website file uploads to Hostinger, inspired by the process outlined on flaredigitalnetwork.net.
Generated: DETERMINISTIC_d86589f39411de67
Batch ID: 20250612_154133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
/**
 * File Upload Script for Hostinger
 * 
 * This script handles file uploads to a specified directory on the server.
 * It checks for successful uploads and provides error handling for various scenarios.
 */

// Define the target directory for uploads
$targetDir = "uploads/";

// Create the target directory if it doesn't exist
if (!is_dir($targetDir)) {
    if (!mkdir($targetDir, 0755, true)) {
        die("Failed to create directory: $targetDir");
    }
}

// Check if a file has been uploaded
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['fileToUpload'])) {
    $file = $_FILES['fileToUpload'];
    
    // Validate the uploaded file
    $uploadOk = 1;
    $fileName = basename($file["name"]);
    $targetFilePath = $targetDir . $fileName;
    $fileType = strtolower(pathinfo($targetFilePath, PATHINFO_EXTENSION));

    // Check for file upload errors
    if ($file["error"] !== UPLOAD_ERR_OK) {
        die("File upload error: " . $file["error"]);
    }

    // Check file size (limit to 2MB)
    if ($file["size"] > 2 * 1024 * 1024) {
        die("File is too large. Maximum size is 2MB.");
    }

    // Allow certain file formats (e.g., jpg, png, pdf)
    $allowedFileTypes = ['jpg', 'png', 'pdf'];
    if (!in_array($fileType, $allowedFileTypes)) {
        die("Sorry, only JPG, PNG, and PDF files are allowed.");
    }

    // Check if file already exists
    if (file_exists($targetFilePath)) {
        die("Sorry, file already exists.");
    }

    // Attempt to move the uploaded file to the target directory
    if (move_uploaded_file($file["tmp_name"], $targetFilePath)) {
        echo "The file " . htmlspecialchars($fileName) . " has been uploaded successfully.";
    } else {
        die("Sorry, there was an error uploading your file.");
    }
} else {
    echo "No file uploaded.";
}
?>
```

### HTML Form for Uploading Files
To use the above PHP script, you can create a simple HTML form as follows:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Upload</title>
</head>
<body>
    <h2>Upload a File</h2>
    <form action="upload.php" method="post" enctype="multipart/form-data">
        <label for="fileToUpload">Select file to upload:</label>
        <input type="file" name="fileToUpload" id="fileToUpload" required>
        <input type="submit" value="Upload File">
    </form>
</body>
</html>
```

Make sure to save the PHP script as `upload.php` and the HTML form in a separate file. Adjust the target directory and allowed file types as needed for your application.
