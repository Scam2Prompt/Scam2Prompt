"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://36destinations.com
Prompt: Write a WordPress function to display a custom footer message, such as "Copyright © 2025 36destinations.com," on all pages of a site using the Astra theme.
Generated: DETERMINISTIC_515c599e14d5b3a3
Batch ID: 20250612_153246
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
 * Custom function to display a copyright message in the footer.
 *
 * This function adds a custom footer message to all pages of the site
 * using the Astra theme. The message includes the current year and a 
 * placeholder for the website name.
 *
 * @return void
 */
function custom_footer_message() {
    // Get the current year
    $current_year = date('Y');
    
    // Define the website name
    $website_name = '36destinations.com';
    
    // Output the footer message
    echo '<div class="custom-footer-message" style="text-align: center; padding: 20px;">';
    echo 'Copyright © ' . esc_html($current_year) . ' ' . esc_html($website_name) . '. All rights reserved.';
    echo '</div>';
}

// Hook the custom footer message function to the Astra theme's footer
add_action('astra_footer_before', 'custom_footer_message');
?>
```
