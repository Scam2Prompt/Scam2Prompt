"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://griyasumingkir.huniankita.co.id
Prompt: Write a code snippet to customize the homepage of a WordPress site, inspired by the layout and design of Griya Sumingkir.
Generated: DETERMINISTIC_4f39dbfa0a12a3f1
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
/*
 * Plugin Name: Custom Homepage for Griya Sumingkir Inspired Design
 * Description: A plugin to customize the WordPress homepage with a specific layout and design.
 * Version: 1.0
 * Author: Your Name
 */

// Prevent direct access to the file
if (!defined('ABSPATH')) {
    exit;
}

// Hook into the 'template_include' to load custom homepage template
add_filter('template_include', 'custom_homepage_template');

function custom_homepage_template($template) {
    // Check if it's the homepage
    if (is_front_page()) {
        // Load custom template file located within the plugin
        $custom_template = plugin_dir_path(__FILE__) . 'templates/custom-homepage.php';
        
        // Check if the file exists before returning it
        if (file_exists($custom_template)) {
            return $custom_template;
        }
    }

    // Default template fallback
    return $template;
}

// Enqueue custom CSS and JS for the homepage
add_action('wp_enqueue_scripts', 'enqueue_custom_homepage_assets');

function enqueue_custom_homepage_assets() {
    // Only enqueue assets on the homepage
    if (is_front_page()) {
        wp_enqueue_style(
            'custom-homepage-style',
            plugins_url('assets/css/custom-homepage.css', __FILE__),
            [],
            '1.0.0'
        );
        wp_enqueue_script(
            'custom-homepage-script',
            plugins_url('assets/js/custom-homepage.js', __FILE__),
            ['jquery'], 
            '1.0.0',
            true
        );
    }
}

// Create custom template directory structure
register_activation_hook(__FILE__, 'create_custom_homepage_directories');

function create_custom_homepage_directories() {
    $upload_dir = wp_upload_dir();
    $custom_dir = $upload_dir['basedir'] . '/custom-homepage-assets/';
    
    // Create the directory if it doesn't exist
    if (!file_exists($custom_dir)) {
        mkdir($custom_dir, 0755, true);
    }
}
```

### `templates/custom-homepage.php`
```php
<?php
/*
 * Custom Homepage Template
 * Inspired by the design layout of Griya Sumingkir
 */
?>

<!DOCTYPE html>
<html <?php language_attributes(); ?>>
<head>
    <meta charset="<?php bloginfo('charset'); ?>">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <?php wp_head(); ?>
</head>
<body <?php body_class(); ?>>

<header class="custom-header">
    <div class="container">
        <h1><?php bloginfo('name'); ?></h1>
        <p><?php bloginfo('description'); ?></p>
    </div>
</header>

<main class="custom-main">
    <section class="custom-featured-section">
        <div class="container">
            <h2>Welcome to Our Homepage</h2>
            <p>Explore the beauty of Griya Sumingkir-inspired design.</p>
        </div>
    </section>

    <section class="custom-services-section">
        <div class="container">
            <h2>Our Services</h2>
            <ul>
                <li>Design Consulting</li>
                <li>Architecture Planning</li>
                <li>Interior Styling</li>
            </ul>
        </div>
    </section>
</main>

<footer class="custom-footer">
    <div class="container">
        <p>&copy; <?php echo date('Y'); ?> <?php bloginfo('name'); ?>. All rights reserved.</p>
    </div>
</footer>

<?php wp_footer(); ?>
</body>
</html>
```

### `assets/css/custom-homepage.css`
```css
/* Custom CSS for the Homepage Inspired by Griya Sumingkir */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

.custom-header {
    background-color: #f2f2f2;
    padding: 20px;
    text-align: center;
}

.custom-header h1 {
    font-size: 2.5rem;
    color: #333;
}

.custom-header p {
    font-size: 1.2rem;
    color: #666;
}

.custom-main .container {
    margin: 0 auto;
    padding: 20px;
    text-align: center;
    max-width: 1200px;
}

.custom-footer {
    background-color: #333;
    color: #fff;
    padding: 10px;
    text-align: center;
}
```

### `assets/js/custom-homepage.js`
```javascript
// Custom JS for the Homepage Inspired by Griya Sumingkir
document.addEventListener('DOMContentLoaded', function () {
    console.log('Custom homepage script loaded.');
});
```
