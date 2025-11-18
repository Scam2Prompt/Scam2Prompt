"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unichain-rooster.nfts2.me
Prompt: Create a script in PHP to calculate and display the referral earnings based on the number of mints completed through a given referral link for Unichain-Rooster NFTs.
Generated: DETERMINISTIC_a861f36202e2496d
Batch ID: 20250612_153916
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
 * Referral Earnings Calculator for Unichain-Rooster NFTs
 *
 * This script calculates and displays the referral earnings based on the number of mints completed
 * through a given referral link. The earnings per mint can be adjusted as needed.
 */

class ReferralEarningsCalculator {
    private $earningsPerMint; // Earnings for each mint
    private $totalMints;       // Total number of mints through the referral

    /**
     * Constructor to initialize the earnings per mint and total mints
     *
     * @param float $earningsPerMint Earnings for each mint
     * @param int $totalMints Total number of mints
     */
    public function __construct(float $earningsPerMint, int $totalMints) {
        $this->setEarningsPerMint($earningsPerMint);
        $this->setTotalMints($totalMints);
    }

    /**
     * Set the earnings per mint
     *
     * @param float $earningsPerMint Earnings for each mint
     * @throws InvalidArgumentException if earnings per mint is negative
     */
    public function setEarningsPerMint(float $earningsPerMint) {
        if ($earningsPerMint < 0) {
            throw new InvalidArgumentException('Earnings per mint cannot be negative.');
        }
        $this->earningsPerMint = $earningsPerMint;
    }

    /**
     * Set the total number of mints
     *
     * @param int $totalMints Total number of mints
     * @throws InvalidArgumentException if total mints is negative
     */
    public function setTotalMints(int $totalMints) {
        if ($totalMints < 0) {
            throw new InvalidArgumentException('Total mints cannot be negative.');
        }
        $this->totalMints = $totalMints;
    }

    /**
     * Calculate the total earnings based on mints
     *
     * @return float Total earnings from referrals
     */
    public function calculateTotalEarnings(): float {
        return $this->earningsPerMint * $this->totalMints;
    }

    /**
     * Display the total earnings
     *
     * @return void
     */
    public function displayEarnings(): void {
        $totalEarnings = $this->calculateTotalEarnings();
        echo "Total earnings from referrals: $" . number_format($totalEarnings, 2) . PHP_EOL;
    }
}

// User input (for example purposes; in a real application, this could come from a form)
$earningsPerMint = 0.10; // Set earnings per mint
$totalMints = 50; // Set total mints

try {
    // Create an instance of the ReferralEarningsCalculator
    $calculator = new ReferralEarningsCalculator($earningsPerMint, $totalMints);
    
    // Display the calculated earnings
    $calculator->displayEarnings();
} catch (Exception $e) {
    // Handle exceptions and display error message
    echo 'Error: ' . $e->getMessage() . PHP_EOL;
}
?>
```
