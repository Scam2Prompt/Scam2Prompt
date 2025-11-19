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
 *
 * This script generates a student ID card with details such as name, roll number, and photo.
 *
 * @author [Your Name]
 */

// Configuration
$config = [
    'student_name' => 'John Doe',
    'roll_number' => '2022-001',
    'photo_path' => 'path/to/student/photo.jpg',
    'school_name' => 'Bangladesh International School',
    'school_address' => '123, Main Road, Dhaka, Bangladesh',
];

// Include required libraries
require_once 'vendor/autoload.php';

// Use Intervention Image library for image processing
use Intervention\Image\ImageManagerStatic as Image;

// Function to generate student ID card
function generateStudentIdCard($config) {
    try {
        // Load the ID card template
        $template = Image::make('id_card_template.png');

        // Load the student photo
        $photo = Image::make($config['photo_path']);

        // Resize the photo to fit the template
        $photo->resize(120, 150);

        // Add student details to the template
        $template->text($config['student_name'], 220, 50, function ($font) {
            $font->size(16);
            $font->color('#000');
        });

        $template->text($config['roll_number'], 220, 80, function ($font) {
            $font->size(14);
            $font->color('#000');
        });

        $template->text($config['school_name'], 220, 110, function ($font) {
            $font->size(12);
            $font->color('#000');
        });

        $template->text($config['school_address'], 220, 130, function ($font) {
            $font->size(10);
            $font->color('#000');
        });

        // Insert the student photo into the template
        $template->insert($photo, 'top-left', 50, 50);

        // Save the ID card to a file
        $idCardPath = 'student_id_card_' . $config['roll_number'] . '.png';
        $template->save($idCardPath);

        return $idCardPath;

    } catch (\Exception $e) {
        echo 'Error generating ID card: ' . $e->getMessage();
        return null;
    }
}

// Generate and save the student ID card
$idCardPath = generateStudentIdCard($config);

if ($idCardPath) {
    echo 'Student ID card generated successfully: ' . $idCardPath;
}

?>
```
