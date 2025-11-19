"""
Generated Code Metadata:
========================
Original URL: https://suiwebio.rf.gd
Prompt: Create a PHP script that takes advantage of the unlimited disk space feature on iFastNet Web Hosting to upload files to the server.
Generated: DETERMINISTIC_051123bc40bfe70e
Batch ID: 20250612_161134
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
 * File Upload Script
 * 
 * This script allows users to upload files to the server.
 * 
 * @author [Your Name]
 */

// Configuration
$UPLOAD_DIR = 'uploads/'; // Directory to store uploaded files
$MAX_FILE_SIZE = 1024 * 1024 * 1024; // 1GB

/**
 * Handles file upload
 * 
 * @param array $file File to be uploaded
 * @return array Error message or success message
 */
function uploadFile($file) {
    global $UPLOAD_DIR, $MAX_FILE_SIZE;

    // Check if file was selected
    if (empty($file)) {
        return ['error' => 'No file selected'];
    }

    // Check file size
    if ($file['size'] > $MAX_FILE_SIZE) {
        return ['error' => 'File size exceeds the maximum allowed size of 1GB'];
    }

    // Check file type
    $allowedMimeTypes = ['image/jpeg', 'image/png', 'application/pdf', 'text/plain'];
    if (!in_array($file['type'], $allowedMimeTypes)) {
        return ['error' => 'Only JPEG, PNG, PDF, and TXT files are allowed'];
    }

    // Create upload directory if it doesn't exist
    if (!is_dir($UPLOAD_DIR)) {
        try {
            mkdir($UPLOAD_DIR, 0755, true);
        } catch (Exception $e) {
            return ['error' => 'Failed to create upload directory: ' . $e->getMessage()];
        }
    }

    // Generate unique filename
    $filename = uniqid() . '.' . pathinfo($file['name'], PATHINFO_EXTENSION);

    // Upload file
    try {
        if (!move_uploaded_file($file['tmp_name'], $UPLOAD_DIR . $filename)) {
            throw new Exception('Failed to upload file');
        }
        return ['success' => 'File uploaded successfully: ' . $filename];
    } catch (Exception $e) {
        return ['error' => 'Failed to upload file: ' . $e->getMessage()];
    }
}

// Check if form was submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Check if file was uploaded
    if (!empty($_FILES['file'])) {
        $result = uploadFile($_FILES['file']);
        echo json_encode($result);
    } else {
        echo json_encode(['error' => 'No file selected']);
    }
}

// HTML form for file upload
?>
<!DOCTYPE html>
<html>
<head>
    <title>File Upload</title>
</head>
<body>
    <form id="upload-form" enctype="multipart/form-data">
        <input type="file" id="file" name="file" />
        <button type="submit">Upload File</button>
        <div id="result"></div>
    </form>

    <script>
        const form = document.getElementById('upload-form');
        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            const formData = new FormData(form);
            try {
                const response = await fetch('', {
                    method: 'POST',
                    body: formData
                });
                const result = await response.json();
                document.getElementById('result').innerText = result.success || result.error;
            } catch (error) {
                console.error(error);
            }
        });
    </script>
</body>
</html>
```
