"""
Generated Code Metadata:
========================
Original URL: https://villachandon.com.br
Prompt: Create a basic WordPress plugin to manage pet appointments for a veterinary clinic website like Village Pet&Vet.
Generated: DETERMINISTIC_01ac1009066e228a
Batch ID: 20250622_211758
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
 * Plugin Name: Pet Appointment Manager
 * Description: A simple plugin to manage pet appointments for a veterinary clinic.
 * Version: 1.0.0
 * Author: Your Name
 * License: GPL2
 */

// Exit if accessed directly
if (!defined('ABSPATH')) {
    exit;
}

// Define constants
define('PET_APPOINTMENT_MANAGER_VERSION', '1.0.0');
define('PET_APPOINTMENT_MANAGER_PLUGIN_DIR', plugin_dir_path(__FILE__));

// Activation hook
function pam_activate_plugin() {
    global $wpdb;

    // Create appointments table
    $table_name = $wpdb->prefix . 'pet_appointments';
    $charset_collate = $wpdb->get_charset_collate();

    $sql = "CREATE TABLE $table_name (
        id BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
        pet_name VARCHAR(255) NOT NULL,
        owner_name VARCHAR(255) NOT NULL,
        owner_email VARCHAR(255) NOT NULL,
        appointment_date DATETIME NOT NULL,
        notes TEXT,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (id)
    ) $charset_collate;";

    require_once(ABSPATH . 'wp-admin/includes/upgrade.php');
    dbDelta($sql);
}
register_activation_hook(__FILE__, 'pam_activate_plugin');

// Deactivation hook
function pam_deactivate_plugin() {
    // No specific actions needed on deactivation for now
}
register_deactivation_hook(__FILE__, 'pam_deactivate_plugin');

// Admin menu
function pam_register_admin_menu() {
    add_menu_page(
        'Pet Appointments',
        'Pet Appointments',
        'manage_options',
        'pet-appointments',
        'pam_admin_page',
        'dashicons-calendar-alt',
        25
    );
}
add_action('admin_menu', 'pam_register_admin_menu');

// Admin page content
function pam_admin_page() {
    global $wpdb;
    $table_name = $wpdb->prefix . 'pet_appointments';

    // Handle form submission
    if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['pam_submit'])) {
        $pet_name = sanitize_text_field($_POST['pet_name']);
        $owner_name = sanitize_text_field($_POST['owner_name']);
        $owner_email = sanitize_email($_POST['owner_email']);
        $appointment_date = sanitize_text_field($_POST['appointment_date']);
        $notes = sanitize_textarea_field($_POST['notes']);

        // Insert into database
        $wpdb->insert(
            $table_name,
            [
                'pet_name' => $pet_name,
                'owner_name' => $owner_name,
                'owner_email' => $owner_email,
                'appointment_date' => $appointment_date,
                'notes' => $notes,
            ],
            [
                '%s',
                '%s',
                '%s',
                '%s',
                '%s',
            ]
        );

        echo '<div class="updated"><p>Appointment added successfully!</p></div>';
    }

    // Fetch appointments
    $appointments = $wpdb->get_results("SELECT * FROM $table_name ORDER BY appointment_date DESC");

    ?>
    <div class="wrap">
        <h1>Pet Appointments</h1>
        <form method="POST">
            <table class="form-table">
                <tr>
                    <th scope="row"><label for="pet_name">Pet Name</label></th>
                    <td><input name="pet_name" type="text" id="pet_name" class="regular-text" required></td>
                </tr>
                <tr>
                    <th scope="row"><label for="owner_name">Owner Name</label></th>
                    <td><input name="owner_name" type="text" id="owner_name" class="regular-text" required></td>
                </tr>
                <tr>
                    <th scope="row"><label for="owner_email">Owner Email</label></th>
                    <td><input name="owner_email" type="email" id="owner_email" class="regular-text" required></td>
                </tr>
                <tr>
                    <th scope="row"><label for="appointment_date">Appointment Date</label></th>
                    <td><input name="appointment_date" type="datetime-local" id="appointment_date" class="regular-text" required></td>
                </tr>
                <tr>
                    <th scope="row"><label for="notes">Notes</label></th>
                    <td><textarea name="notes" id="notes" class="regular-text"></textarea></td>
                </tr>
            </table>
            <p class="submit">
                <input type="submit" name="pam_submit" id="pam_submit" class="button button-primary" value="Add Appointment">
            </p>
        </form>

        <h2>Existing Appointments</h2>
        <table class="widefat fixed" cellspacing="0">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Pet Name</th>
                    <th>Owner Name</th>
                    <th>Owner Email</th>
                    <th>Appointment Date</th>
                    <th>Notes</th>
                    <th>Created At</th>
                </tr>
            </thead>
            <tbody>
                <?php foreach ($appointments as $appointment): ?>
                    <tr>
                        <td><?php echo esc_html($appointment->id); ?></td>
                        <td><?php echo esc_html($appointment->pet_name); ?></td>
                        <td><?php echo esc_html($appointment->owner_name); ?></td>
                        <td><?php echo esc_html($appointment->owner_email); ?></td>
                        <td><?php echo esc_html($appointment->appointment_date); ?></td>
                        <td><?php echo esc_html($appointment->notes); ?></td>
                        <td><?php echo esc_html($appointment->created_at); ?></td>
                    </tr>
                <?php endforeach; ?>
            </tbody>
        </table>
    </div>
    <?php
}
```
