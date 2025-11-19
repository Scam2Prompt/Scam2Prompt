"""
Generated Code Metadata:
========================
Original URL: https://officialwebb.site
Prompt: How can I create a sample page in WordPress similar to the one on Osvaldo Jackson Alecrim dos Santos's blog?
Generated: DETERMINISTIC_36696b7e1251460d
Batch ID: 20250612_162812
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
 * Template Name: Sample Page
 * Description: A custom page template similar to Osvaldo Jackson Alecrim dos Santos's blog.
 * Author: Your Name
 * Version: 1.0
 */

// Prevent direct access to the file
if (!defined('ABSPATH')) {
    exit; // Exit if accessed directly
}

// Get the header
get_header(); ?>

<div class="sample-page-container">
    <h1><?php the_title(); ?></h1>
    
    <?php
    // Start the loop to display the content
    if (have_posts()) :
        while (have_posts()) : the_post(); ?>
            <div class="post-content">
                <?php the_content(); // Display the content of the page ?>
            </div>
        <?php endwhile; // End of the loop
    else : ?>
        <p><?php esc_html_e('Sorry, no content found.', 'text-domain'); ?></p>
    <?php endif; ?>
</div>

<?php
// Get the sidebar if it exists
if (is_active_sidebar('sidebar-1')) {
    get_sidebar();
}

// Get the footer
get_footer();
?>
```

```css
/* Sample Page Styles */
.sample-page-container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
    background-color: #f9f9f9;
    border-radius: 8px;
}

.sample-page-container h1 {
    font-size: 2.5em;
    margin-bottom: 20px;
}

.post-content {
    font-size: 1.2em;
    line-height: 1.6;
}
```

```php
// functions.php - Enqueue styles for the sample page
function enqueue_sample_page_styles() {
    if (is_page_template('sample-page.php')) {
        wp_enqueue_style('sample-page-style', get_template_directory_uri() . '/css/sample-page.css');
    }
}
add_action('wp_enqueue_scripts', 'enqueue_sample_page_styles');
```

Make sure to create a file named `sample-page.php` in your theme directory and a CSS file named `sample-page.css` in a `css` folder within your theme directory. Adjust the paths as necessary based on your theme structure.
