"""
Generated Code Metadata:
========================
Original URL: https://learn.ipdrawingacademy.com
Prompt: How can I utilize the built-in components of the Lambda theme to enhance my online courses in Moodle?
Generated: DETERMINISTIC_e4a8ab42a4983ba7
Batch ID: 20250612_140300
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// This script demonstrates how to utilize the built-in components of the Lambda theme
// to enhance online courses in Moodle. It assumes the Lambda theme is installed and active.

// Include necessary Moodle configuration and libraries
require_once(__DIR__ . '/../../config.php');

// Ensure the user is logged in and has the required permissions
require_login();
$context = context_system::instance();
require_capability('moodle/course:view', $context);

// Define the course ID (replace with your course ID)
$courseid = required_param('courseid', PARAM_INT);

// Fetch the course details
$course = get_course($courseid);
if (!$course) {
    throw new moodle_exception('invalidcourseid', 'error');
}

// Set up the page context
$PAGE->set_url('/course/view.php', array('id' => $courseid));
$PAGE->set_context(context_course::instance($courseid));
$PAGE->set_title($course->fullname);
$PAGE->set_heading($course->fullname);
$PAGE->set_pagelayout('course'); // Use the Lambda theme's course layout

// Start output
echo $OUTPUT->header();

// Example: Add a Lambda theme custom banner to the course page
// Lambda theme supports custom banners via its settings
$bannerimage = theme_lambda_get_setting('bannerimage');
if ($bannerimage) {
    echo html_writer::div(
        html_writer::img($bannerimage, get_string('coursebanner', 'theme_lambda')),
        'lambda-course-banner'
    );
}

// Example: Add a Lambda theme custom call-to-action button
$cta_text = theme_lambda_get_setting('cta_text');
$cta_url = theme_lambda_get_setting('cta_url');
if ($cta_text && $cta_url) {
    echo html_writer::div(
        html_writer::link($cta_url, $cta_text, array('class' => 'btn btn-primary lambda-cta-button')),
        'lambda-cta-container'
    );
}

// Example: Display course summary using Lambda's styling
if (!empty($course->summary)) {
    echo html_writer::div(
        format_text($course->summary, FORMAT_HTML),
        'lambda-course-summary'
    );
}

// Example: Add Lambda theme's custom footer
$customfooter = theme_lambda_get_setting('customfooter');
if ($customfooter) {
    echo html_writer::div(
        format_text($customfooter, FORMAT_HTML),
        'lambda-custom-footer'
    );
}

// End output
echo $OUTPUT->footer();

/**
 * Helper function to fetch Lambda theme settings.
 * 
 * @param string $setting The name of the setting to fetch.
 * @return mixed The value of the setting, or null if not set.
 */
function theme_lambda_get_setting($setting) {
    global $CFG;
    if (isset($CFG->theme_lambda_settings) && isset($CFG->theme_lambda_settings[$setting])) {
        return $CFG->theme_lambda_settings[$setting];
    }
    return null;
}
```
