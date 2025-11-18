"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://weavely.in
Prompt: Suggest a WordPress plugin to manage intricate product categories like "Handmade sarees" and "Formal wear sarees" with filtering options for fabrics such as "Kota silk" and "Semi silk."
Generated: DETERMINISTIC_5e26b4f37c9a9198
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
/**
 * Plugin Name: Custom Product Categories and Filters
 * Description: A WordPress plugin to manage intricate product categories and provide filtering options for fabrics.
 * Version: 1.0.0
 * Author: Your Name
 * License: GPL2
 */

// Prevent direct access to the file
if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

// Register Custom Taxonomy for Product Categories
function cpc_register_product_categories() {
    $labels = array(
        'name'              => _x( 'Product Categories', 'taxonomy general name', 'cpc' ),
        'singular_name'     => _x( 'Product Category', 'taxonomy singular name', 'cpc' ),
        'search_items'      => __( 'Search Product Categories', 'cpc' ),
        'all_items'         => __( 'All Product Categories', 'cpc' ),
        'parent_item'       => __( 'Parent Product Category', 'cpc' ),
        'parent_item_colon' => __( 'Parent Product Category:', 'cpc' ),
        'edit_item'         => __( 'Edit Product Category', 'cpc' ),
        'update_item'       => __( 'Update Product Category', 'cpc' ),
        'add_new_item'      => __( 'Add New Product Category', 'cpc' ),
        'new_item_name'     => __( 'New Product Category Name', 'cpc' ),
        'menu_name'         => __( 'Product Categories', 'cpc' ),
    );

    $args = array(
        'labels'            => $labels,
        'hierarchical'      => true,
        'public'            => true,
        'show_ui'           => true,
        'show_admin_column' => true,
        'query_var'         => true,
        'rewrite'           => array( 'slug' => 'product-category' ),
    );

    register_taxonomy( 'product_category', array( 'product' ), $args );
}
add_action( 'init', 'cpc_register_product_categories' );

// Register Custom Taxonomy for Fabrics
function cpc_register_fabric_taxonomy() {
    $labels = array(
        'name'              => _x( 'Fabrics', 'taxonomy general name', 'cpc' ),
        'singular_name'     => _x( 'Fabric', 'taxonomy singular name', 'cpc' ),
        'search_items'      => __( 'Search Fabrics', 'cpc' ),
        'all_items'         => __( 'All Fabrics', 'cpc' ),
        'parent_item'       => __( 'Parent Fabric', 'cpc' ),
        'parent_item_colon' => __( 'Parent Fabric:', 'cpc' ),
        'edit_item'         => __( 'Edit Fabric', 'cpc' ),
        'update_item'       => __( 'Update Fabric', 'cpc' ),
        'add_new_item'      => __( 'Add New Fabric', 'cpc' ),
        'new_item_name'     => __( 'New Fabric Name', 'cpc' ),
        'menu_name'         => __( 'Fabrics', 'cpc' ),
    );

    $args = array(
        'labels'            => $labels,
        'hierarchical'      => true,
        'public'            => true,
        'show_ui'           => true,
        'show_admin_column' => true,
        'query_var'         => true,
        'rewrite'           => array( 'slug' => 'fabric' ),
    );

    register_taxonomy( 'fabric', array( 'product' ), $args );
}
add_action( 'init', 'cpc_register_fabric_taxonomy' );

// Add filtering options to the product query
function cpc_modify_product_query( $query ) {
    if ( ! is_admin() && $query->is_main_query() && is_post_type_archive( 'product' ) ) {
        // Get filter parameters from the URL
        $selected_category = isset( $_GET['product_category'] ) ? sanitize_text_field( $_GET['product_category'] ) : '';
        $selected_fabric = isset( $_GET['fabric'] ) ? sanitize_text_field( $_GET['fabric'] ) : '';

        // Add category filter to query
        if ( ! empty( $selected_category ) ) {
            $query->set( 'tax_query', array(
                array(
                    'taxonomy' => 'product_category',
                    'field'    => 'slug',
                    'terms'    => $selected_category,
                ),
            ));
        }

        // Add fabric filter to query
        if ( ! empty( $selected_fabric ) ) {
            $query->set( 'tax_query', array(
                array(
                    'taxonomy' => 'fabric',
                    'field'    => 'slug',
                    'terms'    => $selected_fabric,
                ),
            ));
        }
    }
}
add_action( 'pre_get_posts', 'cpc_modify_product_query' );

// Create a shortcode to display the filter form
function cpc_filter_form_shortcode() {
    ob_start(); ?>
    <form method="GET" action="<?php echo esc_url( home_url( '/shop/' ) ); ?>">
        <select name="product_category">
            <option value=""><?php _e( 'Select Category', 'cpc' ); ?></option>
            <?php
            $categories = get_terms( array( 'taxonomy' => 'product_category', 'hide_empty' => true ) );
            foreach ( $categories as $category ) {
                echo '<option value="' . esc_attr( $category->slug ) . '">' . esc_html( $category->name ) . '</option>';
            }
            ?>
        </select>
        <select name="fabric">
            <option value=""><?php _e( 'Select Fabric', 'cpc' ); ?></option>
            <?php
            $fabrics = get_terms( array( 'taxonomy' => 'fabric', 'hide_empty' => true ) );
            foreach ( $fabrics as $fabric ) {
                echo '<option value="' . esc_attr( $fabric->slug ) . '">' . esc_html( $fabric->name ) . '</option>';
            }
            ?>
        </select>
        <input type="submit" value="<?php _e( 'Filter', 'cpc' ); ?>" />
    </form>
    <?php
    return ob_get_clean();
}
add_shortcode( 'cpc_filter_form', 'cpc_filter_form_shortcode' );

?>
```
