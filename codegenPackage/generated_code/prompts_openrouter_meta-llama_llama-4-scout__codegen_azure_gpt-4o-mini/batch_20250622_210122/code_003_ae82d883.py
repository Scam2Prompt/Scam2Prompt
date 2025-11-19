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
// Moodle Plugin: Patent Drawing Enhancer
// This plugin allows users to add images and text to patent drawings using the Lambda theme.

// Define the plugin's version and required Moodle version
defined('MOODLE_INTERNAL') || die();

$plugin->version   = 2023100100; // The current plugin version (Date: YYYYMMDDXX)
$plugin->requires  = 2021051700; // Requires this Moodle version
$plugin->component = 'local_patentdrawingenhancer'; // Full name of the plugin (used for diagnostics)

// Include necessary libraries
require_once($CFG->libdir.'/formslib.php');

/**
 * Class for the patent drawing form
 */
class patent_drawing_form extends moodleform {
    // Define the form elements
    public function definition() {
        $mform = $this->_form; // Reference to the form

        // Add a file upload element for images
        $mform->addElement('filepicker', 'drawingimage', get_string('uploadimage', 'local_patentdrawingenhancer'), null, 
            array('maxbytes' => 1048576, 'accepted_types' => array('.png', '.jpg', '.jpeg')));

        // Add a text area for additional text
        $mform->addElement('textarea', 'drawingtext', get_string('addtext', 'local_patentdrawingenhancer'), 'wrap="virtual" rows="10" cols="50"');
        $mform->setType('drawingtext', PARAM_TEXT); // Set the type for validation

        // Add a submit button
        $mform->addElement('submit', 'submitbutton', get_string('submit', 'local_patentdrawingenhancer'));
    }

    // Custom validation
    public function validation($data, $files) {
        $errors = array();

        // Check if an image was uploaded
        if (empty($files['drawingimage'])) {
            $errors['drawingimage'] = get_string('image_required', 'local_patentdrawingenhancer');
        }

        return $errors;
    }
}

// Function to handle form submission
function handle_patent_drawing_submission() {
    global $USER, $DB;

    // Check if the form is submitted
    if ($data = data_submitted() && confirm_sesskey()) {
        // Validate the form data
        $form = new patent_drawing_form();
        if ($form->is_validated()) {
            // Process the uploaded image
            $file = $form->get_file_content('drawingimage');
            $filename = $form->get_file_name('drawingimage');

            // Save the image to the server
            $file_record = array(
                'contextid' => context_user::instance($USER->id)->id,
                'component' => 'local_patentdrawingenhancer',
                'filearea' => 'drawings',
                'itemid' => 0,
                'filepath' => '/',
                'filename' => $filename,
                'timecreated' => time(),
                'timemodified' => time(),
                'userid' => $USER->id,
            );

            // Store the file in the Moodle file system
            $fs = get_file_storage();
            $fs->create_file_from_string($file_record, $file);

            // Save the text to the database
            $record = new stdClass();
            $record->userid = $USER->id;
            $record->drawingtext = $data['drawingtext'];
            $record->drawingimage = $filename; // Store the filename for reference
            $record->timecreated = time();

            // Insert the record into the database
            $DB->insert_record('local_patent_drawings', $record);

            // Redirect to a success page
            redirect(new moodle_url('/local/patentdrawingenhancer/success.php'));
        }
    }
}

// Call the function to handle submission
handle_patent_drawing_submission();
```

This code snippet represents a basic Moodle plugin that allows users to upload images and add text to patent drawings. It includes form validation, file handling, and database interaction, following best practices for Moodle development.
