"""
Generated Code Metadata:
========================
Original URL: https://learn.ipdrawingacademy.com
Prompt: "Design a system diagram using Moodle's Lambda theme and plugins, incorporating features like image handling and text addition in patent drawings."
Generated: DETERMINISTIC_ae82d88343b1b19c
Batch ID: 20250622_210122
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
 * System Diagram Generator for Moodle using Lambda Theme and Plugins
 * 
 * This script integrates Moodle's Lambda theme and plugins to create a system
 * for handling images and adding text annotations to patent drawings.
 * 
 * Requirements:
 * - Moodle installed with Lambda theme.
 * - Necessary plugins for image handling and text annotations.
 * 
 * Author: Expert Programmer
 * Date: YYYY-MM-DD
 */

// Ensure the script is being run within Moodle's context
defined('MOODLE_INTERNAL') || die();

// Include necessary Moodle libraries
require_once($CFG->libdir . '/filelib.php');
require_once($CFG->libdir . '/gdlib.php');

/**
 * Function to handle image uploads
 * 
 * @param int $contextid Context ID for the course/module
 * @param string $component Component name (e.g., 'mod_assign')
 * @param string $filearea File area name (e.g., 'submission_files')
 * @param int $itemid Item ID for the file
 * @param array $filedata File data from the form submission
 * @return stored_file|null Returns the stored file object or null on failure
 */
function handle_image_upload($contextid, $component, $filearea, $itemid, $filedata) {
    global $USER;

    // Prepare file storage
    $fs = get_file_storage();

    // Define file record
    $file_record = array(
        'contextid' => $contextid,
        'component' => $component,
        'filearea'  => $filearea,
        'itemid'    => $itemid,
        'filepath'  => '/',
        'filename'  => $filedata['name'],
        'userid'    => $USER->id
    );

    // Save the file
    try {
        $stored_file = $fs->create_file_from_pathname($file_record, $filedata['tmp_name']);
        return $stored_file;
    } catch (Exception $e) {
        debugging('Error uploading file: ' . $e->getMessage(), DEBUG_DEVELOPER);
        return null;
    }
}

/**
 * Function to add text annotations to an image
 * 
 * @param stored_file $image_file The image file object
 * @param string $text The text to add to the image
 * @param int $x X-coordinate for the text
 * @param int $y Y-coordinate for the text
 * @return bool Returns true on success, false on failure
 */
function add_text_to_image($image_file, $text, $x, $y) {
    // Get the file path
    $image_path = $image_file->get_content_file_location();

    // Load the image
    $image = imagecreatefromstring(file_get_contents($image_path));
    if (!$image) {
        debugging('Failed to load image.', DEBUG_DEVELOPER);
        return false;
    }

    // Define text color (black)
    $text_color = imagecolorallocate($image, 0, 0, 0);

    // Add the text to the image
    imagestring($image, 5, $x, $y, $text, $text_color);

    // Save the modified image
    try {
        imagepng($image, $image_path);
        imagedestroy($image);
        return true;
    } catch (Exception $e) {
        debugging('Error saving annotated image: ' . $e->getMessage(), DEBUG_DEVELOPER);
        return false;
    }
}

/**
 * Main function to generate the system diagram
 * 
 * @param int $contextid Context ID for the course/module
 * @param string $component Component name (e.g., 'mod_assign')
 * @param string $filearea File area name (e.g., 'submission_files')
 * @param int $itemid Item ID for the file
 * @param array $filedata File data from the form submission
 * @param string $text Text to annotate the image
 * @param int $x X-coordinate for the text
 * @param int $y Y-coordinate for the text
 * @return bool Returns true on success, false on failure
 */
function generate_system_diagram($contextid, $component, $filearea, $itemid, $filedata, $text, $x, $y) {
    // Handle image upload
    $image_file = handle_image_upload($contextid, $component, $filearea, $itemid, $filedata);
    if (!$image_file) {
        return false;
    }

    // Add text annotations to the image
    $result = add_text_to_image($image_file, $text, $x, $y);
    return $result;
}

// Example usage
// Note: Replace the following variables with actual values from your Moodle instance
$contextid = 1; // Example context ID
$component = 'mod_assign'; // Example component
$filearea = 'submission_files'; // Example file area
$itemid = 123; // Example item ID
$filedata = $_FILES['uploaded_file']; // Example file data from form submission
$text = 'Patent Drawing Annotation'; // Example text
$x = 50; // Example X-coordinate
$y = 100; // Example Y-coordinate

// Generate the system diagram
if (generate_system_diagram($contextid, $component, $filearea, $itemid, $filedata, $text, $x, $y)) {
    echo 'System diagram generated successfully.';
} else {
    echo 'Failed to generate system diagram.';
}
?>
```
