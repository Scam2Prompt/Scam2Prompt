"""
Generated Code Metadata:
========================
Original URL: https://flashusdtgenerator.com
Prompt: "Write code to implement a 360° product viewer for WooCommerce, as described in the WoodMart theme features."
Generated: DETERMINISTIC_e696c4a62ee2b39a
Batch ID: 20250612_151141
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here is the code to implement a 360° product viewer for WooCommerce:
```php
// 360° Product Viewer for WooCommerce

// Enqueue required scripts and styles
function woodmart_360_product_viewer_scripts() {
    wp_enqueue_script( 'woodmart-360-viewer', get_template_directory_uri() . '/js/woodmart-360-viewer.js', array( 'jquery' ), '1.0', true );
    wp_enqueue_style( 'woodmart-360-viewer', get_template_directory_uri() . '/css/woodmart-360-viewer.css' );
}
add_action( 'wp_enqueue_scripts', 'woodmart_360_product_viewer_scripts' );

// Add 360° viewer to product page
function woodmart_360_product_viewer_shortcode() {
    $product = wc_get_product();
    if ( ! $product ) {
        return;
    }

    $images = $product->get_gallery_image_ids();
    if ( empty( $images ) ) {
        return;
    }

    $main_image_id = $product->get_image_id();
    $main_image_url = wp_get_attachment_image_src( $main_image_id, 'full' )[0];

    $viewer_html = '<div class="woodmart-360-viewer">';
    $viewer_html .= '<div class="viewer-container">';
    $viewer_html .= '<img src="' . $main_image_url . '" class="viewer-image">';
    $viewer_html .= '</div>';
    $viewer_html .= '<div class="viewer-thumbnails">';

    foreach ( $images as $image_id ) {
        $image_url = wp_get_attachment_image_src( $image_id, 'woocommerce_thumbnail' )[0];
        $viewer_html .= '<img src="' . $image_url . '" data-image-id="' . $image_id . '">';
    }

    $viewer_html .= '</div>';
    $viewer_html .= '</div>';

    return $viewer_html;
}
add_shortcode( 'woodmart_360_product_viewer', 'woodmart_360_product_viewer_shortcode' );

// Add shortcode to product page
function woodmart_360_product_viewer_add_to_product_page() {
    if ( is_product() ) {
        add_action( 'woocommerce_product_single_add_to_cart_text', 'woodmart_360_product_viewer_shortcode' );
    }
}
add_action( 'init', 'woodmart_360_product_viewer_add_to_product_page' );

// JavaScript code for 360° viewer
// woodmart-360-viewer.js
jQuery( document ).ready( function( $ ) {
    $( '.woodmart-360-viewer' ).each( function() {
        var viewerContainer = $( this ).find( '.viewer-container' );
        var viewerImage = $( this ).find( '.viewer-image' );
        var viewerThumbnails = $( this ).find( '.viewer-thumbnails' ).find( 'img' );

        viewerThumbnails.on( 'click', function() {
            var imageId = $( this ).data( 'image-id' );
            var imageUrl = wp.media.attachment( imageId ).url;
            viewerImage.attr( 'src', imageUrl );
        } );

        // Spin 360° viewer
        viewerImage.on( 'mousedown', function( e ) {
            var startX = e.clientX;
            var startY = e.clientY;
            var rotation = 0;

            $( document ).on( 'mousemove', function( e ) {
                rotation += ( e.clientX - startX ) * 0.1;
                startX = e.clientX;
                viewerImage.css( 'transform', 'rotateY(' + rotation + 'deg)' );
            } );

            $( document ).on( 'mouseup', function() {
                $( document ).off( 'mousemove' );
                $( document ).off( 'mouseup' );
            } );
        } );
    } );
} );
```
```css
/* woodmart-360-viewer.css */
.woodmart-360-viewer {
    position: relative;
    width: 500px;
    height: 500px;
}

.viewer-container {
    position: relative;
    width: 100%;
    height: 100%;
}

.viewer-image {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.viewer-thumbnails {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    display: flex;
    flex-wrap: wrap;
}

.viewer-thumbnails img {
    width: 50px;
    height: 50px;
    margin: 5px;
    cursor: pointer;
}
```
