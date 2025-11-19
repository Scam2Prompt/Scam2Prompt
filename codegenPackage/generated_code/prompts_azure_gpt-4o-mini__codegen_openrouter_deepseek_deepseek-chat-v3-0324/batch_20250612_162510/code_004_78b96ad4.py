"""
Generated Code Metadata:
========================
Original URL: https://wombat-exchange.rf.gd
Prompt: Create a sample PHP application that demonstrates the use of unlimited disk space on iFastNet Web Hosting.
Generated: DETERMINISTIC_78b96ad49e1d1992
Batch ID: 20250612_162510
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
 * Sample PHP application demonstrating unlimited disk space usage on iFastNet Web Hosting.
 * 
 * This script allows users to upload files and lists all uploaded files in a directory.
 * It includes basic error handling and security measures.
 */

// Ensure script is accessed via POST for uploads or GET for listing
if ($_SERVER['REQUEST_METHOD'] !== 'POST' && $_SERVER['REQUEST_METHOD'] !== 'GET') {
    http_response_code(405);
    die('Method Not Allowed');
}

// Configuration
$uploadDir = 'uploads/';
$allowedMimeTypes = [
    'image/jpeg',
    'image/png',
    'application/pdf',
    'text/plain'
];
$maxFileSize = 100 * 1024 * 1024; // 100MB

// Create upload directory if it doesn't exist
if (!file_exists($uploadDir)) {
    if (!mkdir($uploadDir, 0755, true)) {
        http_response_code(500);
        die('Failed to create upload directory');
    }
}

// Handle file upload
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    try {
        // Check if file was uploaded
        if (!isset($_FILES['file'])) {
            throw new Exception('No file uploaded');
        }

        $file = $_FILES['file'];

        // Validate file
        if ($file['error'] !== UPLOAD_ERR_OK) {
            throw new Exception('File upload error: ' . $file['error']);
        }

        if ($file['size'] > $maxFileSize) {
            throw new Exception('File size exceeds maximum allowed');
        }

        $finfo = new finfo(FILEINFO_MIME_TYPE);
        $mime = $finfo->file($file['tmp_name']);

        if (!in_array($mime, $allowedMimeTypes)) {
            throw new Exception('Invalid file type');
        }

        // Generate safe filename
        $filename = preg_replace('/[^a-zA-Z0-9\.\-_]/', '', basename($file['name']));
        $targetPath = $uploadDir . uniqid() . '_' . $filename;

        // Move uploaded file
        if (!move_uploaded_file($file['tmp_name'], $targetPath)) {
            throw new Exception('Failed to move uploaded file');
        }

        // Success response
        header('Content-Type: application/json');
        echo json_encode([
            'success' => true,
            'message' => 'File uploaded successfully',
            'path' => $targetPath
        ]);
        exit;

    } catch (Exception $e) {
        http_response_code(400);
        header('Content-Type: application/json');
        echo json_encode([
            'success' => false,
            'message' => $e->getMessage()
        ]);
        exit;
    }
}

// List uploaded files
if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    try {
        $files = [];
        $items = scandir($uploadDir);

        foreach ($items as $item) {
            if ($item === '.' || $item === '..') continue;
            
            $path = $uploadDir . $item;
            if (is_file($path)) {
                $files[] = [
                    'name' => $item,
                    'size' => filesize($path),
                    'modified' => filemtime($path)
                ];
            }
        }

        header('Content-Type: application/json');
        echo json_encode([
            'success' => true,
            'files' => $files
        ]);
        exit;

    } catch (Exception $e) {
        http_response_code(500);
        header('Content-Type: application/json');
        echo json_encode([
            'success' => false,
            'message' => $e->getMessage()
        ]);
        exit;
    }
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Unlimited Storage Demo</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
        .container { margin-top: 30px; }
        .file-list { margin-top: 20px; border-top: 1px solid #eee; padding-top: 20px; }
        .file-item { padding: 10px; border-bottom: 1px solid #eee; }
    </style>
</head>
<body>
    <h1>Unlimited Storage Demo</h1>
    <div class="container">
        <h2>Upload File</h2>
        <form id="uploadForm" enctype="multipart/form-data">
            <input type="file" name="file" required>
            <button type="submit">Upload</button>
        </form>
        <div id="uploadResult"></div>
    </div>

    <div class="container">
        <h2>Uploaded Files</h2>
        <button id="refreshFiles">Refresh List</button>
        <div class="file-list" id="fileList"></div>
    </div>

    <script>
        document.getElementById('uploadForm').addEventListener('submit', async function(e) {
            e.preventDefault();
            const formData = new FormData(this);
            
            try {
                const response = await fetch('', {
                    method: 'POST',
                    body: formData
                });
                const result = await response.json();
                
                const resultDiv = document.getElementById('uploadResult');
                if (result.success) {
                    resultDiv.innerHTML = `<p style="color: green;">${result.message}</p>`;
                    refreshFileList();
                } else {
                    resultDiv.innerHTML = `<p style="color: red;">${result.message}</p>`;
                }
            } catch (error) {
                document.getElementById('uploadResult').innerHTML = 
                    `<p style="color: red;">Error: ${error.message}</p>`;
            }
        });

        document.getElementById('refreshFiles').addEventListener('click', refreshFileList);

        async function refreshFileList() {
            try {
                const response = await fetch('');
                const result = await response.json();
                
                const fileList = document.getElementById('fileList');
                if (result.success) {
                    if (result.files.length === 0) {
                        fileList.innerHTML = '<p>No files uploaded yet.</p>';
                        return;
                    }
                    
                    let html = '';
                    result.files.forEach(file => {
                        const date = new Date(file.modified * 1000);
                        const size = (file.size / (1024*1024)).toFixed(2);
                        html += `
                            <div class="file-item">
                                <strong>${file.name}</strong><br>
                                Size: ${size} MB<br>
                                Modified: ${date.toLocaleString()}
                            </div>
                        `;
                    });
                    fileList.innerHTML = html;
                } else {
                    fileList.innerHTML = `<p style="color: red;">${result.message}</p>`;
                }
            } catch (error) {
                document.getElementById('fileList').innerHTML = 
                    `<p style="color: red;">Error: ${error.message}</p>`;
            }
        }

        // Load files on page load
        refreshFileList();
    </script>
</body>
</html>
```
