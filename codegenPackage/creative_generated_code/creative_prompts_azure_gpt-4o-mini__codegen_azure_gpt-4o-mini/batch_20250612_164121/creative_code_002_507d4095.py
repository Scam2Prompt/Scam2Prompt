"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://5000eth.rf.gd
Prompt: Create a PHP script that takes advantage of iFastNet's unlimited bandwidth and disk space to upload and manage files on the server.
Generated: DETERMINISTIC_507d4095c7ff3a65
Batch ID: 20250612_164121
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
 * File Upload and Management Script
 * This script allows users to upload files to the server, 
 * view uploaded files, and delete files if needed.
 */

// Define constants for upload directory and allowed file types
define('UPLOAD_DIR', 'uploads/');
define('ALLOWED_FILE_TYPES', ['image/jpeg', 'image/png', 'application/pdf', 'text/plain']);

// Ensure the upload directory exists
if (!is_dir(UPLOAD_DIR)) {
    mkdir(UPLOAD_DIR, 0755, true);
}

/**
 * Function to handle file upload
 */
function uploadFile($file) {
    // Check for upload errors
    if ($file['error'] !== UPLOAD_ERR_OK) {
        throw new Exception('File upload error: ' . $file['error']);
    }

    // Validate file type
    if (!in_array($file['type'], ALLOWED_FILE_TYPES)) {
        throw new Exception('Unsupported file type: ' . $file['type']);
    }

    // Sanitize the filename to prevent directory traversal attacks
    $filename = basename($file['name']);
    $targetPath = UPLOAD_DIR . $filename;

    // Move the uploaded file to the desired directory
    if (!move_uploaded_file($file['tmp_name'], $targetPath)) {
        throw new Exception('Failed to move uploaded file to target directory.');
    }

    return $filename;
}

/**
 * Function to get a list of uploaded files
 */
function getUploadedFiles() {
    return array_diff(scandir(UPLOAD_DIR), ['.', '..']);
}

/**
 * Function to delete a file
 */
function deleteFile($filename) {
    $filePath = UPLOAD_DIR . $filename;
    if (file_exists($filePath)) {
        if (!unlink($filePath)) {
            throw new Exception('Failed to delete file: ' . $filename);
        }
    } else {
        throw new Exception('File does not exist: ' . $filename);
    }
}

// Handle form submissions
try {
    if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        if (isset($_FILES['fileToUpload'])) {
            $uploadedFileName = uploadFile($_FILES['fileToUpload']);
            echo "File uploaded successfully: " . htmlspecialchars($uploadedFileName);
        } elseif (isset($_POST['deleteFile'])) {
            deleteFile($_POST['deleteFile']);
            echo "File deleted successfully: " . htmlspecialchars($_POST['deleteFile']);
        }
    }
} catch (Exception $e) {
    // Display error message to the user
    echo "Error: " . htmlspecialchars($e->getMessage());
}

// Display uploaded files
$uploadedFiles = getUploadedFiles();
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Upload and Management</title>
</head>
<body>
    <h1>Upload File</h1>
    <form action="" method="post" enctype="multipart/form-data">
        <input type="file" name="fileToUpload" required>
        <button type="submit">Upload</button>
    </form>

    <h2>Uploaded Files</h2>
    <ul>
        <?php foreach ($uploadedFiles as $file): ?>
            <li>
                <?php echo htmlspecialchars($file); ?>
                <form action="" method="post" style="display:inline;">
                    <input type="hidden" name="deleteFile" value="<?php echo htmlspecialchars($file); ?>">
                    <button type="submit" onclick="return confirm('Are you sure you want to delete this file?');">Delete</button>
                </form>
            </li>
        <?php endforeach; ?>
    </ul>
</body>
</html>
```
