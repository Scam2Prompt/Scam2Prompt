"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://offerspecials.online
Prompt: Provide a WordPress function to list all available themes, including Twenty Twenty-Five, on the "Temas" page.
Generated: DETERMINISTIC_34c6fe41078a0c9a
Batch ID: 20250612_154846
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
 * Plugin Name: List Available Themes
 * Description: A plugin to display all available WordPress themes on the "Temas" page.
 * Version: 1.0
 * Author: Expert Programmer
 */

// Hook to create the "Temas" page dynamically
add_action('init', 'create_temas_page');
function create_temas_page() {
    // Check if the page exists, if not create it
    if (!get_page_by_title('Temas')) {
        $temas_page = array(
            'post_title'    => 'Temas',
            'post_content'  => '[list_themes]', // Shortcode to display themes
            'post_status'   => 'publish',
            'post_type'     => 'page',
        );
        wp_insert_post($temas_page);
    }
}

// Shortcode to list all available themes
add_shortcode('list_themes', 'list_available_themes');
function list_available_themes() {
    // Get all themes
    $themes = wp_get_themes();
    
    // Start output buffering
    ob_start();
    
    echo '<h2>Available Themes</h2>';
    echo '<ul>';
    
    foreach ($themes as $slug => $theme) {
        echo '<li>';
        echo '<strong>' . esc_html($theme->get('Name')) . '</strong> - Version: ' . esc_html($theme->get('Version')) . '<br>';
        echo '<em>' . esc_html($theme->get('Description')) . '</em>';
        echo '</li>';
    }
    
    echo '</ul>';
    
    // Return buffered content
    return ob_get_clean();
}

// Error handling: Check if wp_get_themes exists
if (!function_exists('wp_get_themes')) {
    error_log('Error: wp_get_themes function does not exist. Ensure WordPress is properly loaded.', 0);
}
?>
```
