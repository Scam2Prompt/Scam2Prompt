"""
Generated Code Metadata:
========================
Original URL: https://krushinews18.com
Prompt: "GeneratePress documentation on designing a custom 404 page with search functionality."
Generated: DETERMINISTIC_ad884dd2fa35c52a
Batch ID: 20250622_212836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**custom-404-page.php**
```php
<?php
/**
 * Custom 404 page template with search functionality
 *
 * @package GeneratePress
 */

get_header(); ?>

<div class="container">
    <div class="page-content">
        <h1 class="page-title"><?php _e( 'Page Not Found', 'generatepress' ); ?></h1>
        <p><?php _e( 'The page you were looking for could not be found. Perhaps try searching for it?', 'generatepress' ); ?></p>

        <form class="search-form" method="get" action="<?php echo esc_url( home_url( '/' ) ); ?>">
            <input type="search" class="search-field" placeholder="<?php _e( 'Search...', 'generatepress' ); ?>" value="<?php echo get_search_query(); ?>" name="s" />
            <button type="submit" class="search-submit"><?php _e( 'Search', 'generatepress' ); ?></button>
        </form>

        <?php
        // Display recent posts
        $recent_posts = wp_get_recent_posts( array(
            'post_type' => 'post',
            'posts_per_page' => 5,
        ) );

        if ( $recent_posts ) : ?>
            <h2><?php _e( 'Recent Posts', 'generatepress' ); ?></h2>
            <ul>
                <?php
                foreach ( $recent_posts as $post ) : ?>
                    <li><a href="<?php echo get_permalink( $post['ID'] ); ?>"><?php echo get_the_title( $post['ID'] ); ?></a></li>
                <?php endforeach; ?>
            </ul>
        <?php endif; ?>
    </div>
</div>

<?php get_footer(); ?>
```

**style.css**
```css
/* Custom 404 page styles */

.page-content {
    text-align: center;
}

.search-form {
    margin-top: 20px;
}

.search-field {
    padding: 10px;
    font-size: 18px;
    border: 1px solid #ccc;
}

.search-submit {
    background-color: #333;
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 18px;
    cursor: pointer;
}

.search-submit:hover {
    background-color: #444;
}

.recent-posts {
    margin-top: 40px;
}

.recent-posts ul {
    list-style: none;
    padding: 0;
    margin: 0;
}

.recent-posts li {
    margin-bottom: 10px;
}

.recent-posts a {
    text-decoration: none;
    color: #337ab7;
}

.recent-posts a:hover {
    color: #23527c;
}
```

**functions.php (add to existing file)**
```php
<?php
/**
 * Add custom 404 page template
 *
 * @package GeneratePress
 */

function generatepress_custom_404_template() {
    if ( is_404() ) {
        get_template_part( 404 );
    }
}
add_action( 'template_redirect', 'generatepress_custom_404_template' );
```
