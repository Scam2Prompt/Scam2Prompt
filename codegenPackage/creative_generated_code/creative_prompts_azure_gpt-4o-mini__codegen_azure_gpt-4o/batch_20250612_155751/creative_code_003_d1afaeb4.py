"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ecbc.online
Prompt: Develop a PHP script that automates the posting of new radio program announcements to social media, based on the schedule provided by ECBC Radio.
Generated: DETERMINISTIC_d1afaeb40940af04
Batch ID: 20250612_155751
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.twitter.com/2/tweets": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://graph.facebook.com/v12.0/me/feed": {
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
 * ECBC Radio Program Announcement Automation
 *
 * This script automates the posting of new radio program announcements
 * to social media platforms based on a predefined schedule.
 *
 * Dependencies:
 * 1. Social media API credentials (e.g., Twitter, Facebook).
 * 2. Schedule data stored as a JSON file.
 */

// Load required libraries for HTTP requests and JSON handling.
require 'vendor/autoload.php'; // Composer autoload for external libraries like HTTP clients.

use GuzzleHttp\Client;

// Configuration settings
$config = [
    'schedule_file' => 'radio_schedule.json', // Path to the schedule file.
    'social_media_api_keys' => [
        'twitter' => 'YOUR_TWITTER_API_KEY',
        'facebook' => 'YOUR_FACEBOOK_API_KEY',
    ],
    'timezone' => 'America/New_York', // Update to match your timezone.
];

// Error reporting settings
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Load the radio program schedule
function loadSchedule($filePath)
{
    if (!file_exists($filePath)) {
        throw new Exception("Schedule file not found: {$filePath}");
    }
    $scheduleData = file_get_contents($filePath);
    return json_decode($scheduleData, true);
}

// Post announcement to Twitter
function postToTwitter($message, $apiKey)
{
    $client = new Client();
    try {
        $response = $client->post('https://api.twitter.com/2/tweets', [
            'headers' => [
                'Authorization' => "Bearer {$apiKey}",
                'Content-Type' => 'application/json',
            ],
            'json' => ['text' => $message],
        ]);
        return $response->getStatusCode() === 201;
    } catch (Exception $e) {
        error_log("Error posting to Twitter: " . $e->getMessage());
        return false;
    }
}

// Post announcement to Facebook
function postToFacebook($message, $apiKey)
{
    $client = new Client();
    try {
        $response = $client->post('https://graph.facebook.com/v12.0/me/feed', [
            'headers' => [
                'Authorization' => "Bearer {$apiKey}",
            ],
            'form_params' => ['message' => $message],
        ]);
        return $response->getStatusCode() === 200;
    } catch (Exception $e) {
        error_log("Error posting to Facebook: " . $e->getMessage());
        return false;
    }
}

// Generate the announcement message
function generateMessage($program)
{
    $title = $program['title'];
    $time = $program['time'];
    $description = $program['description'] ?? '';
    return "📻 Tune in to ECBC Radio for \"{$title}\" at {$time}! {$description}";
}

// Main script logic
try {
    date_default_timezone_set($config['timezone']);
    $schedule = loadSchedule($config['schedule_file']);

    // Check today's programs
    $today = date('Y-m-d');
    foreach ($schedule as $program) {
        if ($program['date'] === $today) {
            $message = generateMessage($program);

            // Post announcements to social media
            $twitterSuccess = postToTwitter($message, $config['social_media_api_keys']['twitter']);
            $facebookSuccess = postToFacebook($message, $config['social_media_api_keys']['facebook']);

            if ($twitterSuccess) {
                echo "Successfully posted to Twitter.\n";
            } else {
                echo "Failed to post to Twitter.\n";
            }

            if ($facebookSuccess) {
                echo "Successfully posted to Facebook.\n";
            } else {
                echo "Failed to post to Facebook.\n";
            }
        }
    }
} catch (Exception $e) {
    error_log("An error occurred: " . $e->getMessage());
}

?>
```
