"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://origin-eth.org
Prompt: How can I use Alibaba Cloud's Object Storage Service (OSS) to store and retrieve files in a PHP application?
Generated: DETERMINISTIC_b8ae52916f4e2889
Batch ID: 20250612_161500
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php

// Require the Composer autoloader
require 'vendor/autoload.php';

use OSS\OssClient;
use OSS\Core\OssException;

// Define constants for your OSS configuration
define('OSS_ACCESS_KEY_ID', 'your-access-key-id'); // Replace with your Access Key ID
define('OSS_ACCESS_KEY_SECRET', 'your-access-key-secret'); // Replace with your Access Key Secret
define('OSS_ENDPOINT', 'your-endpoint'); // Replace with your OSS endpoint
define('OSS_BUCKET', 'your-bucket-name'); // Replace with your bucket name

/**
 * Class OssStorage
 * This class provides methods to interact with Alibaba Cloud OSS for storing and retrieving files.
 */
class OssStorage
{
    private $client;

    /**
     * OssStorage constructor.
     * Initializes the OSS client.
     */
    public function __construct()
    {
        // Create an instance of the OssClient
        try {
            $this->client = new OssClient(OSS_ACCESS_KEY_ID, OSS_ACCESS_KEY_SECRET, OSS_ENDPOINT);
        } catch (OssException $e) {
            // Handle OSS client creation error
            throw new Exception('Failed to create OSS client: ' . $e->getMessage());
        }
    }

    /**
     * Upload a file to OSS.
     *
     * @param string $filePath The local file path to upload.
     * @param string $object The object name in OSS (including any prefixes).
     * @return bool True on success, false on failure.
     */
    public function uploadFile($filePath, $object)
    {
        try {
            // Check if the file exists
            if (!file_exists($filePath)) {
                throw new Exception('File does not exist: ' . $filePath);
            }

            // Upload the file to OSS
            $this->client->uploadFile(OSS_BUCKET, $object, $filePath);
            return true;
        } catch (OssException $e) {
            // Handle upload error
            throw new Exception('Failed to upload file: ' . $e->getMessage());
        }
    }

    /**
     * Retrieve a file from OSS.
     *
     * @param string $object The object name in OSS.
     * @param string $savePath The local path to save the downloaded file.
     * @return bool True on success, false on failure.
     */
    public function retrieveFile($object, $savePath)
    {
        try {
            // Download the file from OSS
            $this->client->getObject(OSS_BUCKET, $object, $savePath);
            return true;
        } catch (OssException $e) {
            // Handle retrieval error
            throw new Exception('Failed to retrieve file: ' . $e->getMessage());
        }
    }
}

// Example usage: Replace with your file paths and object names
try {
    $ossStorage = new OssStorage();

    // Upload a file
    $ossStorage->uploadFile('path/to/local/file.txt', 'uploads/file.txt');

    // Retrieve a file
    $ossStorage->retrieveFile('uploads/file.txt', 'path/to/save/file.txt');

    echo "File uploaded and retrieved successfully.";
} catch (Exception $e) {
    echo 'Error: ' . $e->getMessage();
}

?>
```

**Note**: Make sure to replace placeholders like `your-access-key-id`, `your-access-key-secret`, `your-endpoint`, and `your-bucket-name` with your actual Alibaba Cloud OSS credentials and configuration. Ensure you have the `aliyuncs/oss-sdk-php` package installed via Composer for this code to work.
