"""
Generated Code Metadata:
========================
Original URL: https://credidavivienta.webcindario.com
Prompt: Create a PHP script to upload and retrieve files from a MySQL database, suitable for a free website setup similar to the one described.
Generated: DETERMINISTIC_32c36d6a158b6161
Batch ID: 20250612_154420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// Database configuration
define('DB_HOST', 'localhost');
define('DB_USER', 'username');
define('DB_PASS', 'password');
define('DB_NAME', 'database_name');

// File upload configuration
define('MAX_FILE_SIZE', 5 * 1024 * 1024); // 5MB
define('ALLOWED_TYPES', ['image/jpeg', 'image/png', 'application/pdf']);

// Establish database connection
function getDBConnection() {
    $conn = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
    
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }
    
    return $conn;
}

// Create files table if not exists
function createFilesTable() {
    $conn = getDBConnection();
    
    $sql = "CREATE TABLE IF NOT EXISTS files (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        type VARCHAR(100) NOT NULL,
        size INT NOT NULL,
        data LONGBLOB NOT NULL,
        upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )";
    
    if (!$conn->query($sql)) {
        die("Error creating table: " . $conn->error);
    }
    
    $conn->close();
}

// Handle file upload
function uploadFile() {
    if ($_SERVER['REQUEST_METHOD'] !== 'POST' || !isset($_FILES['file'])) {
        return ['success' => false, 'message' => 'Invalid request'];
    }
    
    $file = $_FILES['file'];
    
    // Validate file
    if ($file['error'] !== UPLOAD_ERR_OK) {
        return ['success' => false, 'message' => 'File upload error'];
    }
    
    if ($file['size'] > MAX_FILE_SIZE) {
        return ['success' => false, 'message' => 'File too large'];
    }
    
    if (!in_array($file['type'], ALLOWED_TYPES)) {
        return ['success' => false, 'message' => 'File type not allowed'];
    }
    
    // Read file data
    $data = file_get_contents($file['tmp_name']);
    if ($data === false) {
        return ['success' => false, 'message' => 'Error reading file'];
    }
    
    // Prepare data for database
    $name = $conn->real_escape_string(basename($file['name']));
    $type = $conn->real_escape_string($file['type']);
    $size = $file['size'];
    $data = $conn->real_escape_string($data);
    
    // Insert into database
    $conn = getDBConnection();
    $stmt = $conn->prepare("INSERT INTO files (name, type, size, data) VALUES (?, ?, ?, ?)");
    $stmt->bind_param("ssis", $name, $type, $size, $data);
    
    if ($stmt->execute()) {
        $response = ['success' => true, 'message' => 'File uploaded successfully'];
    } else {
        $response = ['success' => false, 'message' => 'Error uploading file: ' . $conn->error];
    }
    
    $stmt->close();
    $conn->close();
    
    return $response;
}

// Retrieve file from database
function getFile($id) {
    $conn = getDBConnection();
    $id = $conn->real_escape_string($id);
    
    $result = $conn->query("SELECT name, type, size, data FROM files WHERE id = $id");
    
    if ($result && $result->num_rows > 0) {
        $file = $result->fetch_assoc();
        $conn->close();
        return $file;
    }
    
    $conn->close();
    return null;
}

// List all uploaded files
function listFiles() {
    $conn = getDBConnection();
    
    $result = $conn->query("SELECT id, name, type, size, upload_date FROM files ORDER BY upload_date DESC");
    $files = [];
    
    if ($result) {
        while ($row = $result->fetch_assoc()) {
            $files[] = $row;
        }
    }
    
    $conn->close();
    return $files;
}

// Initialize database table
createFilesTable();

// Handle requests
if (isset($_GET['action'])) {
    header('Content-Type: application/json');
    
    try {
        switch ($_GET['action']) {
            case 'upload':
                echo json_encode(uploadFile());
                break;
                
            case 'list':
                echo json_encode(['success' => true, 'files' => listFiles()]);
                break;
                
            case 'download':
                if (!isset($_GET['id'])) {
                    echo json_encode(['success' => false, 'message' => 'File ID required']);
                    break;
                }
                
                $file = getFile($_GET['id']);
                if ($file) {
                    header('Content-Type: ' . $file['type']);
                    header('Content-Length: ' . $file['size']);
                    header('Content-Disposition: attachment; filename="' . $file['name'] . '"');
                    echo $file['data'];
                    exit;
                } else {
                    echo json_encode(['success' => false, 'message' => 'File not found']);
                }
                break;
                
            default:
                echo json_encode(['success' => false, 'message' => 'Invalid action']);
        }
    } catch (Exception $e) {
        echo json_encode(['success' => false, 'message' => 'Error: ' . $e->getMessage()]);
    }
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>File Upload System</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
        .file-list { margin-top: 20px; border: 1px solid #ddd; padding: 10px; }
        .file-item { padding: 8px; border-bottom: 1px solid #eee; }
        .file-item:last-child { border-bottom: none; }
    </style>
</head>
<body>
    <h1>File Upload System</h1>
    
    <form id="uploadForm" enctype="multipart/form-data">
        <input type="file" name="file" required>
        <button type="button" onclick="uploadFile()">Upload</button>
    </form>
    
    <div id="message"></div>
    
    <h2>Uploaded Files</h2>
    <div id="fileList" class="file-list">
        Loading files...
    </div>
    
    <script>
        function uploadFile() {
            const form = document.getElementById('uploadForm');
            const formData = new FormData(form);
            
            fetch('?action=upload', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                document.getElementById('message').innerHTML = data.message;
                if (data.success) {
                    form.reset();
                    loadFiles();
                }
            })
            .catch(error => {
                document.getElementById('message').innerHTML = 'Error: ' + error;
            });
        }
        
        function loadFiles() {
            fetch('?action=list')
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        let html = '';
                        if (data.files.length > 0) {
                            data.files.forEach(file => {
                                html += `<div class="file-item">
                                    <a href="?action=download&id=${file.id}">${file.name}</a>
                                    (${formatBytes(file.size)}) - ${file.upload_date}
                                </div>`;
                            });
                        } else {
                            html = 'No files uploaded yet.';
                        }
                        document.getElementById('fileList').innerHTML = html;
                    }
                });
        }
        
        function formatBytes(bytes) {
            if (bytes === 0) return '0 Bytes';
            const k = 1024;
            const sizes = ['Bytes', 'KB', 'MB', 'GB'];
            const i = Math.floor(Math.log(bytes) / Math.log(k));
            return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
        }
        
        // Load files on page load
        window.onload = loadFiles;
    </script>
</body>
</html>
```
