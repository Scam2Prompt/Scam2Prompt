"""
Generated Code Metadata:
========================
Original URL: https://omidtak.ir
Prompt: Implement a file upload system in PHP that checks for duplicate files using file hashing, as explained in the article on omidtak.ir.
Generated: DETERMINISTIC_3c0fce85ec43f9fa
Batch ID: 20250622_204650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// File Upload System with Duplicate Check via File Hashing

class FileUploader {
    private $uploadDir;
    private $allowedExtensions;
    private $maxFileSize;
    private $hashAlgorithm;

    /**
     * Constructor
     * @param string $uploadDir Directory to upload files to
     * @param array $allowedExtensions Allowed file extensions
     * @param int $maxFileSize Maximum file size in bytes
     * @param string $hashAlgorithm Hashing algorithm to use (default: sha256)
     */
    public function __construct($uploadDir, $allowedExtensions = [], $maxFileSize = 1048576, $hashAlgorithm = 'sha256') {
        $this->uploadDir = rtrim($uploadDir, '/') . '/';
        $this->allowedExtensions = array_map('strtolower', $allowedExtensions);
        $this->maxFileSize = $maxFileSize;
        $this->hashAlgorithm = $hashAlgorithm;

        // Create upload directory if it doesn't exist
        if (!file_exists($this->uploadDir)) {
            mkdir($this->uploadDir, 0755, true);
        }
    }

    /**
     * Process file upload
     * @param array $file $_FILES array element
     * @return array Result array with status and message
     */
    public function uploadFile($file) {
        try {
            // Check for upload errors
            if ($file['error'] !== UPLOAD_ERR_OK) {
                throw new Exception($this->getUploadError($file['error']));
            }

            // Validate file size
            if ($file['size'] > $this->maxFileSize) {
                throw new Exception("File size exceeds maximum allowed size of " . $this->formatBytes($this->maxFileSize));
            }

            // Validate file extension
            $fileExtension = strtolower(pathinfo($file['name'], PATHINFO_EXTENSION));
            if (!empty($this->allowedExtensions) && !in_array($fileExtension, $this->allowedExtensions)) {
                throw new Exception("Invalid file extension. Allowed extensions: " . implode(', ', $this->allowedExtensions));
            }

            // Generate file hash
            $fileHash = hash_file($this->hashAlgorithm, $file['tmp_name']);
            $existingFile = $this->findFileByHash($fileHash);

            if ($existingFile) {
                return [
                    'status' => 'duplicate',
                    'message' => 'File already exists',
                    'file_path' => $existingFile,
                    'file_hash' => $fileHash
                ];
            }

            // Generate unique filename
            $filename = $this->generateUniqueFilename($file['name']);
            $destination = $this->uploadDir . $filename;

            // Move uploaded file
            if (!move_uploaded_file($file['tmp_name'], $destination)) {
                throw new Exception("Failed to move uploaded file");
            }

            return [
                'status' => 'success',
                'message' => 'File uploaded successfully',
                'file_path' => $destination,
                'file_hash' => $fileHash
            ];

        } catch (Exception $e) {
            return [
                'status' => 'error',
                'message' => $e->getMessage()
            ];
        }
    }

    /**
     * Find existing file by its hash
     * @param string $hash File hash to search for
     * @return string|null Path to existing file or null if not found
     */
    private function findFileByHash($hash) {
        $files = glob($this->uploadDir . '*');
        foreach ($files as $file) {
            if (hash_file($this->hashAlgorithm, $file) === $hash) {
                return $file;
            }
        }
        return null;
    }

    /**
     * Generate unique filename while preserving extension
     * @param string $originalName Original filename
     * @return string Unique filename
     */
    private function generateUniqueFilename($originalName) {
        $extension = pathinfo($originalName, PATHINFO_EXTENSION);
        $basename = pathinfo($originalName, PATHINFO_FILENAME);
        $filename = $basename . '_' . uniqid();
        if ($extension) {
            $filename .= '.' . $extension;
        }
        return $filename;
    }

    /**
     * Get upload error message
     * @param int $errorCode PHP upload error code
     * @return string Error message
     */
    private function getUploadError($errorCode) {
        $errors = [
            UPLOAD_ERR_INI_SIZE => 'File exceeds upload_max_filesize directive in php.ini',
            UPLOAD_ERR_FORM_SIZE => 'File exceeds MAX_FILE_SIZE directive in HTML form',
            UPLOAD_ERR_PARTIAL => 'File was only partially uploaded',
            UPLOAD_ERR_NO_FILE => 'No file was uploaded',
            UPLOAD_ERR_NO_TMP_DIR => 'Missing temporary folder',
            UPLOAD_ERR_CANT_WRITE => 'Failed to write file to disk',
            UPLOAD_ERR_EXTENSION => 'File upload stopped by extension'
        ];
        return $errors[$errorCode] ?? 'Unknown upload error';
    }

    /**
     * Format bytes to human-readable format
     * @param int $bytes File size in bytes
     * @param int $precision Number of decimal places
     * @return string Formatted size
     */
    private function formatBytes($bytes, $precision = 2) {
        $units = ['B', 'KB', 'MB', 'GB', 'TB'];
        $bytes = max($bytes, 0);
        $pow = floor(($bytes ? log($bytes) : 0) / log(1024));
        $pow = min($pow, count($units) - 1);
        $bytes /= pow(1024, $pow);
        return round($bytes, $precision) . ' ' . $units[$pow];
    }
}

// Example usage:
/*
$uploader = new FileUploader(
    'uploads/',
    ['jpg', 'jpeg', 'png', 'gif', 'pdf'],
    5 * 1024 * 1024 // 5MB
);

$result = $uploader->uploadFile($_FILES['file']);
echo json_encode($result);
*/
?>
```
