"""
Generated Code Metadata:
========================
Original URL: https://sekolahquranindonesia.com
Prompt: Write PHP code to implement a feature for downloading the "Brosur PSB" from Sekolah Quran Indonesia's website, ensuring secure file handling.
Generated: DETERMINISTIC_447afb7bd8cb163d
Batch ID: 20250612_151847
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
 * File Download Handler for Brosur PSB
 * 
 * This script handles secure downloading of the "Brosur PSB" file from Sekolah Quran Indonesia's website.
 * It includes security checks to prevent directory traversal and ensures only authorized files can be downloaded.
 */

// Define allowed file types and paths
define('ALLOWED_FILES', [
    'brosur-psb.pdf' => 'downloads/brosur-psb.pdf'
]);

// Set security headers
header("X-Content-Type-Options: nosniff");
header("X-Frame-Options: DENY");
header("X-XSS-Protection: 1; mode=block");

// Check if file parameter exists and is valid
if (!isset($_GET['file']) || !array_key_exists($_GET['file'], ALLOWED_FILES)) {
    http_response_code(400);
    die('Invalid file request');
}

$requestedFile = $_GET['file'];
$filePath = ALLOWED_FILES[$requestedFile];

// Verify file exists and is readable
if (!file_exists($filePath) || !is_readable($filePath)) {
    http_response_code(404);
    die('File not found or not accessible');
}

// Get file information
$fileSize = filesize($filePath);
$fileExtension = pathinfo($filePath, PATHINFO_EXTENSION);
$fileName = basename($filePath);

// Set appropriate headers for file download
header("Content-Type: application/octet-stream");
header("Content-Disposition: attachment; filename=\"$fileName\"");
header("Content-Length: " . $fileSize);
header("Content-Transfer-Encoding: binary");
header("Cache-Control: no-cache, must-revalidate");
header("Expires: 0");

// Clear output buffer and send file
ob_clean();
flush();
readfile($filePath);
exit;
```
