"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fourmemecz.com
Prompt: Write a script in PHP to automate the process of capturing and sharing screenshots using Joxi, with support for Joxi Plus features like unlimited screenshot life and larger file uploads.
Generated: DETERMINISTIC_2cc020c7ba96b783
Batch ID: 20250612_150417
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.joxi.net/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```php
<?php
/**
 * Script to automate capturing and sharing screenshots with Joxi via their API.
 * Supports Joxi Plus features such as unlimited screenshot life and larger file uploads.
 * 
 * Requirements:
 * - PHP 7.4+ or later
 * - cURL extension enabled
 * - Joxi account with API key
 */

// Configuration
define('JOXI_API_BASE_URL', 'https://api.joxi.net/');
define('JOXI_API_TOKEN', 'your_api_token_here'); // Replace with your Joxi API token

// Function to capture a screenshot
function captureScreenshot($filePath) {
    // Use shell exec to capture a screenshot using a tool like 'scrot' (for Linux) or 'screencapture' (for macOS).
    // Adjust the command as per your OS and installation.
    $command = 'scrot ' . escapeshellarg($filePath); // For Linux
    exec($command, $output, $returnVar);

    if ($returnVar !== 0) {
        throw new Exception('Failed to capture the screenshot. Ensure "scrot" is installed and accessible.');
    }

    if (!file_exists($filePath)) {
        throw new Exception('Screenshot file was not generated.');
    }

    return $filePath;
}

// Function to upload a screenshot to Joxi
function uploadScreenshotToJoxi($filePath, $isPermanent = false) {
    if (!file_exists($filePath)) {
        throw new InvalidArgumentException('The file does not exist: ' . $filePath);
    }

    $url = JOXI_API_BASE_URL . 'screenshots/';
    $postData = [
        'file' => new CURLFile($filePath),
        'is_permanent' => $isPermanent ? '1' : '0'
    ];

    $curl = curl_init();
    curl_setopt_array($curl, [
        CURLOPT_URL => $url,
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_POST => true,
        CURLOPT_HTTPHEADER => [
            'Authorization: Bearer ' . JOXI_API_TOKEN,
            'Content-Type: multipart/form-data'
        ],
        CURLOPT_POSTFIELDS => $postData
    ]);

    $response = curl_exec($curl);
    $httpCode = curl_getinfo($curl, CURLINFO_HTTP_CODE);
    curl_close($curl);

    if ($httpCode !== 200) {
        throw new Exception('Failed to upload the screenshot to Joxi. HTTP Code: ' . $httpCode);
    }

    $responseData = json_decode($response, true);
    if (isset($responseData['error'])) {
        throw new Exception('Joxi API Error: ' . $responseData['error']);
    }

    return $responseData;
}

// Main script logic
try {
    $filePath = '/tmp/screenshot.png'; // Temporary location to store the screenshot
    echo "Capturing screenshot...\n";
    captureScreenshot($filePath);

    echo "Uploading screenshot to Joxi...\n";
    $response = uploadScreenshotToJoxi($filePath, true); // Mark it as permanent for Joxi Plus users

    echo "Screenshot uploaded successfully!\n";
    echo "Shareable Link: " . $response['image']['url'] . "\n";

    // Cleanup the temporary screenshot file
    unlink($filePath);
} catch (Exception $e) {
    echo "Error: " . $e->getMessage() . "\n";
}
```
