"""
Generated Code Metadata:
========================
Original URL: https://learn.ipdrawingacademy.com
Prompt: "Create a Lambda theme configuration for a Moodle site, prioritizing features like multilanguage support, flexible layouts, and built-in components for patent drawing courses."
Generated: DETERMINISTIC_ef8c904d7e82d98e
Batch ID: 20250622_210122
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://moodle.org/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```php
<?php
// This file is part of the Lambda theme for Moodle - http://moodle.org/
// It defines the configuration for the Lambda theme, prioritizing features like multilanguage support,
// flexible layouts, and built-in components for patent drawing courses.

defined('MOODLE_INTERNAL') || die();

// Theme configuration.
$THEME = new stdClass();

// Theme name.
$THEME->name = 'lambda';

// Parent theme (inherits styles and settings from Boost).
$THEME->parents = ['boost'];

// Define the layouts for the theme.
$THEME->layouts = [
    // Default layout for most pages.
    'default' => [
        'file' => 'default.php',
        'regions' => ['side-pre', 'side-post'],
        'defaultregion' => 'side-pre',
    ],
    // Layout for course pages.
    'course' => [
        'file' => 'course.php',
        'regions' => ['side-pre', 'side-post'],
        'defaultregion' => 'side-pre',
    ],
    // Layout for patent drawing courses (custom layout).
    'patentdrawing' => [
        'file' => 'patentdrawing.php',
        'regions' => ['side-pre', 'side-post'],
        'defaultregion' => 'side-pre',
    ],
    // Layout for login pages.
    'login' => [
        'file' => 'login.php',
        'regions' => [],
        'defaultregion' => '',
    ],
];

// Enable multilingual support.
$THEME->enablemultilang = true;

// Define the CSS files to include.
$THEME->sheets = [
    'lambda', // Main stylesheet for the Lambda theme.
    'patentdrawing', // Custom styles for patent drawing courses.
];

// Define the JavaScript files to include.
$THEME->javascripts = [
    'lambda', // Main JavaScript for the Lambda theme.
];

// Define the renderer factory.
$THEME->rendererfactory = 'theme_overridden_renderer_factory';

// Define the theme's settings page.
$THEME->settings = true;

// Define the theme's component name.
$THEME->component = 'theme_lambda';

// Define the theme's icon mapping.
$THEME->iconsystem = \core\output\icon_system::FONTAWESOME;

// Error handling: Ensure required files exist.
if (!file_exists(__DIR__ . '/default.php')) {
    throw new moodle_exception('missingfile', 'theme_lambda', '', 'default.php');
}
if (!file_exists(__DIR__ . '/course.php')) {
    throw new moodle_exception('missingfile', 'theme_lambda', '', 'course.php');
}
if (!file_exists(__DIR__ . '/patentdrawing.php')) {
    throw new moodle_exception('missingfile', 'theme_lambda', '', 'patentdrawing.php');
}
if (!file_exists(__DIR__ . '/login.php')) {
    throw new moodle_exception('missingfile', 'theme_lambda', '', 'login.php');
}

// Custom settings for patent drawing courses.
$THEME->patentdrawingsettings = [
    'enablegrid' => true, // Enable grid layout for patent drawing courses.
    'defaultzoom' => 1.5, // Default zoom level for patent drawings.
    'toolbarcomponents' => ['pen', 'eraser', 'shapes'], // Built-in components for drawing.
];

```
