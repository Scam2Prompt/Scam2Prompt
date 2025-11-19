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
 * This application allows basic image resizing and watermarking using PHP's GD extension.
 * Ensure the GD extension is enabled in your PHP configuration to run this script.
 */

// Define constants for file paths and watermark text
define('INPUT_IMAGE', 'input.jpg');       // Path to the input image
define('OUTPUT_IMAGE', 'output.jpg');    // Path to the processed image
define('WATERMARK_TEXT', 'Sample Watermark'); // Watermark text
define('FONT_SIZE', 20);                 // Font size for the watermark
define('FONT_PATH', './arial.ttf');      // Path to the true type font for watermarking

/**
 * Main function to handle image processing.
 */
function processImage() {
    try {
        // Load the input image
        $image = loadImage(INPUT_IMAGE);
        if ($image === false) {
            throw new Exception('Failed to load input image.');
        }

        // Resize the image
        $resizedImage = resizeImage($image, 500, 500); // Resize to 500x500 pixels
        imagedestroy($image); // Free memory for the original image

        // Add watermark to the resized image
        addWatermark($resizedImage, WATERMARK_TEXT);

        // Save the processed image
        saveImage($resizedImage, OUTPUT_IMAGE);
        imagedestroy($resizedImage); // Free memory for the resized image

        echo "Image processing completed successfully. Output saved to " . OUTPUT_IMAGE;
    } catch (Exception $e) {
        // Handle any errors
        echo "Error: " . $e->getMessage();
    }
}

/**
 * Load an image from a file.
 *
 * @param string $filePath Path to the image file.
 * @return resource|false GD image resource on success, false on failure.
 */
function loadImage(string $filePath) {
    $imageInfo = getimagesize($filePath);
    if ($imageInfo === false) {
        return false;
    }

    switch ($imageInfo['mime']) {
        case 'image/jpeg':
            return imagecreatefromjpeg($filePath);
        case 'image/png':
            return imagecreatefrompng($filePath);
        case 'image/gif':
            return imagecreatefromgif($filePath);
        default:
            return false;
    }
}

/**
 * Resize an image to specified dimensions.
 *
 * @param resource $image GD image resource.
 * @param int $newWidth Desired width of the resized image.
 * @param int $newHeight Desired height of the resized image.
 * @return resource Resized image resource.
 */
function resizeImage($image, int $newWidth, int $newHeight) {
    $width = imagesx($image);
    $height = imagesy($image);

    $resizedImage = imagecreatetruecolor($newWidth, $newHeight);

    // Preserve transparency for PNG and GIF images
    $imageInfo = getimagesize(INPUT_IMAGE);
    if ($imageInfo['mime'] === 'image/png' || $imageInfo['mime'] === 'image/gif') {
        imagealphablending($resizedImage, false);
        imagesavealpha($resizedImage, true);
    }

    imagecopyresampled($resizedImage, $image, 0, 0, 0, 0, $newWidth, $newHeight, $width, $height);
    return $resizedImage;
}

/**
 * Add a watermark to the image.
 *
 * @param resource $image GD image resource.
 * @param string $text Watermark text.
 * @return void
 */
function addWatermark($image, string $text) {
    $width = imagesx($image);
    $height = imagesy($image);

    $fontColor = imagecolorallocatealpha($image, 255, 255, 255, 50); // White color with transparency
    $x = $width - 250; // Position the watermark near the bottom-right corner
    $y = $height - 50;

    imagettftext($image, FONT_SIZE, 0, $x, $y, $fontColor, FONT_PATH, $text);
}

/**
 * Save the processed image to a file.
 *
 * @param resource $image GD image resource.
 * @param string $filePath Path to save the image.
 * @return void
 */
function saveImage($image, string $filePath) {
    $imageInfo = getimagesize(INPUT_IMAGE);

    switch ($imageInfo['mime']) {
        case 'image/jpeg':
            imagejpeg($image, $filePath, 90); // Save JPEG with quality 90
            break;
        case 'image/png':
            imagepng($image, $filePath);
            break;
        case 'image/gif':
            imagegif($image, $filePath);
            break;
        default:
            throw new Exception('Unsupported image format.');
    }
}

// Execute the image processing
processImage();
?>
```
