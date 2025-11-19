"""
Generated Code Metadata:
========================
Original URL: https://www.consorciochevroletonline.com.br
Prompt: Develop a PHP script to simulate the prize draw mechanism for consórcio participants who opt for MAPFRE life insurance, using the rules outlined on the Consórcio Chevrolet website.
Generated: DETERMINISTIC_e7ce62ecc3af30c4
Batch ID: 20250612_154756
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
 * Prize Draw Simulator for Consórcio Participants with MAPFRE Life Insurance
 * 
 * This script simulates the prize draw mechanism based on the rules outlined on the Consórcio Chevrolet website.
 * It randomly selects winners from a list of participants who have opted for MAPFRE life insurance.
 */

class PrizeDrawSimulator {
    private $participants;
    private $winnersCount;
    private $prizes;

    /**
     * Constructor
     * 
     * @param array $participants List of participants (must have MAPFRE insurance)
     * @param int $winnersCount Number of winners to draw
     * @param array $prizes List of prizes to be awarded
     */
    public function __construct(array $participants, int $winnersCount, array $prizes) {
        $this->validateInput($participants, $winnersCount, $prizes);

        $this->participants = $participants;
        $this->winnersCount = $winnersCount;
        $this->prizes = $prizes;
    }

    /**
     * Validate input parameters
     * 
     * @param array $participants
     * @param int $winnersCount
     * @param array $prizes
     * @throws InvalidArgumentException If validation fails
     */
    private function validateInput(array $participants, int $winnersCount, array $prizes): void {
        if (empty($participants)) {
            throw new InvalidArgumentException('Participants list cannot be empty');
        }

        if ($winnersCount <= 0) {
            throw new InvalidArgumentException('Winners count must be greater than zero');
        }

        if (count($participants) < $winnersCount) {
            throw new InvalidArgumentException('Not enough participants for the requested number of winners');
        }

        if (empty($prizes)) {
            throw new InvalidArgumentException('Prizes list cannot be empty');
        }

        if (count($prizes) < $winnersCount) {
            throw new InvalidArgumentException('Not enough prizes for the requested number of winners');
        }
    }

    /**
     * Perform the prize draw
     * 
     * @return array Array of winners with their assigned prizes
     */
    public function draw(): array {
        $winners = [];
        $availableParticipants = $this->participants;
        $availablePrizes = $this->prizes;

        for ($i = 0; $i < $this->winnersCount; $i++) {
            // Select random participant
            $participantIndex = array_rand($availableParticipants);
            $winner = $availableParticipants[$participantIndex];

            // Select random prize
            $prizeIndex = array_rand($availablePrizes);
            $prize = $availablePrizes[$prizeIndex];

            // Add to winners list
            $winners[] = [
                'participant' => $winner,
                'prize' => $prize
            ];

            // Remove selected participant and prize from available pools
            unset($availableParticipants[$participantIndex]);
            unset($availablePrizes[$prizeIndex]);
        }

        return $winners;
    }

    /**
     * Get all participants
     * 
     * @return array
     */
    public function getParticipants(): array {
        return $this->participants;
    }

    /**
     * Get all prizes
     * 
     * @return array
     */
    public function getPrizes(): array {
        return $this->prizes;
    }
}

// Example usage:
try {
    // Sample data (in a real application, this would come from a database)
    $participants = [
        ['id' => 1, 'name' => 'John Doe', 'has_mapfre_insurance' => true],
        ['id' => 2, 'name' => 'Jane Smith', 'has_mapfre_insurance' => true],
        ['id' => 3, 'name' => 'Robert Johnson', 'has_mapfre_insurance' => true],
        ['id' => 4, 'name' => 'Emily Davis', 'has_mapfre_insurance' => true],
        ['id' => 5, 'name' => 'Michael Brown', 'has_mapfre_insurance' => true],
    ];

    // Filter only participants with MAPFRE insurance
    $eligibleParticipants = array_filter($participants, function($participant) {
        return $participant['has_mapfre_insurance'] === true;
    });

    $prizes = [
        'Car',
        'Motorcycle',
        'Trip',
        'Cash Prize',
        'Electronics'
    ];

    $drawSimulator = new PrizeDrawSimulator($eligibleParticipants, 3, $prizes);
    $winners = $drawSimulator->draw();

    // Output results
    header('Content-Type: application/json');
    echo json_encode([
        'success' => true,
        'winners' => $winners,
        'total_participants' => count($eligibleParticipants),
        'total_winners' => count($winners)
    ], JSON_PRETTY_PRINT);

} catch (Exception $e) {
    header('Content-Type: application/json');
    http_response_code(400);
    echo json_encode([
        'success' => false,
        'error' => $e->getMessage()
    ], JSON_PRETTY_PRINT);
}
?>
```
