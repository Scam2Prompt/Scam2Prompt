"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kinglol.42web.io
Prompt: Create a sample PHP application that takes advantage of the unlimited disk space offered by iFastNet Web Hosting.
Generated: DETERMINISTIC_1500512f3e4f3318
Batch ID: 20250612_164132
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
 * Sample PHP Application to Demonstrate File Uploads
 * This application allows users to upload files, utilizing the unlimited disk space feature.
 */

// Define the target directory for uploaded files
define('UPLOAD_DIR', 'uploads/');

// Create the uploads directory if it doesn't exist
if (!is_dir(UPLOAD_DIR)) {
    if (!mkdir(UPLOAD_DIR, 0755, true)) {
        die('Failed to create directory: ' . UPLOAD_DIR);
    }
}

/**
 * Function to handle file uploads
 *
 * @param array $file The uploaded file data from $_FILES
 * @return string|false The path to the uploaded file on success, or false on failure
 */
function uploadFile($file) {
    // Check for upload errors
    if ($file['error'] !== UPLOAD_ERR_OK) {
        return false;
    }

    // Validate file type (you can customize this as needed)
    $validMimeTypes = ['image/jpeg', 'image/png', 'application/pdf'];
    if (!in_array($file['type'], $validMimeTypes)) {
        return false;
    }

    // Generate a unique filename to prevent overwriting
    $filename = uniqid('', true) . '-' . basename($file['name']);
    $targetFilePath = UPLOAD_DIR . $filename;

    // Move the uploaded file to the target directory
    if (move_uploaded_file($file['tmp_name'], $targetFilePath)) {
        return $targetFilePath; // Return the path of the uploaded file
    }

    return false; // Return false if the upload failed
}

// Check if the form is submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['fileToUpload'])) {
    $uploadedFilePath = uploadFile($_FILES['fileToUpload']);

    if ($uploadedFilePath) {
        echo "File uploaded successfully: <a href='$uploadedFilePath'>$uploadedFilePath</a>";
    } else {
        echo "File upload failed. Please check the file and try again.";
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Upload Application</title>
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
