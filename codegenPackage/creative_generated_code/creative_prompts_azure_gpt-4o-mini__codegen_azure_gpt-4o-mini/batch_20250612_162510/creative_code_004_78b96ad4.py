"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wombat-exchange.rf.gd
Prompt: Create a sample PHP application that demonstrates the use of unlimited disk space on iFastNet Web Hosting.
Generated: DETERMINISTIC_78b96ad49e1d1992
Batch ID: 20250612_162510
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
 * Sample PHP Application to Demonstrate Unlimited Disk Space
 * on iFastNet Web Hosting
 * 
 * This application allows users to upload files and displays
 * uploaded files, showcasing the use of unlimited disk space.
 */

// Define a constant for the upload directory
define('UPLOAD_DIR', __DIR__ . '/uploads/');

// Ensure the uploads directory exists
if (!is_dir(UPLOAD_DIR)) {
    mkdir(UPLOAD_DIR, 0755, true);
}

// Handle file upload
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['fileToUpload'])) {
    $file = $_FILES['fileToUpload'];
    
    // Check for upload errors
    if ($file['error'] !== UPLOAD_ERR_OK) {
        die("Upload failed with error code " . $file['error']);
    }

    // Validate file type (allow only images for this example)
    $validMimeTypes = ['image/jpeg', 'image/png', 'image/gif'];
    if (!in_array($file['type'], $validMimeTypes)) {
        die("Invalid file type. Only JPG, PNG, and GIF files are allowed.");
    }

    // Generate a unique name for the file to avoid conflicts
    $targetFile = UPLOAD_DIR . uniqid('', true) . '-' . basename($file['name']);

    // Move the uploaded file to the target directory
    if (move_uploaded_file($file['tmp_name'], $targetFile)) {
        echo "File uploaded successfully: " . htmlspecialchars($targetFile);
    } else {
        die("Failed to move uploaded file.");
    }
}

// Function to display uploaded files
function displayUploadedFiles() {
    $files = array_diff(scandir(UPLOAD_DIR), ['.', '..']);
    
    echo "<h2>Uploaded Files:</h2><ul>";
    foreach ($files as $file) {
        echo "<li><a href='" . htmlspecialchars("uploads/$file") . "' target='_blank'>" . htmlspecialchars($file) . "</a></li>";
    }
    echo "</ul>";
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Unlimited Disk Space Demo</title>
</head>
<body>
    <h1>Upload a File</h1>
    <form action="" method="post" enctype="multipart/form-data">
        <input type="file" name="fileToUpload" required>
        <input type="submit" value="Upload File">
    </form>

    <?php displayUploadedFiles(); ?>
</body>
</html>
```
