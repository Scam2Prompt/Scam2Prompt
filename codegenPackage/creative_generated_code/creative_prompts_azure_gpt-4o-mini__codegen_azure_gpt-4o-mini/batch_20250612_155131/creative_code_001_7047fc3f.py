"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sayacosmetics.com
Prompt: How can I create a sample page in WordPress that features a simple greeting and is powered by the PopularFX theme?
Generated: DETERMINISTIC_7047fc3f41116253
Batch ID: 20250612_155131
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
 * Template Name: Simple Greeting Page
 * Description: A simple page template that displays a greeting message.
 */

// Ensure that WordPress environment is loaded
if (!defined('ABSPATH')) {
    exit; // Exit if accessed directly
}

// Get header from the active theme
get_header(); ?>

<div class="greeting-container">
    <h1><?php esc_html_e('Welcome to Our Website!', 'your-text-domain'); ?></h1>
    <p><?php esc_html_e('We are glad to have you here. Enjoy your stay!', 'your-text-domain'); ?></p>
</div>

<?php 
// Get footer from the active theme
get_footer(); 
?>
```

### Instructions to Use:
1. Create a new file in your active theme directory and name it `page-simple-greeting.php`.
2. Copy and paste the code above into this file.
3. In the WordPress admin panel, create a new page and select "Simple Greeting Page" as the template.
4. Publish the page to view your greeting message.

### Notes:
- Replace `'your-text-domain'` with the appropriate text domain for translation.
- Ensure that the PopularFX theme is activated in your WordPress installation.
