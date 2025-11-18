"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thesoftware.online
Prompt: Generate PHP code for a WordPress site to dynamically update the "Main menu" location in the header builder based on user preferences, referencing WooCommerce themes like WoodMart.
Generated: DETERMINISTIC_3a959865941b0ff6
Batch ID: 20250612_151611
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
 * Plugin Name: Dynamic Main Menu Updater
 * Description: Dynamically updates the "Main menu" location in the header builder based on user preferences.
 * Version: 1.0.0
 * Author: Your Name
 */

if (!defined('ABSPATH')) {
    exit; // Exit if accessed directly.
}

/**
 * Dynamically update the "Main menu" location based on user preferences.
 */
function update_main_menu_based_on_user_preference()
{
    // Check if WooCommerce is activated.
    if (!class_exists('WooCommerce')) {
        return;
    }

    // Get the current user preferences (example: stored in user meta).
    $current_user_id = get_current_user_id();
    if (!$current_user_id) {
        return; // Exit if no user is logged in.
    }

    // Retrieve the preferred menu ID stored in user meta.
    $preferred_menu_id = get_user_meta($current_user_id, 'preferred_menu_id', true);

    // Validate the menu ID.
    if (empty($preferred_menu_id) || !wp_get_nav_menu_object($preferred_menu_id)) {
        return; // Exit if no valid menu ID is found.
    }

    // Update the theme mod for the "Main menu" location.
    set_theme_mod('nav_menu_locations', array(
        'main-menu' => (int) $preferred_menu_id, // Replace 'main-menu' with your theme's specific menu location slug.
    ));
}
add_action('wp_loaded', 'update_main_menu_based_on_user_preference');

/**
 * Add a settings field to let users choose their preferred menu.
 */
function add_preferred_menu_user_field($user)
{
    // Only show the menu selection field for WooCommerce customers.
    if (!current_user_can('edit_user', $user->ID)) {
        return;
    }

    // Fetch all available menus.
    $menus = wp_get_nav_menus();
    ?>
    <h3><?php esc_html_e('Preferred Menu', 'text-domain'); ?></h3>
    <table class="form-table">
        <tr>
            <th><label for="preferred_menu"><?php esc_html_e('Select Preferred Menu', 'text-domain'); ?></label></th>
            <td>
                <select name="preferred_menu_id" id="preferred_menu">
                    <option value=""><?php esc_html_e('Default Menu', 'text-domain'); ?></option>
                    <?php foreach ($menus as $menu) : ?>
                        <option value="<?php echo esc_attr($menu->term_id); ?>" 
                            <?php selected(get_user_meta($user->ID, 'preferred_menu_id', true), $menu->term_id); ?>>
                            <?php echo esc_html($menu->name); ?>
                        </option>
                    <?php endforeach; ?>
                </select>
                <p class="description"><?php esc_html_e('Choose your preferred menu for the site.', 'text-domain'); ?></p>
            </td>
        </tr>
    </table>
    <?php
}
add_action('show_user_profile', 'add_preferred_menu_user_field');
add_action('edit_user_profile', 'add_preferred_menu_user_field');

/**
 * Save the user's preferred menu.
 */
function save_preferred_menu_user_field($user_id)
{
    // Verify user capabilities before saving.
    if (!current_user_can('edit_user', $user_id)) {
        return false;
    }

    // Save the preferred menu ID.
    if (isset($_POST['preferred_menu_id'])) {
        update_user_meta($user_id, 'preferred_menu_id', sanitize_text_field($_POST['preferred_menu_id']));
    }
}
add_action('personal_options_update', 'save_preferred_menu_user_field');
add_action('edit_user_profile_update', 'save_preferred_menu_user_field');
?>
```
