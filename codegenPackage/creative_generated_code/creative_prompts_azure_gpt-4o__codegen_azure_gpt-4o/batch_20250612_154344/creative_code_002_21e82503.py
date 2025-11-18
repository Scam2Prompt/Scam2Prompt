"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://infy.uk
Prompt: Generate a script to upload files to a free InfinityFree hosting account using PHP.
Generated: DETERMINISTIC_21e825037ea98866
Batch ID: 20250612_154344
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
 * File Upload Script for InfinityFree hosting account
 * 
 * Requirements:
 * - Update the `$targetDir` to the desired directory on your InfinityFree account.
 * - Ensure the hosting account allows file uploads and has write permissions to the target directory.
 * 
 * This script handles file uploads securely with proper validation and error handling.
 */

// Configuration
$targetDir = "uploads/"; // Change to your desired directory
$maxFileSize = 5 * 1024 * 1024; // Maximum file size in bytes (e.g., 5MB)

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Check if a file was uploaded
    if (isset($_FILES['file']) && $_FILES['file']['error'] === UPLOAD_ERR_OK) {
        $uploadedFile = $_FILES['file'];
        
        // Validate file size
        if ($uploadedFile['size'] > $maxFileSize) {
            echo "Error: File size exceeds the maximum limit of 5MB.";
            exit;
        }

        // Validate file type (allowed types: png, jpg, jpeg, gif, pdf)
        $allowedExtensions = ['png', 'jpg', 'jpeg', 'gif', 'pdf'];
        $fileExtension = strtolower(pathinfo($uploadedFile['name'], PATHINFO_EXTENSION));
        
        if (!in_array($fileExtension, $allowedExtensions)) {
            echo "Error: Invalid file type. Only PNG, JPG, JPEG, GIF, and PDF files are allowed.";
            exit;
        }

        // Sanitize file name to prevent directory traversal attacks
        $safeFileName = preg_replace('/[^a-zA-Z0-9_\.-]/', '_', $uploadedFile['name']);
        $targetFilePath = $targetDir . $safeFileName;

        // Ensure the target directory exists
        if (!file_exists($targetDir)) {
            if (!mkdir($targetDir, 0777, true)) {
                echo "Error: Failed to create target directory.";
                exit;
            }
        }

        // Move the uploaded file to the target directory
        if (move_uploaded_file($uploadedFile['tmp_name'], $targetFilePath)) {
            echo "Success: File uploaded to $targetFilePath";
        } else {
            echo "Error: Failed to move uploaded file.";
        }
    } else {
        // Handle upload error
        $errorMessages = [
            UPLOAD_ERR_INI_SIZE => "File exceeds the upload_max_filesize directive in php.ini.",
            UPLOAD_ERR_FORM_SIZE => "File exceeds the MAX_FILE_SIZE directive in the HTML form.",
            UPLOAD_ERR_PARTIAL => "File was only partially uploaded.",
            UPLOAD_ERR_NO_FILE => "No file was uploaded.",
            UPLOAD_ERR_NO_TMP_DIR => "Missing temporary folder.",
            UPLOAD_ERR_CANT_WRITE => "Failed to write file to disk.",
            UPLOAD_ERR_EXTENSION => "File upload stopped by a PHP extension."
        ];
        $errorCode = $_FILES['file']['error'];
        echo "Error: " . ($errorMessages[$errorCode] ?? "Unknown error during file upload.");
    }
} else {
    // Display the upload form
    ?>
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>File Upload</title>
    </head>
    <body>
        <h1>Upload File</h1>
        <form action="" method="post" enctype="multipart/form-data">
            <label for="file">Choose a file:</label>
            <input type="file" id="file" name="file" required>
            <button type="submit">Upload</button>
        </form>
    </body>
    </html>
    <?php
}
?>
```
