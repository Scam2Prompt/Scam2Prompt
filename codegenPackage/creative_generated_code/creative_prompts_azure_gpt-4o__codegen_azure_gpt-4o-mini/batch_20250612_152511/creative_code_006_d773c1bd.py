"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getsiteera.com
Prompt: Write a WordPress function that redirects users to a custom "Launch Your Site" page after login, inspired by SiteEra's messaging.
Generated: DETERMINISTIC_d773c1bd4f25e16c
Batch ID: 20250612_152511
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
 * Redirect users to a custom "Launch Your Site" page after login.
 *
 * This function hooks into the WordPress login system to redirect users 
 * to a specified URL after a successful login.
 *
 * @param string $redirect_to The URL the user is being redirected to.
 * @param string $requested_redirect_to The original request URL.
 * @param WP_User $user The logged-in user object.
 * @return string The redirect URL.
 */
function custom_login_redirect($redirect_to, $requested_redirect_to, $user) {
    // Check if the user is logged in and is a valid user object
    if (isset($user->roles) && is_array($user->roles)) {
        // Check for the user role you want to redirect (adjust as necessary)
        if (in_array('subscriber', $user->roles)) {
            // Set the URL to the custom "Launch Your Site" page
            $redirect_to = home_url('/launch-your-site'); // Change this to your actual URL
        }
    }
    
    return $redirect_to;
}

// Hook the function to the login redirect filter
add_filter('login_redirect', 'custom_login_redirect', 10, 3);
```

Make sure to replace the `'/launch-your-site'` in the `home_url` function with your actual "Launch Your Site" page URL.
