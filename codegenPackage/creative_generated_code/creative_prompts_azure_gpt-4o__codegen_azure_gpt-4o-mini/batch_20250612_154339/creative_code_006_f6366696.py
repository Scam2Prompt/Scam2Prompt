"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://illuviumprotocol.net
Prompt: Recommend PHP extensions for image processing and generate code to resize and watermark an image using one of them.
Generated: DETERMINISTIC_f636669639f04b8b
Batch ID: 20250612_154339
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
 * Image Processing Script
 * This script resizes and watermarks an image using the GD library.
 */

// Function to resize an image to the specified dimensions
function resizeImage($sourcePath, $destinationPath, $newWidth, $newHeight) {
    // Check if the source image exists
    if (!file_exists($sourcePath)) {
        throw new Exception("Source image does not exist: {$sourcePath}");
    }

    // Get the image dimensions and type
    list($width, $height, $type) = getimagesize($sourcePath);

    // Create a new true color image with the specified dimensions
    $resizedImage = imagecreatetruecolor($newWidth, $newHeight);

    // Load the source image based on its type
    switch ($type) {
        case IMAGETYPE_JPEG:
            $sourceImage = imagecreatefromjpeg($sourcePath);
            break;
        case IMAGETYPE_PNG:
            $sourceImage = imagecreatefrompng($sourcePath);
            break;
        case IMAGETYPE_GIF:
            $sourceImage = imagecreatefromgif($sourcePath);
            break;
        default:
            throw new Exception("Unsupported image type: {$type}");
    }

    // Resize the image
    imagecopyresampled($resizedImage, $sourceImage, 0, 0, 0, 0, $newWidth, $newHeight, $width, $height);

    // Save the resized image to the destination path
    switch ($type) {
        case IMAGETYPE_JPEG:
            imagejpeg($resizedImage, $destinationPath);
            break;
        case IMAGETYPE_PNG:
            imagepng($resizedImage, $destinationPath);
            break;
        case IMAGETYPE_GIF:
            imagegif($resizedImage, $destinationPath);
            break;
    }

    // Free memory
    imagedestroy($sourceImage);
    imagedestroy($resizedImage);
}

/**
 * Function to watermark an image
 * 
 * @param string $imagePath Path to the image file
 * @param string $watermarkPath Path to the watermark image file
 * @param string $outputPath Path to save the watermarked image
 * @param int $opacity Opacity level for the watermark (0-100)
 */
function watermarkImage($imagePath, $watermarkPath, $outputPath, $opacity = 50) {
    // Check if the image and watermark exist
    if (!file_exists($imagePath) || !file_exists($watermarkPath)) {
        throw new Exception("Image or watermark file does not exist.");
    }

    // Load the main image
    $image = imagecreatefromstring(file_get_contents($imagePath));
    $watermark = imagecreatefromstring(file_get_contents($watermarkPath));

    // Get dimensions
    $imageWidth = imagesx($image);
    $imageHeight = imagesy($image);
    $watermarkWidth = imagesx($watermark);
    $watermarkHeight = imagesy($watermark);

    // Position the watermark in the bottom-right corner
    $destX = $imageWidth - $watermarkWidth - 10;
    $destY = $imageHeight - $watermarkHeight - 10;

    // Merge the watermark with the image
    imagecopymerge($image, $watermark, $destX, $destY, 0, 0, $watermarkWidth, $watermarkHeight, $opacity);

    // Save the watermarked image
    imagejpeg($image, $outputPath);

    // Free memory
    imagedestroy($image);
    imagedestroy($watermark);
}

// Sample usage
try {
    // Resize the image to 800x600
    resizeImage('path/to/source/image.jpg', 'path/to/resized/image.jpg', 800, 600);

    // Add watermark to the resized image
    watermarkImage('path/to/resized/image.jpg', 'path/to/watermark.png', 'path/to/watermarked/image.jpg', 50);

    echo "Image processing completed successfully.";
} catch (Exception $e) {
    // Log error message
    error_log($e->getMessage());
    echo "An error occurred: " . $e->getMessage();
}
?>
```
