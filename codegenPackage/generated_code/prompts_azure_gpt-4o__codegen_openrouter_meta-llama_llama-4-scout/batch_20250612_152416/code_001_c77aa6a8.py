"""
Generated Code Metadata:
========================
Original URL: https://www.sabrinacarpentermerch.com
Prompt: Generate a WordPress plugin that allows users to manage events and FAQs, inspired by the features listed on the sample page of the website.
Generated: DETERMINISTIC_c77aa6a8ad10cd1b
Batch ID: 20250612_152416
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

**Event and FAQ Manager Plugin**
================================

**Plugin Name:** Event and FAQ Manager
**Description:** A WordPress plugin to manage events and FAQs.

**event-faq-manager.php**
```php
<?php
/*
Plugin Name: Event and FAQ Manager
Description: A WordPress plugin to manage events and FAQs.
Version: 1.0
Author: Your Name
Author URI: https://yourwebsite.com
*/

// Define the plugin's constants
define( 'EVENT_FAQ_MANAGER_DIR', plugin_dir_path( __FILE__ ) );
define( 'EVENT_FAQ_MANAGER_URL', plugin_dir_url( __FILE__ ) );

// Include the plugin's dependencies
require_once EVENT_FAQ_MANAGER_DIR . 'includes/class-event-faq-manager.php';

// Instantiate the plugin
$event_faq_manager = new Event_Faq_Manager();

// Register the plugin's activation and deactivation hooks
register_activation_hook( __FILE__, array( $event_faq_manager, 'activate' ) );
register_deactivation_hook( __FILE__, array( $event_faq_manager, 'deactivate' ) );

// Register the plugin's admin menu
add_action( 'admin_menu', array( $event_faq_manager, 'register_admin_menu' ) );

// Register the plugin's shortcodes
add_shortcode( 'events', array( $event_faq_manager, 'events_shortcode' ) );
add_shortcode( 'faqs', array( $event_faq_manager, 'faqs_shortcode' ) );
```

**includes/class-event-faq-manager.php**
```php
<?php
class Event_Faq_Manager {
  private $events;
  private $faqs;

  public function __construct() {
    $this->events = array();
    $this->faqs = array();
  }

  public function activate() {
    // Create the events and FAQs tables
    global $wpdb;
    $wpdb->query( "
      CREATE TABLE IF NOT EXISTS {$wpdb->prefix}events (
        id INT PRIMARY KEY AUTO_INCREMENT,
        title VARCHAR(255) NOT NULL,
        description TEXT NOT NULL,
        start_date DATE NOT NULL,
        end_date DATE NOT NULL
      );
    " );

    $wpdb->query( "
      CREATE TABLE IF NOT EXISTS {$wpdb->prefix}faqs (
        id INT PRIMARY KEY AUTO_INCREMENT,
        question VARCHAR(255) NOT NULL,
        answer TEXT NOT NULL
      );
    " );
  }

  public function deactivate() {
    // Drop the events and FAQs tables
    global $wpdb;
    $wpdb->query( "DROP TABLE IF EXISTS {$wpdb->prefix}events;" );
    $wpdb->query( "DROP TABLE IF EXISTS {$wpdb->prefix}faqs;" );
  }

  public function register_admin_menu() {
    add_menu_page( 'Event and FAQ Manager', 'Event and FAQ Manager', 'manage_options', 'event-faq-manager', array( $this, 'admin_menu_callback' ) );
    add_submenu_page( 'event-faq-manager', 'Events', 'Events', 'manage_options', 'events', array( $this, 'events_admin_callback' ) );
    add_submenu_page( 'event-faq-manager', 'FAQs', 'FAQs', 'manage_options', 'faqs', array( $this, 'faqs_admin_callback' ) );
  }

  public function admin_menu_callback() {
    ?>
    <div class="wrap">
      <h1>Event and FAQ Manager</h1>
      <p>Manage events and FAQs for your website.</p>
    </div>
    <?php
  }

  public function events_admin_callback() {
    ?>
    <div class="wrap">
      <h1>Events</h1>
      <table class="wp-list-table widefat fixed striped posts">
        <thead>
          <tr>
            <th scope="col">Title</th>
            <th scope="col">Start Date</th>
            <th scope="col">End Date</th>
          </tr>
        </thead>
        <tbody>
          <?php
          global $wpdb;
          $events = $wpdb->get_results( "SELECT * FROM {$wpdb->prefix}events;" );
          foreach ( $events as $event ) {
            ?>
            <tr>
              <td><?php echo $event->title; ?></td>
              <td><?php echo $event->start_date; ?></td>
              <td><?php echo $event->end_date; ?></td>
            </tr>
            <?php
          }
          ?>
        </tbody>
      </table>
      <form action="" method="post">
        <input type="text" name="title" placeholder="Event Title">
        <input type="date" name="start_date" placeholder="Start Date">
        <input type="date" name="end_date" placeholder="End Date">
        <textarea name="description" placeholder="Event Description"></textarea>
        <button type="submit" class="button button-primary">Add Event</button>
      </form>
      <?php
      if ( isset( $_POST['title'] ) && isset( $_POST['start_date'] ) && isset( $_POST['end_date'] ) && isset( $_POST['description'] ) ) {
        $wpdb->insert( $wpdb->prefix . 'events', array(
          'title' => $_POST['title'],
          'description' => $_POST['description'],
          'start_date' => $_POST['start_date'],
          'end_date' => $_POST['end_date'],
        ) );
      }
    }
  }

  public function faqs_admin_callback() {
    ?>
    <div class="wrap">
      <h1>FAQs</h1>
      <table class="wp-list-table widefat fixed striped posts">
        <thead>
          <tr>
            <th scope="col">Question</th>
            <th scope="col">Answer</th>
          </tr>
        </thead>
        <tbody>
          <?php
          global $wpdb;
          $faqs = $wpdb->get_results( "SELECT * FROM {$wpdb->prefix}faqs;" );
          foreach ( $faqs as $faq ) {
            ?>
            <tr>
              <td><?php echo $faq->question; ?></td>
              <td><?php echo $faq->answer; ?></td>
            </tr>
            <?php
          }
          ?>
        </tbody>
      </table>
      <form action="" method="post">
        <input type="text" name="question" placeholder="FAQ Question">
        <textarea name="answer" placeholder="FAQ Answer"></textarea>
        <button type="submit" class="button button-primary">Add FAQ</button>
      </form>
      <?php
      if ( isset( $_POST['question'] ) && isset( $_POST['answer'] ) ) {
        global $wpdb;
        $wpdb->insert( $wpdb->prefix . 'faqs', array(
          'question' => $_POST['question'],
          'answer' => $_POST['answer'],
        ) );
      }
    }
  }

  public function events_shortcode() {
    ?>
    <div class="events">
      <h2>Upcoming Events</h2>
      <ul>
        <?php
        global $wpdb;
        $events = $wpdb->get_results( "SELECT * FROM {$wpdb->prefix}events ORDER BY start_date ASC;" );
        foreach ( $events as $event ) {
          ?>
          <li>
            <h3><?php echo $event->title; ?></h3>
            <p><?php echo $event->description; ?></p>
            <p>Start Date: <?php echo $event->start_date; ?></p>
            <p>End Date: <?php echo $event->end_date; ?></p>
          </li>
          <?php
        }
        ?>
      </ul>
    </div>
    <?php
  }

  public function faqs_shortcode() {
    ?>
    <div class="faqs">
      <h2>Frequently Asked Questions</h2>
      <dl>
        <?php
        global $wpdb;
        $faqs = $wpdb->get_results( "SELECT * FROM {$wpdb->prefix}faqs;" );
        foreach ( $faqs as $faq ) {
          ?>
          <dt><?php echo $faq->question; ?></dt>
          <dd><?php echo $faq->answer; ?></dd>
          <?php
        }
        ?>
      </dl>
    </div>
    <?php
  }
}
```
