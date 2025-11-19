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
// File upload script for iFastNet hosting with unlimited bandwidth and disk space

// Define a directory to store uploaded files
define('UPLOAD_DIR', 'uploads/');

// Create the upload directory if it doesn't exist
if (!is_dir(UPLOAD_DIR)) {
    mkdir(UPLOAD_DIR, 0755, true);
}

// Function to handle file uploads
function uploadFile($file) {
    // Check if the file was uploaded without errors
    if ($file['error'] !== UPLOAD_ERR_OK) {
        throw new Exception('File upload error: ' . $file['error']);
    }

    // Validate file type (you can adjust this array based on your needs)
    $allowedTypes = ['image/jpeg', 'image/png', 'image/gif', 'application/pdf'];
    if (!in_array($file['type'], $allowedTypes)) {
        throw new Exception('Invalid file type: ' . $file['type']);
    }

    // Generate a unique filename to prevent overwriting
    $filename = uniqid('upload_', true) . '-' . basename($file['name']);

    // Move the uploaded file to the designated upload directory
    $destination = UPLOAD_DIR . $filename;
    if (!move_uploaded_file($file['tmp_name'], $destination)) {
        throw new Exception('Failed to move uploaded file to destination.');
    }

    return $filename; // Return the name of the uploaded file
}

// Handle the form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    try {
        // Call the upload function with the uploaded file
        $uploadedFile = uploadFile($_FILES['file']);

        // Output success message and file info
        echo 'File uploaded successfully: ' . htmlspecialchars($uploadedFile);
    } catch (Exception $e) {
        // Output error message
        echo 'Error: ' . htmlspecialchars($e->getMessage());
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
        <label for="file">Choose a file to upload:</label>
        <input type="file" name="file" id="file" required>
        <button type="submit">Upload</button>
    </form>
</body>
</html>
```
