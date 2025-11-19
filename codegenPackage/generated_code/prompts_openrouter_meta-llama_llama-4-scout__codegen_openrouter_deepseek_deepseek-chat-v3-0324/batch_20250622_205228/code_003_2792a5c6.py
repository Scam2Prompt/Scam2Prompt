"""
Generated Code Metadata:
========================
Original URL: https://sajumavi.edu.pe
Prompt: Design a basic layout for a WordPress blog post about educational topics, incorporating a call-to-action to access a virtual classroom.
Generated: DETERMINISTIC_2792a5c6a2675d64
Batch ID: 20250622_205228
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
 * Template Name: Educational Blog Post Layout
 * Description: A custom layout for educational blog posts with a virtual classroom CTA.
 */

get_header(); ?>

<div id="primary" class="content-area">
    <main id="main" class="site-main" role="main">

        <?php
        while ( have_posts() ) : the_post();
            
            // Display featured image if available
            if ( has_post_thumbnail() ) {
                echo '<div class="featured-image">';
                the_post_thumbnail('large');
                echo '</div>';
            }
            ?>

            <article id="post-<?php the_ID(); ?>" <?php post_class(); ?>>
                <header class="entry-header">
                    <?php
                    the_title( '<h1 class="entry-title">', '</h1>' );
                    
                    // Display post meta (date, author, categories)
                    echo '<div class="entry-meta">';
                    echo '<span class="posted-on">' . get_the_date() . '</span>';
                    echo '<span class="byline"> by ' . get_the_author() . '</span>';
                    
                    $categories = get_the_category();
                    if ( ! empty( $categories ) ) {
                        echo '<span class="cat-links"> in ' . esc_html( $categories[0]->name ) . '</span>';
                    }
                    echo '</div>';
                    ?>
                </header>

                <div class="entry-content">
                    <?php
                    the_content();
                    
                    // Display virtual classroom CTA
                    echo '<div class="virtual-classroom-cta">';
                    echo '<h3>Ready to learn more?</h3>';
                    echo '<p>Join our virtual classroom for interactive lessons and discussions.</p>';
                    echo '<a href="' . esc_url( home_url( '/virtual-classroom' ) ) . '" class="cta-button">Access Virtual Classroom</a>';
                    echo '</div>';
                    
                    // Display related posts if available
                    if ( function_exists( 'yarpp_related' ) ) {
                        echo '<div class="related-posts">';
                        echo '<h3>Related Articles</h3>';
                        yarpp_related();
                        echo '</div>';
                    }
                    ?>
                </div>

                <footer class="entry-footer">
                    <?php
                    // Display tags if available
                    $tags = get_the_tags();
                    if ( $tags ) {
                        echo '<div class="tags-links">';
                        echo '<span>Tags: </span>';
                        foreach ( $tags as $tag ) {
                            echo '<a href="' . esc_url( get_tag_link( $tag->term_id ) ) . '">' . esc_html( $tag->name ) . '</a>';
                            if ( next( $tags ) ) {
                                echo ', ';
                            }
                        }
                        echo '</div>';
                    }
                    ?>
                </footer>
            </article>

            <?php
            // If comments are open or we have at least one comment, load up the comment template.
            if ( comments_open() || get_comments_number() ) :
                comments_template();
            endif;

        endwhile; // End of the loop.
        ?>

    </main><!-- #main -->
</div><!-- #primary -->

<?php
get_sidebar();
get_footer();
```


```css
/* Educational Blog Post Layout Styles */
.featured-image {
    margin-bottom: 2rem;
}

.featured-image img {
    width: 100%;
    height: auto;
    border-radius: 4px;
}

.entry-header {
    margin-bottom: 2rem;
}

.entry-title {
    font-size: 2.5rem;
    margin-bottom: 0.5rem;
}

.entry-meta {
    color: #666;
    font-size: 0.9rem;
    margin-bottom: 1rem;
}

.entry-meta span {
    margin-right: 1rem;
}

.virtual-classroom-cta {
    background-color: #f5f5f5;
    padding: 2rem;
    border-radius: 4px;
    margin: 3rem 0;
    text-align: center;
}

.virtual-classroom-cta h3 {
    margin-top: 0;
    color: #2c3e50;
}

.cta-button {
    display: inline-block;
    background-color: #3498db;
    color: white;
    padding: 0.8rem 1.5rem;
    text-decoration: none;
    border-radius: 4px;
    font-weight: bold;
    transition: background-color 0.3s;
}

.cta-button:hover {
    background-color: #2980b9;
}

.related-posts {
    margin: 3rem 0;
}

.tags-links {
    margin-top: 2rem;
    font-size: 0.9rem;
}

.tags-links a {
    color: #3498db;
    text-decoration: none;
}

.tags-links a:hover {
    text-decoration: underline;
}
```
