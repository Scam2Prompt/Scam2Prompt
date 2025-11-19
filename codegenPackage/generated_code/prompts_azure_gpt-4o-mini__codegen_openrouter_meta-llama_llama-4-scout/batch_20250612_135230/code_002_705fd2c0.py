"""
Generated Code Metadata:
========================
Original URL: https://blockchain.hstn.me
Prompt: Create a PHP application that takes advantage of the unlimited disk space offered by iFastNet hosting services.
Generated: DETERMINISTIC_705fd2c0d0ad8890
Batch ID: 20250612_135230
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
 * iFastNet Storage Application
 *
 * This application utilizes the unlimited disk space offered by iFastNet hosting services.
 * It provides basic file management functionality, including file upload, download, and deletion.
 */

// Configuration
$config = [
    'rootDirectory' => '/path/to/website/storage/', // Set to a valid directory within your iFastNet hosting account
];

// Validate root directory
if (!is_dir($config['rootDirectory'])) {
    throw new Exception("Invalid root directory: " . $config['rootDirectory']);
}

// Initialize the application
$app = new iFastNetStorageApp($config);

/**
 * iFastNet Storage Application Class
 */
class iFastNetStorageApp
{
    private $config;

    public function __construct($config)
    {
        $this->config = $config;
    }

    /**
     * Handle file upload
     *
     * @param string $fileName
     * @param string $fileContent
     * @return bool
     */
    public function uploadFile($fileName, $fileContent)
    {
        try {
            $filePath = $this->config['rootDirectory'] . $fileName;
            file_put_contents($filePath, $fileContent);
            return true;
        } catch (Exception $e) {
            error_log("Error uploading file: " . $e->getMessage());
            return false;
        }
    }

    /**
     * Handle file download
     *
     * @param string $fileName
     * @return string|false
     */
    public function downloadFile($fileName)
    {
        try {
            $filePath = $this->config['rootDirectory'] . $fileName;
            if (!file_exists($filePath)) {
                return false;
            }
            return file_get_contents($filePath);
        } catch (Exception $e) {
            error_log("Error downloading file: " . $e->getMessage());
            return false;
        }
    }

    /**
     * Handle file deletion
     *
     * @param string $fileName
     * @return bool
     */
    public function deleteFile($fileName)
    {
        try {
            $filePath = $this->config['rootDirectory'] . $fileName;
            if (!file_exists($filePath)) {
                return false;
            }
            unlink($filePath);
            return true;
        } catch (Exception $e) {
            error_log("Error deleting file: " . $e->getMessage());
            return false;
        }
    }
}

// Example usage
if (isset($_FILES['file'])) {
    $fileName = $_FILES['file']['name'];
    $fileContent = file_get_contents($_FILES['file']['tmp_name']);
    $result = $app->uploadFile($fileName, $fileContent);
    if ($result) {
        echo "File uploaded successfully!";
    } else {
        echo "Error uploading file.";
    }
} elseif (isset($_GET['download'])) {
    $fileName = $_GET['download'];
    $fileContent = $app->downloadFile($fileName);
    if ($fileContent !== false) {
        header('Content-Type: application/octet-stream');
        header('Content-Disposition: attachment; filename="' . $fileName . '"');
        echo $fileContent;
    } else {
        echo "File not found.";
    }
} elseif (isset($_GET['delete'])) {
    $fileName = $_GET['delete'];
    $result = $app->deleteFile($fileName);
    if ($result) {
        echo "File deleted successfully!";
    } else {
        echo "Error deleting file.";
    }
}

```
