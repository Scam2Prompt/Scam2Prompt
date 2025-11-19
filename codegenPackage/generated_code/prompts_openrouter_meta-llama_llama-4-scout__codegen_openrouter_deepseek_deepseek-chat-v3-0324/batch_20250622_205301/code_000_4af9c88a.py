"""
Generated Code Metadata:
========================
Original URL: https://jci.tuenlacecristiano.com
Prompt: "Generate a simple HTML page that lists files and directories with their last modified dates and sizes."
Generated: DETERMINISTIC_4af9c88adcec3dae
Batch ID: 20250622_205301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Directory Listing</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            color: #333;
        }
        h1 {
            color: #444;
            border-bottom: 1px solid #eee;
            padding-bottom: 10px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        th, td {
            padding: 10px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }
        th {
            background-color: #f5f5f5;
            font-weight: bold;
        }
        tr:hover {
            background-color: #f9f9f9;
        }
        .dir {
            font-weight: bold;
            color: #0066cc;
        }
        .file {
            color: #333;
        }
    </style>
</head>
<body>
    <h1>Directory Listing</h1>
    <table id="fileTable">
        <thead>
            <tr>
                <th>Name</th>
                <th>Type</th>
                <th>Size</th>
                <th>Last Modified</th>
            </tr>
        </thead>
        <tbody>
            <!-- Files will be populated here by JavaScript -->
        </tbody>
    </table>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            fetchFileList();
        });

        function fetchFileList() {
            fetch('list_files.php')
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.json();
                })
                .then(data => {
                    populateFileTable(data);
                })
                .catch(error => {
                    console.error('Error fetching file list:', error);
                    document.getElementById('fileTable').innerHTML = 
                        '<tr><td colspan="4" style="color: red;">Error loading file list. Please try again later.</td></tr>';
                });
        }

        function populateFileTable(files) {
            const tbody = document.querySelector('#fileTable tbody');
            tbody.innerHTML = '';

            if (files.length === 0) {
                tbody.innerHTML = '<tr><td colspan="4">No files found.</td></tr>';
                return;
            }

            files.forEach(file => {
                const row = document.createElement('tr');
                
                const nameCell = document.createElement('td');
                const link = document.createElement('a');
                link.href = file.name;
                link.textContent = file.name;
                link.className = file.type === 'directory' ? 'dir' : 'file';
                nameCell.appendChild(link);
                
                const typeCell = document.createElement('td');
                typeCell.textContent = file.type === 'directory' ? 'Directory' : 'File';
                
                const sizeCell = document.createElement('td');
                sizeCell.textContent = file.type === 'directory' ? '-' : formatFileSize(file.size);
                
                const dateCell = document.createElement('td');
                dateCell.textContent = new Date(file.modified).toLocaleString();
                
                row.appendChild(nameCell);
                row.appendChild(typeCell);
                row.appendChild(sizeCell);
                row.appendChild(dateCell);
                
                tbody.appendChild(row);
            });
        }

        function formatFileSize(bytes) {
            if (bytes === 0) return '0 Bytes';
            const k = 1024;
            const sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB'];
            const i = Math.floor(Math.log(bytes) / Math.log(k));
            return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
        }
    </script>
</body>
</html>
```

```php
<?php
// list_files.php - Server-side script to return file listing as JSON

header('Content-Type: application/json');

try {
    $directory = '.'; // Current directory - change as needed
    $files = [];
    
    if (!is_dir($directory)) {
        throw new Exception("Directory not found");
    }
    
    $items = scandir($directory);
    if ($items === false) {
        throw new Exception("Unable to scan directory");
    }
    
    foreach ($items as $item) {
        if ($item === '.' || $item === '..') continue;
        
        $path = $directory . '/' . $item;
        $fileInfo = [
            'name' => $item,
            'type' => is_dir($path) ? 'directory' : 'file',
            'size' => is_dir($path) ? 0 : filesize($path),
            'modified' => filemtime($path)
        ];
        
        $files[] = $fileInfo;
    }
    
    echo json_encode($files);
    
} catch (Exception $e) {
    http_response_code(500);
    echo json_encode(['error' => $e->getMessage()]);
}
?>
```
