"""
Generated Code Metadata:
========================
Original URL: https://cpanel.dexodoor.com
Prompt: Write a PHP script to reset a cPanel user password using the cPanel API.
Generated: DETERMINISTIC_e3959507706fe8a3
Batch ID: 20250612_152441
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
 * cPanel Password Reset Script
 * 
 * This script resets a cPanel user's password using the cPanel API.
 * 
 * Requirements:
 * - cPanel API access with appropriate permissions
 * - PHP with cURL support
 */

class CPanelPasswordReset {
    private $cpanelUsername;
    private $cpanelPassword;
    private $cpanelHost;
    private $port;
    private $useSSL;

    /**
     * Constructor
     * 
     * @param string $cpanelUsername cPanel username with API access
     * @param string $cpanelPassword cPanel password
     * @param string $cpanelHost cPanel host (domain or IP)
     * @param int $port cPanel port (default: 2083 for SSL)
     * @param bool $useSSL Whether to use SSL (default: true)
     */
    public function __construct($cpanelUsername, $cpanelPassword, $cpanelHost, $port = 2083, $useSSL = true) {
        $this->cpanelUsername = $cpanelUsername;
        $this->cpanelPassword = $cpanelPassword;
        $this->cpanelHost = $cpanelHost;
        $this->port = $port;
        $this->useSSL = $useSSL;
    }

    /**
     * Reset a user's password
     * 
     * @param string $username The username whose password to reset
     * @param string $newPassword The new password
     * @return array API response
     * @throws Exception If API call fails
     */
    public function resetPassword($username, $newPassword) {
        if (empty($username) || empty($newPassword)) {
            throw new InvalidArgumentException("Username and password cannot be empty");
        }

        $protocol = $this->useSSL ? 'https' : 'http';
        $url = "$protocol://{$this->cpanelHost}:{$this->port}/execute/Passwd/change_password";

        $postFields = [
            'user' => $username,
            'password' => $newPassword,
            'enabledigest' => 1
        ];

        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, $url);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_POST, true);
        curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($postFields));
        curl_setopt($ch, CURLOPT_USERPWD, "{$this->cpanelUsername}:{$this->cpanelPassword}");
        curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
        curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, false);
        curl_setopt($ch, CURLOPT_TIMEOUT, 30);

        $response = curl_exec($ch);
        $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
        $error = curl_error($ch);
        curl_close($ch);

        if ($error) {
            throw new Exception("cURL Error: $error");
        }

        if ($httpCode !== 200) {
            throw new Exception("API request failed with HTTP code: $httpCode");
        }

        $decodedResponse = json_decode($response, true);
        if (json_last_error() !== JSON_ERROR_NONE) {
            throw new Exception("Failed to decode API response: " . json_last_error_msg());
        }

        return $decodedResponse;
    }
}

// Example usage:
try {
    $cpanel = new CPanelPasswordReset(
        'admin_username',  // cPanel admin username
        'admin_password',  // cPanel admin password
        'example.com'      // cPanel host
    );

    $result = $cpanel->resetPassword('target_user', 'new_secure_password');
    print_r($result);
} catch (Exception $e) {
    echo "Error: " . $e->getMessage();
}
?>
```
