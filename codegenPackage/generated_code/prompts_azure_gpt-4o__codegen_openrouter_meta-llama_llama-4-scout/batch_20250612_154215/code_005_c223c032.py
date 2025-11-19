"""
Generated Code Metadata:
========================
Original URL: https://adelanto.cl
Prompt: Write a PHP script to handle file uploads for downloading PDF descriptions of services like "Cobranza Delegada" and "Confirming," as mentioned on Adelanto.cl.
Generated: DETERMINISTIC_c223c0328d14b3f5
Batch ID: 20250612_154215
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
 * File Upload Handler for Service Descriptions
 *
 * Handles file uploads for downloading PDF descriptions of services.
 */

// Configuration
$UPLOAD_DIR = 'uploads/';
$ALLOWED_MIME_TYPES = ['application/pdf'];
$MAX_FILE_SIZE = 10 * 1024 * 1024; // 10MB

// Initialize error messages
$errorMessages = [];

/**
 * Handles file upload
 *
 * @param array $file File upload data
 * @return array
 */
function handleFileUpload($file)
{
    global $UPLOAD_DIR, $ALLOWED_MIME_TYPES, $MAX_FILE_SIZE, $errorMessages;

    // Check if file was uploaded without errors
    if ($file['error'] !== UPLOAD_ERR_OK) {
        $errorMessages[] = 'Error uploading file: ' . getUploadErrorMessage($file['error']);
        return ['success' => false, 'errorMessages' => $errorMessages];
    }

    // Check file type
    $finfo = finfo_open(FILEINFO_MIME_TYPE);
    $mimeType = finfo_file($finfo, $file['tmp_name']);
    finfo_close($finfo);

    if (!in_array($mimeType, $ALLOWED_MIME_TYPES)) {
        $errorMessages[] = 'Invalid file type. Only PDF files are allowed.';
        return ['success' => false, 'errorMessages' => $errorMessages];
    }

    // Check file size
    if ($file['size'] > $MAX_FILE_SIZE) {
        $errorMessages[] = 'File size exceeds the maximum allowed size of 10MB.';
        return ['success' => false, 'errorMessages' => $errorMessages];
    }

    // Create upload directory if it doesn't exist
    if (!is_dir($UPLOAD_DIR)) {
        mkdir($UPLOAD_DIR, 0755, true);
    }

    // Generate unique filename
    $filename = uniqid() . '.pdf';
    $uploadFile = $UPLOAD_DIR . $filename;

    // Move uploaded file to upload directory
    if (!move_uploaded_file($file['tmp_name'], $uploadFile)) {
        $errorMessages[] = 'Error moving uploaded file.';
        return ['success' => false, 'errorMessages' => $errorMessages];
    }

    return ['success' => true, 'filename' => $filename];
}

/**
 * Gets error message for upload error code
 *
 * @param int $errorCode Upload error code
 * @return string
 */
function getUploadErrorMessage($errorCode)
{
    switch ($errorCode) {
        case UPLOAD_ERR_INI_SIZE:
            return 'The uploaded file exceeds the maximum upload size allowed by the server.';
        case UPLOAD_ERR_FORM_SIZE:
            return 'The uploaded file exceeds the maximum upload size allowed by the form.';
        case UPLOAD_ERR_PARTIAL:
            return 'The uploaded file was only partially uploaded.';
        case UPLOAD_ERR_NO_FILE:
            return 'No file was uploaded.';
        case UPLOAD_ERR_NO_TMP_DIR:
            return 'Missing a temporary folder.';
        case UPLOAD_ERR_CANT_WRITE:
            return 'Failed to write file to disk.';
        case UPLOAD_ERR_EXTENSION:
            return 'A PHP extension stopped the file upload.';
        default:
            return 'Unknown upload error.';
    }
}

// Example usage
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_FILES['file'])) {
        $result = handleFileUpload($_FILES['file']);
        if ($result['success']) {
            http_response_code(201);
            echo json_encode(['message' => 'File uploaded successfully.', 'filename' => $result['filename']]);
        } else {
            http_response_code(400);
            echo json_encode(['message' => 'Error uploading file.', 'errorMessages' => $result['errorMessages']]);
        }
    } else {
        http_response_code(400);
        echo json_encode(['message' => 'No file provided.']);
    }
} else {
    http_response_code(405);
    echo json_encode(['message' => 'Method not allowed.']);
}
```
