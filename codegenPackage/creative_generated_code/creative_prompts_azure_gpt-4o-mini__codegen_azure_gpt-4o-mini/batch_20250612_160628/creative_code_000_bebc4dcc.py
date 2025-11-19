"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asasdasd.pages.dev
Prompt: Write a PHP function that utilizes the `CheckIP` method from the CloakerlyChecker class to validate an IP address and handle the response accordingly.
Generated: DETERMINISTIC_bebc4dcc74d5cae7
Batch ID: 20250612_160628
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
 * Class CloakerlyChecker
 * 
 * This is a placeholder class representing the CloakerlyChecker.
 * Replace this with the actual implementation to connect to the service.
 */
class CloakerlyChecker {
    /**
     * Check if the provided IP address is valid.
     *
     * @param string $ipAddress The IP address to validate.
     * @return array An associative array containing the response data.
     */
    public function CheckIP(string $ipAddress): array {
        // Simulate a response from the CloakerlyChecker service
        return [
            'valid' => true, // Simulate valid/invalid response
            'message' => 'IP address is valid', // Response message
        ];
    }
}

/**
 * Validate an IP address using the CloakerlyChecker service.
 *
 * @param string $ipAddress The IP address to validate.
 * @return void
 * @throws InvalidArgumentException If the IP address is invalid.
 */
function validateIPAddress(string $ipAddress): void {
    // Validate the format of the IP address
    if (!filter_var($ipAddress, FILTER_VALIDATE_IP)) {
        throw new InvalidArgumentException("Invalid IP address format: {$ipAddress}");
    }

    // Create an instance of the CloakerlyChecker service
    $checker = new CloakerlyChecker();

    // Call the CheckIP method and handle the response
    try {
        $response = $checker->CheckIP($ipAddress);
        
        // Check if the response indicates a valid IP address
        if ($response['valid']) {
            echo "Success: " . $response['message'] . PHP_EOL;
        } else {
            echo "Error: " . $response['message'] . PHP_EOL;
        }
    } catch (Exception $e) {
        // Handle any exceptions that may occur during the check
        echo "An error occurred while checking the IP address: " . $e->getMessage() . PHP_EOL;
    }
}

// Example usage
try {
    validateIPAddress('192.168.1.1'); // Replace with any IP to validate
} catch (InvalidArgumentException $e) {
    echo "Input error: " . $e->getMessage() . PHP_EOL;
}
?>
```
