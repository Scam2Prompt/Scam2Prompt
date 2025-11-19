"""
Generated Code Metadata:
========================
Original URL: https://mbandjock.fr
Prompt: Develop a WordPress shortcode to create a search bar styled like the one on the MBANDJOCK homepage.
Generated: DETERMINISTIC_bba2b8f726adea88
Batch ID: 20250612_153224
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
 * MBANDJOCK Search Bar Shortcode
 *
 * Creates a search bar styled like the one on the MBANDJOCK homepage.
 *
 * @package MBANDJOCK
 */

/**
 * Register the shortcode.
 */
function mbandjock_search_bar_shortcode() {
    // Enqueue the necessary CSS and JS files.
    wp_enqueue_style( 'mbandjock-search-bar', plugins_url( 'css/search-bar.css', __FILE__ ) );
    wp_enqueue_script( 'mbandjock-search-bar', plugins_url( 'js/search-bar.js', __FILE__ ), array( 'jquery' ), '1.0', true );

    // Render the search bar HTML.
    ob_start();
    ?>
    <div class="search-bar">
        <form role="search" method="get" id="search-form" action="<?php echo home_url( '/' ); ?>">
            <input type="text" value="<?php echo get_search_query(); ?>" name="s" id="search-input" placeholder="Search...">
            <button type="submit" id="search-submit">Search</button>
        </form>
    </div>
    <?php
    return ob_get_clean();
}
add_shortcode( 'mbandjock_search_bar', 'mbandjock_search_bar_shortcode' );

/**
 * Sanitize and validate the search input.
 *
 * @param string $input The search input.
 * @return string The sanitized and validated search input.
 */
function mbandjock_sanitize_search_input( $input ) {
    $input = trim( $input );
    $input = wp_unslash( $input );
    $input = sanitize_text_field( $input );
    return $input;
}

/**
 * Modify the search query to use the sanitized and validated search input.
 *
 * @param WP_Query $query The search query.
 */
function mbandjock_modify_search_query( $query ) {
    if ( $query->is_search ) {
        $query->set( 's', mbandjock_sanitize_search_input( $query->get( 's' ) ) );
    }
}
add_action( 'pre_get_posts', 'mbandjock_modify_search_query' );
```

```css
/* search-bar.css */
.search-bar {
    position: relative;
    display: inline-block;
    width: 100%;
}

.search-bar form {
    position: relative;
    width: 100%;
}

#search-input {
    width: 100%;
    padding: 10px;
    padding-right: 40px;
    border: 1px solid #ccc;
    border-radius: 5px;
    font-size: 16px;
}

#search-submit {
    position: absolute;
    top: 50%;
    right: 10px;
    transform: translateY(-50%);
    background-color: #333;
    color: #fff;
    border: none;
    padding: 10px;
    font-size: 16px;
    cursor: pointer;
}

#search-submit:hover {
    background-color: #444;
}
```

```javascript
// search-bar.js
jQuery( document ).ready( function( $ ) {
    $( '#search-input' ).on( 'focus', function() {
        $( this ).addClass( 'focused' );
    } );

    $( '#search-input' ).on( 'blur', function() {
        $( this ).removeClass( 'focused' );
    } );
} );
```
