"""
Generated Code Metadata:
========================
Original URL: https://mundialconsorcios.com.br
Prompt: Write code to detect and resolve issues with theme registration in WordPress, ensuring the `wp_is_block_theme` function is used correctly.
Generated: DETERMINISTIC_c47256c8b7c0ae09
Batch ID: 20250612_154454
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
 * Theme Registration Checker
 * 
 * This script checks for proper theme registration in WordPress and ensures
 * the wp_is_block_theme function is used correctly. It also provides
 * resolution for common issues.
 */

if (!defined('ABSPATH')) {
    exit; // Exit if accessed directly
}

class Theme_Registration_Checker {
    /**
     * Initialize the theme checker
     */
    public function __construct() {
        add_action('after_setup_theme', array($this, 'check_theme_registration'), 10);
        add_action('admin_notices', array($this, 'display_admin_notices'));
    }

    /**
     * Check if theme is properly registered and wp_is_block_theme is used correctly
     */
    public function check_theme_registration() {
        // Check if theme supports required features
        if (!current_theme_supports('block-templates')) {
            $this->add_notice(
                'error',
                __('Your theme does not support block templates. Please add theme support for "block-templates".', 'textdomain')
            );
        }

        // Check if wp_is_block_theme exists (WP 5.8+)
        if (!function_exists('wp_is_block_theme')) {
            $this->add_notice(
                'error',
                __('Your WordPress version does not support block themes. Please upgrade to WordPress 5.8 or later.', 'textdomain')
            );
            return;
        }

        // Check if this is a block theme
        if (wp_is_block_theme()) {
            // Verify theme.json exists
            $theme_json_path = get_theme_file_path('theme.json');
            if (!file_exists($theme_json_path)) {
                $this->add_notice(
                    'error',
                    __('Your block theme is missing theme.json file.', 'textdomain')
                );
            }
        }
    }

    /**
     * Add notice to be displayed in admin
     *
     * @param string $type Notice type (error, warning, success, info)
     * @param string $message Notice message
     */
    private function add_notice($type, $message) {
        $notices = get_option('theme_registration_notices', array());
        $notices[] = array(
            'type' => $type,
            'message' => $message
        );
        update_option('theme_registration_notices', $notices);
    }

    /**
     * Display admin notices
     */
    public function display_admin_notices() {
        $notices = get_option('theme_registration_notices', array());
        
        if (empty($notices)) {
            return;
        }

        foreach ($notices as $notice) {
            printf(
                '<div class="notice notice-%s is-dismissible"><p>%s</p></div>',
                esc_attr($notice['type']),
                esc_html($notice['message'])
            );
        }

        // Clear notices after displaying
        delete_option('theme_registration_notices');
    }

    /**
     * Attempt to fix common theme registration issues
     */
    public function fix_theme_registration() {
        // Add block-templates support if missing
        if (!current_theme_supports('block-templates')) {
            add_theme_support('block-templates');
        }

        // For block themes, create a basic theme.json if missing
        if (function_exists('wp_is_block_theme') && wp_is_block_theme()) {
            $theme_json_path = get_theme_file_path('theme.json');
            if (!file_exists($theme_json_path)) {
                $default_json = array(
                    'version' => 2,
                    'settings' => array(),
                    'styles' => array()
                );
                
                if (wp_mkdir_p(dirname($theme_json_path))) {
                    file_put_contents(
                        $theme_json_path,
                        json_encode($default_json, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES)
                    );
                }
            }
        }
    }
}

// Initialize the theme checker
new Theme_Registration_Checker();
```
