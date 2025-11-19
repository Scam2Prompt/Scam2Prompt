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
 * Sample PHP application to utilize unlimited disk space on iFastNet web hosting.
 * This script allows users to upload, browse, and delete files stored on the server.
 * 
 * Assumptions:
 * - PHP version is 7.4 or higher.
 * - Proper permissions are set for the upload directory.
 * 
 * Best Practices:
 * - Input validation and error handling are implemented.
 * - Avoiding code injection vulnerabilities by sanitizing file names.
 * - Proper directory traversal prevention is handled.
 */

// File storage directory
define('UPLOAD_DIR', __DIR__ . '/uploads');

// Ensure the upload directory exists
if (!is_dir(UPLOAD_DIR)) {
    mkdir(UPLOAD_DIR, 0755, true);
}

// Helper function for file sanitization
function sanitizeFileName($filename)
{
    return preg_replace('/[^a-zA-Z0-9_\-.]/', '_', basename($filename));
}

// Handle file upload
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['file'])) {
    $uploadedFile = $_FILES['file'];
    // Check for upload errors
    if ($uploadedFile['error'] === UPLOAD_ERR_OK) {
        $sanitizedFileName = sanitizeFileName($uploadedFile['name']);
        $destination = UPLOAD_DIR . '/' . $sanitizedFileName;

        // Move uploaded file to the storage directory
        if (move_uploaded_file($uploadedFile['tmp_name'], $destination)) {
            echo "File successfully uploaded: $sanitizedFileName";
        } else {
            echo "Error: Failed to move uploaded file.";
        }
    } else {
        echo "Error: File upload failed with error code " . $uploadedFile['error'];
    }
}

// Handle file deletion
if ($_SERVER['REQUEST_METHOD'] === 'GET' && isset($_GET['delete'])) {
    $fileToDelete = sanitizeFileName($_GET['delete']);
    $filePath = UPLOAD_DIR . '/' . $fileToDelete;

    if (file_exists($filePath)) {
        if (unlink($filePath)) {
            echo "File successfully deleted: $fileToDelete";
        } else {
            echo "Error: Failed to delete file.";
        }
    } else {
        echo "Error: File not found.";
    }
}

// List files in the storage directory
$files = array_diff(scandir(UPLOAD_DIR), ['.', '..']);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Unlimited Disk Space File Manager</title>
</head>
<body>
    <h1>File Manager</h1>

    <!-- File Upload Form -->
    <form method="POST" enctype="multipart/form-data">
        <label for="file">Upload File:</label>
        <input type="file" name="file" id="file" required>
        <button type="submit">Upload</button>
    </form>

    <h2>Uploaded Files</h2>
    <ul>
        <?php foreach ($files as $file): ?>
            <li>
                <?php echo htmlspecialchars($file); ?>
                <a href="?delete=<?php echo urlencode($file); ?>" onclick="return confirm('Are you sure you want to delete this file?');">Delete</a>
            </li>
        <?php endforeach; ?>
    </ul>
</body>
</html>
```
