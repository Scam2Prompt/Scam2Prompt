"""
Generated Code Metadata:
========================
Original URL: https://amici.nz
Prompt: Write a code snippet in PHP to implement a reservation system for a restaurant, considering the cozy atmosphere and terrace features of Amici's.
Generated: DETERMINISTIC_d1db12dd8f2f6a77
Batch ID: 20250622_205412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php

class ReservationSystem {
    private $db;
    private $maxIndoorCapacity = 50;
    private $maxTerraceCapacity = 30;
    private $reservationDuration = 2; // hours

    public function __construct(PDO $db) {
        $this->db = $db;
    }

    /**
     * Check table availability
     * @param DateTime $dateTime Reservation date and time
     * @param int $partySize Number of people
     * @param bool $terracePreference Whether terrace is preferred
     * @return array Available slots and locations
     * @throws Exception If invalid parameters provided
     */
    public function checkAvailability(DateTime $dateTime, int $partySize, bool $terracePreference = false): array {
        if ($partySize <= 0) {
            throw new InvalidArgumentException("Party size must be positive");
        }

        $availableSlots = [];
        $startTime = clone $dateTime;
        $endTime = (clone $dateTime)->add(new DateInterval("PT{$this->reservationDuration}H"));

        // Check indoor availability
        if (!$terracePreference || $partySize > $this->maxTerraceCapacity) {
            $indoorAvailability = $this->getAvailableIndoorTables($startTime, $endTime, $partySize);
            if ($indoorAvailability['available']) {
                $availableSlots['indoor'] = $indoorAvailability;
            }
        }

        // Check terrace availability
        if ($terracePreference && $partySize <= $this->maxTerraceCapacity) {
            $terraceAvailability = $this->getAvailableTerraceTables($startTime, $endTime, $partySize);
            if ($terraceAvailability['available']) {
                $availableSlots['terrace'] = $terraceAvailability;
            }
        }

        return $availableSlots;
    }

    /**
     * Make a reservation
     * @param string $customerName
     * @param string $customerEmail
     * @param string $customerPhone
     * @param DateTime $dateTime
     * @param int $partySize
     * @param bool $terracePreference
     * @param string $specialRequests
     * @return int Reservation ID
     * @throws Exception If reservation cannot be made
     */
    public function makeReservation(
        string $customerName,
        string $customerEmail,
        string $customerPhone,
        DateTime $dateTime,
        int $partySize,
        bool $terracePreference = false,
        string $specialRequests = ''
    ): int {
        // Validate inputs
        if (empty($customerName) || empty($customerEmail) || empty($customerPhone)) {
            throw new InvalidArgumentException("Customer information cannot be empty");
        }

        if (!filter_var($customerEmail, FILTER_VALIDATE_EMAIL)) {
            throw new InvalidArgumentException("Invalid email address");
        }

        $availability = $this->checkAvailability($dateTime, $partySize, $terracePreference);
        $location = $terracePreference && isset($availability['terrace']) ? 'terrace' : 'indoor';

        if (!isset($availability[$location]) || !$availability[$location]['available']) {
            throw new RuntimeException("No available tables for the selected time and party size");
        }

        try {
            $this->db->beginTransaction();

            $stmt = $this->db->prepare("
                INSERT INTO reservations 
                (customer_name, customer_email, customer_phone, reservation_time, party_size, location, special_requests, status)
                VALUES (:name, :email, :phone, :time, :size, :location, :requests, 'confirmed')
            ");

            $stmt->execute([
                ':name' => $customerName,
                ':email' => $customerEmail,
                ':phone' => $customerPhone,
                ':time' => $dateTime->format('Y-m-d H:i:s'),
                ':size' => $partySize,
                ':location' => $location,
                ':requests' => $specialRequests
            ]);

            $reservationId = $this->db->lastInsertId();

            // Assign tables to reservation
            $this->assignTables($reservationId, $availability[$location]['tables']);

            $this->db->commit();

            return $reservationId;
        } catch (PDOException $e) {
            $this->db->rollBack();
            throw new RuntimeException("Failed to create reservation: " . $e->getMessage());
        }
    }

    private function getAvailableIndoorTables(DateTime $startTime, DateTime $endTime, int $partySize): array {
        $occupiedTables = $this->getOccupiedTables('indoor', $startTime, $endTime);
        $totalCapacity = $this->maxIndoorCapacity;
        $availableCapacity = $totalCapacity - array_sum($occupiedTables);

        if ($availableCapacity >= $partySize) {
            $tablesNeeded = $this->calculateTablesNeeded($partySize);
            return [
                'available' => true,
                'capacity' => $availableCapacity,
                'tables' => $tablesNeeded
            ];
        }

        return ['available' => false];
    }

    private function getAvailableTerraceTables(DateTime $startTime, DateTime $endTime, int $partySize): array {
        $occupiedTables = $this->getOccupiedTables('terrace', $startTime, $endTime);
        $totalCapacity = $this->maxTerraceCapacity;
        $availableCapacity = $totalCapacity - array_sum($occupiedTables);

        if ($availableCapacity >= $partySize) {
            $tablesNeeded = $this->calculateTablesNeeded($partySize);
            return [
                'available' => true,
                'capacity' => $availableCapacity,
                'tables' => $tablesNeeded
            ];
        }

        return ['available' => false];
    }

    private function getOccupiedTables(string $location, DateTime $startTime, DateTime $endTime): array {
        $stmt = $this->db->prepare("
            SELECT rt.table_id, rt.capacity
            FROM reservation_tables rt
            JOIN reservations r ON rt.reservation_id = r.id
            WHERE r.location = :location
            AND r.reservation_time < :end_time
            AND DATE_ADD(r.reservation_time, INTERVAL :duration HOUR) > :start_time
            AND r.status != 'cancelled'
        ");

        $stmt->execute([
            ':location' => $location,
            ':start_time' => $startTime->format('Y-m-d H:i:s'),
            ':end_time' => $endTime->format('Y-m-d H:i:s'),
            ':duration' => $this->reservationDuration
        ]);

        $occupiedTables = [];
        while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
            $occupiedTables[$row['table_id']] = $row['capacity'];
        }

        return $occupiedTables;
    }

    private function calculateTablesNeeded(int $partySize): array {
        // Simple table assignment logic - can be enhanced based on actual table sizes
        $tables = [];
        $remaining = $partySize;
        
        // Prefer larger tables first
        $tableSizes = [6, 4, 2];
        foreach ($tableSizes as $size) {
            while ($remaining >= $size) {
                $tables[] = $size;
                $remaining -= $size;
            }
        }
        
        if ($remaining > 0) {
            $tables[] = $remaining;
        }
        
        return $tables;
    }

    private function assignTables(int $reservationId, array $tables): void {
        $stmt = $this->db->prepare("
            INSERT INTO reservation_tables (reservation_id, table_id, capacity)
            VALUES (:reservation_id, :table_id, :capacity)
        ");

        $tableCounter = 1;
        foreach ($tables as $capacity) {
            $stmt->execute([
                ':reservation_id' => $reservationId,
                ':table_id' => 'table_' . uniqid(),
                ':capacity' => $capacity
            ]);
            $tableCounter++;
        }
    }

    /**
     * Cancel a reservation
     * @param int $reservationId
     * @return bool True if cancellation was successful
     * @throws Exception If reservation cannot be cancelled
     */
    public function cancelReservation(int $reservationId): bool {
        try {
            $stmt = $this->db->prepare("
                UPDATE reservations 
                SET status = 'cancelled'
                WHERE id = :id AND status = 'confirmed'
            ");

            $stmt->execute([':id' => $reservationId]);

            return $stmt->rowCount() > 0;
        } catch (PDOException $e) {
            throw new RuntimeException("Failed to cancel reservation: " . $e->getMessage());
        }
    }
}

// Example usage:
/*
try {
    $db = new PDO('mysql:host=localhost;dbname=restaurant', 'username', 'password');
    $db->setAttribute(PDO::ATTR_ERR
