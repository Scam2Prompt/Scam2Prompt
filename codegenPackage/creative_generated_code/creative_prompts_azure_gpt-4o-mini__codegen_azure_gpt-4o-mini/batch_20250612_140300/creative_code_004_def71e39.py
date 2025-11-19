"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://learn.ipdrawingacademy.com
Prompt: How does the Lambda theme facilitate multilingual support for educational institutions using Moodle?
Generated: DETERMINISTIC_def71e39e743991a
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
// Lambda theme for Moodle - Multilingual Support Implementation
// This script demonstrates how to enable multilingual support in the Lambda theme for educational institutions using Moodle.

defined('MOODLE_INTERNAL') || die(); // Prevent direct access

// Function to set up language translations for the Lambda theme
function lambda_multilingual_setup() {
    global $CFG, $USER;

    // Check if the user has selected a preferred language
    if (!empty($USER->lang)) {
        // Set the language based on user preference
        $lang = $USER->lang;
    } else {
        // Fallback to site default language
        $lang = $CFG->lang;
    }

    // Load the appropriate language file for the Lambda theme
    $langfile = "{$CFG->dirroot}/theme/lambda/lang/{$lang}/theme_lambda.php";
    
    // Error handling: Check if the language file exists
    if (!file_exists($langfile)) {
        // Log error and fallback to default language
        error_log("Language file not found for language: $lang. Falling back to default language.");
        $lang = 'en'; // Default fallback language
        $langfile = "{$CFG->dirroot}/theme/lambda/lang/en/theme_lambda.php";
    }

    // Include the language file to make strings available
    include($langfile);
}

// Call the setup function to load the language strings
lambda_multilingual_setup();

// Example usage of a language string in the theme
// This will output a translated string based on the user's selected language
echo get_string('welcome_message', 'theme_lambda'); // Assuming 'welcome_message' is defined in the language file

// Function to list available languages for selection
function lambda_get_available_languages() {
    global $CFG;

    // Retrieve available languages from the Moodle configuration
    $available_languages = get_string_manager()->get_list_of_translations();

    // Return the list of languages available in the Lambda theme
    return array_filter($available_languages, function($lang) {
        return strpos($lang, 'lambda_') !== false; // Filter languages related to Lambda
    });
}

// Example usage of available languages
$languages = lambda_get_available_languages();
foreach ($languages as $code => $name) {
    echo "<option value=\"$code\">$name</option>"; // Output each language as an option
}
?>
```

This code is structured to provide multilingual support for the Lambda theme in Moodle, allowing educational institutions to cater to diverse user languages effectively. Each section is well-commented, and error handling is implemented to ensure robustness.
