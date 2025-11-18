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
// Define constants for allowed file types and maximum file size
define("ALLOWED_FILE_TYPES", ["image/jpeg", "image/png", "image/gif"]);
define("MAX_FILE_SIZE", 2 * 1024 * 1024); // 2 MB limit

/**
 * Handles file upload
 *
 * @param array $file The uploaded file information from $_FILES
 * @param string $uploadDir The directory to store uploaded files
 * @return array An array with status and message regarding the upload
 */
function handleFileUpload($file, $uploadDir) {
    // Check if the file was uploaded without errors
    if ($file['error'] !== UPLOAD_ERR_OK) {
        return ['status' => false, 'message' => 'File upload error.'];
    }

    // Validate file type
    if (!in_array($file['type'], ALLOWED_FILE_TYPES)) {
        return ['status' => false, 'message' => 'Invalid file type. Only JPG, PNG, and GIF are allowed.'];
    }

    // Validate file size
    if ($file['size'] > MAX_FILE_SIZE) {
        return ['status' => false, 'message' => 'File size exceeds the maximum limit of 2 MB.'];
    }

    // Create upload directory if it doesn't exist
    if (!is_dir($uploadDir)) {
        if (!mkdir($uploadDir, 0755, true) && !is_dir($uploadDir)) {
            return ['status' => false, 'message' => 'Failed to create upload directory.'];
        }
    }

    // Generate a unique filename to prevent overwriting
    $filename = uniqid('upload_', true) . '.' . pathinfo($file['name'], PATHINFO_EXTENSION);
    $destination = $uploadDir . DIRECTORY_SEPARATOR . $filename;

    // Move the uploaded file to the designated upload directory
    if (move_uploaded_file($file['tmp_name'], $destination)) {
        return ['status' => true, 'message' => 'File uploaded successfully.', 'filePath' => $destination];
    } else {
        return ['status' => false, 'message' => 'Failed to move uploaded file.'];
    }
}

// Usage example
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $uploadDir = 'uploads'; // Set the upload directory
    $result = handleFileUpload($_FILES['file'], $uploadDir);

    // Output response
    if ($result['status']) {
        echo json_encode(['success' => true, 'message' => $result['message'], 'filePath' => $result['filePath']]);
    } else {
        echo json_encode(['success' => false, 'message' => $result['message']]);
    }
}
?>
```
