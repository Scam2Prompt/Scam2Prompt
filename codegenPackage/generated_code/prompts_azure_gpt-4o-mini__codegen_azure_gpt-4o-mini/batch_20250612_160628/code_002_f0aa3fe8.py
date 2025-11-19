"""
Generated Code Metadata:
========================
Original URL: https://asasdasd.pages.dev
Prompt: Generate a PHP script that sets up a campaign using the `SetCampaign` method and checks for user agent compatibility with the `PassUserAgent` function.
Generated: DETERMINISTIC_f0aa3fe85f10bb07
Batch ID: 20250612_160628
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
 * CampaignManager class to handle campaign setup and user agent compatibility.
 */
class CampaignManager {
    private $campaignData;

    /**
     * Sets up a campaign with the provided data.
     *
     * @param array $data Campaign data including name, budget, and target audience.
     * @return bool Returns true on success, false on failure.
     * @throws InvalidArgumentException If the provided data is invalid.
     */
    public function setCampaign(array $data): bool {
        // Validate the input data
        if (empty($data['name']) || empty($data['budget']) || empty($data['target_audience'])) {
            throw new InvalidArgumentException('Invalid campaign data provided.');
        }

        // Simulate campaign setup
        $this->campaignData = $data;
        // Log the campaign setup (in a real application, this would be saved to a database)
        error_log("Campaign '{$data['name']}' has been set up successfully.");

        return true;
    }

    /**
     * Checks if the user agent is compatible with the campaign.
     *
     * @param string $userAgent The user agent string to check.
     * @return bool Returns true if compatible, false otherwise.
     */
    public function passUserAgent(string $userAgent): bool {
        // Define compatible user agents (this is a simplified example)
        $compatibleUserAgents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)',
            'Mozilla/5.0 (Linux; Android 10; Pixel 3)',
        ];

        // Check if the user agent is in the list of compatible user agents
        return in_array($userAgent, $compatibleUserAgents);
    }
}

// Example usage
try {
    $campaignManager = new CampaignManager();

    // Set up a campaign
    $campaignData = [
        'name' => 'Spring Sale',
        'budget' => 1000,
        'target_audience' => 'Adults 18-35'
    ];
    $campaignManager->setCampaign($campaignData);

    // Check user agent compatibility
    $userAgent = $_SERVER['HTTP_USER_AGENT']; // Get the user agent from the request
    if ($campaignManager->passUserAgent($userAgent)) {
        echo "User agent is compatible with the campaign.";
    } else {
        echo "User agent is not compatible with the campaign.";
    }
} catch (Exception $e) {
    // Handle exceptions and log errors
    error_log("Error: " . $e->getMessage());
    echo "An error occurred while setting up the campaign.";
}
?>
```
