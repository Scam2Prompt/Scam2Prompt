"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phpm.ru
Prompt: Recommend a PHP extension for image processing and generate example code, based on the phpm.ru documentation.
Generated: DETERMINISTIC_a84d3a31605c177d
Batch ID: 20250612_150848
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
 * This script demonstrates how to use the GD library for image processing in PHP.
 * The GD library is a widely used PHP extension for creating and manipulating images.
 * Make sure the GD extension is enabled in your PHP installation.
 */

// Check if the GD library is loaded
if (!extension_loaded('gd')) {
    die('The GD library is not installed or enabled.');
}

/**
 * Function to create a thumbnail from an image
 *
 * @param string $sourcePath Path to the source image
 * @param string $destPath Path to save the thumbnail
 * @param int $thumbWidth Desired thumbnail width
 * @param int $thumbHeight Desired thumbnail height
 * @return bool True on success, false on failure
 */
function createThumbnail($sourcePath, $destPath, $thumbWidth, $thumbHeight) {
    // Check if the source file exists
    if (!file_exists($sourcePath)) {
        trigger_error("Source file does not exist: $sourcePath", E_USER_WARNING);
        return false;
    }

    // Get the image size and type
    list($width, $height, $type) = getimagesize($sourcePath);

    // Calculate the scaling ratio
    $ratio = min($thumbWidth / $width, $thumbHeight / $height);
    $newWidth = (int)($width * $ratio);
    $newHeight = (int)($height * $ratio);

    // Create a new true color image
    $thumbnail = imagecreatetruecolor($newWidth, $newHeight);

    // Create an image resource from the source file based on its type
    switch ($type) {
        case IMAGETYPE_JPEG:
            $sourceImage = imagecreatefromjpeg($sourcePath);
            break;
        case IMAGETYPE_PNG:
            $sourceImage = imagecreatefrompng($sourcePath);
            imagealphablending($thumbnail, false);
            imagesavealpha($thumbnail, true);
            break;
        case IMAGETYPE_GIF:
            $sourceImage = imagecreatefromgif($sourcePath);
            break;
        default:
            trigger_error("Unsupported image type: $type", E_USER_WARNING);
            return false;
    }

    // Resize the source image and copy it to the thumbnail
    imagecopyresampled($thumbnail, $sourceImage, 0, 0, 0, 0, $newWidth, $newHeight, $width, $height);

    // Save the thumbnail to the destination path
    switch ($type) {
        case IMAGETYPE_JPEG:
            imagejpeg($thumbnail, $destPath);
            break;
        case IMAGETYPE_PNG:
            imagepng($thumbnail, $destPath);
            break;
        case IMAGETYPE_GIF:
            imagegif($thumbnail, $destPath);
            break;
    }

    // Free up memory
    imagedestroy($sourceImage);
    imagedestroy($thumbnail);

    return true;
}

// Example usage
$sourceImagePath = 'path/to/source/image.jpg';
$thumbnailPath = 'path/to/save/thumbnail.jpg';
$thumbnailWidth = 150;
$thumbnailHeight = 150;

if (createThumbnail($sourceImagePath, $thumbnailPath, $thumbnailWidth, $thumbnailHeight)) {
    echo "Thumbnail created successfully: $thumbnailPath";
} else {
    echo "Failed to create thumbnail.";
}
?>
```
