"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hubsupport.rf.gd
Prompt: Provide a PHP script to manage multiple email accounts hosted on iFastNet, leveraging their modern cPanel and unlimited email account support.
Generated: DETERMINISTIC_ef77663c07e88db4
Batch ID: 20250612_151459
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://{$this->cpanelHost}/json-api/cpanel?cpanel_jsonapi_user={$this->cpanelUser}&cpanel_jsonapi_apiversion=2": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://{$this-": {
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
 * Email Account Manager for iFastNet
 * This script manages multiple email accounts hosted on iFastNet using their cPanel API.
 * 
 * Requirements:
 * - PHP cURL extension enabled
 * - Basic knowledge of PHP and cPanel API
 */

class EmailAccountManager {
    private $cpanelHost;
    private $cpanelUser;
    private $cpanelPass;
    private $apiUrl;

    /**
     * Constructor to initialize cPanel connection details
     *
     * @param string $host iFastNet cPanel host
     * @param string $user cPanel username
     * @param string $pass cPanel password
     */
    public function __construct($host, $user, $pass) {
        $this->cpanelHost = $host;
        $this->cpanelUser = $user;
        $this->cpanelPass = $pass;
        $this->apiUrl = "https://{$this->cpanelHost}/json-api/cpanel?cpanel_jsonapi_user={$this->cpanelUser}&cpanel_jsonapi_apiversion=2";
    }

    /**
     * Create a new email account
     *
     * @param string $domain The domain for the email account
     * @param string $email The desired email address (without domain)
     * @param string $password The password for the email account
     * @param int $quota The mailbox quota in MB (0 for unlimited)
     * @return array Response from the cPanel API
     */
    public function createEmailAccount($domain, $email, $password, $quota = 0) {
        $params = [
            'module' => 'Email',
            'function' => 'add_pop',
            'domain' => $domain,
            'email' => $email,
            'password' => $password,
            'quota' => $quota
        ];

        return $this->callApi($params);
    }

    /**
     * Delete an existing email account
     *
     * @param string $domain The domain of the email account
     * @param string $email The email address to delete (without domain)
     * @return array Response from the cPanel API
     */
    public function deleteEmailAccount($domain, $email) {
        $params = [
            'module' => 'Email',
            'function' => 'del_pop',
            'domain' => $domain,
            'email' => $email
        ];

        return $this->callApi($params);
    }

    /**
     * Call the cPanel API and handle errors
     *
     * @param array $params Parameters to send to the API
     * @return array Response from the cPanel API
     */
    private function callApi($params) {
        // Build the query string from parameters
        $queryString = http_build_query($params);
        $url = $this->apiUrl . '&' . $queryString;

        // Initialize cURL
        $ch = curl_init($url);

        // Setting cURL options
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_USERPWD, "{$this->cpanelUser}:{$this->cpanelPass}");
        curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);

        // Execute the request
        $response = curl_exec($ch);

        // Error Handling
        if (curl_errno($ch)) {
            $errorMessage = curl_error($ch);
            curl_close($ch);
            throw new Exception("cURL Error: $errorMessage");
        }

        // Close cURL session
        curl_close($ch);

        // Decode the JSON response
        $responseData = json_decode($response, true);

        // Check for API errors
        if (isset($responseData['error'])) {
            throw new Exception("cPanel API Error: " . $responseData['error']);
        }

        return $responseData;
    }
}

// Usage example
try {
    $emailManager = new EmailAccountManager('your_cpanel_host', 'your_cpanel_user', 'your_cpanel_password');

    // Create a new email account
    $createResponse = $emailManager->createEmailAccount('example.com', 'user', 'securepassword', 0);
    print_r($createResponse);

    // Delete an existing email account
    $deleteResponse = $emailManager->deleteEmailAccount('example.com', 'user');
    print_r($deleteResponse);
} catch (Exception $e) {
    echo 'Error: ' . $e->getMessage();
}
?>
```
