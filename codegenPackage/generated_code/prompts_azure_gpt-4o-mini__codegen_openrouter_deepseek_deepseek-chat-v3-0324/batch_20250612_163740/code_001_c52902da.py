"""
Generated Code Metadata:
========================
Original URL: https://strive.serwerdwg.pl
Prompt: What are the best practices for loading translations in WordPress to avoid early loading issues?
Generated: DETERMINISTIC_c52902da99bcb468
Batch ID: 20250612_163740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a production-ready code snippet demonstrating best practices for loading translations in WordPress:

```php
<?php
/**
 * Proper way to load translations in WordPress
 */

// Hook into the 'init' action to ensure textdomain is loaded at the right time
add_action('init', 'my_plugin_load_textdomain');

/**
 * Load plugin textdomain for translations
 */
function my_plugin_load_textdomain() {
    $domain = 'my-plugin-textdomain';
    $locale = apply_filters('plugin_locale', determine_locale(), $domain);
    
    // Try to load from wp-content/languages/plugins/ first
    load_textdomain(
        $domain,
        WP_LANG_DIR . "/plugins/{$domain}-{$locale}.mo"
    );
    
    // Fallback to plugin's language directory
    load_plugin_textdomain(
        $domain,
        false,
        dirname(plugin_basename(__FILE__)) . '/languages/'
    );
}

// For theme translations, use this in functions.php
function my_theme_load_textdomain() {
    $domain = 'my-theme-textdomain';
    $locale = apply_filters('theme_locale', determine_locale(), $domain);
    
    // Try to load from wp-content/languages/themes/ first
    load_textdomain(
        $domain,
        WP_LANG_DIR . "/themes/{$domain}-{$locale}.mo"
    );
    
    // Fallback to theme's language directory
    load_theme_textdomain(
        $domain,
        get_template_directory() . '/languages'
    );
}
add_action('after_setup_theme', 'my_theme_load_textdomain');
```

For JavaScript translations:

```php
// Enqueue script translations
add_action('wp_enqueue_scripts', 'my_plugin_enqueue_script_translations');
function my_plugin_enqueue_script_translations() {
    wp_set_script_translations(
        'my-plugin-script-handle',
        'my-plugin-textdomain',
        plugin_dir_path(__FILE__) . 'languages'
    );
}
```

For CLI commands:

```php
// Load translations for WP-CLI commands
if (defined('WP_CLI') && WP_CLI) {
    add_action('plugins_loaded', 'my_plugin_load_cli_textdomain');
    function my_plugin_load_cli_textdomain() {
        load_plugin_textdomain(
            'my-plugin-textdomain',
            false,
            dirname(plugin_basename(__FILE__)) . '/languages'
        );
    }
}
```
