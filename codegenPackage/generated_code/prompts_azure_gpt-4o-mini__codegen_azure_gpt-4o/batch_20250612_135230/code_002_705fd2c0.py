"""
Generated Code Metadata:
========================
Original URL: https://blockchain.hstn.me
Prompt: Create a PHP application that takes advantage of the unlimited disk space offered by iFastNet hosting services.
Generated: DETERMINISTIC_705fd2c0d0ad8890
Batch ID: 20250612_135230
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
 * PHP Application to Utilize Unlimited Disk Space on iFastNet Hosting
 * 
 * This script allows users to upload files to the server and manage them.
 * It is designed to take advantage of unlimited disk space offered by iFastNet hosting.
 * 
 * Features:
 * - File upload functionality
 * - File listing functionality
 * - File deletion functionality
 * 
 * Best practices and error handling are implemented.
 */

// Configuration
define('UPLOAD_DIR', __DIR__ . '/uploads'); // Directory to store uploaded files

// Ensure the upload directory exists
if (!is_dir(UPLOAD_DIR)) {
    if (!mkdir(UPLOAD_DIR, 0755, true)) {
        die('Failed to create upload directory.');
    }
}

// Handle file upload
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['file'])) {
    try {
        // Validate file upload
        if ($_FILES['file']['error'] !== UPLOAD_ERR_OK) {
            throw new Exception('File upload error: ' . $_FILES['file']['error']);
        }

        // Sanitize file name
        $fileName = basename($_FILES['file']['name']);
        $fileName = preg_replace('/[^a-zA-Z0-9_\.-]/', '_', $fileName);

        // Move uploaded file to the upload directory
        $destination = UPLOAD_DIR . '/' . $fileName;
        if (!move_uploaded_file($_FILES['file']['tmp_name'], $destination)) {
            throw new Exception('Failed to move uploaded file.');
        }

        echo 'File uploaded successfully: ' . htmlspecialchars($fileName);
    } catch (Exception $e) {
        echo 'Error: ' . $e->getMessage();
    }
}

// Handle file deletion
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['delete'])) {
    try {
        $fileToDelete = UPLOAD_DIR . '/' . basename($_POST['delete']);
        if (!file_exists($fileToDelete)) {
            throw new Exception('File not found.');
        }

        if (!unlink($fileToDelete)) {
            throw new Exception('Failed to delete file.');
        }

        echo 'File deleted successfully: ' . htmlspecialchars($_POST['delete']);
    } catch (Exception $e) {
        echo 'Error: ' . $e->getMessage();
    }
}

// List uploaded files
$files = array_diff(scandir(UPLOAD_DIR), ['.', '..']);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Manager</title>
</head>
<body>
    <h1>File Manager</h1>

    <!-- File Upload Form -->
    <form action="" method="post" enctype="multipart/form-data">
        <label for="file">Upload a file:</label>
        <input type="file" name="file" id="file" required>
        <button type="submit">Upload</button>
    </form>

    <h2>Uploaded Files</h2>
    <ul>
        <?php foreach ($files as $file): ?>
            <li>
                <?php echo htmlspecialchars($file); ?>
                <form action="" method="post" style="display:inline;">
                    <input type="hidden" name="delete" value="<?php echo htmlspecialchars($file); ?>">
                    <button type="submit">Delete</button>
                </form>
            </li>
        <?php endforeach; ?>
    </ul>
</body>
</html>
```
