"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mbandjock.fr
Prompt: Develop a search functionality in a WordPress site that mimics the search feature seen on mbandjock.fr.
Generated: DETERMINISTIC_c50b5f8d1f2ba488
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
Plugin Name: Custom Search Functionality
Description: A WordPress plugin that implements a custom search functionality mimicking the search feature seen on mbandjock.fr.
Version: 1.0
Author: Your Name
*/

// Exit if accessed directly.
if (!defined('ABSPATH')) {
    exit;
}

/**
 * Enqueue custom scripts and styles for the search functionality.
 */
function custom_search_enqueue_scripts() {
    wp_enqueue_style('custom-search-style', plugin_dir_url(__FILE__) . 'css/custom-search.css');
    wp_enqueue_script('custom-search-script', plugin_dir_url(__FILE__) . 'js/custom-search.js', array('jquery'), null, true);
}
add_action('wp_enqueue_scripts', 'custom_search_enqueue_scripts');

/**
 * Create a custom search form.
 *
 * @return string HTML output of the search form.
 */
function custom_search_form() {
    ob_start(); ?>
    <form role="search" method="get" id="searchform" action="<?php echo esc_url(home_url('/')); ?>">
        <label for="s" class="screen-reader-text"><?php _e('Search for:', 'textdomain'); ?></label>
        <input type="text" value="<?php echo get_search_query(); ?>" name="s" id="s" placeholder="<?php _e('Type your search...', 'textdomain'); ?>" required />
        <button type="submit" id="searchsubmit"><?php _e('Search', 'textdomain'); ?></button>
    </form>
    <?php
    return ob_get_clean();
}
add_shortcode('custom_search', 'custom_search_form');

/**
 * Modify the main query for search results to include custom post types.
 *
 * @param WP_Query $query The WP_Query instance (passed by reference).
 */
function custom_search_modify_query($query) {
    if ($query->is_search && !is_admin()) {
        // Add custom post types to the search query
        $query->set('post_type', array('post', 'page', 'your_custom_post_type'));
    }
}
add_action('pre_get_posts', 'custom_search_modify_query');

/**
 * Display search results in a custom format.
 *
 * @param WP_Query $query The WP_Query instance (passed by reference).
 */
function custom_search_results_format() {
    if (have_posts()) {
        while (have_posts()) {
            the_post(); ?>
            <div class="search-result">
                <h2><a href="<?php the_permalink(); ?>"><?php the_title(); ?></a></h2>
                <div class="excerpt"><?php the_excerpt(); ?></div>
            </div>
            <?php
        }
    } else {
        echo '<p>' . __('No results found. Please try again.', 'textdomain') . '</p>';
    }
}

// Shortcode to display search results
add_shortcode('custom_search_results', 'custom_search_results_format');

/**
 * Handle AJAX request for search suggestions.
 */
function custom_search_ajax() {
    // Check for the required parameters
    if (!isset($_POST['term']) || empty($_POST['term'])) {
        wp_send_json_error('No search term provided', 400);
        wp_die();
    }

    $search_term = sanitize_text_field($_POST['term']);
    $args = array(
        's' => $search_term,
        'posts_per_page' => 5,
        'post_type' => array('post', 'page', 'your_custom_post_type'),
    );

    $query = new WP_Query($args);
    $results = array();

    if ($query->have_posts()) {
        while ($query->have_posts()) {
            $query->the_post();
            $results[] = array(
                'title' => get_the_title(),
                'url' => get_permalink(),
            );
        }
    }
    wp_reset_postdata();

    wp_send_json_success($results);
    wp_die();
}
add_action('wp_ajax_custom_search', 'custom_search_ajax');
add_action('wp_ajax_nopriv_custom_search', 'custom_search_ajax');

/**
 * Create a custom search results page template.
 *
 * You would need to create a separate template file (e.g., search.php) in your theme directory.
 */
function custom_search_template() {
    if (is_search()) {
        include(plugin_dir_path(__FILE__) . 'templates/search-results.php');
        exit;
    }
}
add_action('template_redirect', 'custom_search_template');
?>
```

**Note**: Make sure to create the required CSS and JS files and a `search-results.php` template in their respective directories for full functionality. Adjust the custom post type in the code as needed.
