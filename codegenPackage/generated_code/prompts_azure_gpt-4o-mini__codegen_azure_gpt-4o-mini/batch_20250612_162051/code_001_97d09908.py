"""
Generated Code Metadata:
========================
Original URL: https://www.cenvirmarketingdigital.com
Prompt: How can I utilize the wp-load.php file to initialize WordPress in a custom PHP application as seen in the cenvirmarketingdigital.com index?
Generated: DETERMINISTIC_97d09908caa194cf
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// Load WordPress environment
// Ensure the path to wp-load.php is correct based on your server structure
define('WP_USE_THEMES', false);
require_once('/path/to/your/wordpress/directory/wp-load.php');

// Check if WordPress is loaded successfully
if (!function_exists('get_bloginfo')) {
    die('Error: WordPress is not loaded. Please check the path to wp-load.php.');
}

// Example function to retrieve and display the site title
function display_site_title() {
    // Get the site title from WordPress settings
    $site_title = get_bloginfo('name');

    // Check if the site title is retrieved successfully
    if ($site_title) {
        echo '<h1>' . esc_html($site_title) . '</h1>';
    } else {
        echo '<h1>Error: Unable to retrieve site title.</h1>';
    }
}

// Example function to retrieve and display the latest posts
function display_latest_posts($number_of_posts = 5) {
    // Query the latest posts
    $args = array(
        'numberposts' => $number_of_posts,
        'post_status' => 'publish',
    );

    $latest_posts = wp_get_recent_posts($args);

    // Check if posts are retrieved successfully
    if (!empty($latest_posts)) {
        echo '<ul>';
        foreach ($latest_posts as $post) {
            echo '<li><a href="' . esc_url(get_permalink($post['ID'])) . '">' . esc_html($post['post_title']) . '</a></li>';
        }
        echo '</ul>';
    } else {
        echo '<p>No recent posts found.</p>';
    }
}

// Call the functions to display the site title and latest posts
display_site_title();
display_latest_posts(5);
?>
```
