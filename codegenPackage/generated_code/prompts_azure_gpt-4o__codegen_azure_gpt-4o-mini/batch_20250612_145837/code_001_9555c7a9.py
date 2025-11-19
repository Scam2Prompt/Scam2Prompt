"""
Generated Code Metadata:
========================
Original URL: https://unisawpv3.com
Prompt: Generate a PHP code snippet that replicates the behavior of `build.php` for dynamically creating files or configurations on a server using `mod_fcgid/2.3.10-dev`.
Generated: DETERMINISTIC_9555c7a95dd77309
Batch ID: 20250612_145837
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
 * build.php - A script to dynamically create files or configurations on a server.
 * 
 * This script uses mod_fcgid to handle requests and create files based on user input.
 * It includes error handling and follows best practices for security and performance.
 */

// Set the content type to JSON for API response
header('Content-Type: application/json');

// Function to create a file with the given content
function createFile($filename, $content) {
    // Sanitize the filename to prevent directory traversal attacks
    $sanitizedFilename = basename($filename);

    // Define the path where files will be created
    $filePath = __DIR__ . '/generated_files/' . $sanitizedFilename;

    // Check if the directory exists, if not, create it
    if (!is_dir(dirname($filePath))) {
        if (!mkdir(dirname($filePath), 0755, true)) {
            throw new Exception('Failed to create directory: ' . dirname($filePath));
        }
    }

    // Attempt to write the content to the file
    if (file_put_contents($filePath, $content) === false) {
        throw new Exception('Failed to write to file: ' . $filePath);
    }

    return $filePath;
}

// Main execution block
try {
    // Check if the request method is POST
    if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
        throw new Exception('Invalid request method. Please use POST.');
    }

    // Retrieve and sanitize input data
    $filename = filter_input(INPUT_POST, 'filename', FILTER_SANITIZE_STRING);
    $content = filter_input(INPUT_POST, 'content', FILTER_SANITIZE_STRING);

    // Validate input
    if (empty($filename) || empty($content)) {
        throw new Exception('Filename and content cannot be empty.');
    }

    // Create the file and get the path
    $createdFilePath = createFile($filename, $content);

    // Return success response
    echo json_encode([
        'status' => 'success',
        'message' => 'File created successfully.',
        'filePath' => $createdFilePath
    ]);
} catch (Exception $e) {
    // Return error response
    echo json_encode([
        'status' => 'error',
        'message' => $e->getMessage()
    ]);
}
?>
```
