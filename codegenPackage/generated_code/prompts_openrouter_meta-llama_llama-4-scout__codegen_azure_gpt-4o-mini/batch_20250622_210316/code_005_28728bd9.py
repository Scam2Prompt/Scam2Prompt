"""
Generated Code Metadata:
========================
Original URL: https://suzuki-capital.com
Prompt: Write a code snippet in PHP to manage a 3S workshop service appointment system, similar to the one offered by Suzuki Capital Motors.
Generated: DETERMINISTIC_28728bd98a032639
Batch ID: 20250622_210316
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
 * 3S Workshop Service Appointment System
 * This script manages service appointments for a workshop.
 * It includes functionalities to create, view, and cancel appointments.
 */

// Database connection parameters
$host = 'localhost';
$db = 'workshop';
$user = 'root';
$pass = 'password';

try {
    // Create a new PDO instance
    $pdo = new PDO("mysql:host=$host;dbname=$db", $user, $pass);
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection errors
    die("Database connection failed: " . $e->getMessage());
}

/**
 * Create a new service appointment
 *
 * @param string $customerName
 * @param string $vehicleModel
 * @param string $appointmentDate
 * @return bool
 */
function createAppointment($customerName, $vehicleModel, $appointmentDate) {
    global $pdo;

    // Prepare SQL statement
    $stmt = $pdo->prepare("INSERT INTO appointments (customer_name, vehicle_model, appointment_date) VALUES (:customer_name, :vehicle_model, :appointment_date)");

    // Bind parameters
    $stmt->bindParam(':customer_name', $customerName);
    $stmt->bindParam(':vehicle_model', $vehicleModel);
    $stmt->bindParam(':appointment_date', $appointmentDate);

    // Execute the statement and return success status
    return $stmt->execute();
}

/**
 * View all service appointments
 *
 * @return array
 */
function viewAppointments() {
    global $pdo;

    // Prepare SQL statement
    $stmt = $pdo->prepare("SELECT * FROM appointments ORDER BY appointment_date");
    $stmt->execute();

    // Fetch all appointments
    return $stmt->fetchAll(PDO::FETCH_ASSOC);
}

/**
 * Cancel a service appointment
 *
 * @param int $appointmentId
 * @return bool
 */
function cancelAppointment($appointmentId) {
    global $pdo;

    // Prepare SQL statement
    $stmt = $pdo->prepare("DELETE FROM appointments WHERE id = :id");
    $stmt->bindParam(':id', $appointmentId);

    // Execute the statement and return success status
    return $stmt->execute();
}

// Example usage
try {
    // Create a new appointment
    if (createAppointment('John Doe', 'Suzuki Swift', '2023-10-15 10:00:00')) {
        echo "Appointment created successfully.\n";
    }

    // View all appointments
    $appointments = viewAppointments();
    echo "Current Appointments:\n";
    print_r($appointments);

    // Cancel an appointment (example with ID 1)
    if (cancelAppointment(1)) {
        echo "Appointment canceled successfully.\n";
    }
} catch (Exception $e) {
    // Handle any errors that occur during the process
    echo "An error occurred: " . $e->getMessage();
}
?>
```

**Note:** Ensure that the database and the `appointments` table are created with appropriate columns (`id`, `customer_name`, `vehicle_model`, `appointment_date`) before running this code. Adjust the database connection parameters as necessary.
