"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asasdasd.pages.dev
Prompt: Generate a PHP script to handle IP address detection using the `GetIP` method described in the documentation.
Generated: DETERMINISTIC_ab8f50989e23fc8b
Batch ID: 20250612_151931
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
 * Class IPAddressDetector
 *
 * This class provides a method to detect the client's IP address
 * using various server variables.
 */
class IPAddressDetector {

    /**
     * Gets the client's IP address.
     *
     * This method checks multiple server variables to determine the
     * IP address of the user. It handles cases where the user may be
     * behind a proxy.
     *
     * @return string|null The client's IP address or null on failure.
     */
    public static function getIP() {
        // Initialize the IP address variable
        $ipAddress = null;

        // Check for shared internet access
        if (!empty($_SERVER['HTTP_CLIENT_IP'])) {
            $ipAddress = $_SERVER['HTTP_CLIENT_IP'];
        }
        // Check for the proxy user
        elseif (!empty($_SERVER['HTTP_X_FORWARDED_FOR'])) {
            // Explode the string to get the first valid IP
            $ipArray = explode(',', $_SERVER['HTTP_X_FORWARDED_FOR']);
            $ipAddress = trim($ipArray[0]);
        }
        // Fallback to remote address
        else {
            $ipAddress = $_SERVER['REMOTE_ADDR'];
        }

        // Validate the IP address format
        if (filter_var($ipAddress, FILTER_VALIDATE_IP)) {
            return $ipAddress;
        }

        // Return null if no valid IP address is found
        return null;
    }
}

// Example usage of the IPAddressDetector class
try {
    // Get the client's IP address
    $clientIP = IPAddressDetector::getIP();

    if ($clientIP) {
        echo "Client IP Address: " . htmlspecialchars($clientIP);
    } else {
        throw new Exception("Unable to detect IP address.");
    }
} catch (Exception $e) {
    // Handle any exceptions that occur during the process
    echo "Error: " . htmlspecialchars($e->getMessage());
}
?>
```
