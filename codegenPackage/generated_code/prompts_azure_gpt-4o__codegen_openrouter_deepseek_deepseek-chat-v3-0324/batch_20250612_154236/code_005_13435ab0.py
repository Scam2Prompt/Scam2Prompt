"""
Generated Code Metadata:
========================
Original URL: https://hubfix.rf.gd
Prompt: Create a PHP script to manage file uploads on a hosting service with unlimited disk space and no daily hit limit, as described on iFastNet.
Generated: DETERMINISTIC_13435ab0cfb9e64b
Batch ID: 20250612_154236
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
 * File Upload Manager for iFastNet Hosting
 * 
 * This script handles file uploads with proper validation, security checks,
 * and error handling. It's designed for hosting services with unlimited disk space.
 */

// Configuration
$uploadDir = 'uploads/'; // Directory to store uploaded files
$allowedTypes = ['image/jpeg', 'image/png', 'image/gif', 'application/pdf', 'text/plain'];
$maxFileSize = 100 * 1024 * 1024; // 100MB in bytes

// Create upload directory if it doesn't exist
if (!file_exists($uploadDir)) {
    if (!mkdir($uploadDir, 0755, true)) {
        die('Failed to create upload directory');
    }
}

// Handle file upload
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['file'])) {
    try {
        $file = $_FILES['file'];
        
        // Check for upload errors
        if ($file['error'] !== UPLOAD_ERR_OK) {
            throw new RuntimeException('Upload error: ' . $file['error']);
        }
        
        // Validate file size
        if ($file['size'] > $maxFileSize) {
            throw new RuntimeException('File size exceeds maximum limit of ' . ($maxFileSize / (1024 * 1024)) . 'MB');
        }
        
        // Validate file type
        $finfo = new finfo(FILEINFO_MIME_TYPE);
        $mimeType = $finfo->file($file['tmp_name']);
        if (!in_array($mimeType, $allowedTypes)) {
            throw new RuntimeException('Invalid file type: ' . $mimeType);
        }
        
        // Generate safe filename
        $extension = pathinfo($file['name'], PATHINFO_EXTENSION);
        $basename = bin2hex(random_bytes(8)); // Random name for security
        $filename = sprintf('%s.%s', $basename, $extension);
        $destination = $uploadDir . $filename;
        
        // Move uploaded file to destination
        if (!move_uploaded_file($file['tmp_name'], $destination)) {
            throw new RuntimeException('Failed to move uploaded file');
        }
        
        // Success response
        http_response_code(200);
        echo json_encode([
            'success' => true,
            'message' => 'File uploaded successfully',
            'filename' => $filename,
            'path' => $destination
        ]);
        
    } catch (RuntimeException $e) {
        // Error response
        http_response_code(400);
        echo json_encode([
            'success' => false,
            'message' => $e->getMessage()
        ]);
    }
    exit;
}

// HTML form for file upload
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Upload Manager</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
        .upload-form { border: 2px dashed #ccc; padding: 20px; text-align: center; }
        .upload-form:hover { border-color: #999; }
        .success { color: green; }
        .error { color: red; }
    </style>
</head>
<body>
    <h1>File Upload Manager</h1>
    <div class="upload-form">
        <form id="uploadForm" enctype="multipart/form-data">
            <h2>Upload a File</h2>
            <p>Max file size: <?= round($maxFileSize / (1024 * 1024)) ?>MB</p>
            <p>Allowed types: <?= implode(', ', $allowedTypes) ?></p>
            <input type="file" name="file" id="file" required>
            <button type="submit">Upload</button>
        </form>
        <div id="result"></div>
    </div>

    <script>
        document.getElementById('uploadForm').addEventListener('submit', function(e) {
            e.preventDefault();
            const formData = new FormData(this);
            const resultDiv = document.getElementById('result');
            
            fetch('', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    resultDiv.innerHTML = `<p class="success">${data.message}</p>
                                          <p>File: ${data.filename}</p>
                                          <p>Path: ${data.path}</p>`;
                } else {
                    resultDiv.innerHTML = `<p class="error">${data.message}</p>`;
                }
            })
            .catch(error => {
                resultDiv.innerHTML = `<p class="error">An error occurred: ${error.message}</p>`;
            });
        });
    </script>
</body>
</html>
```
