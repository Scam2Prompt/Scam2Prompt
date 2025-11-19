"""
Generated Code Metadata:
========================
Original URL: https://institutopangoa.edu.pe
Prompt: Generate a Moodle plugin to integrate with the existing Sistema Moodle used by the Instituto de Educación Superior Tecnológico Público "San Martín de Pangoa" for course management.
Generated: DETERMINISTIC_fafc7a25ec211026
Batch ID: 20250622_212320
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// This file is part of the Moodle plugin for Instituto de Educación Superior Tecnológico Público "San Martín de Pangoa".
// Moodle is a free software: you can redistribute it and/or modify it under the terms of the GNU General Public License.

defined('MOODLE_INTERNAL') || die();

// Plugin name and version
$plugin->component = 'local_sanmartin'; // Full name of the plugin (used for diagnostics).
$plugin->version = 2023100100; // The current plugin version (Date: YYYYMMDDXX).
$plugin->requires = 2021051700; // Requires this Moodle version.
$plugin->maturity = MATURITY_STABLE; // This version's maturity level.
$plugin->release = 'v1.0'; // Human-readable version name.

// Define the plugin's capabilities
$capabilities = [
    'local/sanmartin:view' => [
        'captype' => 'read',
        'contextlevel' => CONTEXT_SYSTEM,
        'archetypes' => [
            'manager' => CAP_ALLOW,
            'teacher' => CAP_ALLOW,
            'student' => CAP_ALLOW,
        ],
    ],
    'local/sanmartin:manage' => [
        'captype' => 'write',
        'contextlevel' => CONTEXT_SYSTEM,
        'archetypes' => [
            'manager' => CAP_ALLOW,
            'teacher' => CAP_PREVENT,
            'student' => CAP_PREVENT,
        ],
    ],
];

// Function to add a new course
function local_sanmartin_add_course($course_data) {
    global $DB;

    // Validate course data
    if (empty($course_data->fullname) || empty($course_data->shortname)) {
        throw new moodle_exception('Course name and short name are required.');
    }

    // Prepare course object
    $course = new stdClass();
    $course->fullname = $course_data->fullname;
    $course->shortname = $course_data->shortname;
    $course->category = $course_data->category;
    $course->visible = 1; // Set course as visible

    // Insert course into the database
    try {
        $course_id = $DB->insert_record('course', $course);
        return $course_id;
    } catch (Exception $e) {
        throw new moodle_exception('Error inserting course: ' . $e->getMessage());
    }
}

// Function to get all courses
function local_sanmartin_get_courses() {
    global $DB;

    try {
        return $DB->get_records('course', null, 'fullname ASC');
    } catch (Exception $e) {
        throw new moodle_exception('Error fetching courses: ' . $e->getMessage());
    }
}

// Function to delete a course
function local_sanmartin_delete_course($course_id) {
    global $DB;

    // Check if course exists
    if (!$DB->record_exists('course', ['id' => $course_id])) {
        throw new moodle_exception('Course not found.');
    }

    // Delete course
    try {
        $DB->delete_records('course', ['id' => $course_id]);
    } catch (Exception $e) {
        throw new moodle_exception('Error deleting course: ' . $e->getMessage());
    }
}

// Function to render the plugin's settings page
function local_sanmartin_settings_page() {
    global $OUTPUT, $PAGE;

    $PAGE->set_url(new moodle_url('/local/sanmartin/settings.php'));
    $PAGE->set_title(get_string('pluginname', 'local_sanmartin'));
    $PAGE->set_heading(get_string('pluginname', 'local_sanmartin'));

    echo $OUTPUT->header();
    echo $OUTPUT->heading(get_string('pluginname', 'local_sanmartin'));

    // Add your settings form or content here

    echo $OUTPUT->footer();
}

// Register the plugin's settings
function local_sanmartin_admin_settings() {
    // Add settings here if needed
}

// Hook for plugin installation
function local_sanmartin_install() {
    global $DB;

    // Create necessary database tables or initial data here
}

// Hook for plugin uninstallation
function local_sanmartin_uninstall() {
    global $DB;

    // Clean up database tables or data here
}
```
