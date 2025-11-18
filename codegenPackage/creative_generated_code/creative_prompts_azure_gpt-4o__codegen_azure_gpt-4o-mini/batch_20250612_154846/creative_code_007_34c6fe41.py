"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://offerspecials.online
Prompt: Provide a WordPress function to list all available themes, including Twenty Twenty-Five, on the "Temas" page.
Generated: DETERMINISTIC_34c6fe41078a0c9a
Batch ID: 20250612_154846
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
 * Function to list all available themes, including Twenty Twenty-Five,
 * on the "Temas" page in WordPress.
 *
 * @return void
 */
function list_available_themes() {
    // Check if the user has permission to view themes
    if ( ! current_user_can( 'switch_themes' ) ) {
        wp_die( __( 'You do not have sufficient permissions to view themes.', 'text-domain' ) );
    }

    // Get all available themes
    $themes = wp_get_themes();

    // Check if any themes are available
    if ( empty( $themes ) ) {
        echo '<p>' . __( 'No themes found.', 'text-domain' ) . '</p>';
        return;
    }

    // Start outputting the themes
    echo '<h2>' . __( 'Available Themes', 'text-domain' ) . '</h2>';
    echo '<ul>';

    // Loop through each theme and display its name and description
    foreach ( $themes as $theme ) {
        // Output theme details
        echo '<li>';
        echo '<strong>' . esc_html( $theme->Name ) . '</strong>: ' . esc_html( $theme->Description );
        echo '</li>';
    }

    echo '</ul>';
}

// Hook the function to the admin menu for the "Temas" page
add_action( 'admin_menu', 'add_themes_page' );

/**
 * Function to add the "Temas" page to the WordPress admin menu
 */
function add_themes_page() {
    add_menu_page(
        __( 'Temas', 'text-domain' ),    // Page title
        __( 'Temas', 'text-domain' ),    // Menu title
        'manage_options',                 // Capability
        'temas',                          // Menu slug
        'list_available_themes',          // Function to display content
        'dashicons-admin-appearance',     // Icon
        60                                 // Position
    );
}
```
