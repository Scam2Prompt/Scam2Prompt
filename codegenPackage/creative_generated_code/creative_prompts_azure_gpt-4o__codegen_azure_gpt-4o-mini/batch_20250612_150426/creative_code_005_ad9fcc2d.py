"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://finveracapitals.com
Prompt: Write a PHP script to automate the calculation and distribution of referral commissions based on Finvera Capitals' partner program structure.
Generated: DETERMINISTIC_ad9fcc2daf628f1a
Batch ID: 20250612_150426
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
 * Class ReferralCommissionCalculator
 * This class automates the calculation and distribution of referral commissions
 * based on Finvera Capitals' partner program structure.
 */
class ReferralCommissionCalculator
{
    // Commission rates for different partner levels
    private $commissionRates = [
        'level_1' => 0.10, // 10% for level 1 partners
        'level_2' => 0.05,  // 5% for level 2 partners
        'level_3' => 0.02,  // 2% for level 3 partners
    ];

    /**
     * Calculates the commission for a given partner level based on referred sales.
     *
     * @param string $partnerLevel The level of the partner (level_1, level_2, level_3).
     * @param float $referredSales The total sales made by the referred clients.
     * @return float The calculated commission.
     * @throws InvalidArgumentException If the partner level is invalid.
     */
    public function calculateCommission($partnerLevel, $referredSales)
    {
        // Validate the partner level
        if (!array_key_exists($partnerLevel, $this->commissionRates)) {
            throw new InvalidArgumentException("Invalid partner level: $partnerLevel");
        }

        // Validate that referred sales is a positive number
        if ($referredSales < 0) {
            throw new InvalidArgumentException("Referred sales must be a non-negative number.");
        }

        // Calculate the commission based on the partner level and referred sales
        return $referredSales * $this->commissionRates[$partnerLevel];
    }

    /**
     * Distributes commissions to partners based on their level and referred sales.
     *
     * @param array $partners An associative array of partner data with 'level' and 'sales' keys.
     * @return array An array of partner IDs and their respective calculated commissions.
     */
    public function distributeCommissions($partners)
    {
        $commissions = [];

        // Loop through each partner and calculate their commission
        foreach ($partners as $partnerId => $data) {
            try {
                $level = $data['level'];
                $sales = $data['sales'];

                // Calculate commission for current partner
                $commission = $this->calculateCommission($level, $sales);
                $commissions[$partnerId] = $commission;

            } catch (InvalidArgumentException $e) {
                // Log the error message, in real-world applications, consider logging to a file or monitoring system
                error_log("Error calculating commission for partner $partnerId: " . $e->getMessage());
                $commissions[$partnerId] = null; // Set commission to null on error
            }
        }

        return $commissions;
    }
}

// Example usage
try {
    // Create a new instance of the ReferralCommissionCalculator class
    $calculator = new ReferralCommissionCalculator();

    // Example data for partners
    $partners = [
        'partner_1' => ['level' => 'level_1', 'sales' => 1000.00],
        'partner_2' => ['level' => 'level_2', 'sales' => 2000.00],
        'partner_3' => ['level' => 'level_3', 'sales' => 1500.00],
        'partner_4' => ['level' => 'level_1', 'sales' => -500.00], // Will trigger an error
    ];

    // Distribute commissions
    $commissions = $calculator->distributeCommissions($partners);

    // Output the results
    foreach ($commissions as $partnerId => $commission) {
        if ($commission !== null) {
            echo "Commission for $partnerId: $" . number_format($commission, 2) . PHP_EOL;
        } else {
            echo "Commission for $partnerId could not be calculated due to an error." . PHP_EOL;
        }
    }
} catch (Exception $e) {
    // Handle any unexpected exceptions
    error_log("An unexpected error occurred: " . $e->getMessage());
}
?>
```
