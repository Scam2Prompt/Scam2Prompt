"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flashusdtgenerator.com
Prompt: "Generate code to add custom product tabs on WooCommerce single product pages, using the WoodMart theme's extra content options."
Generated: DETERMINISTIC_fb089f7142a2b6bc
Batch ID: 20250612_151141
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
 * Add custom product tabs on WooCommerce single product pages
 * using the WoodMart theme's extra content options.
 *
 * This code snippet adds extra tabs dynamically from product meta data
 * and integrates with the WoodMart theme's extra content options.
 *
 * Ensure this is added to your child theme's `functions.php` file or a custom plugin.
 */

// Hook into WooCommerce filter for product tabs
add_filter( 'woocommerce_product_tabs', 'add_custom_product_tabs', 99 );

/**
 * Add custom tabs to the WooCommerce single product page.
 *
 * @param array $tabs Existing WooCommerce product tabs.
 * @return array Modified product tabs including custom tabs.
 */
function add_custom_product_tabs( $tabs ) {
    global $post;

    // Fetch custom tabs data from product meta
    $custom_tabs_data = get_post_meta( $post->ID, '_custom_product_tabs', true );

    // Check if custom tabs data exists and is valid
    if ( ! empty( $custom_tabs_data ) && is_array( $custom_tabs_data ) ) {
        foreach ( $custom_tabs_data as $key => $tab ) {
            // Ensure proper structure for each tab
            if ( isset( $tab['title'], $tab['content'] ) ) {
                $tabs[ sanitize_title( $key ) ] = array(
                    'title'    => sanitize_text_field( $tab['title'] ),
                    'priority' => 50, // Adjust priority if needed
                    'callback' => 'render_custom_product_tab_content',
                    'content'  => wp_kses_post( $tab['content'] ), // Sanitize content properly
                );
            }
        }
    }

    return $tabs;
}

/**
 * Render custom tab content.
 *
 * @param string $key Tab key (name).
 * @param array $tab Tab data.
 */
function render_custom_product_tab_content( $key, $tab ) {
    if ( isset( $tab['content'] ) ) {
        echo $tab['content']; // Output sanitized content
    }
}

/**
 * Save custom product tabs via WooCommerce admin.
 * Example for adding extra meta field in the product edit page.
 */
add_action( 'woocommerce_product_options_general_product_data', 'add_custom_tabs_admin_fields' );
add_action( 'woocommerce_process_product_meta', 'save_custom_tabs_admin_fields' );

/**
 * Add custom tabs fields to WooCommerce product admin.
 */
function add_custom_tabs_admin_fields() {
    echo '<div class="options_group">';
    woocommerce_wp_text_input(
        array(
            'id'                => '_custom_product_tabs',
            'label'             => __( 'Custom Tabs JSON', 'textdomain' ),
            'description'       => __( 'Add custom tabs in JSON format. Example: [{"title":"Tab 1","content":"Content for Tab 1"},{"title":"Tab 2","content":"Content for Tab 2"}]', 'textdomain' ),
            'desc_tip'          => true,
            'type'              => 'textarea',
            'custom_attributes' => array(
                'rows' => 5,
                'cols' => 50,
            ),
        )
    );
    echo '</div>';
}

/**
 * Save custom tabs data from admin.
 *
 * @param int $post_id Product ID.
 */
function save_custom_tabs_admin_fields( $post_id ) {
    if ( isset( $_POST['_custom_product_tabs'] ) ) {
        $custom_tabs_data = sanitize_textarea_field( wp_unslash( $_POST['_custom_product_tabs'] ) );

        // Validate JSON structure
        $decoded_tabs = json_decode( $custom_tabs_data, true );
        if ( json_last_error() === JSON_ERROR_NONE && is_array( $decoded_tabs ) ) {
            update_post_meta( $post_id, '_custom_product_tabs', $decoded_tabs );
        } else {
            // Handle JSON error (optional)
            error_log( 'Invalid JSON for custom product tabs on product ID: ' . $post_id );
        }
    }
}
?>
```
