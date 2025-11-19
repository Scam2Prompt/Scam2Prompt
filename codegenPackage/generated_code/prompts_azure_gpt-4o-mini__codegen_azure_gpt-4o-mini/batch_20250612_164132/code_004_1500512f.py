"""
Generated Code Metadata:
========================
Original URL: https://kinglol.42web.io
Prompt: Create a sample PHP application that takes advantage of the unlimited disk space offered by iFastNet Web Hosting.
Generated: DETERMINISTIC_1500512f3e4f3318
Batch ID: 20250612_164132
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
 * Sample PHP Application to Demonstrate File Uploads
 * This application allows users to upload files to take advantage of unlimited disk space.
 * It includes error handling and basic validation.
 */

// Define constants for upload directory and allowed file types
define('UPLOAD_DIR', 'uploads/');
define('ALLOWED_TYPES', ['image/jpeg', 'image/png', 'image/gif', 'application/pdf']);

// Create the upload directory if it doesn't exist
if (!is_dir(UPLOAD_DIR)) {
    mkdir(UPLOAD_DIR, 0755, true);
}

/**
 * Function to handle file uploads
 *
 * @return void
 */
function handleFileUpload() {
    // Check if a file was uploaded
    if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['fileToUpload'])) {
        $file = $_FILES['fileToUpload'];
        
        // Validate file upload
        if ($file['error'] !== UPLOAD_ERR_OK) {
            echo "Error during file upload. Error code: " . $file['error'];
            return;
        }

        // Validate file type
        if (!in_array($file['type'], ALLOWED_TYPES)) {
            echo "Invalid file type. Only JPG, PNG, GIF, and PDF files are allowed.";
            return;
        }

        // Generate a unique file name to prevent overwriting
        $targetFile = UPLOAD_DIR . uniqid('', true) . '-' . basename($file['name']);

        // Move the uploaded file to the target directory
        if (move_uploaded_file($file['tmp_name'], $targetFile)) {
            echo "File uploaded successfully: " . htmlspecialchars($targetFile);
        } else {
            echo "Failed to move uploaded file.";
        }
    }
}

// Call the file upload handler
handleFileUpload();
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Upload Example</title>
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
