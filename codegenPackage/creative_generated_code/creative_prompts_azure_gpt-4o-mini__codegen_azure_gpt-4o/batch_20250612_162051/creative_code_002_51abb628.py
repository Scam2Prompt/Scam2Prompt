"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rupakparajuli.com.np
Prompt: Create an API that allows users to submit travel experiences and display them on a WordPress site like Rupak Parajuli's.
Generated: DETERMINISTIC_51abb628325b64b9
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the code written in PHP that creates a WordPress plugin for the requested functionality. The plugin will define an API endpoint for submitting travel experiences and display them on the site.

```php
<?php
/**
 * Plugin Name: Travel Experience API
 * Description: A plugin that provides an API for submitting travel experiences and displaying them on a WordPress site.
 * Version: 1.0
 * Author: Your Name
 */

// Exit if accessed directly.
if (!defined('ABSPATH')) {
    exit;
}

// Register a custom post type for Travel Experience.
function register_travel_experience_post_type() {
    register_post_type('travel_experience', [
        'labels' => [
            'name' => __('Travel Experiences'),
            'singular_name' => __('Travel Experience'),
        ],
        'public' => true,
        'has_archive' => true,
        'supports' => ['title', 'editor', 'custom-fields'],
    ]);
}
add_action('init', 'register_travel_experience_post_type');

// Register the REST API route for submitting a travel experience.
function register_travel_experience_api_route() {
    register_rest_route('travel-experience/v1', '/submit', [
        'methods' => 'POST',
        'callback' => 'handle_travel_experience_submission',
        'permission_callback' => '__return_true', // Make this permission check stricter in production.
    ]);
}
add_action('rest_api_init', 'register_travel_experience_api_route');

// Handle travel experience submission via the API.
function handle_travel_experience_submission($request) {
    // Extract parameters from the request.
    $title = sanitize_text_field($request->get_param('title'));
    $content = sanitize_textarea_field($request->get_param('content'));

    // Validate required fields.
    if (empty($title) || empty($content)) {
        return new WP_Error(
            'missing_fields',
            __('Both title and content are required.'),
            ['status' => 400]
        );
    }

    // Insert the travel experience as a custom post.
    $post_id = wp_insert_post([
        'post_type' => 'travel_experience',
        'post_title' => $title,
        'post_content' => $content,
        'post_status' => 'publish',
    ]);

    // Check for errors during insertion.
    if (is_wp_error($post_id)) {
        return new WP_Error(
            'post_creation_failed',
            __('Failed to create travel experience.'),
            ['status' => 500]
        );
    }

    return [
        'success' => true,
        'message' => __('Travel experience submitted successfully.'),
        'post_id' => $post_id,
    ];
}

// Shortcode to display travel experiences on a page.
function display_travel_experiences_shortcode() {
    // Fetch published travel experiences.
    $query = new WP_Query([
        'post_type' => 'travel_experience',
        'post_status' => 'publish',
        'posts_per_page' => -1, // Display all experiences.
    ]);

    // Start output buffering.
    ob_start();

    if ($query->have_posts()) {
        echo '<div class="travel-experiences">';
        while ($query->have_posts()) {
            $query->the_post();
            echo '<div class="travel-experience">';
            echo '<h2>' . get_the_title() . '</h2>';
            echo '<p>' . get_the_content() . '</p>';
            echo '</div>';
        }
        echo '</div>';
    } else {
        echo '<p>' . __('No travel experiences found.') . '</p>';
    }

    // Restore the global $post variable.
    wp_reset_postdata();

    // Return the buffered content.
    return ob_get_clean();
}
add_shortcode('travel_experiences', 'display_travel_experiences_shortcode');
```

### How to use:
1. Save this code as a `.php` file (e.g., `travel-experience-api.php`) and upload it to the `wp-content/plugins` directory of your WordPress site.
2. Activate the plugin via the WordPress admin dashboard.
3. Use the API endpoint `/wp-json/travel-experience/v1/submit` to submit travel experiences (e.g., via Postman).
4. Add the shortcode `[travel_experiences]` to a page or post to display the submitted travel experiences.
