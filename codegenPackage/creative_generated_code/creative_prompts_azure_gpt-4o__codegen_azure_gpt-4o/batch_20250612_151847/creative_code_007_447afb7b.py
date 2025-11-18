"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sekolahquranindonesia.com
Prompt: Write PHP code to implement a feature for downloading the "Brosur PSB" from Sekolah Quran Indonesia's website, ensuring secure file handling.
Generated: DETERMINISTIC_447afb7bd8cb163d
Batch ID: 20250612_151847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Define the path to the file to be downloaded
define('FILE_PATH', __DIR__ . '/files/brosur_psb.pdf'); // Ensure the file is stored in a secure location

// Secure file download function
function downloadFile($filePath)
{
    // Check if the file exists
    if (!file_exists($filePath)) {
        http_response_code(404); // Send a 404 response if the file is not found
        echo "File not found.";
        return;
    }

    // Ensure the file path is not malicious (basic security measure)
    if (strpos(realpath($filePath), __DIR__) !== 0) {
        http_response_code(403); // Send a 403 response if the file path is invalid
        echo "Forbidden.";
        return;
    }

    // Set headers for file download
    header('Content-Description: File Transfer');
    header('Content-Type: application/pdf'); // Adjust MIME type based on file type
    header('Content-Disposition: attachment; filename="' . basename($filePath) . '"');
    header('Content-Length: ' . filesize($filePath));
    header('Cache-Control: must-revalidate');
    header('Pragma: public');
    header('Expires: 0');

    // Read the file and output its content
    readfile($filePath);
    exit; // Terminate the script to prevent additional output
}

// Main execution
try {
    // Call the download function with the file path
    downloadFile(FILE_PATH);
} catch (Exception $e) {
    http_response_code(500); // Send a 500 response for server errors
    echo "An error occurred: " . htmlspecialchars($e->getMessage());
}
?>
```
