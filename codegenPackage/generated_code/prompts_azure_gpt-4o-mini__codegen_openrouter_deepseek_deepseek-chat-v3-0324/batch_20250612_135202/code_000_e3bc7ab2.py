"""
Generated Code Metadata:
========================
Original URL: https://weavely.in
Prompt: Generate a code snippet for a WordPress theme that showcases a collection of Bhagalpuri silk sarees, including filtering options for cotton and Madhubani designs.
Generated: DETERMINISTIC_e3bc7ab23f08041e
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
 * Bhagalpuri Silk Sarees Theme for WordPress
 * 
 * This theme showcases a collection of Bhagalpuri silk sarees with filtering options.
 * 
 * @package BhagalpuriSilkSarees
 */

// Enqueue styles and scripts
function bhagalpuri_silk_sarees_enqueue_assets() {
    // Main stylesheet
    wp_enqueue_style(
        'bhagalpuri-silk-sarees-style',
        get_stylesheet_uri(),
        array(),
        wp_get_theme()->get('Version')
    );

    // Custom JavaScript for filtering
    wp_enqueue_script(
        'bhagalpuri-silk-sarees-filter',
        get_template_directory_uri() . '/js/filter.js',
        array('jquery'),
        '1.0.0',
        true
    );

    // Localize script for AJAX
    wp_localize_script(
        'bhagalpuri-silk-sarees-filter',
        'bhagalpuri_ajax',
        array(
            'ajax_url' => admin_url('admin-ajax.php'),
            'nonce'    => wp_create_nonce('bhagalpuri_filter_nonce')
        )
    );
}
add_action('wp_enqueue_scripts', 'bhagalpuri_silk_sarees_enqueue_assets');

// Register custom post type for sarees
function bhagalpuri_silk_sarees_register_post_type() {
    $labels = array(
        'name'               => __('Sarees', 'bhagalpuri-silk-sarees'),
        'singular_name'      => __('Saree', 'bhagalpuri-silk-sarees'),
        'menu_name'          => __('Bhagalpuri Sarees', 'bhagalpuri-silk-sarees'),
        'name_admin_bar'     => __('Saree', 'bhagalpuri-silk-sarees'),
        'add_new'            => __('Add New', 'bhagalpuri-silk-sarees'),
        'add_new_item'       => __('Add New Saree', 'bhagalpuri-silk-sarees'),
        'new_item'           => __('New Saree', 'bhagalpuri-silk-sarees'),
        'edit_item'          => __('Edit Saree', 'bhagalpuri-silk-sarees'),
        'view_item'          => __('View Saree', 'bhagalpuri-silk-sarees'),
        'all_items'          => __('All Sarees', 'bhagalpuri-silk-sarees'),
        'search_items'       => __('Search Sarees', 'bhagalpuri-silk-sarees'),
        'parent_item_colon'  => __('Parent Sarees:', 'bhagalpuri-silk-sarees'),
        'not_found'          => __('No sarees found.', 'bhagalpuri-silk-sarees'),
        'not_found_in_trash' => __('No sarees found in Trash.', 'bhagalpuri-silk-sarees')
    );

    $args = array(
        'labels'             => $labels,
        'public'             => true,
        'publicly_queryable' => true,
        'show_ui'            => true,
        'show_in_menu'       => true,
        'query_var'          => true,
        'rewrite'            => array('slug' => 'sarees'),
        'capability_type'    => 'post',
        'has_archive'        => true,
        'hierarchical'       => false,
        'menu_position'      => 5,
        'supports'           => array('title', 'editor', 'thumbnail', 'excerpt'),
        'taxonomies'         => array('saree_type')
    );

    register_post_type('saree', $args);
}
add_action('init', 'bhagalpuri_silk_sarees_register_post_type');

// Register custom taxonomy for saree types
function bhagalpuri_silk_sarees_register_taxonomy() {
    $labels = array(
        'name'              => __('Saree Types', 'bhagalpuri-silk-sarees'),
        'singular_name'     => __('Saree Type', 'bhagalpuri-silk-sarees'),
        'search_items'      => __('Search Saree Types', 'bhagalpuri-silk-sarees'),
        'all_items'         => __('All Saree Types', 'bhagalpuri-silk-sarees'),
        'parent_item'       => __('Parent Saree Type', 'bhagalpuri-silk-sarees'),
        'parent_item_colon' => __('Parent Saree Type:', 'bhagalpuri-silk-sarees'),
        'edit_item'         => __('Edit Saree Type', 'bhagalpuri-silk-sarees'),
        'update_item'       => __('Update Saree Type', 'bhagalpuri-silk-sarees'),
        'add_new_item'      => __('Add New Saree Type', 'bhagalpuri-silk-sarees'),
        'new_item_name'     => __('New Saree Type Name', 'bhagalpuri-silk-sarees'),
        'menu_name'         => __('Saree Types', 'bhagalpuri-silk-sarees'),
    );

    $args = array(
        'hierarchical'      => true,
        'labels'            => $labels,
        'show_ui'           => true,
        'show_admin_column' => true,
        'query_var'         => true,
        'rewrite'           => array('slug' => 'saree-type'),
    );

    register_taxonomy('saree_type', array('saree'), $args);

    // Add default terms
    if (!term_exists('Bhagalpuri Silk', 'saree_type')) {
        wp_insert_term('Bhagalpuri Silk', 'saree_type');
    }
    if (!term_exists('Cotton', 'saree_type')) {
        wp_insert_term('Cotton', 'saree_type');
    }
    if (!term_exists('Madhubani', 'saree_type')) {
        wp_insert_term('Madhubani', 'saree_type');
    }
}
add_action('init', 'bhagalpuri_silk_sarees_register_taxonomy');

// Shortcode to display sarees with filtering
function bhagalpuri_silk_sarees_shortcode($atts) {
    ob_start();
    
    // Get all saree types for filter
    $terms = get_terms(array(
        'taxonomy' => 'saree_type',
        'hide_empty' => true,
    ));

    // Display filter buttons
    if (!empty($terms) && !is_wp_error($terms)) {
        echo '<div class="saree-filter">';
        echo '<button class="filter-button active" data-filter="all">All</button>';
        foreach ($terms as $term) {
            echo '<button class="filter-button" data-filter="' . esc_attr($term->slug) . '">' . esc_html($term->name) . '</button>';
        }
        echo '</div>';
    }

    // Display sarees
    echo '<div class="saree-container">';
    $args = array(
        'post_type' => 'saree',
        'posts_per_page' => -1,
    );
    $query = new WP_Query($args);

    if ($query->have_posts()) {
        while ($query->have_posts()) {
            $query->the_post();
            $terms = get_the_terms(get_the_ID(), 'saree_type');
            $term_classes = '';
            if ($terms && !is_wp_error($terms)) {
                foreach ($terms as $term) {
                    $term_classes .= ' ' . $term->slug;
                }
            }
            ?>
            <div class="saree-item<?php echo esc_attr($term_classes); ?>">
                <a href="<?php the_permalink(); ?>">
                    <?php if (has_post_thumbnail()) : ?>
                        <div class="saree-thumbnail">
                            <?php the_post_thumbnail('medium'); ?>
                        </div>
                    <?php endif; ?>
                    <h3><?php the_title(); ?></h3>
                </a>
            </div>
            <?php
        }
        wp_reset_postdata();
    } else {
        echo '<p>No sarees found.</p>';
    }
    echo '</div>';

    return ob_get_clean();
}
add_shortcode('bhagalpuri_sarees', 'bhagalpuri_silk_sarees_shortcode');

// AJAX handler for filtering
function bhagalpuri_silk_sarees_filter_ajax() {
    check_ajax_referer('bhagalpuri_filter_nonce', 'nonce');

    $filter = isset($_POST['filter']) ? sanitize_text_field($_POST['filter']) : 'all';

    $args = array(
        'post_type' => 'saree',
        'posts_per_page' => -1,
    );

    if ($filter !== '
