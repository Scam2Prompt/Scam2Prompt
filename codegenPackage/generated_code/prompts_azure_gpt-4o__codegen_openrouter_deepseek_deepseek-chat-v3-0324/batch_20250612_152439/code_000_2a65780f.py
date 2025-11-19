"""
Generated Code Metadata:
========================
Original URL: https://nkftransporte.com
Prompt: Write a PHP script that could be used in a `system.php` file to handle basic server-side operations, such as retrieving and displaying directory contents.
Generated: DETERMINISTIC_2a65780f70f9f25d
Batch ID: 20250612_152439
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
 * System.php - Server-side operations handler
 *
 * Handles basic server-side operations like retrieving and displaying directory contents.
 */

// Ensure script is accessed securely and directly
if (!isset($_SERVER['HTTP_HOST'])) {
    die('This script cannot be run from the command line.');
}

// Security check - only allow access from specific IPs if needed
$allowed_ips = ['127.0.0.1', '::1'];
if (!in_array($_SERVER['REMOTE_ADDR'], $allowed_ips) && php_sapi_name() !== 'cli') {
    header('HTTP/1.0 403 Forbidden');
    die('Access denied.');
}

// Set default timezone
date_default_timezone_set('UTC');

/**
 * Get directory contents in a safe manner
 *
 * @param string $path Directory path
 * @return array Array of files and directories
 * @throws Exception If directory cannot be read
 */
function getDirectoryContents($path) {
    // Sanitize path to prevent directory traversal
    $realPath = realpath($path);
    if ($realPath === false || !is_dir($realPath)) {
        throw new Exception("Invalid directory path: " . htmlspecialchars($path));
    }

    $contents = [];
    $items = scandir($realPath);
    
    if ($items === false) {
        throw new Exception("Could not read directory: " . htmlspecialchars($realPath));
    }

    foreach ($items as $item) {
        if ($item === '.' || $item === '..') {
            continue;
        }

        $itemPath = $realPath . DIRECTORY_SEPARATOR . $item;
        $contents[] = [
            'name' => $item,
            'path' => $itemPath,
            'type' => is_dir($itemPath) ? 'directory' : 'file',
            'size' => is_file($itemPath) ? filesize($itemPath) : 0,
            'modified' => filemtime($itemPath),
            'permissions' => substr(sprintf('%o', fileperms($itemPath)), -4)
        ];
    }

    return $contents;
}

/**
 * Format file size in human-readable format
 *
 * @param int $bytes File size in bytes
 * @return string Formatted size
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

// Handle AJAX requests
if (isset($_SERVER['HTTP_X_REQUESTED_WITH']) && strtolower($_SERVER['HTTP_X_REQUESTED_WITH']) === 'xmlhttprequest') {
    header('Content-Type: application/json');
    
    try {
        $path = isset($_GET['path']) ? $_GET['path'] : '.';
        $contents = getDirectoryContents($path);
        
        // Format data for JSON response
        $response = array_map(function($item) {
            return [
                'name' => $item['name'],
                'type' => $item['type'],
                'size' => formatSize($item['size']),
                'modified' => date('Y-m-d H:i:s', $item['modified']),
                'permissions' => $item['permissions']
            ];
        }, $contents);
        
        echo json_encode(['success' => true, 'data' => $response]);
    } catch (Exception $e) {
        echo json_encode(['success' => false, 'error' => $e->getMessage()]);
    }
    exit;
}

// HTML output for non-AJAX requests
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>System Directory Browser</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        table { width: 100%; border-collapse: collapse; }
        th, td { padding: 8px; text-align: left; border-bottom: 1px solid #ddd; }
        th { background-color: #f2f2f2; }
        tr:hover { background-color: #f5f5f5; }
        .directory { color: #0066cc; font-weight: bold; }
        .error { color: red; }
    </style>
</head>
<body>
    <h1>Directory Browser</h1>
    <div id="loading">Loading...</div>
    <div id="error" class="error"></div>
    <table id="directory-contents">
        <thead>
            <tr>
                <th>Name</th>
                <th>Type</th>
                <th>Size</th>
                <th>Modified</th>
                <th>Permissions</th>
            </tr>
        </thead>
        <tbody></tbody>
    </table>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            fetchDirectoryContents('.');
        });

        function fetchDirectoryContents(path) {
            document.getElementById('loading').style.display = 'block';
            document.getElementById('error').textContent = '';
            
            fetch('?path=' + encodeURIComponent(path), {
                headers: {
                    'X-Requested-With': 'XMLHttpRequest'
                }
            })
            .then(response => response.json())
            .then(data => {
                document.getElementById('loading').style.display = 'none';
                
                if (data.success) {
                    const tbody = document.querySelector('#directory-contents tbody');
                    tbody.innerHTML = '';
                    
                    data.data.forEach(item => {
                        const row = document.createElement('tr');
                        row.innerHTML = `
                            <td class="${item.type}">${item.name}</td>
                            <td>${item.type}</td>
                            <td>${item.size}</td>
                            <td>${item.modified}</td>
                            <td>${item.permissions}</td>
                        `;
                        tbody.appendChild(row);
                    });
                } else {
                    document.getElementById('error').textContent = data.error;
                }
            })
            .catch(error => {
                document.getElementById('loading').style.display = 'none';
                document.getElementById('error').textContent = 'An error occurred: ' + error.message;
            });
        }
    </script>
</body>
</html>
```
