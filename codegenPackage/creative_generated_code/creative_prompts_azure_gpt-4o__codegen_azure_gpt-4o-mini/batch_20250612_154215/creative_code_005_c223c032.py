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
// Define constants for the upload directory and allowed file types
define('UPLOAD_DIR', 'uploads/');
define('ALLOWED_TYPES', ['application/pdf']);
define('MAX_FILE_SIZE', 2 * 1024 * 1024); // 2 MB

/**
 * Handle file uploads.
 */
function handleFileUpload()
{
    // Check if a file was uploaded
    if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['pdfFile'])) {
        // Validate the uploaded file
        $file = $_FILES['pdfFile'];
        return validateAndMoveFile($file);
    } else {
        // Return an error if no file was uploaded
        return ['success' => false, 'message' => 'No file uploaded.'];
    }
}

/**
 * Validate the uploaded file and move it to the upload directory.
 *
 * @param array $file The uploaded file information.
 * @return array Result of the operation.
 */
function validateAndMoveFile($file)
{
    // Check for upload errors
    if ($file['error'] !== UPLOAD_ERR_OK) {
        return ['success' => false, 'message' => 'File upload error.'];
    }

    // Validate file size
    if ($file['size'] > MAX_FILE_SIZE) {
        return ['success' => false, 'message' => 'File size exceeds the maximum limit.'];
    }

    // Validate file type
    if (!in_array($file['type'], ALLOWED_TYPES)) {
        return ['success' => false, 'message' => 'Invalid file type. Only PDF files are allowed.'];
    }

    // Create the upload directory if it doesn't exist
    if (!is_dir(UPLOAD_DIR)) {
        mkdir(UPLOAD_DIR, 0755, true);
    }

    // Generate a unique file name to prevent overwriting
    $fileName = uniqid('service_', true) . '.pdf';
    $destination = UPLOAD_DIR . basename($fileName);

    // Move the uploaded file to the designated directory
    if (move_uploaded_file($file['tmp_name'], $destination)) {
        return ['success' => true, 'message' => 'File uploaded successfully.', 'file' => $destination];
    } else {
        return ['success' => false, 'message' => 'Failed to move the uploaded file.'];
    }
}

// Process the file upload
$response = handleFileUpload();

// Return a JSON response to the client
header('Content-Type: application/json');
echo json_encode($response);
?>
```

### HTML Form Example
To test the PHP script, you can use the following HTML form:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Upload PDF</title>
</head>
<body>
    <h1>Upload PDF Description</h1>
    <form action="upload.php" method="post" enctype="multipart/form-data">
        <label for="pdfFile">Select a PDF file:</label>
        <input type="file" name="pdfFile" id="pdfFile" accept="application/pdf" required>
        <button type="submit">Upload</button>
    </form>
</body>
</html>
```

Save the PHP code in a file named `upload.php` and the HTML form in a separate file to test the upload functionality.
