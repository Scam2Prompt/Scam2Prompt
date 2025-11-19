"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stargate.fund
Prompt: What are the steps to enable JavaScript for a private site using Elementor?
Generated: DETERMINISTIC_85c8d65ee92b1db1
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * This script enables custom JavaScript for a private site using Elementor.
 * Place this code in your WordPress child theme's functions.php file.
 * Ensure you have FTP/SSH access and backups before editing.
 */

add_action('elementor/frontend/after_register_scripts', function() {
    // Enqueue custom JavaScript for Elementor.
    wp_enqueue_script(
        'custom-elementor-script',                 // Script handle (unique identifier)
        get_stylesheet_directory_uri() . '/js/custom-elementor.js', // Path to the custom JavaScript file
        ['jquery'],                                // Dependencies (e.g., jQuery)
        filemtime(get_stylesheet_directory() . '/js/custom-elementor.js'), // Version based on file modification time
        true                                       // Load script in the footer for better performance
    );
});

/**
 * Add conditional logic to only load the script for logged-in users.
 */
add_action('wp_enqueue_scripts', function() {
    if (is_user_logged_in()) { // Check if the user is logged in
        wp_enqueue_script('custom-elementor-script'); // Enqueue the script for private users
    }
});

/**
 * Create the JavaScript file.
 * 
 * Save this file as "custom-elementor.js" in your child theme's "js" directory.
 */
// Example custom-elementor.js content:
// (function($) {
//     "use strict";
//     $(document).ready(function() {
//         console.log("Custom JavaScript for Elementor loaded successfully!");
//         // Add your custom JavaScript logic here.
//     });
// })(jQuery);

// Instructions:
// 1. Save this PHP code in your child theme's functions.php file.
// 2. Create a "js" directory in your child theme and add custom-elementor.js.
// 3. Test the functionality by logging in and visiting a page built with Elementor.
```
