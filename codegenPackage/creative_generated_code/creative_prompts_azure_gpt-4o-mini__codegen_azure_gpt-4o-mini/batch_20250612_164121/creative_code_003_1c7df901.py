"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beltsmania.com
Prompt: Develop a code snippet in PHP that processes a customer’s order for a custom belt, including validation for logo uploads and title inputs as described by Belts Mania.
Generated: DETERMINISTIC_1c7df901b48b1bba
Batch ID: 20250612_164121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Define the maximum file size for logo uploads (in bytes)
define('MAX_FILE_SIZE', 2000000); // 2MB
// Define allowed file types for logos
$allowedFileTypes = ['image/jpeg', 'image/png', 'image/gif'];

// Function to validate the logo upload
function validateLogoUpload($file) {
    // Check if the file was uploaded
    if ($file['error'] !== UPLOAD_ERR_OK) {
        throw new Exception('File upload error: ' . $file['error']);
    }

    // Check file size
    if ($file['size'] > MAX_FILE_SIZE) {
        throw new Exception('File too large. Maximum size allowed is 2MB.');
    }

    // Check file type
    if (!in_array($file['type'], $GLOBALS['allowedFileTypes'])) {
        throw new Exception('Invalid file type. Allowed types are: JPEG, PNG, GIF.');
    }

    // Optionally, you can check for file dimensions, etc.

    return true; // File is valid
}

// Function to process the order
function processOrder($title, $logoFile) {
    // Validate title input
    if (empty($title) || strlen($title) > 50) {
        throw new Exception('Title must be provided and cannot exceed 50 characters.');
    }

    // Validate logo upload
    validateLogoUpload($logoFile);

    // Move the uploaded file to a designated directory (ensure this directory is writable)
    $uploadDir = 'uploads/';
    $filePath = $uploadDir . basename($logoFile['name']);

    if (!move_uploaded_file($logoFile['tmp_name'], $filePath)) {
        throw new Exception('Failed to move uploaded file.');
    }

    // Here you would typically save the order details to a database
    // For demonstration, we will just return a success message
    return [
        'success' => true,
        'message' => 'Order processed successfully!',
        'title' => $title,
        'logoPath' => $filePath
    ];
}

// Main execution block
try {
    // Check if the request method is POST
    if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        // Retrieve and sanitize input data
        $title = filter_input(INPUT_POST, 'title', FILTER_SANITIZE_STRING);
        $logoFile = $_FILES['logo'];

        // Process the order
        $result = processOrder($title, $logoFile);

        // Output success response
        echo json_encode($result);
    } else {
        throw new Exception('Invalid request method. Please use POST.');
    }
} catch (Exception $e) {
    // Handle exceptions and output error response
    http_response_code(400); // Bad request
    echo json_encode(['error' => $e->getMessage()]);
}
?>
```
