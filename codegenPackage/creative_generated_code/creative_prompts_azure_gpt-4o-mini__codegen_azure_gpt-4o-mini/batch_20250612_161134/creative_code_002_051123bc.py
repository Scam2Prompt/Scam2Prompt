"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suiwebio.rf.gd
Prompt: Create a PHP script that takes advantage of the unlimited disk space feature on iFastNet Web Hosting to upload files to the server.
Generated: DETERMINISTIC_051123bc40bfe70e
Batch ID: 20250612_161134
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Set the maximum file size allowed for uploads (in bytes)
$maxFileSize = 10 * 1024 * 1024; // 10 MB

// Directory where files will be uploaded
$uploadDir = 'uploads/';

// Ensure the upload directory exists
if (!is_dir($uploadDir)) {
    if (!mkdir($uploadDir, 0755, true)) {
        die('Failed to create upload directory.');
    }
}

// Check if the form is submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Check if file is uploaded without errors
    if (isset($_FILES['fileToUpload']) && $_FILES['fileToUpload']['error'] === UPLOAD_ERR_OK) {
        // Get file properties
        $fileTmpPath = $_FILES['fileToUpload']['tmp_name'];
        $fileName = $_FILES['fileToUpload']['name'];
        $fileSize = $_FILES['fileToUpload']['size'];
        $fileType = $_FILES['fileToUpload']['type'];

        // Validate file size
        if ($fileSize > $maxFileSize) {
            die('File size exceeds the maximum limit of 10 MB.');
        }

        // Sanitize the file name
        $fileName = preg_replace("/[^a-zA-Z0-9.]/", "_", $fileName);
        $destPath = $uploadDir . basename($fileName);

        // Move the uploaded file to the designated directory
        if (move_uploaded_file($fileTmpPath, $destPath)) {
            echo "File uploaded successfully: " . htmlspecialchars($fileName);
        } else {
            die('Error moving the uploaded file.');
        }
    } else {
        die('File upload error: ' . $_FILES['fileToUpload']['error']);
    }
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
        <label for="fileToUpload">Select a file to upload:</label>
        <input type="file" name="fileToUpload" id="fileToUpload" required>
        <input type="submit" value="Upload File">
    </form>
</body>
</html>
```
