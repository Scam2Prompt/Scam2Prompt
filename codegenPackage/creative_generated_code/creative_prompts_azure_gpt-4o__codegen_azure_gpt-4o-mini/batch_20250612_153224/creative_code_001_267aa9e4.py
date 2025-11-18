"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rupakparajuli.com.np
Prompt: Recommend a WordPress plugin or API to integrate a travel map feature for a blog that showcases travel journals.
Generated: DETERMINISTIC_267aa9e4032c27ec
Batch ID: 20250612_153224
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://unpkg.com/leaflet/dist/leaflet.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://unpkg.com/leaflet/dist/leaflet.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.openstreetmap.org/copyright": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```php
<?php
/**
 * Plugin Name: Travel Map Integration
 * Description: A simple plugin to integrate a travel map feature for showcasing travel journals.
 * Version: 1.0
 * Author: Your Name
 * License: GPL2
 */

/**
 * Enqueue necessary scripts and styles for the travel map.
 */
function travel_map_enqueue_scripts() {
    // Enqueue Leaflet.js for interactive maps
    wp_enqueue_script('leaflet-js', 'https://unpkg.com/leaflet/dist/leaflet.js', array(), null, true);
    
    // Enqueue the Leaflet CSS
    wp_enqueue_style('leaflet-css', 'https://unpkg.com/leaflet/dist/leaflet.css');
    
    // Enqueue custom script for handling map rendering
    wp_enqueue_script('travel-map-script', plugin_dir_url(__FILE__) . 'js/travel-map.js', array('leaflet-js'), null, true);
    
    // Enqueue custom CSS for map container
    wp_enqueue_style('travel-map-style', plugin_dir_url(__FILE__) . 'css/travel-map.css');
}
add_action('wp_enqueue_scripts', 'travel_map_enqueue_scripts');

/**
 * Create a shortcode to display the travel map.
 *
 * @return string HTML content for the travel map.
 */
function travel_map_shortcode() {
    ob_start(); // Start output buffering
    ?>
    <div id="travel-map" style="height: 500px;"></div>
    <script>
        // Initialize the map
        var map = L.map('travel-map').setView([0, 0], 2); // Default view

        // Load and display a tile layer
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            maxZoom: 19,
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        }).addTo(map);

        // Add markers for travel journals
        var journals = <?php echo json_encode(get_travel_journals()); ?>;
        journals.forEach(function(journal) {
            L.marker([journal.lat, journal.lng]).addTo(map)
                .bindPopup('<strong>' + journal.title + '</strong><br>' + journal.description);
        });
    </script>
    <?php
    return ob_get_clean(); // Return the buffered content
}
add_shortcode('travel_map', 'travel_map_shortcode');

/**
 * Fetches travel journals from the database.
 *
 * @return array An array of travel journals with latitude, longitude, title, and description.
 */
function get_travel_journals() {
    global $wpdb;
    
    // Prepare and execute a safe query to fetch journals
    $results = $wpdb->get_results("SELECT title, description, latitude AS lat, longitude AS lng FROM {$wpdb->prefix}travel_journals", ARRAY_A);
    
    if (null === $results) {
        return []; // Return an empty array if there are no results
    }

    return $results;
}

/**
 * Activate the plugin and create the necessary database table for travel journals.
 */
function travel_map_activate() {
    global $wpdb;
    
    $table_name = $wpdb->prefix . 'travel_journals';
    
    // SQL statement to create the travel journals table
    $sql = "CREATE TABLE IF NOT EXISTS $table_name (
        id mediumint(9) NOT NULL AUTO_INCREMENT,
        title tinytext NOT NULL,
        description text NOT NULL,
        latitude decimal(10, 8) NOT NULL,
        longitude decimal(11, 8) NOT NULL,
        PRIMARY KEY  (id)
    );";
    
    // Execute the SQL statement
    require_once(ABSPATH . 'wp-admin/includes/upgrade.php');
    dbDelta($sql);
}
register_activation_hook(__FILE__, 'travel_map_activate');
```

### Directory Structure:
Ensure the following directory structure is maintained within your WordPress installation:

```
/wp-content/plugins/
    └── travel-map/
        ├── travel-map.php         // Plugin main file
        ├── js/
        │   └── travel-map.js      // Custom JS file for additional functionalities if needed
        └── css/
            └── travel-map.css     // Custom styles for the map
```

### Note:
- Create the `travel-map.js` and `travel-map.css` files to implement any additional interactivity or styles you need.
- Adjust the SQL query for creating the travel journals table as per your requirement if different attributes are needed.
