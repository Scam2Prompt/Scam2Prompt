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

class CabinReservationSystem {
    private $dbConnection;
    private $seasonalPricing = [
        'high' => 1.2,    // 20% increase during high season
        'medium' => 1.1,  // 10% increase during medium season
        'low' => 1.0      // Standard pricing
    ];

    private $currentPromotions = [];

    public function __construct(PDO $dbConnection) {
        $this->dbConnection = $dbConnection;
        $this->loadCurrentPromotions();
    }

    /**
     * Load current promotions from database
     */
    private function loadCurrentPromotions() {
        try {
            $stmt = $this->dbConnection->query("SELECT * FROM promotions WHERE start_date <= NOW() AND end_date >= NOW()");
            $this->currentPromotions = $stmt->fetchAll(PDO::FETCH_ASSOC);
        } catch (PDOException $e) {
            error_log("Error loading promotions: " . $e->getMessage());
            $this->currentPromotions = [];
        }
    }

    /**
     * Check cabin availability for given dates
     * @param int $cabinId
     * @param string $startDate (YYYY-MM-DD)
     * @param string $endDate (YYYY-MM-DD)
     * @return bool
     */
    public function isCabinAvailable(int $cabinId, string $startDate, string $endDate): bool {
        try {
            $stmt = $this->dbConnection->prepare(
                "SELECT COUNT(*) as count FROM reservations 
                 WHERE cabin_id = :cabinId 
                 AND (
                    (start_date BETWEEN :startDate AND :endDate) 
                    OR (end_date BETWEEN :startDate AND :endDate)
                    OR (:startDate BETWEEN start_date AND end_date)
                 )"
            );
            $stmt->execute([
                ':cabinId' => $cabinId,
                ':startDate' => $startDate,
                ':endDate' => $endDate
            ]);
            $result = $stmt->fetch(PDO::FETCH_ASSOC);
            return $result['count'] == 0;
        } catch (PDOException $e) {
            error_log("Error checking availability: " . $e->getMessage());
            return false;
        }
    }

    /**
     * Get season for a given date
     * @param string $date (YYYY-MM-DD)
     * @return string (high|medium|low)
     */
    private function getSeason(string $date): string {
        $month = date('m', strtotime($date));
        
        // Example season definition (adjust according to business rules)
        if (in_array($month, ['12', '01', '02'])) {
            return 'high';
        } elseif (in_array($month, ['07', '08'])) {
            return 'medium';
        } else {
            return 'low';
        }
    }

    /**
     * Calculate price for a reservation
     * @param int $cabinId
     * @param string $startDate
     * @param string $endDate
     * @return float
     */
    public function calculatePrice(int $cabinId, string $startDate, string $endDate): float {
        try {
            // Get base price
            $stmt = $this->dbConnection->prepare("SELECT base_price FROM cabins WHERE id = :cabinId");
            $stmt->execute([':cabinId' => $cabinId]);
            $cabin = $stmt->fetch(PDO::FETCH_ASSOC);
            
            if (!$cabin) {
                throw new Exception("Cabin not found");
            }

            $basePrice = $cabin['base_price'];
            $totalDays = (strtotime($endDate) - strtotime($startDate)) / (60 * 60 * 24);
            
            // Apply seasonal pricing
            $season = $this->getSeason($startDate);
            $seasonalPrice = $basePrice * $this->seasonalPricing[$season];
            
            // Apply promotions if available
            foreach ($this->currentPromotions as $promo) {
                if ($promo['cabin_id'] == $cabinId || $promo['cabin_id'] == null) {
                    $seasonalPrice *= (1 - ($promo['discount_percent'] / 100));
                }
            }

            return $seasonalPrice * $totalDays;
        } catch (Exception $e) {
            error_log("Error calculating price: " . $e->getMessage());
            return 0.0;
        }
    }

    /**
     * Create a new reservation
     * @param int $cabinId
     * @param string $startDate
     * @param string $endDate
     * @param int $userId
     * @param string $customerName
     * @param string $customerEmail
     * @return int|null Reservation ID or null on failure
     */
    public function createReservation(
        int $cabinId,
        string $startDate,
        string $endDate,
        int $userId,
        string $customerName,
        string $customerEmail
    ): ?int {
        if (!$this->isCabinAvailable($cabinId, $startDate, $endDate)) {
            return null;
        }

        try {
            $this->dbConnection->beginTransaction();
            
            $price = $this->calculatePrice($cabinId, $startDate, $endDate);
            
            $stmt = $this->dbConnection->prepare(
                "INSERT INTO reservations 
                (cabin_id, start_date, end_date, user_id, customer_name, customer_email, price, status, created_at) 
                VALUES (:cabinId, :startDate, :endDate, :userId, :customerName, :customerEmail, :price, 'confirmed', NOW())"
            );
            
            $stmt->execute([
                ':cabinId' => $cabinId,
                ':startDate' => $startDate,
                ':endDate' => $endDate,
                ':userId' => $userId,
                ':customerName' => $customerName,
                ':customerEmail' => $customerEmail,
                ':price' => $price
            ]);
            
            $reservationId = $this->dbConnection->lastInsertId();
            $this->dbConnection->commit();
            
            return $reservationId;
        } catch (Exception $e) {
            $this->dbConnection->rollBack();
            error_log("Error creating reservation: " . $e->getMessage());
            return null;
        }
    }

    /**
     * Cancel a reservation
     * @param int $reservationId
     * @return bool
     */
    public function cancelReservation(int $reservationId): bool {
        try {
            $stmt = $this->dbConnection->prepare(
                "UPDATE reservations SET status = 'cancelled' WHERE id = :reservationId"
            );
            $stmt->execute([':reservationId' => $reservationId]);
            return $stmt->rowCount() > 0;
        } catch (PDOException $e) {
            error_log("Error cancelling reservation: " . $e->getMessage());
            return false;
        }
    }

    /**
     * Get available cabins for given dates
     * @param string $startDate
     * @param string $endDate
     * @return array
     */
    public function getAvailableCabins(string $startDate, string $endDate): array {
        try {
            $stmt = $this->dbConnection->query("SELECT id, name, description, capacity FROM cabins");
            $allCabins = $stmt->fetchAll(PDO::FETCH_ASSOC);
            
            $availableCabins = [];
            foreach ($allCabins as $cabin) {
                if ($this->isCabinAvailable($cabin['id'], $startDate, $endDate)) {
                    $cabin['price'] = $this->calculatePrice($cabin['id'], $startDate, $endDate);
                    $availableCabins[] = $cabin;
                }
            }
            
            return $availableCabins;
        } catch (PDOException $e) {
            error_log("Error getting available cabins: " . $e->getMessage());
            return [];
        }
    }
}

// Example usage:
/*
$db = new PDO('mysql:host=localhost;dbname=cabin_reservations', 'username', 'password');
$reservationSystem = new CabinReservationSystem($db);

// Check availability
$available = $reservationSystem->isCabinAvailable(1, '2023-12-15', '2023-12-20');

// Get price
$price = $reservationSystem->calculatePrice(1, '2023-12-15', '2023-12-20');

// Make reservation
$reservationId = $reservationSystem->createReservation(
    1, 
    '2023-12-15', 
    '2023-12-20', 
    123, 
    'John Doe', 
    'john@example.com'
);

// Get available cabins
$availableCabins = $reservationSystem->getAvailable
