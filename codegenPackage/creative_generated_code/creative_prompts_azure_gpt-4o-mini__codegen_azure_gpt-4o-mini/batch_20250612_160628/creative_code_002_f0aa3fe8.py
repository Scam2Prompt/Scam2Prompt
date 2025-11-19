"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asasdasd.pages.dev
Prompt: Generate a PHP script that sets up a campaign using the `SetCampaign` method and checks for user agent compatibility with the `PassUserAgent` function.
Generated: DETERMINISTIC_f0aa3fe85f10bb07
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
 * CampaignManager class handles campaign setup and user agent checks.
 */
class CampaignManager
{
    /**
     * Sets up a campaign using given parameters.
     *
     * @param array $campaignData An associative array containing campaign information.
     * @return bool Returns true if the campaign is set up successfully, false otherwise.
     * @throws InvalidArgumentException If the input data is invalid.
     */
    public function setCampaign(array $campaignData): bool
    {
        // Validate the input data
        if (!$this->isValidCampaignData($campaignData)) {
            throw new InvalidArgumentException('Invalid campaign data provided.');
        }

        // Assuming we have a method to actually set the campaign in the system
        try {
            // Simulated campaign setup logic
            // In a real-world scenario, this would involve database calls or API requests.
            // For example: CampaignAPI::create($campaignData);
            echo "Campaign '{$campaignData['name']}' has been set up successfully.\n";
            return true;
        } catch (Exception $e) {
            // Log the exception message (in a production scenario, use a logging library)
            error_log('Error setting up campaign: ' . $e->getMessage());
            return false;
        }
    }

    /**
     * Checks if the user agent is compatible.
     *
     * @param string $userAgent The user agent string to be checked.
     * @return bool Returns true if compatible, false otherwise.
     */
    public function passUserAgent(string $userAgent): bool
    {
        // Define a list of compatible user agents (for demonstration purposes)
        $compatibleUserAgents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Safari/605.1.15',
            // Add more compatible user agents as necessary
        ];

        // Check if the user agent is in the list of compatible user agents
        return in_array($userAgent, $compatibleUserAgents);
    }

    /**
     * Validates the campaign data.
     *
     * @param array $data The campaign data to validate.
     * @return bool Returns true if valid, false otherwise.
     */
    private function isValidCampaignData(array $data): bool
    {
        // Check for required fields (for example: 'name' and 'budget')
        return isset($data['name']) && isset($data['budget']) && is_numeric($data['budget']);
    }
}

// Example usage
try {
    $campaignManager = new CampaignManager();

    // Example campaign data
    $campaignData = [
        'name' => 'Fall Sale',
        'budget' => 5000,
        // Other campaign parameters can be added here
    ];

    // Set up the campaign
    $isCampaignSet = $campaignManager->setCampaign($campaignData);

    // Check user agent compatibility
    $userAgent = $_SERVER['HTTP_USER_AGENT'] ?? '';
    if ($campaignManager->passUserAgent($userAgent)) {
        echo "User agent is compatible.\n";
    } else {
        echo "User agent is not compatible.\n";
    }

} catch (InvalidArgumentException $e) {
    echo 'Campaign setup error: ' . $e->getMessage() . "\n";
} catch (Exception $e) {
    echo 'An unexpected error occurred: ' . $e->getMessage() . "\n";
}
?>
```
