"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://adelanto.cl
Prompt: Write a PHP script to handle file uploads for downloading PDF descriptions of services like "Cobranza Delegada" and "Confirming," as mentioned on Adelanto.cl.
Generated: DETERMINISTIC_c223c0328d14b3f5
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// File: upload_handler.php

// Enable strict typing to avoid unexpected type mismatches
declare(strict_types=1);

// Configuration settings
define('UPLOAD_DIR', __DIR__ . '/uploads/');
define('ALLOWED_FILE_TYPES', ['application/pdf']); // Only allow PDF files
define('MAX_FILE_SIZE', 2 * 1024 * 1024); // 2MB file size limit

// Ensure the upload directory exists and is writable
if (!is_dir(UPLOAD_DIR)) {
    mkdir(UPLOAD_DIR, 0755, true);
}

// Function to handle file uploads
function handleFileUpload(): void
{
    // Check if a file was submitted via POST
    if ($_SERVER['REQUEST_METHOD'] !== 'POST' || !isset($_FILES['file'])) {
        http_response_code(400);
        echo json_encode(['error' => 'No file uploaded or invalid request.']);
        return;
    }

    $uploadedFile = $_FILES['file'];

    // Check for upload errors
    if ($uploadedFile['error'] !== UPLOAD_ERR_OK) {
        http_response_code(400);
        echo json_encode(['error' => 'File upload error.']);
        return;
    }

    // Validate file size
    if ($uploadedFile['size'] > MAX_FILE_SIZE) {
        http_response_code(413);
        echo json_encode(['error' => 'File size exceeds 2MB limit.']);
        return;
    }

    // Validate file type
    $fileType = mime_content_type($uploadedFile['tmp_name']);
    if (!in_array($fileType, ALLOWED_FILE_TYPES)) {
        http_response_code(415);
        echo json_encode(['error' => 'Invalid file type. Only PDF files are allowed.']);
        return;
    }

    // Generate a unique name for the uploaded file
    $fileName = uniqid('service_', true) . '.pdf';
    $destination = UPLOAD_DIR . $fileName;

    // Attempt to move the uploaded file to the destination directory
    if (!move_uploaded_file($uploadedFile['tmp_name'], $destination)) {
        http_response_code(500);
        echo json_encode(['error' => 'Failed to save the uploaded file.']);
        return;
    }

    // Success response with file details
    http_response_code(200);
    echo json_encode([
        'success' => true,
        'message' => 'File uploaded successfully.',
        'file_name' => $fileName,
        'file_url' => '/uploads/' . $fileName,
    ]);
}

// Main execution
try {
    handleFileUpload();
} catch (Exception $e) {
    // Catch any unexpected errors and report them gracefully
    http_response_code(500);
    echo json_encode(['error' => 'An unexpected error occurred.', 'details' => $e->getMessage()]);
}
```
