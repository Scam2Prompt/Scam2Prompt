"""
Generated Code Metadata:
========================
Original URL: https://learn.ipdrawingacademy.com
Prompt: How does the Lambda theme facilitate multilingual support for educational institutions using Moodle?
Generated: DETERMINISTIC_def71e39e743991a
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
/**
 * Lambda Theme Multilingual Support for Moodle
 * 
 * This script enhances the Lambda theme to support multilingual capabilities
 * for educational institutions using Moodle.
 */

// Ensure this file is being included by Moodle
defined('MOODLE_INTERNAL') || die();

/**
 * Lambda theme multilingual support class
 */
class theme_lambda_multilingual {

    /**
     * Initialize multilingual support
     */
    public static function init() {
        global $PAGE;

        // Add language menu to navigation
        self::add_language_menu();

        // Load language strings
        self::load_language_strings();

        // Add RTL support if needed
        if (right_to_left()) {
            $PAGE->requires->css('/theme/lambda/style/rtl.css');
        }
    }

    /**
     * Add language selection menu to navigation
     */
    private static function add_language_menu() {
        global $CFG, $OUTPUT;

        if (empty($CFG->langmenu) || $CFG->langmenu == 1) {
            $langs = get_string_manager()->get_list_of_translations();
            if (count($langs) > 1) {
                $currentlang = current_language();
                $langmenu = new custom_menu();
                $langmenu->add(get_string('language'), new moodle_url('#'), get_string('language'), 10000);
                
                foreach ($langs as $langtype => $langname) {
                    $langmenu->add(
                        $langname,
                        new moodle_url($PAGE->url, array('lang' => $langtype)),
                        $langname,
                        $langtype
                    )->set_selected($langtype == $currentlang);
                }
                
                $OUTPUT->custom_menu($langmenu);
            }
        }
    }

    /**
     * Load theme-specific language strings
     */
    private static function load_language_strings() {
        global $PAGE;
        
        $PAGE->requires->strings_for_js(
            array(
                'chooselanguage',
                'languagecurrent',
                'languagemissing'
            ),
            'theme_lambda'
        );
    }

    /**
     * Get available languages for the theme
     * 
     * @return array List of available languages
     */
    public static function get_available_languages() {
        return get_string_manager()->get_list_of_translations();
    }

    /**
     * Check if RTL support is needed for current language
     * 
     * @return bool True if RTL is needed
     */
    public static function is_rtl_needed() {
        return right_to_left();
    }
}

// Initialize multilingual support when theme is loaded
theme_lambda_multilingual::init();
```
