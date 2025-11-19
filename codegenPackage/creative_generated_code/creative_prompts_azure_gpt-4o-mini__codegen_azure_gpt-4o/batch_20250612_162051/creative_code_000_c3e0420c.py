"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mbandjock.fr
Prompt: Generate a simple WordPress plugin that displays a custom welcome message on the homepage, similar to the "Hello world!" post on mbandjock.fr.
Generated: DETERMINISTIC_c3e0420c63ed8e2f
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://yourwebsite.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```php
<?php
/*
Plugin Name: Custom Welcome Message
Plugin URI: https://yourwebsite.com
Description: A simple WordPress plugin to display a custom welcome message on the homepage.
Version: 1.0
Author: Your Name
Author URI: https://yourwebsite.com
License: GPL2
*/

// Exit if accessed directly
if (!defined('ABSPATH')) {
    exit;
}

/**
 * Function to display the custom welcome message on the homepage.
 */
function cwm_display_welcome_message() {
    // Check if the current page is the homepage
    if (is_front_page()) {
        // Output the custom welcome message
        echo '<div class="custom-welcome-message" style="text-align: center; margin: 20px 0; font-size: 1.5em; color: #333;">';
        echo 'Welcome to our website! We are glad to have you here.';
        echo '</div>';
    }
}

// Hook the function to the 'wp_footer' action
add_action('wp_footer', 'cwm_display_welcome_message');

/**
 * Enqueue styles for the welcome message, if needed.
 */
function cwm_enqueue_styles() {
    // Add custom styles for the welcome message (optional)
    wp_enqueue_style(
        'cwm-custom-style', 
        plugin_dir_url(__FILE__) . 'assets/cwm-style.css', 
        array(), 
        '1.0.0', 
        'all'
    );
}

// Hook the enqueue function to 'wp_enqueue_scripts'
add_action('wp_enqueue_scripts', 'cwm_enqueue_styles');

/**
 * Plugin activation hook - setup tasks, if needed.
 */
function cwm_activate_plugin() {
    // Code to run upon plugin activation (optional)
    // For now, just a placeholder
}

// Register the activation hook
register_activation_hook(__FILE__, 'cwm_activate_plugin');

/**
 * Plugin deactivation hook - cleanup tasks, if needed.
 */
function cwm_deactivate_plugin() {
    // Code to run upon plugin deactivation (optional)
    // For now, just a placeholder
}

// Register the deactivation hook
register_deactivation_hook(__FILE__, 'cwm_deactivate_plugin');
```

### Optional: Create a `cwm-style.css` file in the `assets/` folder of the plugin directory if you want to customize the appearance of the message. Example content for `cwm-style.css`:

```css
.custom-welcome-message {
    background-color: #f9f9f9;
    border: 1px solid #ddd;
    border-radius: 5px;
    padding: 10px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
```
