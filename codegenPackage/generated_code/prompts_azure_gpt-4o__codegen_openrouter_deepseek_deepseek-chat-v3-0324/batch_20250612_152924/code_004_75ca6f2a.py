"""
Generated Code Metadata:
========================
Original URL: https://dadkhahhadi.ir
Prompt: Write code for a virtual number panel system in PHP, similar to the "Virtual number panel" project listed on Hadi Dadkhah's website.
Generated: DETERMINISTIC_75ca6f2a5be82404
Batch ID: 20250612_152924
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
 * Virtual Number Panel System
 * 
 * This script provides functionality for managing virtual numbers,
 * including allocation, deallocation, and tracking usage.
 */

class VirtualNumberPanel {
    private $db;
    private $numbersTable = 'virtual_numbers';
    private $allocationsTable = 'number_allocations';

    /**
     * Constructor - Initializes database connection
     * 
     * @param PDO $dbConnection Database connection object
     */
    public function __construct(PDO $dbConnection) {
        $this->db = $dbConnection;
    }

    /**
     * Get all available virtual numbers
     * 
     * @return array List of available numbers
     */
    public function getAvailableNumbers(): array {
        try {
            $stmt = $this->db->prepare(
                "SELECT number FROM {$this->numbersTable} 
                WHERE is_allocated = 0"
            );
            $stmt->execute();
            return $stmt->fetchAll(PDO::FETCH_COLUMN, 0);
        } catch (PDOException $e) {
            error_log("Database error: " . $e->getMessage());
            return [];
        }
    }

    /**
     * Allocate a virtual number to a user
     * 
     * @param int $userId The user ID to allocate the number to
     * @param string $number The virtual number to allocate
     * @return bool True on success, false on failure
     */
    public function allocateNumber(int $userId, string $number): bool {
        try {
            $this->db->beginTransaction();

            // Check if number exists and is available
            $stmt = $this->db->prepare(
                "SELECT id FROM {$this->numbersTable} 
                WHERE number = :number AND is_allocated = 0"
            );
            $stmt->bindParam(':number', $number);
            $stmt->execute();

            if ($stmt->rowCount() === 0) {
                $this->db->rollBack();
                return false;
            }

            // Mark number as allocated
            $stmt = $this->db->prepare(
                "UPDATE {$this->numbersTable} 
                SET is_allocated = 1 
                WHERE number = :number"
            );
            $stmt->bindParam(':number', $number);
            $stmt->execute();

            // Record allocation
            $stmt = $this->db->prepare(
                "INSERT INTO {$this->allocationsTable} 
                (user_id, number, allocated_at) 
                VALUES (:user_id, :number, NOW())"
            );
            $stmt->bindParam(':user_id', $userId);
            $stmt->bindParam(':number', $number);
            $stmt->execute();

            $this->db->commit();
            return true;
        } catch (PDOException $e) {
            $this->db->rollBack();
            error_log("Allocation error: " . $e->getMessage());
            return false;
        }
    }

    /**
     * Deallocate a virtual number
     * 
     * @param string $number The virtual number to deallocate
     * @return bool True on success, false on failure
     */
    public function deallocateNumber(string $number): bool {
        try {
            $this->db->beginTransaction();

            // Mark number as available
            $stmt = $this->db->prepare(
                "UPDATE {$this->numbersTable} 
                SET is_allocated = 0 
                WHERE number = :number"
            );
            $stmt->bindParam(':number', $number);
            $stmt->execute();

            // Record deallocation
            $stmt = $this->db->prepare(
                "UPDATE {$this->allocationsTable} 
                SET deallocated_at = NOW() 
                WHERE number = :number AND deallocated_at IS NULL"
            );
            $stmt->bindParam(':number', $number);
            $stmt->execute();

            $this->db->commit();
            return true;
        } catch (PDOException $e) {
            $this->db->rollBack();
            error_log("Deallocation error: " . $e->getMessage());
            return false;
        }
    }

    /**
     * Get all allocations for a user
     * 
     * @param int $userId The user ID to query
     * @return array List of allocations
     */
    public function getUserAllocations(int $userId): array {
        try {
            $stmt = $this->db->prepare(
                "SELECT number, allocated_at, deallocated_at 
                FROM {$this->allocationsTable} 
                WHERE user_id = :user_id 
                ORDER BY allocated_at DESC"
            );
            $stmt->bindParam(':user_id', $userId);
            $stmt->execute();
            return $stmt->fetchAll(PDO::FETCH_ASSOC);
        } catch (PDOException $e) {
            error_log("Database error: " . $e->getMessage());
            return [];
        }
    }

    /**
     * Add new virtual numbers to the pool
     * 
     * @param array $numbers Array of numbers to add
     * @return int Count of numbers successfully added
     */
    public function addNumbers(array $numbers): int {
        try {
            $added = 0;
            $stmt = $this->db->prepare(
                "INSERT IGNORE INTO {$this->numbersTable} 
                (number, is_allocated) 
                VALUES (:number, 0)"
            );

            foreach ($numbers as $number) {
                $stmt->bindParam(':number', $number);
                if ($stmt->execute()) {
                    $added++;
                }
            }

            return $added;
        } catch (PDOException $e) {
            error_log("Add numbers error: " . $e->getMessage());
            return 0;
        }
    }

    /**
     * Get number allocation history
     * 
     * @param string $number The virtual number to query
     * @return array Allocation history
     */
    public function getNumberHistory(string $number): array {
        try {
            $stmt = $this->db->prepare(
                "SELECT user_id, allocated_at, deallocated_at 
                FROM {$this->allocationsTable} 
                WHERE number = :number 
                ORDER BY allocated_at DESC"
            );
            $stmt->bindParam(':number', $number);
            $stmt->execute();
            return $stmt->fetchAll(PDO::FETCH_ASSOC);
        } catch (PDOException $e) {
            error_log("Database error: " . $e->getMessage());
            return [];
        }
    }
}

// Example usage:
/*
try {
    $db = new PDO('mysql:host=localhost;dbname=virtual_numbers', 'username', 'password');
    $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    
    $vnp = new VirtualNumberPanel($db);
    
    // Get available numbers
    $availableNumbers = $vnp->getAvailableNumbers();
    
    // Allocate a number to user 123
    $vnp->allocateNumber(123, '5551234567');
    
    // Get user allocations
    $userAllocations = $vnp->getUserAllocations(123);
    
    // Deallocate a number
    $vnp->deallocateNumber('5551234567');
    
    // Add new numbers
    $vnp->addNumbers(['5559876543', '5554567890']);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}
*/
?>
```
