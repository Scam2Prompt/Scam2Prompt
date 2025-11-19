"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://learn.ipdrawingacademy.com
Prompt: How can I utilize the built-in components of the Lambda theme to enhance my online courses in Moodle?
Generated: DETERMINISTIC_e4a8ab42a4983ba7
Batch ID: 20250612_140300
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// This script demonstrates how to utilize the built-in components of the Lambda theme
// to enhance online courses in Moodle. Replace placeholders like COURSE_ID with
// appropriate values for your Moodle instance.

// Include necessary Moodle libraries
require_once(__DIR__ . '/../../config.php');
require_login(); // Ensure user is logged in

// Get course ID from URL parameters
$courseid = required_param('id', PARAM_INT);

// Validate that the course exists
$course = get_course($courseid);
if (!$course) {
    throw new moodle_exception('invalidcourse', 'error', '', $courseid);
}

// Ensure Lambda theme is active
$theme = theme_get_theme();
if ($theme !== 'lambda') {
    throw new moodle_exception('themerequired', 'error', '', 'Lambda theme is not active');
}

// Set page context and URL
$context = context_course::instance($courseid);
$PAGE->set_context($context);
$PAGE->set_url('/course/view.php', ['id' => $courseid]);
$PAGE->set_pagelayout('course'); // Use 'course' layout for styling compatibility

// Define page title and heading
$PAGE->set_title(format_string($course->fullname));
$PAGE->set_heading(format_string($course->fullname));

// Output starts here
echo $OUTPUT->header();

// Lambda theme provides customizable course banners, we will display one
if (theme_lambda_course_banner_enabled()) {
    echo theme_lambda_render_course_banner($courseid);
}

// Lambda also provides custom course summary boxes
echo '<div class="lambda-course-summary">';
echo format_text($course->summary, FORMAT_HTML);
// Add additional course information if needed
echo '<p>Enrolled Users: ' . count_enrolled_users($context) . '</p>';
echo '<p>Start Date: ' . userdate($course->startdate) . '</p>';
echo '</div>';

// Demonstrate Lambda's collapsible sections for organizing course materials
$sections = get_fast_modinfo($course)->get_section_info_all();
echo '<div class="lambda-collapsible-sections">';
foreach ($sections as $section) {
    if ($section->section > 0 && $section->uservisible) { // Skip section 0 (general section)
        echo '<div class="lambda-section">';
        echo '<h3 class="lambda-section-title">' . format_string($section->name) . '</h3>';
        echo '<div class="lambda-section-content">' . $section->summary . '</div>';
        echo '</div>';
    }
}
echo '</div>';

// Output ends here
echo $OUTPUT->footer();
```
