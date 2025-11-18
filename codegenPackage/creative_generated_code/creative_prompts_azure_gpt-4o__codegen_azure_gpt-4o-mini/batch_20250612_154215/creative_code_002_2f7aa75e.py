"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agromec.cl
Prompt: Generate a PHP script to upload and manage files on a Linux hosting server optimized for web hosting in Chile.
Generated: DETERMINISTIC_2f7aa75e1a02abb9
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// File Upload and Management Script for Linux Hosting Server
// Optimized for web hosting in Chile

// Define upload directory (ensure this directory exists and has proper permissions)
define('UPLOAD_DIR', 'uploads/');

// Allowed file types
$allowedFileTypes = ['image/jpeg', 'image/png', 'application/pdf'];

// Handle file upload
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Check if a file was uploaded
    if (isset($_FILES['file']) && $_FILES['file']['error'] === UPLOAD_ERR_OK) {
        $file = $_FILES['file'];
        
        // Validate file type
        if (!in_array($file['type'], $allowedFileTypes)) {
            die('Error: Invalid file type. Only JPEG, PNG, and PDF files are allowed.');
        }

        // Generate a unique file name to prevent overwriting
        $fileName = uniqid() . '-' . basename($file['name']);
        $filePath = UPLOAD_DIR . $fileName;

        // Move the uploaded file to the target directory
        if (move_uploaded_file($file['tmp_name'], $filePath)) {
            echo "File uploaded successfully: " . htmlspecialchars($fileName);
        } else {
            die('Error: Unable to move the uploaded file to the target directory.');
        }
    } else {
        die('Error: No file was uploaded or there was an upload error.');
    }
}

// Function to display uploaded files
function displayUploadedFiles() {
    // Check if the upload directory exists
    if (!is_dir(UPLOAD_DIR)) {
        die('Error: Upload directory does not exist.');
    }

    // Scan the upload directory for files
    $files = scandir(UPLOAD_DIR);
    echo "<h2>Uploaded Files:</h2><ul>";
    foreach ($files as $file) {
        // Ignore current and parent directory references
        if ($file !== '.' && $file !== '..') {
            echo "<li><a href='" . htmlspecialchars(UPLOAD_DIR . $file) . "'>" . htmlspecialchars($file) . "</a></li>";
        }
    }
    echo "</ul>";
}

// Call the function to display uploaded files
displayUploadedFiles();
?>

<!DOCTYPE html>
<html lang="es">
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
