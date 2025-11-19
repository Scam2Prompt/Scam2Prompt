"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fuel.network-drop.net
Prompt: Create a PHP script that integrates with an affiliate marketing platform to manage and optimize campaigns, reflecting the techniques mentioned in the provided content.
Generated: DETERMINISTIC_2b043cebb346462d
Batch ID: 20250612_155601
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://affiliate-platform.com/api": {
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
 * Affiliate Campaign Manager
 * 
 * This PHP script integrates with an affiliate marketing platform to manage and optimize campaigns.
 * It retrieves campaign data via API, calculates key performance metrics, and optimizes campaigns based on the data.
 * 
 * Requirements:
 * - PHP 7.4 or higher
 * - Curl extension enabled
 */

declare(strict_types=1);

class AffiliateCampaignManager
{
    private string $apiBaseUrl;
    private string $apiKey;

    /**
     * Constructor to initialize API base URL and key.
     *
     * @param string $apiBaseUrl Base URL of the affiliate platform API.
     * @param string $apiKey API key for authentication.
     */
    public function __construct(string $apiBaseUrl, string $apiKey)
    {
        $this->apiBaseUrl = rtrim($apiBaseUrl, '/');
        $this->apiKey = $apiKey;
    }

    /**
     * Fetch campaign data from the affiliate platform.
     *
     * @param string $endpoint API endpoint for campaigns.
     * @return array An associative array of campaign data.
     * @throws Exception If the API request fails.
     */
    public function fetchCampaignData(string $endpoint): array
    {
        $url = "{$this->apiBaseUrl}/{$endpoint}";

        $curl = curl_init($url);
        curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($curl, CURLOPT_HTTPHEADER, [
            "Authorization: Bearer {$this->apiKey}",
            "Content-Type: application/json"
        ]);

        $response = curl_exec($curl);
        $httpCode = curl_getinfo($curl, CURLINFO_HTTP_CODE);

        if (curl_errno($curl)) {
            throw new Exception('Curl error: ' . curl_error($curl));
        }

        curl_close($curl);

        if ($httpCode !== 200) {
            throw new Exception("API request failed with HTTP code $httpCode");
        }

        $data = json_decode($response, true);
        if (json_last_error() !== JSON_ERROR_NONE) {
            throw new Exception('Failed to decode JSON response: ' . json_last_error_msg());
        }

        return $data;
    }

    /**
     * Calculate performance metrics for campaigns.
     *
     * @param array $campaigns List of campaigns.
     * @return array An array of campaigns with performance metrics (e.g., ROI, CTR).
     */
    public function calculateMetrics(array $campaigns): array
    {
        foreach ($campaigns as &$campaign) {
            // Ensure required fields exist
            if (!isset($campaign['spend'], $campaign['revenue'], $campaign['clicks'], $campaign['impressions'])) {
                throw new Exception('Missing required fields in campaign data');
            }

            // Calculate ROI (Return on Investment)
            $campaign['roi'] = $campaign['revenue'] > 0 && $campaign['spend'] > 0 
                ? ($campaign['revenue'] - $campaign['spend']) / $campaign['spend'] * 100 
                : 0;

            // Calculate CTR (Click-through rate)
            $campaign['ctr'] = $campaign['clicks'] > 0 && $campaign['impressions'] > 0 
                ? ($campaign['clicks'] / $campaign['impressions']) * 100 
                : 0;
        }

        return $campaigns;
    }

    /**
     * Optimize campaigns based on performance data.
     *
     * @param array $campaigns List of campaigns with performance metrics.
     * @return array An array of optimized campaigns.
     */
    public function optimizeCampaigns(array $campaigns): array
    {
        foreach ($campaigns as &$campaign) {
            // Disable campaigns with negative ROI
            if ($campaign['roi'] < 0) {
                $campaign['status'] = 'paused';
            } else {
                $campaign['status'] = 'active';
            }

            // Adjust budget for campaigns with high CTR and positive ROI
            if ($campaign['ctr'] > 5 && $campaign['roi'] > 20) {
                $campaign['budget'] = isset($campaign['budget']) ? $campaign['budget'] * 1.2 : 0;
            }
        }

        return $campaigns;
    }

    /**
     * Update campaign data on the affiliate platform.
     *
     * @param array $campaigns List of campaigns to update.
     * @param string $endpoint API endpoint for updating campaigns.
     * @return void
     * @throws Exception If the API request to update fails.
     */
    public function updateCampaignData(array $campaigns, string $endpoint): void
    {
        $url = "{$this->apiBaseUrl}/{$endpoint}";

        $curl = curl_init($url);
        curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($curl, CURLOPT_HTTPHEADER, [
            "Authorization: Bearer {$this->apiKey}",
            "Content-Type: application/json"
        ]);
        curl_setopt($curl, CURLOPT_POST, true);
        curl_setopt($curl, CURLOPT_POSTFIELDS, json_encode($campaigns));

        $response = curl_exec($curl);
        $httpCode = curl_getinfo($curl, CURLINFO_HTTP_CODE);

        if (curl_errno($curl)) {
            throw new Exception('Curl error: ' . curl_error($curl));
        }

        curl_close($curl);

        if ($httpCode !== 200) {
            throw new Exception("Failed to update campaigns. HTTP code: $httpCode");
        }
    }
}

// Example usage
try {
    $apiBaseUrl = 'https://affiliate-platform.com/api';
    $apiKey = 'your-api-key-here';

    $manager = new AffiliateCampaignManager($apiBaseUrl, $apiKey);

    // Step 1: Fetch campaign data
    $campaignData = $manager->fetchCampaignData('campaigns');

    // Step 2: Calculate performance metrics
    $campaignsWithMetrics = $manager->calculateMetrics($campaignData);

    // Step 3: Optimize campaigns
    $optimizedCampaigns = $manager->optimizeCampaigns($campaignsWithMetrics);

    // Step 4: Update optimized campaigns
    $manager->updateCampaignData($optimizedCampaigns, 'update-campaigns');

    echo "Campaigns successfully managed and updated.";
} catch (Exception $e) {
    echo "Error: " . $e->getMessage();
}
?>
```
