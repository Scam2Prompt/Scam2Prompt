"""
Generated Code Metadata:
========================
Original URL: https://learn.ipdrawingacademy.com
Prompt: Can you provide a step-by-step guide on how to integrate plugins with the Lambda theme in Moodle?
Generated: DETERMINISTIC_0af58349e4e001ad
Batch ID: 20250612_140300
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "http://www.gnu.org/licenses/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://www.gnu.org/copyleft/gpl.html": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
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

Here's a clean, production-ready PHP code example demonstrating how to integrate a custom plugin with the Lambda theme in Moodle:

```php
<?php
// This file is part of Moodle - http://moodle.org/
//
// Moodle is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// Moodle is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with Moodle.  If not, see <http://www.gnu.org/licenses/>.

/**
 * Plugin integration with Lambda theme.
 *
 * @package    theme_lambda
 * @copyright  2023 Your Name
 * @license    http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later
 */

defined('MOODLE_INTERNAL') || die();

/**
 * Adds custom CSS for the plugin when using Lambda theme.
 */
function theme_lambda_plugin_css() {
    global $CFG, $PAGE;

    // Only add CSS if we're using the Lambda theme.
    if ($PAGE->theme->name == 'lambda') {
        $cssfile = $CFG->dirroot . '/path/to/your/plugin/styles.css';
        if (file_exists($cssfile)) {
            $PAGE->requires->css('/path/to/your/plugin/styles.css');
        }
    }
}

/**
 * Extends Lambda theme navigation.
 *
 * @param navigation_node $nav Current navigation node
 */
function theme_lambda_extend_navigation(navigation_node $nav) {
    global $CFG, $PAGE;

    // Only modify navigation if we're using the Lambda theme.
    if ($PAGE->theme->name == 'lambda') {
        $pluginnode = $nav->add(
            get_string('pluginname', 'your_plugin'),
            new moodle_url('/path/to/your/plugin/index.php'),
            navigation_node::TYPE_CUSTOM,
            null,
            'your_plugin_node'
        );
        $pluginnode->showinflatnavigation = true;
    }
}

/**
 * Adds custom JS for the plugin when using Lambda theme.
 */
function theme_lambda_plugin_js() {
    global $PAGE;

    // Only add JS if we're using the Lambda theme.
    if ($PAGE->theme->name == 'lambda') {
        $PAGE->requires->js_call_amd('your_plugin/your_module', 'init');
    }
}

/**
 * Callback to add custom elements to Lambda theme's settings page.
 *
 * @param admin_settingpage $settings The settings page object
 */
function theme_lambda_plugin_settings(admin_settingpage $settings) {
    // Only add settings if we're editing the Lambda theme.
    if ($settings->name == 'themesettinglambda') {
        $settings->add(new admin_setting_configcheckbox(
            'your_plugin/enablefeature',
            get_string('enablefeature', 'your_plugin'),
            get_string('enablefeature_desc', 'your_plugin'),
            0
        ));
    }
}

/**
 * Modifies Lambda theme's renderer.
 *
 * @param moodle_page $page The current page
 * @param string $target The target renderer
 * @return object The modified renderer
 */
function theme_lambda_plugin_renderer(moodle_page $page, $target) {
    if ($page->theme->name == 'lambda') {
        require_once($CFG->dirroot . '/path/to/your/plugin/renderer.php');
        return new your_plugin_renderer($page, $target);
    }
    return null;
}

// Register all callbacks.
$callbacks = [
    [
        'hook' => 'before_http_headers',
        'callback' => 'theme_lambda_plugin_css',
    ],
    [
        'hook' => 'before_http_headers',
        'callback' => 'theme_lambda_plugin_js',
    ],
    [
        'hook' => 'extend_navigation',
        'callback' => 'theme_lambda_extend_navigation',
    ],
    [
        'hook' => 'after_config',
        'callback' => 'theme_lambda_plugin_settings',
    ],
    [
        'hook' => 'renderer_factory',
        'callback' => 'theme_lambda_plugin_renderer',
    ],
];

foreach ($callbacks as $callback) {
    $callback = new \core\hook\callback($callback);
    \core\hook\manager::get_instance()->add_callback($callback);
}
```
