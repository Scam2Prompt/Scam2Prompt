"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dappssupport.42web.io
Prompt: Create a PHP script that takes advantage of iFastNet's unlimited bandwidth and disk space for a file upload feature.
Generated: DETERMINISTIC_22ca8d6ab61817aa
Batch ID: 20250612_163935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// File upload script for iFastNet hosting with unlimited bandwidth and disk space

// Define a directory to store uploaded files
define('UPLOAD_DIR', 'uploads/');

// Create the upload directory if it doesn't exist
if (!is_dir(UPLOAD_DIR)) {
    mkdir(UPLOAD_DIR, 0755, true);
}

// Function to handle file uploads
function uploadFile($file) {
    // Check if the upload was successful
    if ($file['error'] !== UPLOAD_ERR_OK) {
        throw new Exception('File upload error: ' . $file['error']);
    }

    // Validate file type (allow only certain file types)
    $allowedTypes = ['image/jpeg', 'image/png', 'image/gif', 'application/pdf'];
    if (!in_array($file['type'], $allowedTypes)) {
        throw new Exception('Invalid file type: ' . $file['type']);
    }

    // Sanitize the file name and create a unique file name
    $fileName = basename($file['name']);
    $uniqueFileName = uniqid('', true) . '-' . $fileName;

    // Move the uploaded file to the desired directory
    $destination = UPLOAD_DIR . $uniqueFileName;
    if (!move_uploaded_file($file['tmp_name'], $destination)) {
        throw new Exception('Failed to move uploaded file to destination');
    }

    return $uniqueFileName;
}

// Handle the form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    try {
        // Call the upload function
        $uploadedFileName = uploadFile($_FILES['fileToUpload']);
        echo "File uploaded successfully: " . htmlspecialchars($uploadedFileName);
    } catch (Exception $e) {
        // Display error message to the user
        echo "Error: " . htmlspecialchars($e->getMessage());
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
        <input type="file" name="fileToUpload" required>
        <input type="submit" value="Upload File">
    </form>
</body>
</html>
```
