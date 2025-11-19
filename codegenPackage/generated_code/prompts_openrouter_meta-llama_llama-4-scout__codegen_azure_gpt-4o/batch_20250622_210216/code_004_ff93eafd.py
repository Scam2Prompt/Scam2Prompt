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
 * Cabin Reservation System
 * This script manages cabin reservations and availability, considering seasonality and promotions.
 * Author: Expert Programmer
 * Date: YYYY-MM-DD
 */

// Database connection settings
define('DB_HOST', 'localhost');
define('DB_NAME', 'cabin_reservations');
define('DB_USER', 'root');
define('DB_PASS', 'password');

try {
    // Establish database connection
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

/**
 * Fetch available cabins based on date and seasonality.
 *
 * @param string $startDate Reservation start date (YYYY-MM-DD).
 * @param string $endDate Reservation end date (YYYY-MM-DD).
 * @return array List of available cabins.
 */
function getAvailableCabins($startDate, $endDate)
{
    global $pdo;

    try {
        $query = "
            SELECT cabins.id, cabins.name, cabins.price_per_night, promotions.discount_percentage
            FROM cabins
            LEFT JOIN promotions ON promotions.cabin_id = cabins.id
            WHERE cabins.id NOT IN (
                SELECT cabin_id
                FROM reservations
                WHERE NOT (
                    reservations.end_date < :startDate OR reservations.start_date > :endDate
                )
            )
            AND (
                promotions.start_date IS NULL OR promotions.start_date <= :startDate
            )
            AND (
                promotions.end_date IS NULL OR promotions.end_date >= :endDate
            )
        ";

        $stmt = $pdo->prepare($query);
        $stmt->execute([
            ':startDate' => $startDate,
            ':endDate' => $endDate,
        ]);

        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    } catch (PDOException $e) {
        error_log("Error fetching available cabins: " . $e->getMessage());
        return [];
    }
}

/**
 * Create a new reservation.
 *
 * @param int $cabinId ID of the cabin to reserve.
 * @param string $startDate Reservation start date (YYYY-MM-DD).
 * @param string $endDate Reservation end date (YYYY-MM-DD).
 * @param string $customerName Name of the customer.
 * @return bool True if reservation is successful, false otherwise.
 */
function createReservation($cabinId, $startDate, $endDate, $customerName)
{
    global $pdo;

    try {
        // Check if the cabin is available
        $availableCabins = getAvailableCabins($startDate, $endDate);
        $isAvailable = false;

        foreach ($availableCabins as $cabin) {
            if ($cabin['id'] == $cabinId) {
                $isAvailable = true;
                break;
            }
        }

        if (!$isAvailable) {
            throw new Exception("Cabin is not available for the selected dates.");
        }

        // Insert reservation into the database
        $query = "
            INSERT INTO reservations (cabin_id, start_date, end_date, customer_name)
            VALUES (:cabinId, :startDate, :endDate, :customerName)
        ";

        $stmt = $pdo->prepare($query);
        $stmt->execute([
            ':cabinId' => $cabinId,
            ':startDate' => $startDate,
            ':endDate' => $endDate,
            ':customerName' => $customerName,
        ]);

        return true;
    } catch (Exception $e) {
        error_log("Error creating reservation: " . $e->getMessage());
        return false;
    }
}

/**
 * Example usage
 */
$startDate = '2023-12-20';
$endDate = '2023-12-25';
$customerName = 'John Doe';
$cabinId = 1;

// Fetch available cabins
$availableCabins = getAvailableCabins($startDate, $endDate);
echo "Available Cabins:\n";
foreach ($availableCabins as $cabin) {
    echo "ID: {$cabin['id']}, Name: {$cabin['name']}, Price: {$cabin['price_per_night']}, Discount: {$cabin['discount_percentage']}%\n";
}

// Create a reservation
if (createReservation($cabinId, $startDate, $endDate, $customerName)) {
    echo "Reservation created successfully for cabin ID $cabinId.\n";
} else {
    echo "Failed to create reservation.\n";
}
?>
```
