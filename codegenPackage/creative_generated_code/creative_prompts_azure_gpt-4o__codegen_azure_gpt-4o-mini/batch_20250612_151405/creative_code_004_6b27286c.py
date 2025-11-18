"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://omantelmyworld.nowsport365.com
Prompt: Create a function in PHP to authenticate a user and retrieve their account details from the NowSport365 website's "My Account" section using cookies and session management.
Generated: DETERMINISTIC_6b27286c1e5a70de
Batch ID: 20250612_151405
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.nowsport365.com": {
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
 * Class NowSport365Authenticator
 *
 * This class handles user authentication and retrieval of account details
 * from the NowSport365 website. It manages cookies and sessions for secure
 * access to user data.
 */
class NowSport365Authenticator
{
    private $baseUrl = 'https://www.nowsport365.com'; // Base URL for the NowSport365 site
    private $session; // Session handler

    /**
     * Constructor to initialize session
     */
    public function __construct()
    {
        session_start(); // Start the PHP session
        $this->session = $_SESSION; // Reference to session variable
    }

    /**
     * Authenticate a user with the given credentials.
     *
     * @param string $username The username of the user
     * @param string $password The password of the user
     * @return array|null The user account details or null on failure
     */
    public function authenticate($username, $password)
    {
        // Prepare the request data
        $postData = http_build_query([
            'username' => $username,
            'password' => $password,
        ]);

        // Initialize cURL
        $ch = curl_init("{$this->baseUrl}/login"); // Set the login URL
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true); // Return response instead of printing
        curl_setopt($ch, CURLOPT_POST, true); // Enable POST
        curl_setopt($ch, CURLOPT_POSTFIELDS, $postData); // Set POST fields
        curl_setopt($ch, CURLOPT_COOKIEJAR, 'cookies.txt'); // Store cookies
        curl_setopt($ch, CURLOPT_COOKIEFILE, 'cookies.txt'); // Use stored cookies

        // Execute the request
        $response = curl_exec($ch);
        if ($response === false) {
            throw new Exception('Curl error: ' . curl_error($ch)); // Error handling for Curl
        }

        // Check for successful login
        if (strpos($response, 'Login successful') === false) {
            return null; // Return null if login failed
        }

        // Retrieve account details
        curl_setopt($ch, CURLOPT_URL, "{$this->baseUrl}/my-account"); // Set the account URL
        $accountResponse = curl_exec($ch);
        if ($accountResponse === false) {
            throw new Exception('Curl error: ' . curl_error($ch)); // Error handling for Curl
        }

        // Close cURL session
        curl_close($ch);

        // Parse and return account details (assuming JSON response)
        return $this->parseAccountDetails($accountResponse);
    }

    /**
     * Parse account details from the response.
     *
     * @param string $response The response from the account page
     * @return array The parsed account details
     */
    private function parseAccountDetails($response)
    {
        // Assuming response contains JSON data for account details
        $data = json_decode($response, true);
        if (json_last_error() !== JSON_ERROR_NONE) {
            throw new Exception('Failed to parse account details: ' . json_last_error_msg()); // JSON error handling
        }

        return $data; // Return parsed account details
    }

    /**
     * Clear session data and cookies.
     */
    public function logout()
    {
        // Clear session data
        session_unset();
        session_destroy(); // Destroy session
        if (file_exists('cookies.txt')) {
            unlink('cookies.txt'); // Remove cookie file
        }
    }
}

// Example usage
try {
    $authenticator = new NowSport365Authenticator();
    $accountDetails = $authenticator->authenticate('your_username', 'your_password');
    if ($accountDetails !== null) {
        // Successfully authenticated, display account details
        print_r($accountDetails);
    } else {
        echo "Authentication failed. Please check your username and password.";
    }
} catch (Exception $e) {
    // Handle exceptions gracefully
    echo "Error: " . $e->getMessage();
}

?>
```
