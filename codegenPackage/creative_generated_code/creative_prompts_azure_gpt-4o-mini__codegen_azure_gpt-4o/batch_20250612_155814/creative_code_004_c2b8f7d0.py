"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sophon-farming.pro
Prompt: Provide a code example for handling file retrieval from the index directory of sophon-farming.pro using PHP.
Generated: DETERMINISTIC_c2b8f7d062691755
Batch ID: 20250612_155814
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// File: file_retrieval.php

/**
 * Retrieves a file from the index directory of sophon-farming.pro.
 * 
 * This script fetches the requested file if it exists and streams it to the client.
 * Proper error handling is implemented to ensure security and reliability.
 */

// Define the directory path
define('INDEX_DIRECTORY', '/var/www/sophon-farming.pro/index/');

/**
 * Safely retrieves a file from the index directory.
 * 
 * @param string $fileName The name of the file to retrieve.
 * @return void Sends the file to the client if successful; otherwise, sends an error message.
 */
function retrieveFile($fileName)
{
    try {
        // Sanitize the file name to prevent directory traversal attacks
        $sanitizedFileName = basename($fileName);

        // Construct the full file path
        $filePath = INDEX_DIRECTORY . $sanitizedFileName;

        // Check if the file exists and is readable
        if (!file_exists($filePath) || !is_readable($filePath)) {
            http_response_code(404); // Send 404 response code
            echo json_encode(['error' => 'File not found or inaccessible.']);
            return;
        }

        // Get file mime type
        $mimeType = mime_content_type($filePath);

        // Send appropriate headers
        header('Content-Type: ' . $mimeType);
        header('Content-Disposition: attachment; filename="' . $sanitizedFileName . '"');
        header('Content-Length: ' . filesize($filePath));

        // Stream the file content to the client
        readfile($filePath);
    } catch (Exception $e) {
        // Handle unexpected errors
        http_response_code(500); // Send 500 response code
        echo json_encode(['error' => 'An internal server error occurred.', 'details' => $e->getMessage()]);
        return;
    }
}

// Only allow GET requests
if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    // Ensure 'file' parameter is provided
    if (!isset($_GET['file']) || empty($_GET['file'])) {
        http_response_code(400); // Send 400 response code
        echo json_encode(['error' => 'Missing file parameter.']);
        exit;
    }

    // Retrieve the requested file
    retrieveFile($_GET['file']);
} else {
    // Reject non-GET requests
    http_response_code(405); // Send 405 response code
    echo json_encode(['error' => 'Method not allowed.']);
}
?>
```
