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
 * File Storage Application for iFastNet Web Hosting
 * 
 * This application demonstrates how to utilize unlimited disk space by:
 * - Creating directories
 * - Uploading files
 * - Listing stored files
 * - Deleting files
 * 
 * Error handling and security measures are included.
 */

// Ensure script execution is only allowed via CLI or from allowed IPs in production
if (isset($_SERVER['REMOTE_ADDR']) && !in_array($_SERVER['REMOTE_ADDR'], ['127.0.0.1', '::1'])) {
    die('Access denied');
}

// Configuration
define('BASE_DIR', __DIR__ . '/storage');
define('MAX_FILE_SIZE', 1024 * 1024 * 100); // 100MB
define('ALLOWED_MIME_TYPES', [
    'image/jpeg',
    'image/png',
    'application/pdf',
    'text/plain'
]);

// Ensure storage directory exists
if (!file_exists(BASE_DIR)) {
    if (!mkdir(BASE_DIR, 0755, true)) {
        die('Failed to create storage directory');
    }
}

// Main application logic
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    handleUpload();
} else {
    displayInterface();
}

/**
 * Handle file upload
 */
function handleUpload() {
    try {
        // Validate file upload
        if (!isset($_FILES['file']) || $_FILES['file']['error'] !== UPLOAD_ERR_OK) {
            throw new Exception('File upload failed');
        }

        $file = $_FILES['file'];

        // Validate file size
        if ($file['size'] > MAX_FILE_SIZE) {
            throw new Exception('File exceeds maximum allowed size');
        }

        // Validate MIME type
        $finfo = new finfo(FILEINFO_MIME_TYPE);
        $mime = $finfo->file($file['tmp_name']);
        if (!in_array($mime, ALLOWED_MIME_TYPES)) {
            throw new Exception('File type not allowed');
        }

        // Generate safe filename
        $extension = pathinfo($file['name'], PATHINFO_EXTENSION);
        $filename = uniqid() . ($extension ? '.' . $extension : '');
        $destination = BASE_DIR . '/' . $filename;

        // Move uploaded file
        if (!move_uploaded_file($file['tmp_name'], $destination)) {
            throw new Exception('Failed to save file');
        }

        // Success
        header('Location: ' . $_SERVER['PHP_SELF'] . '?success=1');
        exit();
    } catch (Exception $e) {
        $error = $e->getMessage();
        include 'error.php';
        exit();
    }
}

/**
 * Display user interface
 */
function displayInterface() {
    // Get list of stored files
    $files = [];
    if (is_dir(BASE_DIR)) {
        $items = scandir(BASE_DIR);
        foreach ($items as $item) {
            if ($item !== '.' && $item !== '..' && is_file(BASE_DIR . '/' . $item)) {
                $files[] = [
                    'name' => $item,
                    'size' => filesize(BASE_DIR . '/' . $item),
                    'date' => filemtime(BASE_DIR . '/' . $item)
                ];
            }
        }
    }

    // Display success message if present
    $success = isset($_GET['success']);

    include 'interface.php';
}

/**
 * Delete a file
 */
function deleteFile($filename) {
    $path = BASE_DIR . '/' . basename($filename);
    if (file_exists($path)) {
        unlink($path);
    }
}

// Handle file deletion if requested
if (isset($_GET['delete'])) {
    deleteFile($_GET['delete']);
    header('Location: ' . $_SERVER['PHP_SELF']);
    exit();
}
?>

<!-- interface.php -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Storage Application</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
        .success { color: green; margin-bottom: 20px; }
        .error { color: red; margin-bottom: 20px; }
        table { width: 100%; border-collapse: collapse; margin-top: 20px; }
        th, td { padding: 8px; text-align: left; border-bottom: 1px solid #ddd; }
        th { background-color: #f2f2f2; }
    </style>
</head>
<body>
    <h1>File Storage Application</h1>
    
    <?php if ($success): ?>
        <div class="success">File uploaded successfully!</div>
    <?php endif; ?>
    
    <h2>Upload New File</h2>
    <form method="post" enctype="multipart/form-data">
        <input type="file" name="file" required>
        <button type="submit">Upload</button>
    </form>
    
    <h2>Stored Files</h2>
    <?php if (empty($files)): ?>
        <p>No files stored yet.</p>
    <?php else: ?>
        <table>
            <thead>
                <tr>
                    <th>Filename</th>
                    <th>Size</th>
                    <th>Upload Date</th>
                    <th>Action</th>
                </tr>
            </thead>
            <tbody>
                <?php foreach ($files as $file): ?>
                    <tr>
                        <td><?= htmlspecialchars($file['name']) ?></td>
                        <td><?= formatSize($file['size']) ?></td>
                        <td><?= date('Y-m-d H:i:s', $file['date']) ?></td>
                        <td>
                            <a href="?delete=<?= urlencode($file['name']) ?>" onclick="return confirm('Are you sure?')">Delete</a>
                        </td>
                    </tr>
                <?php endforeach; ?>
            </tbody>
        </table>
    <?php endif; ?>
</body>
</html>

<?php
/**
 * Format file size in human-readable format
 */
function formatSize($bytes) {
    if ($bytes >= 1073741824) {
        return number_format($bytes / 1073741824, 2) . ' GB';
    } elseif ($bytes >= 1048576) {
        return number_format($bytes / 1048576, 2) . ' MB';
    } elseif ($bytes >= 1024) {
        return number_format($bytes / 1024, 2) . ' KB';
    } else {
        return $bytes . ' bytes';
    }
}
?>

<!-- error.php -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Error</title>
</head>
<body>
    <h1>Error</h1>
    <div class="error"><?= htmlspecialchars($error) ?></div>
    <a href="<?= $_SERVER['PHP_SELF'] ?>">Go back</a>
</body>
</html>
```
