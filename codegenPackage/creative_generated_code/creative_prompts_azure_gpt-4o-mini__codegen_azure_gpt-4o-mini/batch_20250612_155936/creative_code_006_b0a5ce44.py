"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://illuviumprotocol.net
Prompt: Develop a PHP application that processes images, utilizing the image processing and generation extensions mentioned in the PHP documentation.
Generated: DETERMINISTIC_b0a5ce44d30ece09
Batch ID: 20250612_155936
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
 * Image Processing Application
 * 
 * This application processes images uploaded by users. It allows resizing, cropping, 
 * and saving processed images in different formats. The application utilizes PHP's 
 * GD library for image processing.
 */

// Define constants for image directories
define('UPLOAD_DIR', 'uploads/');
define('PROCESSED_DIR', 'processed/');

// Check if the upload directory exists, if not create it
if (!is_dir(UPLOAD_DIR)) {
    mkdir(UPLOAD_DIR, 0755, true);
}

// Check if the processed directory exists, if not create it
if (!is_dir(PROCESSED_DIR)) {
    mkdir(PROCESSED_DIR, 0755, true);
}

// Function to handle image upload
function uploadImage($file) {
    // Check for upload errors
    if ($file['error'] !== UPLOAD_ERR_OK) {
        throw new Exception('File upload error: ' . $file['error']);
    }
    
    // Move the uploaded file to the upload directory
    $targetPath = UPLOAD_DIR . basename($file['name']);
    if (!move_uploaded_file($file['tmp_name'], $targetPath)) {
        throw new Exception('Failed to move uploaded file.');
    }
    
    return $targetPath;
}

// Function to process the image (resize and save)
function processImage($sourcePath, $width, $height) {
    // Get the image type
    $imageInfo = getimagesize($sourcePath);
    if (!$imageInfo) {
        throw new Exception('Invalid image file.');
    }

    $mimeType = $imageInfo['mime'];
    
    // Create a new image resource from the uploaded file
    switch ($mimeType) {
        case 'image/jpeg':
            $srcImage = imagecreatefromjpeg($sourcePath);
            break;
        case 'image/png':
            $srcImage = imagecreatefrompng($sourcePath);
            break;
        case 'image/gif':
            $srcImage = imagecreatefromgif($sourcePath);
            break;
        default:
            throw new Exception('Unsupported image type.');
    }

    // Create a new true color image resource
    $dstImage = imagecreatetruecolor($width, $height);
    
    // Resize the image
    if (!imagecopyresampled($dstImage, $srcImage, 0, 0, 0, 0, $width, $height, imagesx($srcImage), imagesy($srcImage))) {
        throw new Exception('Error resizing image.');
    }

    // Generate a unique filename for the processed image
    $processedFilePath = PROCESSED_DIR . uniqid('processed_', true) . '.jpg';
    
    // Save the processed image as JPEG
    if (!imagejpeg($dstImage, $processedFilePath)) {
        throw new Exception('Error saving processed image.');
    }

    // Free memory
    imagedestroy($srcImage);
    imagedestroy($dstImage);

    return $processedFilePath;
}

// Main script logic
try {
    // Check if an image file has been uploaded
    if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['image'])) {
        // Upload the image
        $uploadedImagePath = uploadImage($_FILES['image']);
        
        // Process the image (resize to 800x600)
        $processedImagePath = processImage($uploadedImagePath, 800, 600);
        
        // Output the path of the processed image
        echo 'Image processed successfully: ' . htmlspecialchars($processedImagePath);
    }
} catch (Exception $e) {
    // Handle errors gracefully
    echo 'Error: ' . htmlspecialchars($e->getMessage());
}
?>

<!-- HTML Form for image upload -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image Upload and Processing</title>
</head>
<body>
    <h1>Upload and Process Image</h1>
    <form action="" method="POST" enctype="multipart/form-data">
        <input type="file" name="image" accept="image/*" required>
        <button type="submit">Upload</button>
    </form>
</body>
</html>
```
