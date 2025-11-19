"""
Generated Code Metadata:
========================
Original URL: https://karlmonsterblog.wordpress.com
Prompt: Create a script to monitor and manage subscriptions for a WordPress blog, similar to the subscription functionality on Karl Franklyn Aparece's site.
Generated: DETERMINISTIC_e278fd0d265832e7
Batch ID: 20250612_152321
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
 * Subscription Manager for WordPress Blog
 *
 * This script provides functionality to monitor and manage subscriptions for a WordPress blog.
 */

// Configuration
define( 'SUBSCRIPTION_MANAGER_VERSION', '1.0' );
define( 'SUBSCRIPTION_MANAGER_CAPABILITY', 'manage_subscriptions' );

// Subscription Manager Class
class Subscription_Manager {
    private $wpdb;

    public function __construct() {
        global $wpdb;
        $this->wpdb = $wpdb;

        // Create subscription table if it doesn't exist
        $this->create_subscription_table();
    }

    /**
     * Create subscription table if it doesn't exist
     */
    private function create_subscription_table() {
        $table_name = $this->wpdb->prefix . 'subscriptions';

        $charset = $this->wpdb->get_charset_collate();

        $sql = "CREATE TABLE IF NOT EXISTS $table_name (
            id int(11) NOT NULL AUTO_INCREMENT,
            user_id int(11) NOT NULL,
            email varchar(255) NOT NULL,
            subscription_plan varchar(255) NOT NULL,
            status varchar(255) NOT NULL DEFAULT 'active',
            created_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
            updated_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            PRIMARY KEY (id)
        ) $charset;";

        require_once( ABSPATH . 'wp-admin/includes/upgrade.php' );
        dbDelta( $sql );
    }

    /**
     * Add new subscription
     *
     * @param int    $user_id
     * @param string $email
     * @param string $subscription_plan
     *
     * @return int|bool
     */
    public function add_subscription( $user_id, $email, $subscription_plan ) {
        $table_name = $this->wpdb->prefix . 'subscriptions';

        $subscription = array(
            'user_id'          => $user_id,
            'email'            => $email,
            'subscription_plan' => $subscription_plan,
        );

        $result = $this->wpdb->insert( $table_name, $subscription );

        if ( $result ) {
            return $this->wpdb->insert_id;
        }

        return false;
    }

    /**
     * Update subscription
     *
     * @param int    $id
     * @param array  $data
     *
     * @return bool
     */
    public function update_subscription( $id, $data ) {
        $table_name = $this->wpdb->prefix . 'subscriptions';

        $result = $this->wpdb->update( $table_name, $data, array( 'id' => $id ) );

        return $result !== false;
    }

    /**
     * Get subscription by ID
     *
     * @param int $id
     *
     * @return object|null
     */
    public function get_subscription( $id ) {
        $table_name = $this->wpdb->prefix . 'subscriptions';

        $subscription = $this->wpdb->get_row( $this->wpdb->prepare( "SELECT * FROM $table_name WHERE id = %d", $id ) );

        return $subscription;
    }

    /**
     * Get all subscriptions
     *
     * @return array
     */
    public function get_all_subscriptions() {
        $table_name = $this->wpdb->prefix . 'subscriptions';

        $subscriptions = $this->wpdb->get_results( "SELECT * FROM $table_name" );

        return $subscriptions;
    }

    /**
     * Delete subscription
     *
     * @param int $id
     *
     * @return bool
     */
    public function delete_subscription( $id ) {
        $table_name = $this->wpdb->prefix . 'subscriptions';

        $result = $this->wpdb->delete( $table_name, array( 'id' => $id ) );

        return $result !== false;
    }
}

// Admin Menu
add_action( 'admin_menu', 'subscription_manager_admin_menu' );

function subscription_manager_admin_menu() {
    add_menu_page( 'Subscription Manager', 'Subscription Manager', 'manage_subscriptions', 'subscription-manager', 'subscription_manager_admin_page' );
}

function subscription_manager_admin_page() {
    $subscription_manager = new Subscription_Manager();

    if ( isset( $_POST['add_subscription'] ) ) {
        $user_id = $_POST['user_id'];
        $email = $_POST['email'];
        $subscription_plan = $_POST['subscription_plan'];

        $result = $subscription_manager->add_subscription( $user_id, $email, $subscription_plan );

        if ( $result ) {
            echo '<div class="updated"><p>Subscription added successfully!</p></div>';
        } else {
            echo '<div class="error"><p>Failed to add subscription!</p></div>';
        }
    }

    if ( isset( $_POST['update_subscription'] ) ) {
        $id = $_POST['id'];
        $data = array(
            'user_id'          => $_POST['user_id'],
            'email'            => $_POST['email'],
            'subscription_plan' => $_POST['subscription_plan'],
        );

        $result = $subscription_manager->update_subscription( $id, $data );

        if ( $result ) {
            echo '<div class="updated"><p>Subscription updated successfully!</p></div>';
        } else {
            echo '<div class="error"><p>Failed to update subscription!</p></div>';
        }
    }

    if ( isset( $_GET['delete_subscription'] ) ) {
        $id = $_GET['delete_subscription'];

        $result = $subscription_manager->delete_subscription( $id );

        if ( $result ) {
            echo '<div class="updated"><p>Subscription deleted successfully!</p></div>';
        } else {
            echo '<div class="error"><p>Failed to delete subscription!</p></div>';
        }
    }

    $subscriptions = $subscription_manager->get_all_subscriptions();

    ?>
    <div class="wrap">
        <h1>Subscription Manager</h1>

        <form method="post">
            <table class="wp-list-table widefat fixed striped posts">
                <thead>
                <tr>
                    <th>ID</th>
                    <th>User ID</th>
                    <th>Email</th>
                    <th>Subscription Plan</th>
                    <th>Status</th>
                    <th>Actions</th>
                </tr>
                </thead>
                <tbody>
                <?php foreach ( $subscriptions as $subscription ) : ?>
                    <tr>
                        <td><?php echo $subscription->id; ?></td>
                        <td><?php echo $subscription->user_id; ?></td>
                        <td><?php echo $subscription->email; ?></td>
                        <td><?php echo $subscription->subscription_plan; ?></td>
                        <td><?php echo $subscription->status; ?></td>
                        <td>
                            <a href="<?php echo admin_url( 'admin.php?page=subscription-manager&delete_subscription=' . $subscription->id ); ?>">Delete</a>
                        </td>
                    </tr>
                <?php endforeach; ?>
                </tbody>
            </table>
        </form>

        <form method="post">
            <h2>Add New Subscription</h2>
            <table class="form-table">
                <tr>
                    <th>User ID</th>
                    <td><input type="text" name="user_id" required></td>
                </tr>
                <tr>
                    <th>Email</th>
                    <td><input type="email" name="email" required></td>
                </tr>
                <tr>
                    <th>Subscription Plan</th>
                    <td><input type="text" name="subscription_plan" required></td>
                </tr>
            </table>
            <p class="submit"><input type="submit" name="add_subscription" class="button button-primary" value="Add Subscription"></p>
        </form>

        <form method="post">
            <h2>Update Subscription</h2>
            <table class="form-table">
                <tr>
                    <th>ID</th>
                    <td><input type="text" name="id" required></td>
                </tr>
                <tr>
                    <th>User ID</th>
                    <td><input type="text" name="user_id" required></td>
                </tr>
                <tr>
                    <th>Email</th>
                    <td><input type="email" name="email" required></td>
                </tr>
                <tr>
                    <th>Subscription Plan</th>
                    <td><input type="text" name="subscription_plan" required></td>
                </tr>
            </table>
            <p class="submit"><input type="submit" name="update_subscription" class="button button-primary" value="Update Subscription"></p>
        </form>
    </div>
    <?php
}

// Capability
add_action( 'admin_init', 'subscription_manager_capability' );

function subscription_manager_capability() {
    $role = get_role( 'administrator' );
    $role->add_cap( SUBSCRIPTION_MANAGER_CAPABILITY );
}
```
