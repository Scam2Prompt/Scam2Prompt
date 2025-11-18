"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yourpalmreading.com
Prompt: Write code in PHP to handle file uploads (e.g., hand images) and validate the file type and size before storing them, similar to the functionality described on YourPalmReading.com.
Generated: DETERMINISTIC_3d22ebe5cdb2664e
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Set allowed file types and maximum file size
define('ALLOWED_FILE_TYPES', ['image/jpeg', 'image/png', 'image/gif']);
define('MAX_FILE_SIZE', 5 * 1024 * 1024); // 5 MB

// Define the upload directory
define('UPLOAD_DIR', __DIR__ . '/uploads/');

// Ensure the upload directory exists
if (!is_dir(UPLOAD_DIR)) {
    if (!mkdir(UPLOAD_DIR, 0755, true)) {
        die("Failed to create upload directory.");
    }
}

// Function to handle file upload
function handleFileUpload($file)
{
    // Check if there was an upload error
    if ($file['error'] !== UPLOAD_ERR_OK) {
        return ['success' => false, 'error' => 'File upload error.'];
    }

    // Validate file type
    $fileType = mime_content_type($file['tmp_name']);
    if (!in_array($fileType, ALLOWED_FILE_TYPES)) {
        return ['success' => false, 'error' => 'Invalid file type. Only JPEG, PNG, and GIF are allowed.'];
    }

    // Validate file size
    if ($file['size'] > MAX_FILE_SIZE) {
        return ['success' => false, 'error' => 'File size exceeds the maximum allowed limit of 5 MB.'];
    }

    // Generate a unique filename to avoid overwriting
    $fileExtension = pathinfo($file['name'], PATHINFO_EXTENSION);
    $uniqueFileName = uniqid('upload_', true) . '.' . $fileExtension;

    // Move the file to the upload directory
    $destination = UPLOAD_DIR . $uniqueFileName;
    if (!move_uploaded_file($file['tmp_name'], $destination)) {
        return ['success' => false, 'error' => 'Failed to move uploaded file.'];
    }

    // Return success response
    return ['success' => true, 'filePath' => $destination];
}

// Check if a file was submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['file'])) {
    $uploadResult = handleFileUpload($_FILES['file']);

    // Respond accordingly
    if ($uploadResult['success']) {
        echo "File uploaded successfully! File path: " . htmlspecialchars($uploadResult['filePath']);
    } else {
        echo "File upload failed: " . htmlspecialchars($uploadResult['error']);
    }
} else {
    // Display a basic HTML form for file upload
    echo '<form method="POST" enctype="multipart/form-data">';
    echo '<label for="file">Upload an image:</label>';
    echo '<input type="file" name="file" id="file" required>';
    echo '<button type="submit">Upload</button>';
    echo '</form>';
}
?>
```
