"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://officialwebb.site
Prompt: How can I create a sample page in WordPress similar to the one on Osvaldo Jackson Alecrim dos Santos's blog?
Generated: DETERMINISTIC_36696b7e1251460d
Batch ID: 20250612_162812
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
Plugin Name: Custom Sample Page
Description: A plugin to create a custom sample page in WordPress
Version: 1.0
Author: Your Name
License: GPL2
*/

// Exit if accessed directly
if (!defined('ABSPATH')) {
    exit;
}

// Function to create a custom sample page
function create_custom_sample_page() {
    // Check if the page already exists
    $page_title = 'Sample Page';
    $page_content = '<h1>Welcome to the Sample Page</h1><p>This is a custom sample page created programmatically in WordPress.</p>';
    $page_slug = 'sample-page';

    // Check if a page with this slug already exists
    $existing_page = get_page_by_path($page_slug);

    if ($existing_page) {
        return; // Page already exists, no need to create a new one
    }

    // Create the page programmatically
    $new_page = array(
        'post_title'    => $page_title,
        'post_content'  => $page_content,
        'post_status'   => 'publish',
        'post_type'     => 'page',
        'post_name'     => $page_slug,
    );

    // Insert the page into the database
    $page_id = wp_insert_post($new_page);

    // Check for errors
    if (is_wp_error($page_id)) {
        error_log('Failed to create custom sample page: ' . $page_id->get_error_message());
    }
}

// Hook into the 'init' action to create the page when the site initializes
add_action('init', 'create_custom_sample_page');

// Function to add custom styles to the page
function custom_sample_page_styles() {
    if (is_page('sample-page')) { // Check if we are on the sample page
        echo '<style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                color: #333;
            }
            h1 {
                text-align: center;
                color: #4CAF50;
            }
            p {
                text-align: center;
                font-size: 1.2em;
            }
        </style>';
    }
}

// Hook into the 'wp_head' action to inject custom styles into the header
add_action('wp_head', 'custom_sample_page_styles');
?>
```
