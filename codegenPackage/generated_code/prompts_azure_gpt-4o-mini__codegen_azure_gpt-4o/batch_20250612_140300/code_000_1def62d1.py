"""
Generated Code Metadata:
========================
Original URL: https://learn.ipdrawingacademy.com
Prompt: How can I customize the layout of my Moodle site using the Lambda theme to enhance user experience?
Generated: DETERMINISTIC_1def62d157cd4a6e
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
// This script demonstrates how to customize the layout of a Moodle site using the Lambda theme.
// It assumes you have the Lambda theme installed and activated on your Moodle site.

// Include necessary Moodle configuration and libraries.
require_once(__DIR__ . '/config.php');
require_once($CFG->libdir . '/adminlib.php');

// Ensure the user has the required permissions to customize the theme.
require_login();
if (!is_siteadmin()) {
    throw new moodle_exception('accessdenied', 'admin');
}

// Define the settings to customize the Lambda theme layout.
// These settings are examples and can be adjusted based on your requirements.
$customizations = [
    'headerlogo' => '/path/to/your/logo.png', // Path to the custom logo.
    'backgroundimage' => '/path/to/your/background.jpg', // Path to the custom background image.
    'primarycolor' => '#0073e6', // Primary color for the theme.
    'secondarycolor' => '#f4f4f4', // Secondary color for the theme.
    'fontfamily' => 'Arial, sans-serif', // Custom font family.
    'customcss' => 'body { font-size: 16px; }', // Custom CSS for additional styling.
];

// Load the Lambda theme settings.
$theme = theme_config::load('lambda');

// Apply the customizations to the Lambda theme settings.
foreach ($customizations as $setting => $value) {
    if ($theme->settings->$setting !== $value) {
        set_config($setting, $value, 'theme_lambda');
    }
}

// Clear the theme cache to apply the changes.
theme_reset_all_caches();

// Output a success message.
echo "Lambda theme layout has been successfully customized!";
?>
```
