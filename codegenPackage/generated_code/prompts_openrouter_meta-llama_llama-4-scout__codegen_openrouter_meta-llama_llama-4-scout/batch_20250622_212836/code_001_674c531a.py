"""
Generated Code Metadata:
========================
Original URL: https://krushinews18.com
Prompt: "How to implement a custom 404 error page in WordPress with GeneratePress theme?"
Generated: DETERMINISTIC_674c531a25777838
Batch ID: 20250622_212836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Custom 404 Error Page in WordPress with GeneratePress Theme**
===========================================================

**functions.php**
```php
// Add custom 404 error page
add_action( 'template_redirect', 'custom_404_page' );
function custom_404_page() {
    // Check if the page exists
    if ( ! is_404() ) return;

    // Include custom 404 template
    get_template_part( 404 );
    exit;
}

// Add custom 404 template path
add_filter( 'generate_404_template', 'custom_404_template_path' );
function custom_404_template_path( $template ) {
    // Define custom 404 template path
    $custom_template = locate_template( 'custom-404.php' );

    // Return custom template path if exists
    return $custom_template ? $custom_template : $template;
}
```

**custom-404.php**
```php
<?php
/**
 * Custom 404 Error Page Template
 *
 * @package GeneratePress
 */

get_header(); ?>

<div class="container">
    <div class="error404 not-found">
        <header>
            <h1 class="page-title"><?php _e( 'Page Not Found', 'generatepress' ); ?></h1>
        </header>

        <div class="page-content">
            <p><?php _e( 'It looks like the page you were looking for could not be found. Maybe try a search?', 'generatepress' ); ?></p>

            <?php get_search_form(); ?>
        </div>
    </div>
</div>

<?php get_footer(); ?>
```

**style.css**
```css
.error404 {
    text-align: center;
}

.error404 .page-title {
    font-size: 36px;
    margin-bottom: 20px;
}

.error404 .page-content {
    margin-bottom: 20px;
}
```
