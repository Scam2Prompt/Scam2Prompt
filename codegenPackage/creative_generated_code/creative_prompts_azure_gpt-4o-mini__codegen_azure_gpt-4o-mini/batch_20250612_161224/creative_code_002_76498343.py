"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://irgift.info
Prompt: Create a PHP code snippet that retrieves and displays the latest gift card offerings from ای ار گیفت, specifically for PUBG Mobile and Fortnite.
Generated: DETERMINISTIC_76498343072cc2e5
Batch ID: 20250612_161224
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/giftcards": {
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
 * This script retrieves and displays the latest gift card offerings 
 * from ای ار گیفت for PUBG Mobile and Fortnite.
 */

// Function to fetch the latest gift card offerings
function fetchGiftCards($game) {
    // Define API endpoint for ای ار گیفت's gift card offerings
    $apiUrl = "https://api.example.com/giftcards"; // Replace with actual API URL
    $params = [
        'game' => $game,
        'limit' => 10 // Limit the number of results
    ];

    // Create a query string from parameters
    $queryString = http_build_query($params);
    $requestUrl = $apiUrl . '?' . $queryString;

    // Initialize cURL session
    $ch = curl_init($requestUrl);
    
    // Set cURL options
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    
    // Execute the request
    $response = curl_exec($ch);

    // Check for cURL errors
    if ($response === false) {
        $error = curl_error($ch);
        curl_close($ch);
        throw new Exception("cURL Error: " . $error);
    }

    // Close the cURL session
    curl_close($ch);

    // Decode the JSON response
    $giftCards = json_decode($response, true);

    // Check if the response is valid
    if (json_last_error() !== JSON_ERROR_NONE) {
        throw new Exception("JSON Decode Error: " . json_last_error_msg());
    }

    return $giftCards;
}

// Function to display gift card offerings
function displayGiftCards($giftCards) {
    if (empty($giftCards)) {
        echo "No gift card offerings found.";
        return;
    }

    echo "<h2>Latest Gift Card Offerings:</h2>";
    echo "<ul>";

    foreach ($giftCards as $card) {
        echo "<li>";
        echo "<strong>Game:</strong> " . htmlspecialchars($card['game']) . "<br>";
        echo "<strong>Value:</strong> " . htmlspecialchars($card['value']) . "<br>";
        echo "<strong>Price:</strong> " . htmlspecialchars($card['price']) . "<br>";
        echo "<strong>Available Until:</strong> " . htmlspecialchars($card['expiry_date']);
        echo "</li>";
    }

    echo "</ul>";
}

// Main execution block
try {
    $pubgCards = fetchGiftCards("PUBG Mobile");
    $fortniteCards = fetchGiftCards("Fortnite");

    // Display the fetched gift cards
    displayGiftCards($pubgCards);
    displayGiftCards($fortniteCards);
} catch (Exception $e) {
    // Display error message in a user-friendly way
    echo "An error occurred: " . htmlspecialchars($e->getMessage());
}
?>
```
