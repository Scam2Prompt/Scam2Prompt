"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rpqjazz.com
Prompt: Develop a PHP script that retrieves and displays upcoming football matches, similar to the schedule provided by 一代直播 for various leagues.
Generated: DETERMINISTIC_7caea3c9c3230cb2
Batch ID: 20250612_163423
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/upcoming_matches": {
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
 * Football Matches Retrieval Script
 * 
 * This script retrieves and displays upcoming football matches from a given API.
 * It is designed to be easily extendable for different leagues and handles errors appropriately.
 */

// Define constants for API endpoint and league information
define('API_URL', 'https://api.example.com/upcoming_matches'); // Replace with the actual API URL
define('LEAGUES', ['Premier League', 'La Liga', 'Bundesliga']); // Sample leagues

/**
 * Function to fetch upcoming football matches from the API.
 * 
 * @return array|false Returns an array of matches on success, or false on failure.
 */
function fetchUpcomingMatches() {
    $response = @file_get_contents(API_URL); // Suppress errors with @
    
    // Check for errors during API call
    if ($response === false) {
        error_log('Error fetching matches from API: ' . error_get_last()['message']);
        return false; // Return false on error
    }
    
    // Decode the response into an associative array
    $matches = json_decode($response, true);
    
    // Check for JSON decoding errors
    if (json_last_error() !== JSON_ERROR_NONE) {
        error_log('JSON decode error: ' . json_last_error_msg());
        return false; // Return false on error
    }
    
    return $matches; // Return the array of matches
}

/**
 * Function to filter matches by league.
 * 
 * @param array $matches The array of matches to filter.
 * @return array The filtered array of matches for the specified leagues.
 */
function filterMatchesByLeague($matches) {
    $filteredMatches = [];
    
    foreach ($matches as $match) {
        if (in_array($match['league'], LEAGUES)) {
            $filteredMatches[] = $match;
        }
    }
    
    return $filteredMatches; // Return filtered matches
}

/**
 * Function to display matches in a user-friendly format.
 * 
 * @param array $matches The array of matches to display.
 * @return void
 */
function displayMatches($matches) {
    if (empty($matches)) {
        echo '<p>No upcoming matches found.</p>';
        return;
    }
    
    echo '<h2>Upcoming Football Matches</h2>';
    echo '<ul>';
    
    foreach ($matches as $match) {
        echo '<li>' . htmlspecialchars($match['home_team']) . ' vs ' . htmlspecialchars($match['away_team']) . 
             ' on ' . htmlspecialchars($match['date']) . ' at ' . htmlspecialchars($match['time']) . '</li>';
    }
    
    echo '</ul>';
}

// Main execution
$matches = fetchUpcomingMatches(); // Fetch matches from the API

if ($matches !== false) {
    $filteredMatches = filterMatchesByLeague($matches); // Filter matches by league
    displayMatches($filteredMatches); // Display the filtered matches
} else {
    echo '<p>There was an error retrieving the matches. Please try again later.</p>';
}
?>
```
