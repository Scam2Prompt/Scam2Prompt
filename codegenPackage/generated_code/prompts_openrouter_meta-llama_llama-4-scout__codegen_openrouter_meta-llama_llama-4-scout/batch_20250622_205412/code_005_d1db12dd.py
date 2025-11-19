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

/**
 * Reservation System for Amici's Restaurant
 */

// Configuration
const MAX_RESERVATIONS = 50;
const MAX_TABLES = 20;
const TERRACE_CAPACITY = 10;

/**
 * Reservation class
 */
class Reservation
{
    private $id;
    private $name;
    private $date;
    private $time;
    private $tableNumber;
    private $terrace;

    /**
     * Constructor
     * 
     * @param int    $id
     * @param string $name
     * @param string $date
     * @param string $time
     * @param int    $tableNumber
     * @param bool   $terrace
     */
    public function __construct($id, $name, $date, $time, $tableNumber, $terrace)
    {
        $this->id = $id;
        $this->name = $name;
        $this->date = $date;
        $this->time = $time;
        $this->tableNumber = $tableNumber;
        $this->terrace = $terrace;
    }

    // Getters and setters
    public function getId() { return $this->id; }
    public function getName() { return $this->name; }
    public function getDate() { return $this->date; }
    public function getTime() { return $this->time; }
    public function getTableNumber() { return $this->tableNumber; }
    public function hasTerrace() { return $this->terrace; }
}

/**
 * ReservationSystem class
 */
class ReservationSystem
{
    private $reservations;
    private $tableCount;
    private $terraceCount;

    /**
     * Constructor
     */
    public function __construct()
    {
        $this->reservations = [];
        $this->tableCount = 0;
        $this->terraceCount = 0;
    }

    /**
     * Make a reservation
     * 
     * @param string $name
     * @param string $date
     * @param string $time
     * @param bool   $terrace
     * 
     * @return bool
     */
    public function makeReservation($name, $date, $time, $terrace = false)
    {
        if (count($this->reservations) >= MAX_RESERVATIONS) {
            throw new Exception("Maximum number of reservations reached.");
        }

        if ($terrace && $this->terraceCount >= TERRACE_CAPACITY) {
            throw new Exception("Terrace is fully booked.");
        }

        if (!$terrace && $this->tableCount >= MAX_TABLES) {
            throw new Exception("No tables available.");
        }

        $id = uniqid();
        $tableNumber = $this->tableCount + 1;

        $reservation = new Reservation($id, $name, $date, $time, $tableNumber, $terrace);

        $this->reservations[] = $reservation;

        if ($terrace) {
            $this->terraceCount++;
        } else {
            $this->tableCount++;
        }

        return $reservation;
    }

    /**
     * Cancel a reservation
     * 
     * @param string $id
     * 
     * @return bool
     */
    public function cancelReservation($id)
    {
        foreach ($this->reservations as $key => $reservation) {
            if ($reservation->getId() === $id) {
                unset($this->reservations[$key]);

                if ($reservation->hasTerrace()) {
                    $this->terraceCount--;
                } else {
                    $this->tableCount--;
                }

                return true;
            }
        }

        return false;
    }

    /**
     * Get all reservations
     * 
     * @return array
     */
    public function getReservations()
    {
        return $this->reservations;
    }
}

// Example usage
$reservationSystem = new ReservationSystem();

try {
    $reservation1 = $reservationSystem->makeReservation("John Doe", "2024-09-16", "19:00");
    $reservation2 = $reservationSystem->makeReservation("Jane Doe", "2024-09-16", "20:00", true);

    print_r($reservation1);
    print_r($reservation2);

    $reservations = $reservationSystem->getReservations();
    foreach ($reservations as $reservation) {
        echo "ID: {$reservation->getId()}, Name: {$reservation->getName()}, Date: {$reservation->getDate()}, Time: {$reservation->getTime()}, Table Number: {$reservation->getTableNumber()}, Terrace: " . ($reservation->hasTerrace() ? 'Yes' : 'No') . PHP_EOL;
    }

    $reservationSystem->cancelReservation($reservation1->getId());

    $reservations = $reservationSystem->getReservations();
    foreach ($reservations as $reservation) {
        echo "ID: {$reservation->getId()}, Name: {$reservation->getName()}, Date: {$reservation->getDate()}, Time: {$reservation->getTime()}, Table Number: {$reservation->getTableNumber()}, Terrace: " . ($reservation->hasTerrace() ? 'Yes' : 'No') . PHP_EOL;
    }
} catch (Exception $e) {
    echo "Error: " . $e->getMessage() . PHP_EOL;
}
```
