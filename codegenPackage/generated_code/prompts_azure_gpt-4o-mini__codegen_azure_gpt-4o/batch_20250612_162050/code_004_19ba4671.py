"""
Generated Code Metadata:
========================
Original URL: https://s-tel.pl
Prompt: How can I customize the WordPress installation process to include language options such as Русский and Italiano, as outlined on the s-tel.pl page?
Generated: DETERMINISTIC_19ba467114ef87fd
Batch ID: 20250612_162050
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
 * Plugin Name: Custom WordPress Installation Language Selector
 * Description: Adds custom language options (Русский and Italiano) during the WordPress installation process.
 * Version: 1.0
 * Author: Your Name
 * License: GPL2
 */

// Hook into the installation process to add custom language options
add_action('install_themes_table', 'add_custom_language_options');

/**
 * Adds custom language options to the WordPress installation process.
 */
function add_custom_language_options() {
    ?>
    <div class="custom-language-selector">
        <h2><?php esc_html_e('Select Installation Language', 'custom-language-selector'); ?></h2>
        <form method="post" action="">
            <label for="language"><?php esc_html_e('Choose Language:', 'custom-language-selector'); ?></label>
            <select name="language" id="language">
                <option value="en_US"><?php esc_html_e('English', 'custom-language-selector'); ?></option>
                <option value="ru_RU"><?php esc_html_e('Русский', 'custom-language-selector'); ?></option>
                <option value="it_IT"><?php esc_html_e('Italiano', 'custom-language-selector'); ?></option>
            </select>
            <button type="submit"><?php esc_html_e('Continue', 'custom-language-selector'); ?></button>
        </form>
    </div>
    <?php
}

// Hook into the installation process to handle the selected language
add_action('init', 'handle_language_selection');

/**
 * Handles the language selection during installation.
 */
function handle_language_selection() {
    if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['language'])) {
        $selected_language = sanitize_text_field($_POST['language']);

        // Validate the selected language
        $valid_languages = ['en_US', 'ru_RU', 'it_IT'];
        if (in_array($selected_language, $valid_languages, true)) {
            // Set the selected language for installation
            update_option('WPLANG', $selected_language);
        } else {
            // Handle invalid language selection
            wp_die(__('Invalid language selected.', 'custom-language-selector'));
        }
    }
}
?>
```
