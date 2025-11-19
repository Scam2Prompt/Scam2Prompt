"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lunarwalletnectcapital.finance.blog
Prompt: Can you provide code snippets for customizing a WordPress portfolio site to effectively present different genres of projects?
Generated: DETERMINISTIC_4d315f39a3e3286c
Batch ID: 20250612_135940
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
 * Plugin Name: Custom Portfolio Genres
 * Description: Adds functionality to customize portfolio genres for better project organization.
 * Version: 1.0.0
 * Author: Your Name
 * License: GPL2
 */

// Prevent direct access to the file
if (!defined('ABSPATH')) {
    exit;
}

/**
 * Register custom taxonomy for portfolio genres.
 */
function register_portfolio_genres_taxonomy() {
    // Labels for the taxonomy
    $labels = array(
        'name'                       => 'Genres',
        'singular_name'              => 'Genre',
        'search_items'               => 'Search Genres',
        'popular_items'              => 'Popular Genres',
        'all_items'                  => 'All Genres',
        'parent_item'                => 'Parent Genre',
        'parent_item_colon'          => 'Parent Genre:',
        'edit_item'                  => 'Edit Genre',
        'update_item'                => 'Update Genre',
        'add_new_item'               => 'Add New Genre',
        'new_item_name'              => 'New Genre Name',
        'menu_name'                  => 'Genres',
    );

    // Arguments for the taxonomy
    $args = array(
        'hierarchical'      => true, // Use hierarchical structure like categories
        'labels'            => $labels,
        'show_ui'           => true,
        'show_admin_column' => true,
        'query_var'         => true,
        'rewrite'           => array('slug' => 'genre'), // URL slug for genres
    );

    // Register the taxonomy for 'portfolio' post type
    register_taxonomy('genre', 'portfolio', $args);
}
add_action('init', 'register_portfolio_genres_taxonomy');

/**
 * Register 'portfolio' custom post type.
 */
function register_portfolio_post_type() {
    // Labels for the post type
    $labels = array(
        'name'                  => 'Portfolios',
        'singular_name'         => 'Portfolio',
        'menu_name'             => 'Portfolios',
        'name_admin_bar'        => 'Portfolio',
        'add_new'               => 'Add New',
        'add_new_item'          => 'Add New Portfolio',
        'edit_item'             => 'Edit Portfolio',
        'new_item'              => 'New Portfolio',
        'view_item'             => 'View Portfolio',
        'search_items'          => 'Search Portfolios',
        'not_found'             => 'No portfolios found.',
        'not_found_in_trash'    => 'No portfolios found in trash.',
        'all_items'             => 'All Portfolios',
        'archives'              => 'Portfolio Archives',
        'insert_into_item'      => 'Insert into portfolio',
        'uploaded_to_this_item' => 'Uploaded to this portfolio',
    );

    // Arguments for the post type
    $args = array(
        'labels'             => $labels,
        'public'             => true,
        'exclude_from_search' => false,
        'publicly_queryable' => true,
        'show_ui'            => true,
        'show_in_menu'       => true,
        'menu_position'      => 5,
        'menu_icon'          => 'dashicons-portfolio', // Dashicon for portfolio
        'capability_type'    => 'post',
        'hierarchical'       => false,
        'supports'           => array('title', 'editor', 'thumbnail', 'excerpt', 'custom-fields'),
        'has_archive'        => true,
        'rewrite'            => array('slug' => 'portfolio'),
        'query_var'          => true,
    );

    // Register the post type
    register_post_type('portfolio', $args);
}
add_action('init', 'register_portfolio_post_type');

/**
 * Add Genre filter to Admin Portfolio List.
 */
function add_genre_filter_to_portfolio_admin($post_type, $which) {
    if ('portfolio' !== $post_type) {
        return;
    }

    $taxonomy = 'genre';
    $genres = get_terms(array('taxonomy' => $taxonomy, 'hide_empty' => false));

    if (!empty($genres)) {
        echo '<select name="' . esc_attr($taxonomy) . '" id="' . esc_attr($taxonomy) . '" class="postform">';
        echo '<option value="">' . esc_html__('All Genres', 'textdomain') . '</option>';
        foreach ($genres as $genre) {
            $selected = (isset($_GET[$taxonomy]) && $_GET[$taxonomy] === $genre->slug) ? ' selected="selected"' : '';
            echo '<option value="' . esc_attr($genre->slug) . '"' . $selected . '>' . esc_html($genre->name) . '</option>';
        }
        echo '</select>';
    }
}
add_action('restrict_manage_posts', 'add_genre_filter_to_portfolio_admin', 10, 2);

/**
 * Enqueue styles for portfolio genre customization (if needed).
 */
function enqueue_portfolio_genre_styles() {
    if (is_post_type_archive('portfolio') || is_singular('portfolio')) {
        wp_enqueue_style('portfolio-genres-style', plugin_dir_url(__FILE__) . 'css/portfolio-genres.css');
    }
}
add_action('wp_enqueue_scripts', 'enqueue_portfolio_genre_styles');

/**
 * Flush rewrite rules on plugin activation.
 */
function custom_portfolio_genres_activate() {
    register_portfolio_post_type();
    register_portfolio_genres_taxonomy();
    flush_rewrite_rules(); // Ensure new URLs work immediately
}
register_activation_hook(__FILE__, 'custom_portfolio_genres_activate');

/**
 * Flush rewrite rules on plugin deactivation.
 */
function custom_portfolio_genres_deactivate() {
    flush_rewrite_rules();
}
register_deactivation_hook(__FILE__, 'custom_portfolio_genres_deactivate');

?>
```
