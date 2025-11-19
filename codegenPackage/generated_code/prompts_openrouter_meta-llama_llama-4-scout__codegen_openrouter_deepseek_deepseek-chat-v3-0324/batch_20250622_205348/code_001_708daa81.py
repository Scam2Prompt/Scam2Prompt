"""
Generated Code Metadata:
========================
Original URL: https://bloombinmaley.com
Prompt: "Generate a blog post about developing a tourism website using WordPress and the Rara Theme, inspired by Bloom Binmaley."
Generated: DETERMINISTIC_708daa817f50df23
Batch ID: 20250622_205348
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
 * Blog Post: Developing a Tourism Website Using WordPress and Rara Theme
 * Inspired by Bloom Binmaley
 */

// Register custom post type for tourism destinations
function register_tourism_destination_post_type() {
    $labels = array(
        'name'                  => 'Destinations',
        'singular_name'         => 'Destination',
        'menu_name'             => 'Tourism Destinations',
        'name_admin_bar'        => 'Tourism Destination',
        'add_new'               => 'Add New',
        'add_new_item'          => 'Add New Destination',
        'new_item'              => 'New Destination',
        'edit_item'             => 'Edit Destination',
        'view_item'             => 'View Destination',
        'all_items'             => 'All Destinations',
        'search_items'          => 'Search Destinations',
        'not_found'             => 'No destinations found.',
        'not_found_in_trash'    => 'No destinations found in Trash.'
    );

    $args = array(
        'labels'                => $labels,
        'public'                => true,
        'publicly_queryable'    => true,
        'show_ui'               => true,
        'show_in_menu'          => true,
        'query_var'             => true,
        'rewrite'               => array('slug' => 'destination'),
        'capability_type'       => 'post',
        'has_archive'           => true,
        'hierarchical'          => false,
        'menu_position'         => 5,
        'supports'              => array('title', 'editor', 'thumbnail', 'excerpt', 'comments'),
        'taxonomies'            => array('category', 'post_tag'),
        'menu_icon'             => 'dashicons-location-alt'
    );

    register_post_type('tourism_destination', $args);
}
add_action('init', 'register_tourism_destination_post_type');

// Customize Rara Theme for tourism website
function customize_rara_theme_for_tourism() {
    // Add custom CSS
    wp_enqueue_style('tourism-custom-css', get_stylesheet_directory_uri() . '/css/tourism-custom.css');

    // Register custom widgets
    register_sidebar(array(
        'name'          => 'Destination Sidebar',
        'id'            => 'destination-sidebar',
        'description'   => 'Widgets for destination pages',
        'before_widget' => '<div id="%1$s" class="widget %2$s">',
        'after_widget'  => '</div>',
        'before_title'  => '<h3 class="widget-title">',
        'after_title'   => '</h3>',
    ));

    // Add theme support for featured images
    add_theme_support('post-thumbnails');
    add_image_size('destination-thumbnail', 400, 300, true);
    add_image_size('destination-featured', 1200, 800, true);
}
add_action('after_setup_theme', 'customize_rara_theme_for_tourism');

// Create shortcode for featured destinations
function featured_destinations_shortcode($atts) {
    $atts = shortcode_atts(array(
        'count' => 3,
        'category' => ''
    ), $atts);

    $args = array(
        'post_type' => 'tourism_destination',
        'posts_per_page' => $atts['count'],
        'orderby' => 'rand'
    );

    if (!empty($atts['category'])) {
        $args['category_name'] = $atts['category'];
    }

    $query = new WP_Query($args);

    if ($query->have_posts()) {
        $output = '<div class="featured-destinations">';
        while ($query->have_posts()) {
            $query->the_post();
            $output .= '<div class="destination-card">';
            $output .= '<a href="' . get_permalink() . '">';
            $output .= get_the_post_thumbnail(get_the_ID(), 'destination-thumbnail');
            $output .= '<h3>' . get_the_title() . '</h3>';
            $output .= '</a>';
            $output .= '<p>' . get_the_excerpt() . '</p>';
            $output .= '</div>';
        }
        $output .= '</div>';
        wp_reset_postdata();
        return $output;
    } else {
        return '<p>No destinations found.</p>';
    }
}
add_shortcode('featured_destinations', 'featured_destinations_shortcode');

// Add custom meta box for destination details
function add_destination_meta_box() {
    add_meta_box(
        'destination_details',
        'Destination Details',
        'render_destination_meta_box',
        'tourism_destination',
        'normal',
        'high'
    );
}
add_action('add_meta_boxes', 'add_destination_meta_box');

function render_destination_meta_box($post) {
    wp_nonce_field('save_destination_details', 'destination_details_nonce');

    $location = get_post_meta($post->ID, '_destination_location', true);
    $opening_hours = get_post_meta($post->ID, '_destination_opening_hours', true);
    $entrance_fee = get_post_meta($post->ID, '_destination_entrance_fee', true);

    echo '<p><label for="destination_location">Location:</label>';
    echo '<input type="text" id="destination_location" name="destination_location" value="' . esc_attr($location) . '" class="widefat"></p>';

    echo '<p><label for="destination_opening_hours">Opening Hours:</label>';
    echo '<input type="text" id="destination_opening_hours" name="destination_opening_hours" value="' . esc_attr($opening_hours) . '" class="widefat"></p>';

    echo '<p><label for="destination_entrance_fee">Entrance Fee:</label>';
    echo '<input type="text" id="destination_entrance_fee" name="destination_entrance_fee" value="' . esc_attr($entrance_fee) . '" class="widefat"></p>';
}

function save_destination_meta_box($post_id) {
    if (!isset($_POST['destination_details_nonce']) || !wp_verify_nonce($_POST['destination_details_nonce'], 'save_destination_details')) {
        return;
    }

    if (defined('DOING_AUTOSAVE') && DOING_AUTOSAVE) {
        return;
    }

    if (!current_user_can('edit_post', $post_id)) {
        return;
    }

    if (isset($_POST['destination_location'])) {
        update_post_meta($post_id, '_destination_location', sanitize_text_field($_POST['destination_location']));
    }

    if (isset($_POST['destination_opening_hours'])) {
        update_post_meta($post_id, '_destination_opening_hours', sanitize_text_field($_POST['destination_opening_hours']));
    }

    if (isset($_POST['destination_entrance_fee'])) {
        update_post_meta($post_id, '_destination_entrance_fee', sanitize_text_field($_POST['destination_entrance_fee']));
    }
}
add_action('save_post', 'save_destination_meta_box');

// Display destination details in single template
function display_destination_details($content) {
    if (is_singular('tourism_destination')) {
        $location = get_post_meta(get_the_ID(), '_destination_location', true);
        $opening_hours = get_post_meta(get_the_ID(), '_destination_opening_hours', true);
        $entrance_fee = get_post_meta(get_the_ID(), '_destination_entrance_fee', true);

        $details = '<div class="destination-details">';
        $details .= '<h3>Destination Information</h3>';
        $details .= '<ul>';
        if ($location) $details .= '<li><strong>Location:</strong> ' . esc_html($location) . '</li>';
        if ($opening_hours) $details .= '<li><strong>Opening Hours:</strong> ' . esc_html($opening_hours) . '</li>';
        if ($entrance_fee) $details .= '<li><strong>Entrance Fee:</strong> ' . esc_html($entrance_fee) . '</li>';
        $details .= '</ul>';
        $details .= '</div>';

        return $content . $details;
    }
    return $content;
}
add_filter('the_content', 'display_destination_details');
```
