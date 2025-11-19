"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solitairenetwork.com
Prompt: Write a PHP script that retrieves and displays the list of all 82 solitaire games from Solitaire Network, categorizing them by type and popularity.
Generated: DETERMINISTIC_f649b56e92ef3c37
Batch ID: 20250612_160526
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.solitaire-network.com/games": {
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
 * Solitaire Games Retriever
 *
 * This script fetches and displays a list of all solitaire games from the Solitaire Network,
 * categorizing them by type and popularity. It handles potential errors gracefully and follows
 * best practices for a production-ready PHP application.
 */

// Define the Solitaire Network API URL
define('SOLITAIRE_NETWORK_API_URL', 'https://api.solitaire-network.com/games');

// Function to fetch games from the Solitaire Network API
function fetchSolitaireGames($url) {
    // Initialize a cURL session
    $ch = curl_init($url);

    // Set cURL options
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_TIMEOUT, 10);

    // Execute the cURL request
    $response = curl_exec($ch);

    // Check for cURL errors
    if ($response === false) {
        $error = curl_error($ch);
        curl_close($ch);
        throw new Exception("cURL Error: $error");
    }

    // Close the cURL session
    curl_close($ch);

    // Decode the JSON response
    $games = json_decode($response, true);

    // Check for JSON errors
    if (json_last_error() !== JSON_ERROR_NONE) {
        throw new Exception("JSON Decode Error: " . json_last_error_msg());
    }

    return $games;
}

// Function to categorize and display games by type and popularity
function displayGames($games) {
    // Check if games array is empty
    if (empty($games)) {
        echo "No games found.";
        return;
    }

    // Categorize games by type
    $categorizedGames = [];
    foreach ($games as $game) {
        $type = $game['type'] ?? 'Unknown';
        $popularity = $game['popularity'] ?? 0;

        // Organizing games into categories
        if (!isset($categorizedGames[$type])) {
            $categorizedGames[$type] = [];
        }
        $categorizedGames[$type][] = [
            'name' => $game['name'],
            'popularity' => $popularity
        ];
    }

    // Display games categorized by type and popularity
    foreach ($categorizedGames as $type => $games) {
        echo "<h2>" . htmlspecialchars($type) . "</h2>";
        echo "<ul>";
        usort($games, function($a, $b) {
            return $b['popularity'] <=> $a['popularity']; // Sort by popularity descending
        });
        foreach ($games as $game) {
            echo "<li>" . htmlspecialchars($game['name']) . " - Popularity: " . htmlspecialchars($game['popularity']) . "</li>";
        }
        echo "</ul>";
    }
}

// Main execution block
try {
    // Fetch the list of solitaire games
    $games = fetchSolitaireGames(SOLITAIRE_NETWORK_API_URL);

    // Display the categorized games
    displayGames($games);

} catch (Exception $e) {
    // Display error message
    echo "An error occurred: " . htmlspecialchars($e->getMessage());
}
?>
```
