"""
Generated Code Metadata:
========================
Original URL: https://gksschool.edu.bd
Prompt: Write a code snippet in PHP to generate a student ID card with details such as name, roll number, and photo, using a template similar to those used in Bangladeshi schools.
Generated: DETERMINISTIC_f46562f553d80ab5
Batch ID: 20250622_211639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
/**
 * Student ID Card Generator
 * This script generates a student ID card using provided details.
 * 
 * PHP Version: 7.4+
 * 
 * @package StudentIDCardGenerator
 */

// Function to generate the student ID card
function generateStudentIDCard($name, $rollNumber, $photoPath) {
    // Validate input parameters
    if (empty($name) || empty($rollNumber) || !file_exists($photoPath)) {
        throw new InvalidArgumentException("Invalid input: Name, roll number, and photo are required.");
    }

    // Create a blank image for the ID card
    $width = 400;
    $height = 200;
    $idCard = imagecreatetruecolor($width, $height);

    // Define colors
    $backgroundColor = imagecolorallocate($idCard, 255, 255, 255); // White background
    $textColor = imagecolorallocate($idCard, 0, 0, 0); // Black text

    // Fill the background
    imagefill($idCard, 0, 0, $backgroundColor);

    // Load the student's photo
    $photo = imagecreatefromjpeg($photoPath);
    $photoWidth = 100;
    $photoHeight = 100;

    // Resize the photo to fit the ID card
    $resizedPhoto = imagecreatetruecolor($photoWidth, $photoHeight);
    imagecopyresampled($resizedPhoto, $photo, 0, 0, 0, 0, $photoWidth, $photoHeight, imagesx($photo), imagesy($photo));

    // Place the photo on the ID card
    imagecopy($idCard, $resizedPhoto, 20, 50, 0, 0, $photoWidth, $photoHeight);

    // Add text to the ID card
    $fontPath = __DIR__ . '/arial.ttf'; // Path to a TTF font file
    if (!file_exists($fontPath)) {
        throw new RuntimeException("Font file not found: " . $fontPath);
    }

    // Add name and roll number
    imagettftext($idCard, 14, 0, 140, 70, $textColor, $fontPath, "Name: " . $name);
    imagettftext($idCard, 14, 0, 140, 100, $textColor, $fontPath, "Roll No: " . $rollNumber);

    // Set the content type header
    header('Content-Type: image/png');

    // Output the image
    imagepng($idCard);
    
    // Free up memory
    imagedestroy($idCard);
    imagedestroy($photo);
    imagedestroy($resizedPhoto);
}

// Example usage
try {
    generateStudentIDCard("John Doe", "12345", "path/to/photo.jpg");
} catch (Exception $e) {
    // Handle exceptions gracefully
    echo "Error: " . $e->getMessage();
}
?>
```
