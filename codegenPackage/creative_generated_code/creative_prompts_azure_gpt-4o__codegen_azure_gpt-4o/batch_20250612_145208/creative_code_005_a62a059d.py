"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connectwallet.digital
Prompt: Write a PHP script that interacts with a server running Apache/2.4.62 and PHP/8.3.14, as seen on connectwallet.digital, to manage temporary files in a `tmp/` directory.
Generated: DETERMINISTIC_a62a059d7552a454
Batch ID: 20250612_145208
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
/**
 * Temporary File Manager
 * 
 * This script interacts with an Apache server to manage temporary files 
 * in the `tmp/` directory. It provides functionality to list, delete, 
 * and create temporary files securely.
 * 
 * Requirements:
 * - PHP 8.3 or later
 * - Directory `tmp/` must be writable by the web server
 */

// Configuration
define('TMP_DIR', __DIR__ . '/tmp/'); // Path to the temporary directory

// Ensure TMP_DIR exists and is writable
if (!is_dir(TMP_DIR)) {
    mkdir(TMP_DIR, 0755, true);
}

if (!is_writable(TMP_DIR)) {
    http_response_code(500);
    echo json_encode(['error' => 'Temporary directory is not writable.']);
    exit;
}

// Handle HTTP requests
$requestMethod = $_SERVER['REQUEST_METHOD'];

switch ($requestMethod) {
    case 'GET':
        listTemporaryFiles();
        break;

    case 'POST':
        createTemporaryFile();
        break;

    case 'DELETE':
        deleteTemporaryFile();
        break;

    default:
        http_response_code(405);
        echo json_encode(['error' => 'Method not allowed.']);
        break;
}

/**
 * List all temporary files in the TMP_DIR.
 */
function listTemporaryFiles()
{
    try {
        $files = array_filter(scandir(TMP_DIR), function ($file) {
            return !is_dir(TMP_DIR . $file);
        });

        echo json_encode(['files' => $files]);
    } catch (Exception $e) {
        http_response_code(500);
        echo json_encode(['error' => 'Failed to fetch files.', 'details' => $e->getMessage()]);
    }
}

/**
 * Create a new temporary file.
 * Expects POST data with `name` parameter for file name and optional `content`.
 */
function createTemporaryFile()
{
    $data = json_decode(file_get_contents('php://input'), true);
    $fileName = $data['name'] ?? null;
    $fileContent = $data['content'] ?? '';

    if (!$fileName || preg_match('/[^a-zA-Z0-9_\-\.]/', $fileName)) {
        http_response_code(400);
        echo json_encode(['error' => 'Invalid file name.']);
        return;
    }

    $filePath = TMP_DIR . $fileName;

    try {
        file_put_contents($filePath, $fileContent);
        echo json_encode(['message' => 'File created successfully.', 'file' => $fileName]);
    } catch (Exception $e) {
        http_response_code(500);
        echo json_encode(['error' => 'Failed to create file.', 'details' => $e->getMessage()]);
    }
}

/**
 * Delete a temporary file.
 * Expects DELETE data with `name` parameter for file name.
 */
function deleteTemporaryFile()
{
    parse_str(file_get_contents('php://input'), $data);
    $fileName = $data['name'] ?? null;

    if (!$fileName || preg_match('/[^a-zA-Z0-9_\-\.]/', $fileName)) {
        http_response_code(400);
        echo json_encode(['error' => 'Invalid file name.']);
        return;
    }

    $filePath = TMP_DIR . $fileName;

    if (!file_exists($filePath)) {
        http_response_code(404);
        echo json_encode(['error' => 'File not found.']);
        return;
    }

    try {
        unlink($filePath);
        echo json_encode(['message' => 'File deleted successfully.', 'file' => $fileName]);
    } catch (Exception $e) {
        http_response_code(500);
        echo json_encode(['error' => 'Failed to delete file.', 'details' => $e->getMessage()]);
    }
}

?>
```
