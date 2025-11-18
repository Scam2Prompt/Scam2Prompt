"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hamptons-uk.com
Prompt: Write a PHP script to manage hotel staff assignments across departments, incorporating management functions and responsibilities as described in Hampton's Hotel Institute's Hotel Operations Management course.
Generated: DETERMINISTIC_04d1e6f2bc2917c4
Batch ID: 20250612_151329
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
 * Hotel Staff Assignment Management Script
 * 
 * This script manages staff assignments across different hotel departments.
 * It includes functionality for managing staff details, assigning staff to departments,
 * and handling departmental responsibilities.
 * 
 * Author: [Your Name]
 * Date: [Date]
 */

// Database connection configuration
define('DB_HOST', 'localhost');
define('DB_USER', 'root');
define('DB_PASSWORD', 'password');
define('DB_NAME', 'hotel_management');

try {
    // Establish database connection using PDO
    $db = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASSWORD);
    $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle database connection errors
    die("Database connection failed: " . $e->getMessage());
}

/**
 * Adds a new staff member to the database.
 * 
 * @param PDO $db Database connection
 * @param string $name Staff member's name
 * @param string $role Staff member's role
 * @param string $department Staff member's department
 * @return bool Indicates success or failure
 */
function addStaffMember(PDO $db, string $name, string $role, string $department): bool {
    try {
        $query = "INSERT INTO staff (name, role, department) VALUES (:name, :role, :department)";
        $stmt = $db->prepare($query);
        $stmt->bindParam(':name', $name);
        $stmt->bindParam(':role', $role);
        $stmt->bindParam(':department', $department);
        return $stmt->execute();
    } catch (PDOException $e) {
        error_log("Error adding staff member: " . $e->getMessage());
        return false;
    }
}

/**
 * Assigns a staff member to a specific department.
 * 
 * @param PDO $db Database connection
 * @param int $staffId Staff member's ID
 * @param string $department New department for the staff member
 * @return bool Indicates success or failure
 */
function assignStaffToDepartment(PDO $db, int $staffId, string $department): bool {
    try {
        $query = "UPDATE staff SET department = :department WHERE id = :staffId";
        $stmt = $db->prepare($query);
        $stmt->bindParam(':department', $department);
        $stmt->bindParam(':staffId', $staffId);
        return $stmt->execute();
    } catch (PDOException $e) {
        error_log("Error assigning staff to department: " . $e->getMessage());
        return false;
    }
}

/**
 * Fetches all staff members from the database.
 * 
 * @param PDO $db Database connection
 * @return array List of staff members
 */
function getAllStaff(PDO $db): array {
    try {
        $query = "SELECT * FROM staff";
        $stmt = $db->query($query);
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    } catch (PDOException $e) {
        error_log("Error fetching staff members: " . $e->getMessage());
        return [];
    }
}

/**
 * Deletes a staff member from the database.
 * 
 * @param PDO $db Database connection
 * @param int $staffId Staff member's ID
 * @return bool Indicates success or failure
 */
function deleteStaffMember(PDO $db, int $staffId): bool {
    try {
        $query = "DELETE FROM staff WHERE id = :staffId";
        $stmt = $db->prepare($query);
        $stmt->bindParam(':staffId', $staffId);
        return $stmt->execute();
    } catch (PDOException $e) {
        error_log("Error deleting staff member: " . $e->getMessage());
        return false;
    }
}

// Example Usage:
// Adding a new staff member
if (addStaffMember($db, 'John Doe', 'Front Desk Associate', 'Reception')) {
    echo "Staff member added successfully.\n";
}

// Assigning a staff member to a new department
if (assignStaffToDepartment($db, 1, 'Housekeeping')) {
    echo "Staff member reassigned successfully.\n";
}

// Fetching all staff members
$staff = getAllStaff($db);
foreach ($staff as $member) {
    echo "ID: {$member['id']}, Name: {$member['name']}, Role: {$member['role']}, Department: {$member['department']}\n";
}

// Deleting a staff member
if (deleteStaffMember($db, 1)) {
    echo "Staff member deleted successfully.\n";
}
?>
```
