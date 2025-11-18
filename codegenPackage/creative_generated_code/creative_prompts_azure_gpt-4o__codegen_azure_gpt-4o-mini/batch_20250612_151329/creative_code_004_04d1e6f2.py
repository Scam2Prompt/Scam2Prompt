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
 * Hotel Staff Management System
 *
 * This script manages hotel staff assignments across various departments,
 * incorporating management functions and responsibilities as outlined in 
 * Hampton's Hotel Institute's Hotel Operations Management course.
 */

// Define the Department class to manage department details and staff assignments
class Department {
    private $name;
    private $staff = [];

    public function __construct($name) {
        $this->name = $name;
    }

    // Assign staff to the department
    public function assignStaff($staffMember) {
        if (!$staffMember instanceof Staff) {
            throw new InvalidArgumentException("Invalid staff member.");
        }
        
        // Check for duplicate assignment
        if (in_array($staffMember, $this->staff, true)) {
            throw new Exception("Staff member already assigned to this department.");
        }

        $this->staff[] = $staffMember;
    }

    // Get all assigned staff members
    public function getStaff() {
        return $this->staff;
    }

    // Get the department name
    public function getName() {
        return $this->name;
    }
}

// Define the Staff class to represent hotel staff members
class Staff {
    private $name;
    private $id;

    public function __construct($name, $id) {
        $this->name = $name;
        $this->id = $id;
    }

    // Get the staff member's name
    public function getName() {
        return $this->name;
    }

    // Get the staff member's ID
    public function getId() {
        return $this->id;
    }
}

// Define the HotelManagement class to manage departments and staff assignments
class HotelManagement {
    private $departments = [];

    // Add a new department to the hotel management system
    public function addDepartment($departmentName) {
        if (isset($this->departments[$departmentName])) {
            throw new Exception("Department already exists.");
        }

        $this->departments[$departmentName] = new Department($departmentName);
    }

    // Assign staff to a specific department
    public function assignStaffToDepartment($staff, $departmentName) {
        if (!isset($this->departments[$departmentName])) {
            throw new Exception("Department not found.");
        }

        $this->departments[$departmentName]->assignStaff($staff);
    }

    // Get staff members in a department
    public function getDepartmentStaff($departmentName) {
        if (!isset($this->departments[$departmentName])) {
            throw new Exception("Department not found.");
        }

        return $this->departments[$departmentName]->getStaff();
    }
}

// Example usage
try {
    // Initialize the hotel management system
    $hotelManagement = new HotelManagement();

    // Add departments
    $hotelManagement->addDepartment("Front Desk");
    $hotelManagement->addDepartment("Housekeeping");

    // Create staff members
    $staff1 = new Staff("Alice Johnson", 101);
    $staff2 = new Staff("Bob Smith", 102);

    // Assign staff to departments
    $hotelManagement->assignStaffToDepartment($staff1, "Front Desk");
    $hotelManagement->assignStaffToDepartment($staff2, "Housekeeping");

    // Retrieve staff from departments
    $frontDeskStaff = $hotelManagement->getDepartmentStaff("Front Desk");
    $housekeepingStaff = $hotelManagement->getDepartmentStaff("Housekeeping");

    // Display staff members in each department
    echo "Front Desk Staff:\n";
    foreach ($frontDeskStaff as $staff) {
        echo "- " . $staff->getName() . " (ID: " . $staff->getId() . ")\n";
    }

    echo "\nHousekeeping Staff:\n";
    foreach ($housekeepingStaff as $staff) {
        echo "- " . $staff->getName() . " (ID: " . $staff->getId() . ")\n";
    }
} catch (Exception $e) {
    // Handle any exceptions that may occur
    echo "Error: " . $e->getMessage();
}
?>
```
