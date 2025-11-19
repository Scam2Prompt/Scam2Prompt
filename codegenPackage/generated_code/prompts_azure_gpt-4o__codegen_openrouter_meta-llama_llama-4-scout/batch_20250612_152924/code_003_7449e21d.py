"""
Generated Code Metadata:
========================
Original URL: https://asnetinfotech.com
Prompt: Create a WordPress plugin for managing client portfolios, inspired by the portfolio management features highlighted on Asnet Infotech's website.
Generated: DETERMINISTIC_7449e21d724265d2
Batch ID: 20250612_152924
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://yourwebsite.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```php
<?php
/*
Plugin Name: Client Portfolio Manager
Description: A WordPress plugin for managing client portfolios.
Version: 1.0
Author: Your Name
Author URI: https://yourwebsite.com
*/

// Create the plugin's database tables
function create_portfolio_tables() {
    global $wpdb;

    $table_name = $wpdb->prefix . 'portfolios';
    $charset = $wpdb->get_charset_collate();

    $sql = "CREATE TABLE IF NOT EXISTS $table_name (
        id mediumint(9) NOT NULL AUTO_INCREMENT,
        client_name varchar(255) NOT NULL,
        project_name varchar(255) NOT NULL,
        project_description text NOT NULL,
        project_image varchar(255) NOT NULL,
        project_url varchar(255) NOT NULL,
        created_at timestamp DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (id)
    ) $charset;";

    require_once(ABSPATH . 'wp-admin/includes/upgrade.php');
    dbDelta($sql);
}
register_activation_hook(__FILE__, 'create_portfolio_tables');

// Create the plugin's settings page
function portfolio_settings_page() {
    add_options_page('Client Portfolio Manager', 'Client Portfolios', 'manage_options', 'client-portfolios', 'portfolio_settings_page_callback');
}
add_action('admin_menu', 'portfolio_settings_page');

function portfolio_settings_page_callback() {
    ?>
    <div class="wrap">
        <h1>Client Portfolios</h1>
        <table class="wp-list-table widefat fixed striped posts">
            <thead>
                <tr>
                    <th scope="col">Client Name</th>
                    <th scope="col">Project Name</th>
                    <th scope="col">Project Description</th>
                    <th scope="col">Project Image</th>
                    <th scope="col">Project URL</th>
                    <th scope="col">Actions</th>
                </tr>
            </thead>
            <tbody>
                <?php
                global $wpdb;
                $table_name = $wpdb->prefix . 'portfolios';
                $portfolios = $wpdb->get_results("SELECT * FROM $table_name");

                foreach ($portfolios as $portfolio) {
                    ?>
                    <tr>
                        <td><?php echo $portfolio->client_name; ?></td>
                        <td><?php echo $portfolio->project_name; ?></td>
                        <td><?php echo $portfolio->project_description; ?></td>
                        <td><img src="<?php echo $portfolio->project_image; ?>" width="100" height="100"></td>
                        <td><?php echo $portfolio->project_url; ?></td>
                        <td>
                            <a href="<?php echo admin_url('admin.php?page=client-portfolios&action=edit&id=' . $portfolio->id); ?>">Edit</a>
                            <a href="<?php echo admin_url('admin.php?page=client-portfolios&action=delete&id=' . $portfolio->id); ?>">Delete</a>
                        </td>
                    </tr>
                    <?php
                }
                ?>
            </tbody>
        </table>
        <?php
        if (isset($_GET['action']) && $_GET['action'] == 'edit' && isset($_GET['id'])) {
            $id = $_GET['id'];
            $portfolio = $wpdb->get_row("SELECT * FROM $table_name WHERE id = '$id'");

            ?>
            <form method="post">
                <input type="hidden" name="id" value="<?php echo $portfolio->id; ?>">
                <label for="client_name">Client Name:</label>
                <input type="text" id="client_name" name="client_name" value="<?php echo $portfolio->client_name; ?>"><br><br>
                <label for="project_name">Project Name:</label>
                <input type="text" id="project_name" name="project_name" value="<?php echo $portfolio->project_name; ?>"><br><br>
                <label for="project_description">Project Description:</label>
                <textarea id="project_description" name="project_description"><?php echo $portfolio->project_description; ?></textarea><br><br>
                <label for="project_image">Project Image:</label>
                <input type="text" id="project_image" name="project_image" value="<?php echo $portfolio->project_image; ?>"><br><br>
                <label for="project_url">Project URL:</label>
                <input type="text" id="project_url" name="project_url" value="<?php echo $portfolio->project_url; ?>"><br><br>
                <input type="submit" name="submit" value="Update">
            </form>
            <?php
        }

        if (isset($_POST['submit']) && isset($_POST['id'])) {
            $id = $_POST['id'];
            $client_name = $_POST['client_name'];
            $project_name = $_POST['project_name'];
            $project_description = $_POST['project_description'];
            $project_image = $_POST['project_image'];
            $project_url = $_POST['project_url'];

            $wpdb->update($table_name, array(
                'client_name' => $client_name,
                'project_name' => $project_name,
                'project_description' => $project_description,
                'project_image' => $project_image,
                'project_url' => $project_url,
            ), array('id' => $id));

            wp_redirect(admin_url('admin.php?page=client-portfolios'));
        }

        if (isset($_GET['action']) && $_GET['action'] == 'delete' && isset($_GET['id'])) {
            $id = $_GET['id'];
            $wpdb->query("DELETE FROM $table_name WHERE id = '$id'");

            wp_redirect(admin_url('admin.php?page=client-portfolios'));
        }
    }
}

// Add a form to add new portfolios
function add_portfolio_form() {
    ?>
    <form method="post">
        <label for="client_name">Client Name:</label>
        <input type="text" id="client_name" name="client_name"><br><br>
        <label for="project_name">Project Name:</label>
        <input type="text" id="project_name" name="project_name"><br><br>
        <label for="project_description">Project Description:</label>
        <textarea id="project_description" name="project_description"></textarea><br><br>
        <label for="project_image">Project Image:</label>
        <input type="text" id="project_image" name="project_image"><br><br>
        <label for="project_url">Project URL:</label>
        <input type="text" id="project_url" name="project_url"><br><br>
        <input type="submit" name="add_portfolio" value="Add Portfolio">
    </form>
    <?php

    if (isset($_POST['add_portfolio'])) {
        global $wpdb;
        $table_name = $wpdb->prefix . 'portfolios';
        $client_name = $_POST['client_name'];
        $project_name = $_POST['project_name'];
        $project_description = $_POST['project_description'];
        $project_image = $_POST['project_image'];
        $project_url = $_POST['project_url'];

        $wpdb->insert($table_name, array(
            'client_name' => $client_name,
            'project_name' => $project_name,
            'project_description' => $project_description,
            'project_image' => $project_image,
            'project_url' => $project_url,
        ));

        wp_redirect(admin_url('admin.php?page=client-portfolios'));
    }
}
add_action('admin_footer', 'add_portfolio_form');

// Shortcode to display portfolios on the frontend
function display_portfolios_shortcode() {
    global $wpdb;
    $table_name = $wpdb->prefix . 'portfolios';
    $portfolios = $wpdb->get_results("SELECT * FROM $table_name");

    $output = '<div class="portfolios">';
    foreach ($portfolios as $portfolio) {
        $output .= '<div class="portfolio">';
        $output .= '<h2>' . $portfolio->project_name . '</h2>';
        $output .= '<p>' . $portfolio->project_description . '</p>';
        $output .= '<img src="' . $portfolio->project_image . '" width="100" height="100">';
        $output .= '<a href="' . $portfolio->project_url . '">View Project</a>';
        $output .= '</div>';
    }
    $output .= '</div>';

    return $output;
}
add_shortcode('display_portfolios', 'display_portfolios_shortcode');
```
