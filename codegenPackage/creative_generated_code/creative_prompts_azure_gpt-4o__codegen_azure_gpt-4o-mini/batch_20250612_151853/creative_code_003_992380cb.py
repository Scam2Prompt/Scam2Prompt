"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smartd.org.ls
Prompt: Generate a PHP script to secure WordPress directories (`wp-admin`, `wp-includes`) from unauthorized access, referencing the structure shown at https://smartd.org.ls.
Generated: DETERMINISTIC_992380cb4bfb8c15
Batch ID: 20250612_151853
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
 * Secure WordPress Directories
 * 
 * This script prevents unauthorized access to the wp-admin and wp-includes directories 
 * by checking for valid authentication or restricting access based on IP addresses.
 * 
 * Make sure to place this script in your WordPress root directory.
 */

// Define the paths to the directories that need to be secured
define('WP_ADMIN_DIR', __DIR__ . '/wp-admin/');
define('WP_INCLUDES_DIR', __DIR__ . '/wp-includes/');

// Function to restrict access based on authentication
function restrict_access() {
    // Check if the user is logged in
    if (!is_user_logged_in()) {
        // If not logged in, send a 403 Forbidden response
        header('HTTP/1.0 403 Forbidden');
        echo "You are not authorized to access this directory.";
        exit;
    }
}

// Function to check if user is logged in
function is_user_logged_in() {
    // Check for a valid session or authentication method
    // This can be customized based on your authentication system
    return isset($_SERVER['PHP_AUTH_USER']) && isset($_SERVER['PHP_AUTH_PW']);
}

// Function to restrict access based on IP address
function restrict_access_by_ip($allowed_ips) {
    // Get the user's IP address
    $user_ip = $_SERVER['REMOTE_ADDR'];

    // Check if the user's IP is in the allowed list
    if (!in_array($user_ip, $allowed_ips)) {
        header('HTTP/1.0 403 Forbidden');
        echo "Access denied for IP: " . htmlspecialchars($user_ip);
        exit;
    }
}

// Allowed IP addresses for access (modify as needed)
$allowed_ips = ['123.456.789.000']; // Replace with your allowed IPs

// Check if the request is for wp-admin or wp-includes directories
$request_uri = $_SERVER['REQUEST_URI'];
if (strpos($request_uri, '/wp-admin/') === 0 || strpos($request_uri, '/wp-includes/') === 0) {
    // Uncomment the line you want to use for access control
    // restrict_access(); // Use this for user authentication
    restrict_access_by_ip($allowed_ips); // Use this for IP-based access control
}
?>
```

> **Note:** Replace `['123.456.789.000']` with the actual IP addresses you want to allow. Adjust the authentication logic as needed to suit your particular user management setup. This script should be thoroughly tested in a staging environment before deploying to production.
