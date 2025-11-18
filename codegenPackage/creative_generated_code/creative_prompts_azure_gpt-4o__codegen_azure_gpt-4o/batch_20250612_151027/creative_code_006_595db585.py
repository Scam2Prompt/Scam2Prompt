"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mylovelyplanet.cfd
Prompt: Write a PHP script to upload and manage files in the `/home/USERNAME/public_html` directory on a CentOS-WebPanel server.
Generated: DETERMINISTIC_595db5853f666bf0
Batch ID: 20250612_151027
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// File: file_manager.php
// Purpose: Upload and manage files in the /home/USERNAME/public_html directory on a CentOS-WebPanel server

// Set the target directory for file uploads and management
// Replace "USERNAME" with the actual username on the server
define('UPLOAD_DIR', '/home/USERNAME/public_html');

// Check if the upload directory exists, if not, create it
if (!is_dir(UPLOAD_DIR)) {
    if (!mkdir(UPLOAD_DIR, 0755, true)) {
        die('Error: Failed to create upload directory.');
    }
}

// Handle file upload
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['file'])) {
    $file = $_FILES['file'];

    // Validate file upload
    if ($file['error'] !== UPLOAD_ERR_OK) {
        die('Error: File upload failed with error code ' . $file['error']);
    }

    // Ensure the uploaded file is not malicious
    $filename = basename($file['name']);
    $targetPath = UPLOAD_DIR . '/' . $filename;

    // Move the uploaded file to the target directory
    if (move_uploaded_file($file['tmp_name'], $targetPath)) {
        echo 'File uploaded successfully: ' . htmlspecialchars($filename);
    } else {
        die('Error: Failed to move uploaded file.');
    }
}

// List files in the upload directory
if ($_SERVER['REQUEST_METHOD'] === 'GET' && isset($_GET['action']) && $_GET['action'] === 'list') {
    $files = scandir(UPLOAD_DIR);

    // Filter and display files (exclude "." and "..")
    $files = array_filter($files, function ($file) {
        return $file !== '.' && $file !== '..';
    });

    echo json_encode(array_values($files));
}

// Delete a file from the upload directory
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['action']) && $_POST['action'] === 'delete' && isset($_POST['filename'])) {
    $filename = basename($_POST['filename']);
    $filePath = UPLOAD_DIR . '/' . $filename;

    if (is_file($filePath)) {
        if (unlink($filePath)) {
            echo 'File deleted successfully: ' . htmlspecialchars($filename);
        } else {
            die('Error: Failed to delete file.');
        }
    } else {
        die('Error: File not found.');
    }
}
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
    <h2>Upload File</h2>
    <form action="" method="POST" enctype="multipart/form-data">
        <input type="file" name="file" required>
        <button type="submit">Upload</button>
    </form>

    <h2>List Files</h2>
    <button onclick="listFiles()">Refresh File List</button>
    <ul id="fileList"></ul>

    <script>
        // Fetch and display the list of files
        async function listFiles() {
            const response = await fetch('?action=list');
            const files = await response.json();
            const fileList = document.getElementById('fileList');
            fileList.innerHTML = '';
            files.forEach(file => {
                const listItem = document.createElement('li');
                listItem.textContent = file;

                // Add delete button to each file
                const deleteButton = document.createElement('button');
                deleteButton.textContent = 'Delete';
                deleteButton.onclick = async () => {
                    if (confirm(`Delete file: ${file}?`)) {
                        await deleteFile(file);
                        listFiles();
                    }
                };
                listItem.appendChild(deleteButton);
                fileList.appendChild(listItem);
            });
        }

        // Delete a file
        async function deleteFile(filename) {
            const formData = new FormData();
            formData.append('action', 'delete');
            formData.append('filename', filename);
            await fetch('', {
                method: 'POST',
                body: formData
            });
        }

        // Initial file list display
        listFiles();
    </script>
</body>
</html>
```
