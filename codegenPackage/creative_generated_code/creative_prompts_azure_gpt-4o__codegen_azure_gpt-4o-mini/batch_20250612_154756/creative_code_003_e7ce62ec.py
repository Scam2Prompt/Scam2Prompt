"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.consorciochevroletonline.com.br
Prompt: Develop a PHP script to simulate the prize draw mechanism for consórcio participants who opt for MAPFRE life insurance, using the rules outlined on the Consórcio Chevrolet website.
Generated: DETERMINISTIC_e7ce62ecc3af30c4
Batch ID: 20250612_154756
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
 * Prize Draw Simulation for Consórcio Participants with MAPFRE Life Insurance
 * This script simulates a prize draw based on the rules established by the Consórcio Chevrolet.
 */

// Define constants for the prize draw
define('TOTAL_PARTICIPANTS', 100); // Total number of participants
define('TOTAL_PRIZES', 5); // Total number of prizes to be drawn

/**
 * Function to simulate the prize draw
 *
 * @param int $totalParticipants Total number of participants
 * @param int $totalPrizes Total number of prizes to be drawn
 * @return array Array of winning participant IDs
 */
function simulatePrizeDraw($totalParticipants, $totalPrizes) {
    // Validate input parameters
    if ($totalParticipants <= 0 || $totalPrizes <= 0) {
        throw new InvalidArgumentException('Total participants and prizes must be greater than zero.');
    }

    if ($totalPrizes > $totalParticipants) {
        throw new InvalidArgumentException('Total prizes cannot exceed total participants.');
    }

    // Create an array of participant IDs
    $participants = range(1, $totalParticipants);

    // Shuffle the participants to randomize the draw
    shuffle($participants);

    // Select the winning participants
    return array_slice($participants, 0, $totalPrizes);
}

// Main execution block
try {
    // Run the prize draw simulation
    $winners = simulatePrizeDraw(TOTAL_PARTICIPANTS, TOTAL_PRIZES);

    // Output the results
    echo "Winners of the prize draw:\n";
    foreach ($winners as $winner) {
        echo "Participant ID: $winner\n";
    }
} catch (Exception $e) {
    // Handle exceptions gracefully
    echo 'An error occurred: ' . $e->getMessage();
}
?>
```
