"""
Generated Code Metadata:
========================
Original URL: https://99pancakes.help
Prompt: How do I set up user roles and permissions for a WordPress help desk using custom code?
Generated: DETERMINISTIC_0262913c34e23d64
Batch ID: 20250612_163506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php

// Define custom roles and capabilities
function create_custom_roles() {
    // Create new roles
    $roles = array(
        'support_agent' => 'Support Agent',
        'support_manager' => 'Support Manager',
    );

    foreach ( $roles as $role_slug => $role_name ) {
        // Check if role already exists
        if ( ! get_role( $role_slug ) ) {
            add_role( $role_slug, $role_name );
        }
    }

    // Define capabilities for each role
    $capabilities = array(
        'support_agent' => array(
            'read' => true,
            'edit_posts' => true,
            'publish_posts' => false,
            'manage_categories' => false,
        ),
        'support_manager' => array(
            'read' => true,
            'edit_posts' => true,
            'publish_posts' => true,
            'manage_categories' => true,
        ),
    );

    foreach ( $capabilities as $role_slug => $capabilities_array ) {
        $role = get_role( $role_slug );
        foreach ( $capabilities_array as $capability => $value ) {
            $role->add_cap( $capability, $value );
        }
    }
}

// Hook to create custom roles on plugin activation
register_activation_hook( __FILE__, 'create_custom_roles' );

// Function to add custom capabilities to existing roles
function add_custom_capabilities() {
    // Get existing roles
    $roles = wp_roles()->get_roles();

    // Define custom capabilities
    $custom_capabilities = array(
        'manage_helpdesk' => 'Manage help desk',
        'view_tickets' => 'View tickets',
        'edit_tickets' => 'Edit tickets',
    );

    // Add custom capabilities to existing roles
    foreach ( $roles as $role_slug => $role ) {
        // Support Agent role
        if ( $role_slug === 'support_agent' ) {
            $role->add_cap( 'view_tickets' );
            $role->add_cap( 'edit_tickets' );
        }
        // Support Manager role
        elseif ( $role_slug === 'support_manager' ) {
            $role->add_cap( 'manage_helpdesk' );
            $role->add_cap( 'view_tickets' );
            $role->add_cap( 'edit_tickets' );
        }
    }
}

// Hook to add custom capabilities on plugin activation
add_action( 'admin_init', 'add_custom_capabilities' );

// Function to check if user has specific capability
function has_capability( $capability ) {
    $current_user = wp_get_current_user();
    return $current_user->has_cap( $capability );
}

// Shortcode to display user role and capabilities
function display_user_role_capabilities() {
    $current_user = wp_get_current_user();
    $roles = $current_user->roles;
    $capabilities = $current_user->all_capabilities;

    echo '<h2>User Role and Capabilities</h2>';
    echo '<p>Roles: ' . implode( ', ', $roles ) . '</p>';
    echo '<p>Capabilities: ';
    foreach ( $capabilities as $capability => $value ) {
        echo $capability . ': ' . ( $value ? 'true' : 'false' ) . ', ';
    }
    echo '</p>';
}

add_shortcode( 'user_role_capabilities', 'display_user_role_capabilities' );

// Example usage:
// [user_role_capabilities]

// Filter to restrict access to certain pages based on user role
function restrict_access_to_pages() {
    $current_user = wp_get_current_user();
    $roles = $current_user->roles;

    // Restrict access to help desk page for non-support agents
    if ( ! in_array( 'support_agent', $roles ) && ! in_array( 'support_manager', $roles ) ) {
        if ( is_page( 'help-desk' ) ) {
            wp_redirect( home_url() );
            exit;
        }
    }
}

add_action( 'template_redirect', 'restrict_access_to_pages' );

?>
```
