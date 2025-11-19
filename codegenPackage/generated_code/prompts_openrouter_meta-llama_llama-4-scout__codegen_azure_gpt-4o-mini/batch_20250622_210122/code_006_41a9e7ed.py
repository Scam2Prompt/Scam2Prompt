"""
Generated Code Metadata:
========================
Original URL: https://learn.ipdrawingacademy.com
Prompt: "Write a script to automate the process of creating and managing patent drawing courses on a Moodle site using Lambda theme and plugins."
Generated: DETERMINISTIC_41a9e7ede17aac43
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
// Moodle Course Automation Script
// This script automates the creation and management of patent drawing courses on a Moodle site using the Lambda theme and relevant plugins.

// Include necessary Moodle configuration and libraries
require_once(__DIR__ . '/config.php');
require_once($CFG->libdir . '/courselib.php');
require_once($CFG->libdir . '/filelib.php');

// Function to create a new course
function create_course($course_data) {
    global $DB;

    // Validate course data
    if (empty($course_data['fullname']) || empty($course_data['shortname'])) {
        throw new Exception('Course fullname and shortname are required.');
    }

    // Prepare course object
    $course = new stdClass();
    $course->fullname = $course_data['fullname'];
    $course->shortname = $course_data['shortname'];
    $course->category = $course_data['category'];
    $course->format = 'topics'; // Set course format
    $course->visible = 1; // Make course visible
    $course->startdate = time(); // Set start date to now
    $course->enddate = strtotime('+6 months'); // Set end date to 6 months from now

    // Create the course
    $course_id = create_course($course);
    return $course_id;
}

// Function to add a module to the course
function add_module_to_course($course_id, $module_data) {
    global $DB;

    // Validate module data
    if (empty($module_data['name']) || empty($module_data['modtype'])) {
        throw new Exception('Module name and type are required.');
    }

    // Prepare module object
    $module = new stdClass();
    $module->course = $course_id;
    $module->name = $module_data['name'];
    $module->modtype = $module_data['modtype'];
    $module->instance = $module_data['instance'];
    $module->visible = 1; // Make module visible

    // Add the module to the course
    $module_id = add_module($module);
    return $module_id;
}

// Main script execution
try {
    // Example course data
    $course_data = [
        'fullname' => 'Patent Drawing Course',
        'shortname' => 'PDC101',
        'category' => 1 // Assuming category ID 1 exists
    ];

    // Create the course
    $course_id = create_course($course_data);
    echo "Course created with ID: $course_id\n";

    // Example module data
    $module_data = [
        'name' => 'Introduction to Patent Drawing',
        'modtype' => 'resource', // Example module type
        'instance' => 1 // Assuming instance ID 1 exists
    ];

    // Add a module to the course
    $module_id = add_module_to_course($course_id, $module_data);
    echo "Module added with ID: $module_id\n";

} catch (Exception $e) {
    // Handle errors gracefully
    echo 'Error: ' . $e->getMessage() . "\n";
}
?>
```
