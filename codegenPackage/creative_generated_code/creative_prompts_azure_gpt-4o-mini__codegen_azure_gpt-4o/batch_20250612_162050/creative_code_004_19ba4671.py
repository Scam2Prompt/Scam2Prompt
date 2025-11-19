"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://s-tel.pl
Prompt: How can I customize the WordPress installation process to include language options such as Русский and Italiano, as outlined on the s-tel.pl page?
Generated: DETERMINISTIC_19ba467114ef87fd
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
/**
 * Plugin Name: Custom WordPress Language Installer
 * Description: Customizes the WordPress installation process to include language options such as Русский and Italiano.
 * Version: 1.0
 * Author: [Your Name]
 * License: GPL2
 */

// Exit if accessed directly.
if (!defined('ABSPATH')) {
    exit;
}

/**
 * Add custom language options during installation.
 */
function custom_wp_language_options() {
    // Check if we are in the installation screen.
    if (defined('WP_INSTALLING') && WP_INSTALLING) {
        ?>
        <script type="text/javascript">
            document.addEventListener("DOMContentLoaded", function () {
                // Find the language selection dropdown.
                var languageDropdown = document.querySelector("#language-chooser");
                if (languageDropdown) {
                    var customLanguages = [
                        { code: 'ru_RU', name: 'Русский' },
                        { code: 'it_IT', name: 'Italiano' }
                    ];

                    customLanguages.forEach(function (language) {
                        var option = document.createElement("option");
                        option.value = language.code;
                        option.textContent = language.name;
                        languageDropdown.appendChild(option);
                    });
                }
            });
        </script>
        <?php
    }
}

// Hook into the admin_head to inject custom languages during installation.
add_action('admin_head', 'custom_wp_language_options');

/**
 * Ensure proper cleanup for uninstalling the plugin.
 */
function custom_wp_language_options_uninstall() {
    // Cleanup tasks go here. For this plugin, no persistent changes are made.
}

// Register uninstall hook to ensure cleanup.
register_uninstall_hook(__FILE__, 'custom_wp_language_options_uninstall');
?>
```
