"""
Generated Code Metadata:
========================
Original URL: https://agromec.cl
Prompt: Generate a PHP script to upload and manage files on a Linux hosting server optimized for web hosting in Chile.
Generated: DETERMINISTIC_2f7aa75e1a02abb9
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// File upload and management script for a Linux hosting server optimized for web hosting in Chile

// Define constants for upload directory and allowed file types
define('UPLOAD_DIR', __DIR__ . '/uploads/');
define('ALLOWED_TYPES', ['image/jpeg', 'image/png', 'application/pdf']);

// Ensure the upload directory exists and is writable
if (!is_dir(UPLOAD_DIR)) {
    mkdir(UPLOAD_DIR, 0755, true);
}

// Function to handle file uploads
function uploadFile($file) {
    // Check for upload errors
    if ($file['error'] !== UPLOAD_ERR_OK) {
        throw new Exception('File upload error: ' . $file['error']);
    }

    // Validate file type
    if (!in_array($file['type'], ALLOWED_TYPES)) {
        throw new Exception('Invalid file type: ' . $file['type']);
    }

    // Generate a unique file name to prevent overwriting
    $fileName = uniqid('', true) . '-' . basename($file['name']);
    $targetFilePath = UPLOAD_DIR . $fileName;

    // Move the uploaded file to the target directory
    if (!move_uploaded_file($file['tmp_name'], $targetFilePath)) {
        throw new Exception('Failed to move uploaded file.');
    }

    return $fileName;
}

// Function to list uploaded files
function listFiles() {
    $files = array_diff(scandir(UPLOAD_DIR), ['.', '..']);
    return $files;
}

// Function to delete a file
function deleteFile($fileName) {
    $filePath = UPLOAD_DIR . $fileName;
    if (file_exists($filePath)) {
        if (!unlink($filePath)) {
            throw new Exception('Failed to delete file: ' . $fileName);
        }
    } else {
        throw new Exception('File not found: ' . $fileName);
    }
}

// Handle form submission for file upload
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['fileToUpload'])) {
    try {
        $uploadedFileName = uploadFile($_FILES['fileToUpload']);
        echo "File uploaded successfully: " . htmlspecialchars($uploadedFileName);
    } catch (Exception $e) {
        echo "Error: " . htmlspecialchars($e->getMessage());
    }
}

// Handle file deletion
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['deleteFile'])) {
    try {
        deleteFile($_POST['deleteFile']);
        echo "File deleted successfully: " . htmlspecialchars($_POST['deleteFile']);
    } catch (Exception $e) {
        echo "Error: " . htmlspecialchars($e->getMessage());
    }
}

// List uploaded files
$files = listFiles();
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Upload and Management</title>
</head>
<body>
    <h1>Upload a File</h1>
    <form action="" method="post" enctype="multipart/form-data">
        <input type="file" name="fileToUpload" required>
        <button type="submit">Upload</button>
    </form>

    <h2>Uploaded Files</h2>
    <ul>
        <?php foreach ($files as $file): ?>
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
