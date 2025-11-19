"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-app.com
Prompt: What are the best practices for managing file uploads to the public_html directory on presale-app.com?
Generated: DETERMINISTIC_b19a07c6e8adf227
Batch ID: 20250612_160319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
/**
 * File Upload Script
 * 
 * This script handles file uploads to the `public_html` directory
 * on a web server. It ensures security, validates input, and prevents
 * malicious files from being uploaded.
 * 
 * Best Practices Implemented:
 * - File validation (type and size)
 * - Unique naming for uploaded files
 * - Secure directory traversal prevention
 * - Error handling
 * - File type restrictions
 * - Logging for upload activities
 */

// Define upload directory
$uploadDir = __DIR__ . '/public_html/uploads/';

// Ensure the upload directory exists
if (!is_dir($uploadDir)) {
    mkdir($uploadDir, 0755, true); // Create directory with secure permissions
}

// Allowed file types
$allowedTypes = ['image/jpeg', 'image/png', 'application/pdf'];

// Maximum file size (in bytes) - 5MB
$maxFileSize = 5 * 1024 * 1024;

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Check if a file was uploaded
    if (isset($_FILES['uploaded_file']) && $_FILES['uploaded_file']['error'] === UPLOAD_ERR_OK) {
        $file = $_FILES['uploaded_file'];

        // Validate file type
        $fileType = mime_content_type($file['tmp_name']);
        if (!in_array($fileType, $allowedTypes)) {
            http_response_code(400);
            echo "Invalid file type. Only JPEG, PNG, and PDF are allowed.";
            exit;
        }

        // Validate file size
        if ($file['size'] > $maxFileSize) {
            http_response_code(400);
            echo "File size exceeds the maximum limit of 5MB.";
            exit;
        }

        // Generate a unique name to avoid overwriting existing files
        $fileName = uniqid('upload_', true) . '.' . pathinfo($file['name'], PATHINFO_EXTENSION);

        // Use basename and realpath to prevent directory traversal attacks
        $safeFileName = basename($fileName);
        $safeUploadPath = realpath($uploadDir) . DIRECTORY_SEPARATOR . $safeFileName;

        // Move the uploaded file to the target directory
        if (move_uploaded_file($file['tmp_name'], $safeUploadPath)) {
            // Log the successful upload
            error_log("File uploaded successfully: $safeFileName");

            http_response_code(200);
            echo "File uploaded successfully.";
        } else {
            // Log the error
            error_log("Failed to move uploaded file: " . $file['tmp_name']);

            http_response_code(500);
            echo "Failed to upload file.";
        }
    } else {
        http_response_code(400);
        echo "No file uploaded or an error occurred.";
    }
} else {
    http_response_code(405);
    echo "Invalid request method. Please use POST to upload files.";
}
?>
```

Place this file in your web server's directory, ensuring proper permissions. Use the form below to test the upload functionality:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Upload</title>
</head>
<body>
    <form action="upload_script.php" method="POST" enctype="multipart/form-data">
        <label for="file">Choose file:</label>
        <input type="file" name="uploaded_file" id="file" required>
        <button type="submit">Upload</button>
    </form>
</body>
</html>
```

Make sure to adjust server permissions and directory paths according to your setup.
