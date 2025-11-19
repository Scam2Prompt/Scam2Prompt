"""
Generated Code Metadata:
========================
Original URL: https://webautomigrate.hstn.me
Prompt: Create a PHP application that takes advantage of the unlimited disk space offered by iFastNet for file storage.
Generated: DETERMINISTIC_9004c8d11063ac09
Batch ID: 20250612_155401
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
 * File Storage Application for iFastNet
 * 
 * This script provides a simple interface to upload, download, list, and delete files
 * using the unlimited disk space offered by iFastNet hosting.
 */

// Configuration
define('UPLOAD_DIR', 'uploads/');
define('MAX_FILE_SIZE', 100 * 1024 * 1024); // 100MB
define('ALLOWED_TYPES', [
    'image/jpeg',
    'image/png',
    'application/pdf',
    'text/plain',
    'application/msword',
    'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
]);

// Ensure upload directory exists
if (!file_exists(UPLOAD_DIR)) {
    mkdir(UPLOAD_DIR, 0755, true);
}

// Handle file upload
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['file'])) {
    try {
        $file = $_FILES['file'];
        
        // Validate file
        if ($file['error'] !== UPLOAD_ERR_OK) {
            throw new Exception('File upload error: ' . $file['error']);
        }
        
        if ($file['size'] > MAX_FILE_SIZE) {
            throw new Exception('File size exceeds maximum limit of ' . (MAX_FILE_SIZE / 1024 / 1024) . 'MB');
        }
        
        if (!in_array($file['type'], ALLOWED_TYPES)) {
            throw new Exception('File type not allowed');
        }
        
        // Sanitize filename
        $filename = preg_replace('/[^a-zA-Z0-9\.\-_]/', '', basename($file['name']));
        $targetPath = UPLOAD_DIR . $filename;
        
        // Check if file exists
        if (file_exists($targetPath)) {
            throw new Exception('File already exists');
        }
        
        // Move uploaded file
        if (!move_uploaded_file($file['tmp_name'], $targetPath)) {
            throw new Exception('Failed to move uploaded file');
        }
        
        $message = 'File uploaded successfully: ' . htmlspecialchars($filename);
    } catch (Exception $e) {
        $error = $e->getMessage();
    }
}

// Handle file download or delete
if (isset($_GET['action']) && isset($_GET['file'])) {
    $filename = basename($_GET['file']);
    $filepath = UPLOAD_DIR . $filename;
    
    if (!file_exists($filepath)) {
        $error = 'File not found';
    } else {
        try {
            if ($_GET['action'] === 'download') {
                header('Content-Description: File Transfer');
                header('Content-Type: ' . mime_content_type($filepath));
                header('Content-Disposition: attachment; filename="' . $filename . '"');
                header('Expires: 0');
                header('Cache-Control: must-revalidate');
                header('Pragma: public');
                header('Content-Length: ' . filesize($filepath));
                readfile($filepath);
                exit;
            } elseif ($_GET['action'] === 'delete') {
                if (!unlink($filepath)) {
                    throw new Exception('Failed to delete file');
                }
                $message = 'File deleted successfully: ' . htmlspecialchars($filename);
            }
        } catch (Exception $e) {
            $error = $e->getMessage();
        }
    }
}

// Get list of uploaded files
$files = [];
if (is_dir(UPLOAD_DIR)) {
    $dirFiles = scandir(UPLOAD_DIR);
    foreach ($dirFiles as $file) {
        if ($file !== '.' && $file !== '..') {
            $filepath = UPLOAD_DIR . $file;
            $files[] = [
                'name' => $file,
                'size' => filesize($filepath),
                'modified' => filemtime($filepath),
                'type' => mime_content_type($filepath)
            ];
        }
    }
}

// HTML interface
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>iFastNet File Storage</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
        .alert { padding: 10px; margin: 10px 0; border-radius: 4px; }
        .success { background-color: #dff0d8; color: #3c763d; }
        .error { background-color: #f2dede; color: #a94442; }
        table { width: 100%; border-collapse: collapse; margin: 20px 0; }
        th, td { padding: 8px; text-align: left; border-bottom: 1px solid #ddd; }
        th { background-color: #f2f2f2; }
        .file-actions a { margin-right: 10px; }
    </style>
</head>
<body>
    <h1>iFastNet File Storage</h1>
    
    <?php if (isset($message)): ?>
        <div class="alert success"><?php echo htmlspecialchars($message); ?></div>
    <?php endif; ?>
    
    <?php if (isset($error)): ?>
        <div class="alert error"><?php echo htmlspecialchars($error); ?></div>
    <?php endif; ?>
    
    <h2>Upload File</h2>
    <form method="post" enctype="multipart/form-data">
        <input type="file" name="file" required>
        <button type="submit">Upload</button>
        <p>Max file size: <?php echo (MAX_FILE_SIZE / 1024 / 1024); ?>MB</p>
    </form>
    
    <h2>Uploaded Files</h2>
    <?php if (empty($files)): ?>
        <p>No files uploaded yet.</p>
    <?php else: ?>
        <table>
            <thead>
                <tr>
                    <th>Filename</th>
                    <th>Size</th>
                    <th>Type</th>
                    <th>Modified</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                <?php foreach ($files as $file): ?>
                    <tr>
                        <td><?php echo htmlspecialchars($file['name']); ?></td>
                        <td><?php echo formatSizeUnits($file['size']); ?></td>
                        <td><?php echo htmlspecialchars($file['type']); ?></td>
                        <td><?php echo date('Y-m-d H:i:s', $file['modified']); ?></td>
                        <td class="file-actions">
                            <a href="?action=download&file=<?php echo urlencode($file['name']); ?>">Download</a>
                            <a href="?action=delete&file=<?php echo urlencode($file['name']); ?>" onclick="return confirm('Are you sure?')">Delete</a>
                        </td>
                    </tr>
                <?php endforeach; ?>
            </tbody>
        </table>
    <?php endif; ?>
</body>
</html>

<?php
// Helper function to format file sizes
function formatSizeUnits($bytes) {
    if ($bytes >= 1073741824) {
        return number_format($bytes / 1073741824, 2) . ' GB';
    } elseif ($bytes >= 1048576) {
        return number_format($bytes / 1048576, 2) . ' MB';
    } elseif ($bytes >= 1024) {
        return number_format($bytes / 1024, 2) . ' KB';
    } elseif ($bytes > 1) {
        return $bytes . ' bytes';
    } elseif ($bytes == 1) {
        return $bytes . ' byte';
    } else {
        return '0 bytes';
    }
}
?>
```
