"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ibcaj.org
Prompt: Write a PHP script to calculate the total entry fees for a group attending the Holy Saraswati Puja, based on the age categories and lunch options provided by the India (Bengal) Cultural Association Japan.
Generated: DETERMINISTIC_75fb5f5b1d910f4c
Batch ID: 20250612_162051
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
 * Class to calculate total entry fees for the Holy Saraswati Puja event.
 */
class SaraswatiPujaEntryFeeCalculator
{
    // Define age categories and corresponding fees
    private $ageCategories = [
        'child' => 5,   // Fee for children (age 0-12)
        'adult' => 10,  // Fee for adults (age 13-59)
        'senior' => 7    // Fee for seniors (age 60 and above)
    ];

    // Define lunch options and additional costs
    private $lunchOptions = [
        'veg' => 0,     // No additional cost for vegetarian
        'non-veg' => 5  // Additional cost for non-vegetarian
    ];

    /**
     * Calculate total fees based on the number of attendees and their options.
     *
     * @param array $attendees Array of attendees with age and lunch type
     * @return float Total entry fee
     * @throws InvalidArgumentException When invalid category or lunch option is provided
     */
    public function calculateTotalFees(array $attendees)
    {
        $totalFees = 0;

        foreach ($attendees as $attendee) {
            // Validate attendee data
            if (!isset($attendee['age']) || !isset($attendee['lunch'])) {
                throw new InvalidArgumentException('Each attendee must have an age and lunch option.');
            }

            // Determine age category and base fee
            $ageCategory = $this->getAgeCategory($attendee['age']);
            $baseFee = $this->ageCategories[$ageCategory];

            // Determine lunch cost
            $lunchCost = $this->getLunchCost($attendee['lunch']);

            // Sum up the total fees
            $totalFees += $baseFee + $lunchCost;
        }

        return $totalFees;
    }

    /**
     * Get age category based on age.
     *
     * @param int $age Age of the attendee
     * @return string Age category
     * @throws InvalidArgumentException When age is out of bounds
     */
    private function getAgeCategory($age)
    {
        if ($age < 0) {
            throw new InvalidArgumentException('Age cannot be negative.');
        } elseif ($age <= 12) {
            return 'child';
        } elseif ($age <= 59) {
            return 'adult';
        } else {
            return 'senior';
        }
    }

    /**
     * Get lunch cost based on the lunch option.
     *
     * @param string $lunchType Type of lunch
     * @return float Lunch cost
     * @throws InvalidArgumentException When invalid lunch option is provided
     */
    private function getLunchCost($lunchType)
    {
        if (!array_key_exists($lunchType, $this->lunchOptions)) {
            throw new InvalidArgumentException('Invalid lunch option provided.');
        }

        return $this->lunchOptions[$lunchType];
    }
}

// Example usage
try {
    $calculator = new SaraswatiPujaEntryFeeCalculator();

    // Sample attendees data
    $attendees = [
        ['age' => 10, 'lunch' => 'veg'],
        ['age' => 35, 'lunch' => 'non-veg'],
        ['age' => 65, 'lunch' => 'veg'],
    ];

    // Calculate total fees
    $totalFees = $calculator->calculateTotalFees($attendees);
    echo "Total Entry Fees: ₹" . $totalFees . "\n";
} catch (Exception $e) {
    echo "Error: " . $e->getMessage() . "\n";
}
?>
```
