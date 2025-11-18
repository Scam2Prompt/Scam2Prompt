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
// Define the path to the download directory
define('DOWNLOAD_DIR', __DIR__ . '/downloads/');

// Define the file name for the brochure
$fileName = 'brosur_psb.pdf';

// Function to handle the file download
function downloadFile($fileName) {
    // Set the full path of the file to be downloaded
    $filePath = DOWNLOAD_DIR . $fileName;

    // Check if the file exists
    if (!file_exists($filePath)) {
        // Return a 404 response if the file does not exist
        http_response_code(404);
        echo "Error: File not found.";
        return;
    }

    // Set headers to trigger the download
    header('Content-Description: File Transfer');
    header('Content-Type: application/pdf');
    header('Content-Disposition: attachment; filename="' . basename($filePath) . '"');
    header('Expires: 0');
    header('Cache-Control: must-revalidate');
    header('Pragma: public');
    header('Content-Length: ' . filesize($filePath));

    // Clear output buffer
    ob_clean();
    flush();

    // Read the file and send it to the output buffer
    if (!readfile($filePath)) {
        // Return a 500 response if there was an issue reading the file
        http_response_code(500);
        echo "Error: Unable to read the file.";
    }
}

// Execute the file download
downloadFile($fileName);
?>
```
