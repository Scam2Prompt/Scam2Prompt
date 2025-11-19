"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://initiald.co.uk
Prompt: How can I create a WordPress site similar to the one found at initiald.co.uk, including setting up sample pages and posts?
Generated: DETERMINISTIC_7d7d8db04327c4db
Batch ID: 20250612_162535
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Functions.php file in the WordPress theme directory
// This script sets up a WordPress site with sample pages, posts, and basic configurations.

function setup_initiald_site() {
    // Check if the setup has already run to avoid duplicates
    if (get_option('initiald_site_setup_complete')) {
        return;
    }

    // Create sample pages
    $pages = [
        ['title' => 'Home', 'content' => 'Welcome to the Home Page!'],
        ['title' => 'About Us', 'content' => 'This is the About Us page.'],
        ['title' => 'Contact', 'content' => 'Feel free to reach out to us through this page.']
    ];

    foreach ($pages as $page) {
        // Check if the page already exists
        if (!get_page_by_title($page['title'])) {
            $page_id = wp_insert_post([
                'post_title'   => $page['title'],
                'post_content' => $page['content'],
                'post_status'  => 'publish',
                'post_type'    => 'page'
            ]);

            // Log an error if page insertion fails
            if (is_wp_error($page_id)) {
                error_log('Failed to create page: ' . $page['title']);
            }
        }
    }

    // Create sample posts
    $posts = [
        ['title' => 'Sample Post 1', 'content' => 'This is the content of Sample Post 1.'],
        ['title' => 'Sample Post 2', 'content' => 'Here is some content for Sample Post 2.']
    ];

    foreach ($posts as $post) {
        // Check if the post already exists
        if (!get_page_by_title($post['title'], 'OBJECT', 'post')) {
            $post_id = wp_insert_post([
                'post_title'   => $post['title'],
                'post_content' => $post['content'],
                'post_status'  => 'publish',
                'post_type'    => 'post'
            ]);

            // Log an error if post insertion fails
            if (is_wp_error($post_id)) {
                error_log('Failed to create post: ' . $post['title']);
            }
        }
    }

    // Set the homepage to the "Home" page
    $home_page = get_page_by_title('Home');
    if ($home_page) {
        update_option('page_on_front', $home_page->ID);
        update_option('show_on_front', 'page');
    }

    // Mark setup as complete
    update_option('initiald_site_setup_complete', true);
}

// Hook the setup function to run after theme activation
add_action('after_switch_theme', 'setup_initiald_site');
```

This code should be placed in the `functions.php` file of your active WordPress theme. When the theme is activated, it will automatically set up the sample pages and posts, configure the homepage, and ensure this setup runs only once to avoid duplications.
