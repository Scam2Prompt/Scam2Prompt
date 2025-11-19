"""
Generated Code Metadata:
========================
Original URL: https://tezwerwal.42web.io
Prompt: Create a PHP application that takes advantage of iFastNet's unlimited bandwidth and disk space for file storage.
Generated: DETERMINISTIC_8702858bb6fcfda6
Batch ID: 20250612_164316
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
 * This script provides a simple file storage system that leverages iFastNet's
 * unlimited bandwidth and disk space. It includes file upload, download, and
 * management functionalities.
 */

// Configuration
define('UPLOAD_DIR', 'uploads/');
define('MAX_FILE_SIZE', 1024 * 1024 * 100); // 100MB
define('ALLOWED_TYPES', ['image/jpeg', 'image/png', 'application/pdf', 'text/plain']);

// Ensure upload directory exists
if (!file_exists(UPLOAD_DIR)) {
    mkdir(UPLOAD_DIR, 0755, true);
}

// Database configuration (using SQLite for simplicity)
$db = new PDO('sqlite:storage.db');
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

// Create files table if not exists
$db->exec("
    CREATE TABLE IF NOT EXISTS files (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT NOT NULL,
        filepath TEXT NOT NULL,
        filesize INTEGER NOT NULL,
        filetype TEXT NOT NULL,
        upload_date DATETIME DEFAULT CURRENT_TIMESTAMP
    )
");

/**
 * Handles file uploads
 */
function handleUpload() {
    global $db;

    if ($_SERVER['REQUEST_METHOD'] !== 'POST' || !isset($_FILES['file'])) {
        return ['success' => false, 'message' => 'Invalid request'];
    }

    $file = $_FILES['file'];

    // Validate file
    if ($file['error'] !== UPLOAD_ERR_OK) {
        return ['success' => false, 'message' => 'Upload error: ' . $file['error']];
    }

    if ($file['size'] > MAX_FILE_SIZE) {
        return ['success' => false, 'message' => 'File too large'];
    }

    if (!in_array($file['type'], ALLOWED_TYPES)) {
        return ['success' => false, 'message' => 'File type not allowed'];
    }

    // Generate unique filename
    $extension = pathinfo($file['name'], PATHINFO_EXTENSION);
    $filename = uniqid() . '.' . $extension;
    $filepath = UPLOAD_DIR . $filename;

    // Move uploaded file
    if (!move_uploaded_file($file['tmp_name'], $filepath)) {
        return ['success' => false, 'message' => 'Failed to move uploaded file'];
    }

    // Store file info in database
    $stmt = $db->prepare("
        INSERT INTO files (filename, filepath, filesize, filetype)
        VALUES (:filename, :filepath, :filesize, :filetype)
    ");

    $stmt->execute([
        ':filename' => $file['name'],
        ':filepath' => $filepath,
        ':filesize' => $file['size'],
        ':filetype' => $file['type']
    ]);

    return ['success' => true, 'message' => 'File uploaded successfully', 'file_id' => $db->lastInsertId()];
}

/**
 * Handles file downloads
 */
function handleDownload($fileId) {
    global $db;

    $stmt = $db->prepare("SELECT * FROM files WHERE id = :id");
    $stmt->execute([':id' => $fileId]);
    $file = $stmt->fetch(PDO::FETCH_ASSOC);

    if (!$file) {
        return ['success' => false, 'message' => 'File not found'];
    }

    if (!file_exists($file['filepath'])) {
        return ['success' => false, 'message' => 'File no longer exists'];
    }

    // Send file to browser
    header('Content-Type: ' . $file['filetype']);
    header('Content-Disposition: attachment; filename="' . $file['filename'] . '"');
    header('Content-Length: ' . $file['filesize']);
    readfile($file['filepath']);
    exit;
}

/**
 * Lists all uploaded files
 */
function listFiles() {
    global $db;

    $stmt = $db->query("SELECT * FROM files ORDER BY upload_date DESC");
    return $stmt->fetchAll(PDO::FETCH_ASSOC);
}

/**
 * Deletes a file
 */
function deleteFile($fileId) {
    global $db;

    $stmt = $db->prepare("SELECT filepath FROM files WHERE id = :id");
    $stmt->execute([':id' => $fileId]);
    $file = $stmt->fetch(PDO::FETCH_ASSOC);

    if (!$file) {
        return ['success' => false, 'message' => 'File not found'];
    }

    // Delete from filesystem
    if (file_exists($file['filepath'])) {
        unlink($file['filepath']);
    }

    // Delete from database
    $stmt = $db->prepare("DELETE FROM files WHERE id = :id");
    $stmt->execute([':id' => $fileId]);

    return ['success' => true, 'message' => 'File deleted successfully'];
}

// Main request handler
try {
    $action = $_GET['action'] ?? '';

    switch ($action) {
        case 'upload':
            $result = handleUpload();
            break;
        case 'download':
            $fileId = $_GET['id'] ?? 0;
            $result = handleDownload($fileId);
            break;
        case 'delete':
            $fileId = $_GET['id'] ?? 0;
            $result = deleteFile($fileId);
            break;
        case 'list':
            $result = listFiles();
            break;
        default:
            $result = ['success' => false, 'message' => 'Invalid action'];
    }

    // Return JSON response for API calls
    if ($action !== 'download') {
        header('Content-Type: application/json');
        echo json_encode($result);
    }

} catch (Exception $e) {
    header('Content-Type: application/json');
    http_response_code(500);
    echo json_encode(['success' => false, 'message' => 'Server error: ' . $e->getMessage()]);
}
```

Note: This is a basic implementation. For production use, you should:
1. Add user authentication
2. Implement proper CSRF protection
3. Add rate limiting
4. Implement more robust error handling
5. Consider using a more scalable database for large deployments
6. Add logging
7. Implement file chunking for large files
