"""
Generated Code Metadata:
========================
Original URL: https://metamask.io.lirc.com.hk
Prompt: Write a WordPress sample page using the default theme, including a greeting and instructions for editing.
Generated: DETERMINISTIC_927f1dbe787e1bd7
Batch ID: 20250622_210231
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
 * Description: A sample WordPress page template that displays a greeting and instructions for editing.
 * 
 * @package WordPress
 * @subpackage Default_Theme
 */

// Exit if accessed directly.
if (!defined('ABSPATH')) {
    exit;
}

get_header(); // Include the header template.
?>

<div id="primary" class="content-area">
    <main id="main" class="site-main" role="main">
        <article id="post-<?php the_ID(); ?>" <?php post_class(); ?>>
            <header class="entry-header">
                <h1 class="entry-title"><?php esc_html_e('Welcome to the Sample Page', 'default-theme'); ?></h1>
            </header><!-- .entry-header -->

            <div class="entry-content">
                <p><?php esc_html_e('Hello! This is a sample page created using the default WordPress theme.', 'default-theme'); ?></p>
                <p><?php esc_html_e('To edit this page, log in to your WordPress admin dashboard, navigate to Pages, and select "Sample Page".', 'default-theme'); ?></p>
            </div><!-- .entry-content -->
        </article><!-- #post-<?php the_ID(); ?> -->
    </main><!-- #main -->
</div><!-- #primary -->

<?php
get_footer(); // Include the footer template.
?>
```
