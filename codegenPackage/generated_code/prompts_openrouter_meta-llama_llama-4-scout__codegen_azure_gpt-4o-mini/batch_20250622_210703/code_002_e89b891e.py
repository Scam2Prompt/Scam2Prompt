"""
Generated Code Metadata:
========================
Original URL: https://rokometni.agencijau3p.si
Prompt: Generate a code snippet in PHP to create a simple data room service for securely exchanging sensitive business documents, inspired by the "Data Room Services for High-Stakes Projects" article on the RK Kočevje website.
Generated: DETERMINISTIC_e89b891eaf273a08
Batch ID: 20250622_210703
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
 * Simple Data Room Service for Secure Document Exchange
 * 
 * This script provides a basic implementation of a data room service
 * for securely uploading and downloading sensitive business documents.
 * 
 * @package DataRoomService
 * @version 1.0
 */

// Define constants for file upload settings
define('UPLOAD_DIR', __DIR__ . '/uploads/');
define('MAX_FILE_SIZE', 10485760); // 10 MB
define('ALLOWED_FILE_TYPES', ['application/pdf', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document', 'application/msword']);

/**
 * Function to handle file uploads
 *
 * @param array $file The uploaded file information from $_FILES
 * @return string|false The path to the uploaded file or false on failure
 */
function uploadFile($file) {
    // Check for upload errors
    if ($file['error'] !== UPLOAD_ERR_OK) {
        return false;
    }

    // Validate file size
    if ($file['size'] > MAX_FILE_SIZE) {
        return false;
    }

    // Validate file type
    if (!in_array($file['type'], ALLOWED_FILE_TYPES)) {
        return false;
    }

    // Create upload directory if it doesn't exist
    if (!is_dir(UPLOAD_DIR)) {
        mkdir(UPLOAD_DIR, 0755, true);
    }

    // Generate a unique file name to prevent overwriting
    $fileName = uniqid('doc_', true) . '.' . pathinfo($file['name'], PATHINFO_EXTENSION);
    $destination = UPLOAD_DIR . $fileName;

    // Move the uploaded file to the designated directory
    if (move_uploaded_file($file['tmp_name'], $destination)) {
        return $destination;
    }

    return false;
}

/**
 * Function to download a file securely
 *
 * @param string $filePath The path to the file to be downloaded
 * @return void
 */
function downloadFile($filePath) {
    // Check if the file exists
    if (!file_exists($filePath)) {
        http_response_code(404);
        echo "File not found.";
        return;
    }

    // Set headers for file download
    header('Content-Description: File Transfer');
    header('Content-Type: application/octet-stream');
    header('Content-Disposition: attachment; filename="' . basename($filePath) . '"');
    header('Expires: 0');
    header('Cache-Control: must-revalidate');
    header('Pragma: public');
    header('Content-Length: ' . filesize($filePath));

    // Clear output buffer and read the file
    ob_clean();
    flush();
    readfile($filePath);
    exit;
}

// Example usage
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['document'])) {
    $uploadResult = uploadFile($_FILES['document']);
    if ($uploadResult) {
        echo "File uploaded successfully: " . htmlspecialchars($uploadResult);
    } else {
        echo "File upload failed. Please check the file size and type.";
    }
}

// Handle file download request
if (isset($_GET['file'])) {
    $filePath = UPLOAD_DIR . basename($_GET['file']);
    downloadFile($filePath);
}
?>
```

### Usage Instructions:
1. Save the code in a PHP file (e.g., `data_room_service.php`).
2. Create an HTML form to upload files and link to this script for handling uploads and downloads.
3. Ensure the server has write permissions to the `uploads` directory.
