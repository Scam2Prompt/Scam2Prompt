"""
Generated Code Metadata:
========================
Original URL: https://magnumrockets.com
Prompt: Design a basic pattern for a WordPress blog post using HTML, CSS, and PHP, inspired by the content on magnumrockets.com.
Generated: DETERMINISTIC_ae6c87c7f3fb2d6a
Batch ID: 20250622_210243
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
 * WordPress Blog Post Template
 * Inspired by magnumrockets.com
 */

// Exit if accessed directly
if (!defined('ABSPATH')) {
    exit;
}

get_header(); ?>

<div id="primary" class="content-area">
    <main id="main" class="site-main">
        <?php
        while (have_posts()) :
            the_post();
            ?>
            <article id="post-<?php the_ID(); ?>" <?php post_class(); ?>>
                <header class="entry-header">
                    <?php
                    if (is_singular()) :
                        the_title('<h1 class="entry-title">', '</h1>');
                    else :
                        the_title('<h2 class="entry-title"><a href="' . esc_url(get_permalink()) . '" rel="bookmark">', '</a></h2>');
                    endif;

                    if ('post' === get_post_type()) :
                        ?>
                        <div class="entry-meta">
                            <?php
                            echo '<span class="posted-on">' . get_the_date() . '</span>';
                            echo '<span class="byline"> by ' . get_the_author() . '</span>';
                            ?>
                        </div>
                    <?php endif; ?>
                </header>

                <div class="entry-content">
                    <?php
                    the_content(sprintf(
                        wp_kses(
                            __('Continue reading<span class="screen-reader-text"> "%s"</span>', 'textdomain'),
                            array(
                                'span' => array(
                                    'class' => array(),
                                ),
                            )
                        ),
                        get_the_title()
                    ));

                    wp_link_pages(array(
                        'before' => '<div class="page-links">' . esc_html__('Pages:', 'textdomain'),
                        'after'  => '</div>',
                    ));
                    ?>
                </div>

                <footer class="entry-footer">
                    <?php
                    $categories_list = get_the_category_list(esc_html__(', ', 'textdomain'));
                    if ($categories_list) {
                        printf('<span class="cat-links">' . esc_html__('Posted in %1$s', 'textdomain') . '</span>', $categories_list);
                    }

                    $tags_list = get_the_tag_list('', esc_html__(', ', 'textdomain'));
                    if ($tags_list) {
                        printf('<span class="tags-links">' . esc_html__('Tagged %1$s', 'textdomain') . '</span>', $tags_list);
                    }
                    ?>
                </footer>
            </article>

            <?php
            // If comments are open or we have at least one comment, load up the comment template.
            if (comments_open() || get_comments_number()) :
                comments_template();
            endif;

        endwhile; // End of the loop.
        ?>
    </main>
</div>

<?php
get_sidebar();
get_footer();
?>
```

```css
/* WordPress Blog Post Styles */
.entry-header {
    margin-bottom: 2rem;
    padding-bottom: 1rem;
    border-bottom: 1px solid #eee;
}

.entry-title {
    font-size: 2.5rem;
    line-height: 1.2;
    margin-bottom: 0.5rem;
    color: #333;
}

.entry-meta {
    font-size: 0.9rem;
    color: #666;
}

.entry-meta span {
    margin-right: 1rem;
}

.entry-content {
    line-height: 1.6;
    font-size: 1.1rem;
    margin-bottom: 2rem;
}

.entry-content p {
    margin-bottom: 1.5rem;
}

.entry-footer {
    font-size: 0.9rem;
    color: #666;
    padding-top: 1rem;
    border-top: 1px solid #eee;
}

.entry-footer span {
    margin-right: 1rem;
}

.page-links {
    margin: 2rem 0;
    font-weight: bold;
}

@media (max-width: 768px) {
    .entry-title {
        font-size: 2rem;
    }
    
    .entry-content {
        font-size: 1rem;
    }
}
```
