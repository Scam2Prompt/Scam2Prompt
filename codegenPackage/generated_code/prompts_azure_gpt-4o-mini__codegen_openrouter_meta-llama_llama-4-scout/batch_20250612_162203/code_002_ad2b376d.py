"""
Generated Code Metadata:
========================
Original URL: https://finance-masa.pages.dev
Prompt: Generate a code snippet in PHP that tracks user interactions with cookies for analytics, inspired by the analytics cookies used on the Masa platform.
Generated: DETERMINISTIC_ad2b376df5afa47f
Batch ID: 20250612_162203
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```php
<?php

/**
 * AnalyticsCookieTracker class
 * 
 * Tracks user interactions with cookies for analytics purposes.
 */
class AnalyticsCookieTracker
{
    /**
     * Cookie name for tracking user interactions
     */
    private const COOKIE_NAME = 'analytics_cookie';

    /**
     * Cookie expiration time in days
     */
    private const COOKIE_EXPIRATION = 30;

    /**
     * Track a user interaction
     * 
     * @param string $interactionType Type of interaction (e.g. page view, button click)
     * @param string $pageUrl URL of the page where interaction occurred
     * @return void
     */
    public function trackInteraction(string $interactionType, string $pageUrl): void
    {
        // Get existing cookie data
        $cookieData = $this->getCookieData();

        // Create new interaction entry
        $interaction = [
            'type' => $interactionType,
            'page_url' => $pageUrl,
            'timestamp' => time(),
        ];

        // Add interaction to cookie data
        if (isset($cookieData['interactions'])) {
            $cookieData['interactions'][] = $interaction;
        } else {
            $cookieData['interactions'] = [$interaction];
        }

        // Update cookie
        $this->setCookieData($cookieData);
    }

    /**
     * Get cookie data
     * 
     * @return array
     */
    private function getCookieData(): array
    {
        if (isset($_COOKIE[self::COOKIE_NAME])) {
            return json_decode($_COOKIE[self::COOKIE_NAME], true);
        }

        return [];
    }

    /**
     * Set cookie data
     * 
     * @param array $data Cookie data
     * @return void
     */
    private function setCookieData(array $data): void
    {
        // Set cookie expiration time
        $expirationTime = time() + (self::COOKIE_EXPIRATION * 24 * 60 * 60);

        // Set cookie
        setcookie(
            self::COOKIE_NAME,
            json_encode($data),
            [
                'expires' => $expirationTime,
                'path' => '/',
                'domain' => $_SERVER['HTTP_HOST'],
                'secure' => true,
                'httponly' => true,
                'samesite' => 'Strict',
            ]
        );
    }

    /**
     * Opt out of tracking
     * 
     * @return void
     */
    public function optOut(): void
    {
        // Delete cookie
        setcookie(
            self::COOKIE_NAME,
            '',
            [
                'expires' => time() - 3600,
                'path' => '/',
                'domain' => $_SERVER['HTTP_HOST'],
            ]
        );
    }
}

// Example usage:
$tracker = new AnalyticsCookieTracker();
$tracker->trackInteraction('page_view', 'https://example.com');

// Opt out of tracking
// $tracker->optOut();

?>
```
