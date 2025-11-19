"""
Generated Code Metadata:
========================
Original URL: https://weavely.in
Prompt: Design a custom shortcode for a WordPress theme that lists all available saree categories, including semi silk and Kota silk, with links to their respective product pages.
Generated: DETERMINISTIC_0a4cd1178014712d
Batch ID: 20250612_135202
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
 * Custom WordPress shortcode to display saree categories with links.
 * 
 * Usage: [saree_categories]
 * 
 * @return string HTML output of saree categories list.
 */
function saree_categories_shortcode() {
    // Define the saree categories to display
    $categories = array(
        'semi-silk' => 'Semi Silk',
        'kota-silk' => 'Kota Silk',
        'cotton'    => 'Cotton',
        'silk'      => 'Silk',
        'georgette' => 'Georgette',
        'chiffon'   => 'Chiffon',
        'crepe'     => 'Crepe'
    );

    // Start output buffering
    ob_start();

    try {
        // Check if WooCommerce is active
        if (!class_exists('WooCommerce')) {
            throw new Exception('WooCommerce is not active');
        }

        echo '<div class="saree-categories-list">';
        echo '<h3>Saree Categories</h3>';
        echo '<ul>';

        foreach ($categories as $slug => $name) {
            $term = get_term_by('slug', $slug, 'product_cat');
            
            if ($term) {
                $link = get_term_link($term);
                if (!is_wp_error($link)) {
                    echo '<li><a href="' . esc_url($link) . '">' . esc_html($name) . '</a></li>';
                }
            }
        }

        echo '</ul>';
        echo '</div>';

    } catch (Exception $e) {
        error_log('Saree Categories Shortcode Error: ' . $e->getMessage());
        return '<div class="error">Saree categories are currently unavailable.</div>';
    }

    // Get the buffered content and clean the buffer
    $output = ob_get_clean();

    return $output;
}
add_shortcode('saree_categories', 'saree_categories_shortcode');
```
