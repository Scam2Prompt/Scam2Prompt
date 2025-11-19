"""
Generated Code Metadata:
========================
Original URL: https://elchallao.com.ar
Prompt: Write a code example in PHP to manage cabin reservations and availability for a website like El Challao, considering factors like seasonality and promotions.
Generated: DETERMINISTIC_ff93eafda2feaaa4
Batch ID: 20250622_210216
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
 * CabinReservationManager class handles cabin reservations and availability.
 */
class CabinReservationManager {
    private $cabins = [];
    private $reservations = [];
    private $seasonalRates = [];
    private $promotions = [];

    /**
     * Constructor to initialize cabins and seasonal rates.
     */
    public function __construct() {
        $this->initializeCabins();
        $this->initializeSeasonalRates();
        $this->initializePromotions();
    }

    /**
     * Initializes cabin data.
     */
    private function initializeCabins() {
        // Example cabin data
        $this->cabins = [
            ['id' => 1, 'name' => 'Cabin A', 'capacity' => 4],
            ['id' => 2, 'name' => 'Cabin B', 'capacity' => 6],
            ['id' => 3, 'name' => 'Cabin C', 'capacity' => 2],
        ];
    }

    /**
     * Initializes seasonal rates.
     */
    private function initializeSeasonalRates() {
        // Example seasonal rates
        $this->seasonalRates = [
            '2023-12-01' => 150, // Winter season
            '2024-06-01' => 120, // Summer season
        ];
    }

    /**
     * Initializes promotional offers.
     */
    private function initializePromotions() {
        // Example promotions
        $this->promotions = [
            'WINTER20' => 20, // 20% off in winter
            'SUMMER10' => 10, // 10% off in summer
        ];
    }

    /**
     * Checks cabin availability for a given date range.
     *
     * @param string $cabinId
     * @param string $startDate
     * @param string $endDate
     * @return bool
     */
    public function isCabinAvailable($cabinId, $startDate, $endDate) {
        foreach ($this->reservations as $reservation) {
            if ($reservation['cabinId'] == $cabinId &&
                $this->datesOverlap($startDate, $endDate, $reservation['startDate'], $reservation['endDate'])) {
                return false; // Cabin is not available
            }
        }
        return true; // Cabin is available
    }

    /**
     * Checks if two date ranges overlap.
     *
     * @param string $start1
     * @param string $end1
     * @param string $start2
     * @param string $end2
     * @return bool
     */
    private function datesOverlap($start1, $end1, $start2, $end2) {
        return ($start1 < $end2 && $start2 < $end1);
    }

    /**
     * Makes a reservation for a cabin.
     *
     * @param string $cabinId
     * @param string $startDate
     * @param string $endDate
     * @param string|null $promoCode
     * @return string
     * @throws Exception
     */
    public function makeReservation($cabinId, $startDate, $endDate, $promoCode = null) {
        if (!$this->isCabinAvailable($cabinId, $startDate, $endDate)) {
            throw new Exception("Cabin is not available for the selected dates.");
        }

        $rate = $this->getRateForDateRange($startDate, $endDate);
        $totalCost = $this->calculateTotalCost($rate, $startDate, $endDate, $promoCode);

        // Store the reservation
        $this->reservations[] = [
            'cabinId' => $cabinId,
            'startDate' => $startDate,
            'endDate' => $endDate,
            'totalCost' => $totalCost,
        ];

        return "Reservation successful! Total cost: $" . number_format($totalCost, 2);
    }

    /**
     * Gets the rate for the specified date range.
     *
     * @param string $startDate
     * @param string $endDate
     * @return float
     */
    private function getRateForDateRange($startDate, $endDate) {
        $rate = 100; // Default rate
        foreach ($this->seasonalRates as $date => $seasonRate) {
            if ($startDate >= $date) {
                $rate = $seasonRate;
            }
        }
        return $rate;
    }

    /**
     * Calculates the total cost based on the rate, date range, and promotional code.
     *
     * @param float $rate
     * @param string $startDate
     * @param string $endDate
     * @param string|null $promoCode
     * @return float
     */
    private function calculateTotalCost($rate, $startDate, $endDate, $promoCode) {
        $numDays = (strtotime($endDate) - strtotime($startDate)) / (60 * 60 * 24);
        $totalCost = $rate * $numDays;

        // Apply promotion if valid
        if ($promoCode && isset($this->promotions[$promoCode])) {
            $discount = $this->promotions[$promoCode];
            $totalCost -= ($totalCost * ($discount / 100));
        }

        return $totalCost;
    }

    /**
     * Retrieves all reservations.
     *
     * @return array
     */
    public function getReservations() {
        return $this->reservations;
    }
}

// Example usage
try {
    $manager = new CabinReservationManager();
    echo $manager->makeReservation(1, '2023-12-10', '2023-12-15', 'WINTER20');
} catch (Exception $e) {
    echo "Error: " . $e->getMessage();
}
?>
```
